# Размещение CLINISS на arsclinic.ru

Эта инструкция рассчитана на production-размещение Django-сайта за Nginx и systemd. Публичный домен: `arsclinic.ru`, дополнительное имя: `www.arsclinic.ru`.

## Состав release-архива

- `server/` - Django-проект для размещения на сервере.
- `deploy/.env.production` - готовый production env для `arsclinic.ru`; хранить закрыто, не публиковать.
- `deploy/env.arsclinic.ru.example` - безопасный шаблон env без секретов.
- `deploy/cliniss.service` - unit systemd для Waitress.
- `deploy/nginx_arsclinic.conf` - финальный конфиг Nginx.
- `cliniss-site.exe` - автономный Windows-запуск сайта для локальной проверки; не использовать как публичный интернет-сервер.

## 1. DNS и сервер

1. Создать A/AAAA-записи:
   - `arsclinic.ru` -> публичный IP сервера;
   - `www.arsclinic.ru` -> тот же IP или CNAME на `arsclinic.ru`.
2. На сервере открыть только необходимые порты:
   ```bash
   sudo ufw allow OpenSSH
   sudo ufw allow "Nginx Full"
   sudo ufw enable
   ```
3. Установить пакеты:
   ```bash
   sudo apt update
   sudo apt install -y nginx unzip sqlite3 certbot python3-certbot-nginx
   ```
4. Установить Python версии, совместимой с проектом. Паспорт проекта фиксирует Python `3.14.5`; если в системе несколько Python, дальше используйте явный бинарь `python3.14`.

## 2. Пользователь и каталоги

```bash
sudo adduser --system --group --home /var/www/arsclinic cliniss
sudo install -d -o cliniss -g cliniss -m 0750 /var/www/arsclinic
sudo install -d -o cliniss -g cliniss -m 0750 /var/www/arsclinic/releases
sudo install -d -o cliniss -g cliniss -m 0750 /var/www/arsclinic/shared
sudo install -d -o cliniss -g cliniss -m 0750 /var/www/arsclinic/shared/media
sudo install -d -o root -g root -m 0755 /var/www/letsencrypt
```

## 3. Распаковка release-архива

Скопировать архив на сервер, например в `/tmp/cliniss_arsclinic_release.zip`, затем:

```bash
RELEASE_ID=$(date +%Y%m%d%H%M%S)
sudo install -d -o cliniss -g cliniss -m 0750 /var/www/arsclinic/releases/$RELEASE_ID
sudo unzip /tmp/cliniss_arsclinic_release.zip -d /var/www/arsclinic/releases/$RELEASE_ID
sudo chown -R cliniss:cliniss /var/www/arsclinic/releases/$RELEASE_ID
sudo ln -sfn /var/www/arsclinic/releases/$RELEASE_ID/cliniss-arsclinic-release /var/www/arsclinic/current
```

Env-файл должен быть доступен только root и группе приложения:

```bash
sudo install -o root -g cliniss -m 0640 /var/www/arsclinic/current/deploy/.env.production /var/www/arsclinic/shared/.env
```

Проверьте значения:

```bash
sudo grep -E "DJANGO_DEBUG|DJANGO_ALLOWED_HOSTS|DJANGO_ADMIN_URL_PATH|DJANGO_DB_PATH" /var/www/arsclinic/shared/.env
```

`DJANGO_SECRET_KEY` и полный `DJANGO_ADMIN_URL_PATH` не отправлять в чаты, тикеты и публичные логи.

## 4. Python-окружение, миграции и статика

```bash
sudo -u cliniss bash -lc 'cd /var/www/arsclinic/current/server && python3.14 -m venv .venv'
sudo -u cliniss bash -lc 'cd /var/www/arsclinic/current/server && .venv/bin/python -m pip install --upgrade pip'
sudo -u cliniss bash -lc 'cd /var/www/arsclinic/current/server && .venv/bin/python -m pip install -r requirements.txt'
sudo -u cliniss bash -lc 'cd /var/www/arsclinic/current/server && set -a && . /var/www/arsclinic/shared/.env && set +a && .venv/bin/python manage.py migrate'
sudo -u cliniss bash -lc 'cd /var/www/arsclinic/current/server && set -a && . /var/www/arsclinic/shared/.env && set +a && .venv/bin/python manage.py collectstatic --noinput'
sudo -u cliniss bash -lc 'cd /var/www/arsclinic/current/server && set -a && . /var/www/arsclinic/shared/.env && set +a && .venv/bin/python manage.py check --deploy'
```

Последняя команда должна завершиться без предупреждений.

Создать администратора Django:

```bash
sudo -u cliniss bash -lc 'cd /var/www/arsclinic/current/server && set -a && . /var/www/arsclinic/shared/.env && set +a && .venv/bin/python manage.py createsuperuser'
```

Админка будет доступна по пути из `DJANGO_ADMIN_URL_PATH`, например `https://arsclinic.ru/<значение-из-env>`.

## 5. TLS-сертификат

До установки финального HTTPS-конфига выпустите сертификат через временный HTTP-конфиг:

```bash
sudo tee /etc/nginx/sites-available/arsclinic.ru >/dev/null <<'NGINX'
server {
    listen 80;
    server_name arsclinic.ru www.arsclinic.ru;

    location /.well-known/acme-challenge/ {
        root /var/www/letsencrypt;
    }

    location / {
        return 200 "arsclinic.ru certificate bootstrap";
    }
}
NGINX
sudo ln -sfn /etc/nginx/sites-available/arsclinic.ru /etc/nginx/sites-enabled/arsclinic.ru
sudo nginx -t
sudo systemctl reload nginx
sudo certbot certonly --webroot -w /var/www/letsencrypt -d arsclinic.ru -d www.arsclinic.ru
```

После выпуска сертификата установите финальный конфиг:

```bash
sudo cp /var/www/arsclinic/current/deploy/nginx_arsclinic.conf /etc/nginx/sites-available/arsclinic.ru
sudo nginx -t
sudo systemctl reload nginx
```

В готовом env и Nginx включены HSTS `includeSubDomains` и `preload`. Перед первым публичным запуском убедитесь, что все поддомены `arsclinic.ru` обслуживаются только по HTTPS. Если это не так, временно поставьте `DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=0`, `DJANGO_SECURE_HSTS_PRELOAD=0` и уберите `includeSubDomains; preload` из Nginx-заголовка.

## 6. systemd

```bash
sudo cp /var/www/arsclinic/current/deploy/cliniss.service /etc/systemd/system/cliniss.service
sudo systemctl daemon-reload
sudo systemctl enable --now cliniss
sudo systemctl status cliniss --no-pager
```

Логи приложения:

```bash
sudo journalctl -u cliniss -f
```

## 7. Smoke-test после запуска

```bash
curl -I http://arsclinic.ru/
curl -I https://arsclinic.ru/
curl -I https://arsclinic.ru/static/site/css/main.css
curl -I https://arsclinic.ru/robots.txt
curl -I https://arsclinic.ru/sitemap.xml
```

Ожидания:

- HTTP отдает `301` на HTTPS.
- HTTPS главной страницы отдает `200`.
- Есть заголовки `Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`.
- `/static/site/css/main.css` отдается Nginx без 404.
- `/admin/` не должен быть рабочей админкой, если в env задан скрытый `DJANGO_ADMIN_URL_PATH`.

## 8. Бэкапы SQLite и медиа

Минимальный ежедневный backup:

```bash
sudo install -d -o root -g root -m 0700 /var/backups/arsclinic
sudo sqlite3 /var/www/arsclinic/shared/db.sqlite3 ".backup '/var/backups/arsclinic/db-$(date +%F).sqlite3'"
sudo tar -C /var/www/arsclinic/shared -czf /var/backups/arsclinic/media-$(date +%F).tar.gz media
sudo find /var/backups/arsclinic -type f -mtime +30 -delete
```

Добавьте эти команды в root cron или systemd timer. База содержит персональные данные заявок, поэтому backups должны быть доступны только администратору сервера.

## 9. Обновление релиза

1. Распаковать новый архив в новый каталог внутри `/var/www/arsclinic/releases/`.
2. Переключить symlink `/var/www/arsclinic/current` на новый релиз.
3. Повторить установку venv-зависимостей, `migrate`, `collectstatic`, `check --deploy`.
4. Перезапустить сервис:
   ```bash
   sudo systemctl restart cliniss
   sudo systemctl status cliniss --no-pager
   ```
5. Выполнить smoke-test.

Rollback: вернуть symlink `/var/www/arsclinic/current` на предыдущий релиз и выполнить `sudo systemctl restart cliniss`.

## 10. Что не публиковать

- `.env`, `db.sqlite3`, backups, `.git`, `.venv`, старый Tilda-экспорт `cliniss/`, исходный zip Tilda, логи и любые файлы из `/var/www/arsclinic/shared`.
- Не запускать публичный сайт через `manage.py runserver`.
- Не открывать Waitress-порт `8010` наружу; он должен слушать только `127.0.0.1`.
