LANGUAGE_PAIRS = {
    '': 'en',
    'center': 'center-en',
    'license': 'license-en',
    'employees': 'employees-en',
    'missions': 'missions-en',
    'system': 'system-en',
    'areaswork': 'areaswork-en',
    'price': 'price-en',
    'volunteers': 'volunteers-en',
    'contacts': 'contacts-en',
    'docs': 'docs-en',
    'issledovaniya-bioekvivalentnosti': 'issledovaniya-bioekvivalentnosti-en',
    'policy': 'policy-en',
    'agreement': 'agreement-en',
}
LANGUAGE_PAIRS.update({value: key for key, value in list(LANGUAGE_PAIRS.items())})


LEAD_TYPE_LABELS = {
    'ru': {
        'proposal': 'Запросить коммерческое предложение',
        'callback': 'Заказать звонок',
        'volunteer': 'Анкета добровольца',
        'team': 'Стать частью команды',
        'review': 'Оставить отзыв',
        'study': 'Записаться на исследование',
        'question': 'Задать вопрос',
    },
    'en': {
        'proposal': 'Request a proposal',
        'callback': 'Request a callback',
        'volunteer': 'Volunteer form',
        'team': 'Join the team',
        'review': 'Leave feedback',
        'study': 'Apply for a study',
        'question': 'Ask a question',
    },
}


def lead_form_config(
    language,
    *,
    title=None,
    lead=None,
    default_type='proposal',
    types=None,
):
    labels = LEAD_TYPE_LABELS[language]
    selected_types = types or ('proposal', 'callback', 'question')
    return {
        'eyebrow': 'Request' if language == 'en' else 'Заявка',
        'title': title or ('Contact CLINISS' if language == 'en' else 'Связаться с CLINISS'),
        'lead': lead or '',
        'default_type': default_type,
        'types': [
            {'value': lead_type, 'label': labels[lead_type]}
            for lead_type in selected_types
        ],
        'submit_label': 'Send Request' if language == 'en' else 'Отправить заявку',
    }


def page(
    slug,
    language,
    title,
    nav_title,
    eyebrow,
    hero_title,
    hero_lead,
    sections,
    *,
    cta_label=None,
    show_lead_form=True,
    hero_image=None,
    stats=None,
    form_title=None,
    form_lead=None,
    default_lead_type='proposal',
    lead_types=None,
):
    return {
        'slug': slug,
        'language': language,
        'title': title,
        'nav_title': nav_title,
        'eyebrow': eyebrow,
        'hero_title': hero_title,
        'hero_lead': hero_lead,
        'sections': sections,
        'cta_label': cta_label,
        'show_lead_form': show_lead_form,
        'hero_image': hero_image,
        'stats': stats or [],
        'lead_form': lead_form_config(
            language,
            title=form_title,
            lead=form_lead,
            default_type=default_lead_type,
            types=lead_types,
        ),
        'alternate_slug': LANGUAGE_PAIRS.get(slug),
    }


def media(src, alt, caption=''):
    return {'src': src, 'alt': alt, 'caption': caption}


def fact(value, label):
    return {'value': value, 'label': label}


def card(title, text='', *, meta='', image='', alt='', value=''):
    return {
        'title': title,
        'text': text,
        'meta': meta,
        'image': image,
        'alt': alt,
        'value': value,
    }


def link(label, url, note='', external=True):
    return {'label': label, 'url': url, 'note': note, 'external': external}


def map_block(title, address, url, embed_url, button_label, note=''):
    return {
        'title': title,
        'address': address,
        'url': url,
        'embed_url': embed_url,
        'button_label': button_label,
        'note': note,
    }


TEAM_RU = [
    card('Устинья Жидкова', meta='менеджер по развитию бизнеса', image='site/img/team/ustinya-zhidkova.png'),
    card('Евгений Хайтович', meta='заместитель директора по клиническим исследованиям', image='site/img/team/evgeny-khaitovich.png'),
    card('Филиппова Полина', meta='заведующий отделением клинических исследований', image='site/img/team/polina-filippova.png'),
    card('Романова Анастасия', meta='менеджер по качеству', image='site/img/team/anastasia-romanova.png'),
    card('Зарифа Мустафаева', meta='медицинская сестра-регистратор', image='site/img/team/zarifa-mustafaeva.png'),
    card('Александрова Виктория', meta='медицинская сестра', image='site/img/team/victoria-aleksandrova.webp'),
    card('Гузаревич Любовь', meta='научный консультант', image='site/img/team/lubov-guzarevich.png'),
    card('Рыжова Снежана', meta='врач-кардиолог', image='site/img/team/snezhana-ryzhova.png'),
    card('Назарова Валерия', meta='врач-терапевт', image='site/img/team/valeria-nazarova.png'),
]

TEAM_EN = [
    card('Ustinia Zhidkova', meta='business development manager', image='site/img/team/ustinya-zhidkova.png'),
    card('Eugene Khaitovich', meta='deputy director for clinical trials', image='site/img/team/evgeny-khaitovich.png'),
    card('Polina Filippova', meta='head of clinical research department', image='site/img/team/polina-filippova.png'),
    card('Anastasia Romanova', meta='quality manager', image='site/img/team/anastasia-romanova.png'),
    card('Zarifa Mustafaeva', meta='registration nurse', image='site/img/team/zarifa-mustafaeva.png'),
    card('Victoria Aleksandrova', meta='nurse', image='site/img/team/victoria-aleksandrova.webp'),
    card('Lubov Guzarevich', meta='scientific consultant', image='site/img/team/lubov-guzarevich.png'),
    card('Snezhana Ryzhova', meta='cardiologist', image='site/img/team/snezhana-ryzhova.png'),
    card('Valeria Nazarova', meta='general practitioner', image='site/img/team/valeria-nazarova.png'),
]

CENTER_FACTS_RU = [
    fact('54', 'койко-места в палатах для добровольцев'),
    fact('3', 'холодовые центрифуги ThermoFisher'),
    fact('-40/-80°C', 'морозильное оборудование Haier'),
    fact('GCP', 'работа по международным стандартам исследований'),
]

CENTER_FACTS_EN = [
    fact('54', 'volunteer beds in the inpatient department'),
    fact('3', 'ThermoFisher refrigerated centrifuges'),
    fact('-40/-80°C', 'Haier freezer equipment'),
    fact('GCP', 'clinical trial processes aligned with global standards'),
]

AREAS_RU = [
    card('Функциональная диагностика', 'Комплексные исследования для оценки и мониторинга работы органов и систем организма, выявления функциональных нарушений и уточнения диагностики.'),
    card('Эндокринология', 'Исследования методов диагностики и лечения заболеваний эндокринной системы, коррекции гормональных нарушений и улучшения общего состояния пациентов.'),
    card('Клинические исследования', 'Оценка безопасности и эффективности новых методов лечения и лекарственных препаратов с учетом требований качества, этики и регуляторного контроля.'),
    card('Кардиология', 'Исследования и разработка подходов к диагностике и лечению сердечно-сосудистых заболеваний, направленные на улучшение качества жизни пациентов.'),
    card('Психиатрия и наркология', 'Изучение методов диагностики, лечения и поддержки пациентов с психическими расстройствами и зависимостями.'),
    card('Ревматология', 'Исследования заболеваний суставов и соединительных тканей, направленные на снижение боли, улучшение подвижности и качества жизни.'),
    card('Пульмонология', 'Исследования новых методов диагностики и лечения заболеваний органов дыхания, направленных на улучшение функции легких.'),
    card('Травматология и ортопедия', 'Исследования восстановления и реабилитации при травмах и повреждениях опорно-двигательного аппарата.'),
    card('Клиническая фармакология', 'Изучение воздействия лекарственных препаратов на организм, их эффективности, безопасности и возможностей оптимизации терапии.'),
    card('Неврология', 'Разработка и оценка новых подходов к диагностике и лечению заболеваний нервной системы.'),
]

AREAS_EN = [
    card('Functional Diagnostics', 'Comprehensive testing to assess and monitor organs and body systems, detect functional disorders, and support diagnostics.'),
    card('Endocrinology', 'Studies of diagnostic and treatment methods for endocrine diseases, hormonal disorders, and overall patient health improvement.'),
    card('Clinical Trials', 'Safety and efficacy evaluation of new treatment methods and medicines with quality, ethics, and regulatory control in mind.'),
    card('Cardiology', 'Research and development of approaches for cardiovascular diagnostics and therapy aimed at improving quality of life.'),
    card('Psychiatry and Narcology', 'Diagnostics, treatment, and patient support in mental health and addiction studies.'),
    card('Rheumatology', 'Studies focused on joint and connective tissue diseases, pain reduction, and mobility.'),
    card('Pulmonology', 'Studies of new diagnostics and treatment methods for respiratory diseases and lung function improvement.'),
    card('Traumatology and Orthopedics', 'Recovery and rehabilitation studies for musculoskeletal injuries.'),
    card('Clinical Pharmacology', 'Assessment of drug effects, efficacy, safety, and treatment optimization opportunities.'),
    card('Neurology', 'New approaches to diagnostics and treatment of nervous system diseases.'),
]

VOLUNTEER_FAQ_RU = [
    {
        'question': 'Что я получу за участие в исследованиях?',
        'answer': 'Интересно проведенное время, новые знакомства, бесплатную проверку здоровья и денежную компенсацию, если она предусмотрена условиями конкретного протокола.',
    },
    {
        'question': 'Безопасны ли клинические исследования?',
        'answer': 'Центр работает только с исследованиями, прошедшими необходимую оценку безопасности. Добровольца не включают в исследование при состояниях или заболеваниях, которые могут повысить риск. Команда стремится минимизировать риски на каждом этапе.',
    },
    {
        'question': 'Кто будет иметь доступ к персональным данным?',
        'answer': 'Персональные данные и медицинская тайна защищаются. При включении в исследование данные добровольца кодируются, а доступ к ним получают только уполномоченные участники исследовательского процесса.',
    },
    {
        'question': 'Могу ли я привести с собой друзей или членов семьи?',
        'answer': 'Да, если они соответствуют требованиям конкретного исследования. Каждый кандидат проходит отдельную анкету, информирование и скрининг; участие одного человека не гарантирует включение другого в тот же протокол.',
    },
    {
        'question': 'Как долго длится исследование?',
        'answer': 'Срок зависит от протокола. Обычно есть стартовый визит, беседа с врачом, лабораторные и клинические обследования, затем несколько визитов. Часто каждый период пребывания в центре длится от 24 до 48 часов.',
    },
    {
        'question': 'Что такое клиническое исследование?',
        'answer': 'Это комплекс мероприятий, который помогает вывести на рынок безопасный и эффективный лекарственный препарат. Клинические исследования проводятся по международным стандартам и регулируются российским законодательством.',
    },
    {
        'question': 'Может ли участие навредить мне?',
        'answer': 'Любой медицинский препарат имеет ограничения и возможные побочные эффекты. Перед включением оцениваются противопоказания и риски, а во время исследования доброволец находится под медицинским наблюдением.',
    },
    {
        'question': 'Как часто можно участвовать?',
        'answer': 'Как правило, участвовать в клинических исследованиях можно раз в 3 месяца и нельзя быть участником двух исследований одновременно.',
    },
    {
        'question': 'Что если я принимаю другие лекарства?',
        'answer': 'Обязательно сообщите об этом менеджеру и врачу. Во время исследования часто запрещено принимать другие препараты, витамины и биологически активные добавки; сроки отмены зависят от протокола.',
    },
    {
        'question': 'У меня есть вредные привычки. Это повлияет на участие?',
        'answer': 'Возможность участия зависит от протокола, результатов скрининга и критериев включения. Алкогольная или наркотическая зависимость обычно исключает участие. Курение может требовать временного отказа на период исследования.',
    },
    {
        'question': 'Что такое денежное вознаграждение?',
        'answer': 'Это компенсация за время и соблюдение процедур исследования. Размер и порядок выплаты зависят от протокола; при нарушении правил исследования выплата может не полагаться.',
    },
    {
        'question': 'Что делать, если я согласен с условиями?',
        'answer': 'Заполните анкету добровольца или закажите обратный звонок. Менеджер свяжется с вами и расскажет о ближайших наборах.',
    },
]

VOLUNTEER_FAQ_EN = [
    {
        'question': 'What will I get for participating?',
        'answer': 'A useful health check, new connections, time spent comfortably at the center, and financial compensation when it is provided by a specific protocol.',
    },
    {
        'question': 'Are clinical trials safe?',
        'answer': 'The center works with studies that have passed the required safety assessment. A volunteer will not be enrolled if medical findings or health conditions increase risk.',
    },
    {
        'question': 'Who can access my personal data?',
        'answer': 'Personal and medical data are protected. Once enrolled, volunteer data are coded, and access is limited to authorized participants in the research process.',
    },
    {
        'question': 'Can I bring friends or family members?',
        'answer': 'Yes, if they meet the requirements of a specific study. Every candidate completes a separate form, consent process, and screening; one person being eligible does not guarantee enrollment for another.',
    },
    {
        'question': 'How long does a study take?',
        'answer': 'Timing depends on the protocol. Usually there is a start visit, a physician conversation, lab and clinical checks, and several visits. A common stay format is 24 to 48 hours.',
    },
    {
        'question': 'What is a clinical study?',
        'answer': 'It is a set of procedures that helps bring a safe and effective medicine to market. Clinical studies follow international standards and are regulated by Russian law.',
    },
    {
        'question': 'Can participation harm me?',
        'answer': 'Any medicine may have limitations and possible side effects. Contraindications and risks are assessed before enrollment, and the volunteer is medically monitored throughout the study.',
    },
    {
        'question': 'How often can I participate?',
        'answer': 'Usually once every 3 months, and a volunteer cannot participate in two studies at the same time.',
    },
    {
        'question': 'What if I take other medicines?',
        'answer': 'Tell the manager and physician about all medicines. During many studies, other medicines, vitamins, and dietary supplements are restricted; timing depends on the protocol.',
    },
    {
        'question': 'Can habits affect participation?',
        'answer': 'Eligibility depends on the protocol, screening results, and inclusion criteria. Alcohol or drug dependence usually excludes participation. Smoking may need to be stopped during the study period.',
    },
    {
        'question': 'What is financial compensation?',
        'answer': 'It is compensation for time and study procedures. The amount and payment process depend on the protocol; compensation may not be paid if study rules are violated.',
    },
    {
        'question': 'What should I do if I agree with the conditions?',
        'answer': 'Fill out the volunteer form or request a callback. A manager will contact you and explain current recruitment options.',
    },
]

DOC_LINKS_RU = [
    link('Перечень жизненно необходимых и важнейших лекарственных препаратов', 'https://normativ.kontur.ru/document?moduleId=1&documentId=491464#l17', 'Контур.Норматив'),
    link('Перечень лекарственных препаратов для отдельных категорий заболеваний', 'https://normativ.kontur.ru/document?moduleId=1&documentId=491464#l5559', 'Контур.Норматив'),
    link('Перечень групп населения с 50-процентной скидкой на лекарства', 'https://normativ.kontur.ru/document?moduleId=1&documentId=61472#l1103', 'Контур.Норматив'),
    link('Лицензия организации на сайте Росздравнадзора', 'https://roszdravnadzor.gov.ru/services/licenses?qrguid=3b7bfa5fa5ada8922d28ae1d74d0ebd5', 'Росздравнадзор'),
    link('Структура организации', 'https://disk.yandex.ru/i/V63Iu60aFevphA', 'Яндекс.Диск'),
    link('Программа государственных гарантий медицинской помощи', 'https://www.garant.ru/products/ipo/prime/doc/411138101/', 'Гарант'),
    link('Сведения о медицинских работниках', 'https://disk.yandex.ru/i/qh_t2MgV98YNGA', 'Яндекс.Диск'),
    link('Политика об обработке персональных данных', 'https://disk.yandex.ru/i/zNO3XYku2JzNeg', 'Яндекс.Диск'),
    link('Информированное добровольное согласие на медицинское вмешательство', 'https://disk.yandex.ru/i/oEXu78YjBmLc4g', 'Яндекс.Диск'),
]

DOC_LINKS_EN = [
    link('Vital and Essential Medicines List', 'https://normativ.kontur.ru/document?moduleId=1&documentId=491464#l17', 'Kontur.Normativ'),
    link('Medicines for Certain Disease Categories', 'https://normativ.kontur.ru/document?moduleId=1&documentId=491464#l5559', 'Kontur.Normativ'),
    link('Medicine Discount Eligibility List', 'https://normativ.kontur.ru/document?moduleId=1&documentId=61472#l1103', 'Kontur.Normativ'),
    link('Organization License at Roszdravnadzor', 'https://roszdravnadzor.gov.ru/services/licenses?qrguid=3b7bfa5fa5ada8922d28ae1d74d0ebd5', 'Roszdravnadzor'),
    link('Organizational Structure', 'https://disk.yandex.ru/i/V63Iu60aFevphA', 'Yandex Disk'),
    link('State Guarantees Program for Medical Care', 'https://www.garant.ru/products/ipo/prime/doc/411138101/', 'Garant'),
    link('Medical Staff Details', 'https://disk.yandex.ru/i/qh_t2MgV98YNGA', 'Yandex Disk'),
    link('Personal Data Processing Policy', 'https://disk.yandex.ru/i/zNO3XYku2JzNeg', 'Yandex Disk'),
    link('Informed Voluntary Consent for Medical Intervention', 'https://disk.yandex.ru/i/oEXu78YjBmLc4g', 'Yandex Disk'),
]

CONTACT_LINKS_RU = [
    link('Телефон центра', 'tel:+79091578618', '+7 (909) 157-86-18', external=False),
    link('Email', 'mailto:info@arsclinic.ru', 'info@arsclinic.ru', external=False),
    link('Telegram', 'https://t.me/cliniss_tver', 'Канал связи с центром'),
    link('WhatsApp', 'https://wa.me/79091578618', 'Быстрое сообщение'),
    link('VK', 'https://vk.com/cliniss_tver', 'Сообщество CLINISS'),
]

CONTACT_LINKS_EN = [
    link('Center phone', 'tel:+79091578618', '+7 (909) 157-86-18', external=False),
    link('Email', 'mailto:info@arsclinic.ru', 'info@arsclinic.ru', external=False),
    link('Telegram', 'https://t.me/cliniss_tver', 'Contact channel'),
    link('WhatsApp', 'https://wa.me/79091578618', 'Quick message'),
    link('VK', 'https://vk.com/cliniss_tver', 'CLINISS community'),
]

YANDEX_MAPS_ORG_URL = 'https://yandex.ru/maps/org/cliniss/80092053546/'
YANDEX_MAPS_REVIEWS_URL = 'https://yandex.ru/maps/org/cliniss/80092053546/reviews/'
YANDEX_MAPS_WIDGET_URL = 'https://yandex.ru/map-widget/v1/?mode=search&oid=80092053546&ol=biz&z=16'

CONTACT_MAP_RU = map_block(
    'CLINISS на карте',
    '170100, г. Тверь, Вагжановский переулок, 9, 2 этаж',
    YANDEX_MAPS_ORG_URL,
    YANDEX_MAPS_WIDGET_URL,
    'Открыть в Яндекс Картах',
    'Вход в центр расположен на 2 этаже. Перед визитом на скрининг дождитесь подтверждения времени от менеджера.',
)

CONTACT_MAP_EN = map_block(
    'CLINISS on the Map',
    '2nd floor, 9 Vagzhanovsky lane, Tver, Russian Federation, 170100',
    YANDEX_MAPS_ORG_URL,
    YANDEX_MAPS_WIDGET_URL,
    'Open in Yandex Maps',
    'The center is located on the 2nd floor. Please wait for the manager to confirm your screening time before visiting.',
)


PAGES = {
    '': page(
        '',
        'ru',
        'CLINISS - Современный центр клинических исследований биоэквивалентности и ранних фаз',
        'Главная',
        'Современный центр клинических исследований',
        'CLINISS',
        'Центр ориентирован на проведение клинических исследований биоэквивалентности и ранних фаз, а также исследований эффективности, безопасности и терапевтической эквивалентности.',
        [
            {
                'title': 'О центре',
                'body': [
                    'CLINISS - это современный центр клинических исследований, оборудованный по последнему слову техники.',
                    'Мы специализируемся на исследованиях биоэквивалентности и ранних фаз, а также предлагаем широкие возможности для изучения эффективности, безопасности и терапевтической эквивалентности препаратов.',
                ],
                'image': media('site/img/photos/center-equipment.png', 'Оборудование CLINISS для хранения и контроля образцов'),
            },
            {
                'title': 'Наша работа в цифрах',
                'body': [
                    'Мы оставили на главной только те показатели, которые помогают быстро понять масштаб центра и его исследовательскую инфраструктуру.',
                ],
                'facts': [
                    fact('54', 'койко-места в палатах для добровольцев'),
                    fact('50+', 'завершенных исследований'),
                    fact('600+', 'добровольцев в базе центра'),
                    fact('15+', 'партнеров и фармацевтических компаний'),
                ],
            },
            {
                'title': 'Фотогалерея',
                'body': [
                    'Реальные рабочие зоны центра без случайных декоративных изображений: оборудование, амбулаторное обследование и палата для добровольцев.',
                ],
                'images': [
                    media('site/img/photos/center-equipment.png', 'Лабораторное оборудование центра'),
                    media('site/img/photos/outpatient-checkup.jpeg', 'Амбулаторный прием и обследование добровольца'),
                    media('site/img/photos/patient-room.png', 'Палата для добровольцев CLINISS'),
                ],
            },
            {
                'title': 'Слово специалиста',
                'body': [
                    'Основа нашей работы - принцип GCP: благополучие добровольца превыше всего.',
                    'От начала и до конца исследования мы сопровождаем вас, создавая атмосферу комфорта и полного понимания. Прозрачность условий, внимательное, индивидуальное отношение к каждому добровольцу, ваши комфорт и безопасность - наши приоритеты.',
                ],
                'image': media('site/img/photos/doctor-documents.jpeg', 'Врач CLINISS работает с документами исследования'),
                'image_position': 'left',
            },
            {
                'title': 'Готовы внести вклад в будущее медицины?',
                'body': [
                    'Анкета добровольца открывается отдельной страницей: там собраны условия участия, FAQ и форма заявки.',
                ],
                'cta_label': 'Заполнить анкету добровольца',
                'cta_url': '/volunteers',
            },
            {
                'title': 'Отзывы на Яндекс Картах',
                'body': [
                    'Актуальную обратную связь удобнее смотреть в карточке организации: там обновляются рейтинг, оценки и новые отзывы.',
                    'По данным Яндекс Карт у CLINISS отмечают внимательное отношение персонала, чистоту помещений и комфортные условия участия в исследованиях.',
                ],
                'facts': [
                    fact('4,8', 'рейтинг организации на Яндекс Картах'),
                    fact('24', 'оценки в карточке организации'),
                    fact('17', 'отзывов доступно для чтения'),
                ],
                'links': [
                    link('Смотреть отзывы CLINISS', YANDEX_MAPS_REVIEWS_URL, 'Яндекс Карты'),
                ],
            },
        ],
        cta_label='Связаться с центром',
        hero_image='site/img/hero-lab.jpg',
        stats=[fact('50+', 'завершенных исследований'), fact('600+', 'добровольцев'), fact('15+', 'партнеров')],
        form_title='Обсудить исследование',
        form_lead='Оставьте контактные данные, если хотите запросить коммерческое предложение, звонок или консультацию по исследованию.',
        default_lead_type='proposal',
        lead_types=('proposal', 'callback', 'study', 'question'),
    ),
    'en': page(
        'en',
        'en',
        'CLINISS - Modern Clinical Research Center',
        'Home',
        'Modern Clinical Research Center',
        'CLINISS',
        'A clinical research center for bioequivalence and early-phase studies with modern infrastructure, skilled specialists, and transparent processes.',
        [
            {
                'title': 'About the Center',
                'body': [
                    'CLINISS is a modern clinical research center equipped with advanced technology.',
                    'We specialize in bioequivalence and early-phase studies and provide broad capabilities for studying drug efficacy, safety, and therapeutic equivalence.',
                ],
                'image': media('site/img/photos/center-equipment.png', 'CLINISS equipment for sample storage and control'),
            },
            {
                'title': 'Our Work in Numbers',
                'body': [
                    'The home page keeps the core indicators that explain the center scale and research infrastructure at a glance.',
                ],
                'facts': [
                    fact('54', 'volunteer beds in the inpatient department'),
                    fact('50+', 'completed studies'),
                    fact('600+', 'volunteers in the center database'),
                    fact('15+', 'partners and pharmaceutical companies'),
                ],
            },
            {
                'title': 'Photo Gallery',
                'body': [
                    'Real working areas of the center without random decorative images: equipment, outpatient screening, and a volunteer room.',
                ],
                'images': [
                    media('site/img/photos/center-equipment.png', 'Center laboratory equipment'),
                    media('site/img/photos/outpatient-checkup.jpeg', 'Outpatient checkup and volunteer screening'),
                    media('site/img/photos/patient-room.png', 'Volunteer room at CLINISS'),
                ],
            },
            {
                'title': 'Specialist Note',
                'body': [
                    'The foundation of our work is the GCP principle: volunteer well-being comes first.',
                    'From the beginning to the end of a study, we guide each participant with comfort, clarity, transparent conditions, and attentive individual support.',
                ],
                'image': media('site/img/photos/doctor-documents.jpeg', 'CLINISS doctor working with study documents'),
                'image_position': 'left',
            },
            {
                'title': 'Ready to Contribute to the Future of Medicine?',
                'body': [
                    'The volunteer questionnaire is available on a dedicated page with participation conditions, FAQ, and the request form.',
                ],
                'cta_label': 'Fill Out the Volunteer Form',
                'cta_url': '/volunteers-en',
            },
            {
                'title': 'Yandex Maps Reviews',
                'body': [
                    'The current feedback is best viewed in the organization profile where the rating, scores, and new reviews are updated.',
                    'According to Yandex Maps, visitors mention attentive staff, clean rooms, and comfortable study participation conditions.',
                ],
                'facts': [
                    fact('4.8', 'organization rating on Yandex Maps'),
                    fact('24', 'scores in the organization profile'),
                    fact('17', 'reviews available to read'),
                ],
                'links': [
                    link('View CLINISS reviews', YANDEX_MAPS_REVIEWS_URL, 'Yandex Maps'),
                ],
            },
        ],
        cta_label='Contact the Center',
        hero_image='site/img/hero-lab.jpg',
        stats=[fact('50+', 'completed studies'), fact('600+', 'volunteers'), fact('15+', 'partners')],
        form_title='Discuss a Study',
        form_lead='Leave your contact details to request a proposal, callback, or study consultation.',
        default_lead_type='proposal',
        lead_types=('proposal', 'callback', 'study', 'question'),
    ),
    'center': page(
        'center',
        'ru',
        'CLINISS / Наш центр',
        'Наш центр',
        'О центре',
        'Наш центр',
        'Центр ориентирован на проведение клинических исследований биоэквивалентности и обладает широкими возможностями для исследований эффективности, безопасности и терапевтической эквивалентности.',
        [
            {
                'title': 'Инфраструктура и контроль',
                'body': [
                    'Точность исследований обеспечивают современное оборудование, технологичная преаналитическая лаборатория и соблюдение стандартов GCP.',
                    'В центре используются системы дистанционного контроля: HOST CALL для вызова медсестер и врачей, СКУД, Unimon для контроля климата помещений и холодильников, видеоконтроль и синхронизированные часы.',
                ],
                'facts': CENTER_FACTS_RU,
                'image': media('site/img/photos/center-equipment.png', 'Оборудование CLINISS для контроля хранения образцов'),
            },
            {
                'title': 'Амбулаторное отделение',
                'body': ['Отделение включает врачебные кабинеты, процедурный кабинет, сухой туалет для сбора мочи, современное диагностическое оборудование и переговорную комнату.'],
                'bullets': ['Врачебные кабинеты', 'Процедурный кабинет', 'Сбор биоматериала', 'Диагностическое оборудование', 'Переговорная комната'],
                'image': media('site/img/photos/outpatient-checkup.jpeg', 'Амбулаторное обследование добровольца'),
                'image_position': 'left',
            },
            {
                'title': 'Стационарное отделение',
                'body': [
                    'Для участников исследований предусмотрены палаты, реанимационная зона, большой процедурный кабинет, контролируемый доступ, санитарные зоны и система экстренного вызова у каждой койки.',
                ],
                'bullets': ['54 койко-места', 'Палаты для добровольцев', 'Реанимационная зона', 'Контролируемый доступ', 'Санитарные зоны', 'Экстренный вызов'],
                'image': media('site/img/photos/patient-room.png', 'Палата для добровольцев'),
            },
            {
                'title': 'Условия для исследований',
                'body': [
                    'Центр располагает холодовыми центрифугами ThermoFisher, морозильным оборудованием Haier для раздельного хранения архивных и аналитических аликвот, обособленным архивом и комнатами хранения лекарственных средств.',
                ],
                'bullets': ['Преаналитическая лаборатория', 'Хранение -40°C и -80°C', 'Архив', 'Рабочие места для мониторов', 'Wi-Fi с идентификацией пользователей'],
                'image': media('site/img/photos/lab-tubes.jpg', 'Преаналитическая зона CLINISS'),
                'image_position': 'left',
            },
            {
                'title': 'Реквизиты организации',
                'body': [
                    'Общество с ограниченной ответственностью «АРС Клинический Центр». Лицензия на осуществление медицинской деятельности № Л041-01186-69/01327284 от 31.07.2024 г.',
                    'Директор: Тихонов Михаил Юрьевич. ИНН: 7709986403. КПП: 695001001. ОГРН: 1177746054430. Юридический адрес: 170100, Тверская область, г. Тверь, пер. Вагжановский, д. 9, эт/пом 2/1.',
                ],
            },
        ],
        cta_label='Связаться с центром',
        hero_image='site/img/photos/center-equipment.png',
        form_title='Связаться с центром',
        form_lead='Расскажите, какой вопрос хотите обсудить: исследование, визит, документы или партнерство.',
        default_lead_type='callback',
        lead_types=('callback', 'proposal', 'question'),
    ),
    'center-en': page(
        'center-en',
        'en',
        'CLINISS / About the Center',
        'About the Center',
        'About the Center',
        'About the Center',
        'The modern CLINISS center offers bioequivalence, early-phase, therapeutic equivalence, efficacy, and safety studies.',
        [
            {
                'title': 'Infrastructure and Control',
                'body': [
                    'Study accuracy is supported by modern equipment, a technological pre-analytical laboratory, and GCP-aligned procedures.',
                    'The center uses remote monitoring systems, access control, climate monitoring for rooms and freezers, video monitoring, and synchronized clocks.',
                ],
                'facts': CENTER_FACTS_EN,
                'image': media('site/img/photos/center-equipment.png', 'CLINISS equipment for sample storage control'),
            },
            {
                'title': 'Outpatient Department',
                'body': ['The outpatient area includes doctor offices, a procedure room, a dry toilet for urine collection, modern diagnostics, and a meeting room.'],
                'bullets': ['Doctor offices', 'Procedure room', 'Sample collection', 'Diagnostic equipment', 'Meeting room'],
                'image': media('site/img/photos/outpatient-checkup.jpeg', 'Outpatient volunteer checkup'),
                'image_position': 'left',
            },
            {
                'title': 'Inpatient Department',
                'body': ['The inpatient department provides volunteer rooms, an intensive care area, a large procedure room, controlled access, sanitary zones, and emergency call systems.'],
                'bullets': ['54 beds', 'Volunteer rooms', 'Intensive care area', 'Controlled access', 'Sanitary zones', 'Emergency call system'],
                'image': media('site/img/photos/patient-room.png', 'Volunteer room'),
            },
            {
                'title': 'Clinical Trial Conditions',
                'body': ['The center has ThermoFisher refrigerated centrifuges, Haier -40°C and -80°C freezers for separate archival and analytical aliquot storage, an isolated archive, and medicine storage areas.'],
                'bullets': ['Pre-analytical laboratory', '-40°C and -80°C storage', 'Archive', 'Monitor workspaces', 'Wi-Fi with user identification'],
                'image': media('site/img/photos/lab-tubes.jpg', 'CLINISS pre-analytical area'),
                'image_position': 'left',
            },
        ],
        cta_label='Contact the Center',
        hero_image='site/img/photos/center-equipment.png',
        form_title='Contact the Center',
        form_lead='Tell us what you would like to discuss: a study, visit, documents, or partnership.',
        default_lead_type='callback',
        lead_types=('callback', 'proposal', 'question'),
    ),
    'license': page(
        'license',
        'ru',
        'CLINISS / Лицензия',
        'Лицензия',
        'Документы',
        'Лицензия',
        'Лицензия на осуществление медицинской деятельности Л041-01186-69/01327284 от 31.07.2024.',
        [
            {
                'title': 'Медицинская деятельность',
                'body': [
                    'ООО «АРС Клинический Центр» имеет лицензию на осуществление медицинской деятельности № Л041-01186-69/01327284 от 31.07.2024.',
                    'Для публичной проверки доступна ссылка на реестр лицензий Росздравнадзора.',
                ],
                'links': [link('Проверить лицензию на сайте Росздравнадзора', 'https://roszdravnadzor.gov.ru/services/licenses?qrguid=3b7bfa5fa5ada8922d28ae1d74d0ebd5', 'Росздравнадзор')],
            },
            {
                'title': 'Скан-копии',
                'body': ['Из Tilda-экспорта перенесены изображения страниц лицензии.'],
                'images': [
                    media('site/img/documents/license-page-1.png', 'Первая страница лицензии CLINISS'),
                    media('site/img/documents/license-page-2.png', 'Вторая страница лицензии CLINISS'),
                ],
                'gallery_style': 'documents',
            },
        ],
        show_lead_form=False,
        hero_image='site/img/documents/license-page-1.png',
    ),
    'license-en': page(
        'license-en',
        'en',
        'CLINISS / Licenses',
        'Licenses',
        'Documents',
        'Licenses',
        'Medical activity license No. Л041-01186-69/01327284 dated 31.07.2024.',
        [
            {
                'title': 'Medical Activity',
                'body': [
                    'ARS Clinical Center LLC holds medical activity license No. Л041-01186-69/01327284 dated 31.07.2024.',
                    'The public register entry is available through Roszdravnadzor.',
                ],
                'links': [link('Check the license in the Roszdravnadzor register', 'https://roszdravnadzor.gov.ru/services/licenses?qrguid=3b7bfa5fa5ada8922d28ae1d74d0ebd5', 'Roszdravnadzor')],
            },
            {
                'title': 'Scans',
                'body': ['License page images have been migrated from the Tilda export.'],
                'images': [
                    media('site/img/documents/license-page-1.png', 'CLINISS license page one'),
                    media('site/img/documents/license-page-2.png', 'CLINISS license page two'),
                ],
                'gallery_style': 'documents',
            },
        ],
        show_lead_form=False,
        hero_image='site/img/documents/license-page-1.png',
    ),
    'employees': page(
        'employees',
        'ru',
        'CLINISS / Наши сотрудники',
        'Наши сотрудники',
        'Команда',
        'Наши сотрудники',
        'Команда центра включает врачей, специалистов по качеству, клиническим исследованиям, медицинскому сопровождению и развитию бизнеса.',
        [
            {
                'title': 'Специалисты CLINISS',
                'body': ['Карточки сотрудников перенесены из Tilda в структурированный формат с фотографиями и должностями.'],
                'cards': TEAM_RU,
                'card_style': 'people',
            },
            {
                'title': 'Хотите стать частью нашей команды?',
                'body': ['Оставьте заявку, и мы свяжемся с вами, чтобы обсудить возможное сотрудничество и открытые роли.'],
            },
        ],
        cta_label='Стать частью команды',
        hero_image='site/img/graphics/proposal-banner.png',
        stats=[fact('9', 'специалистов в карточках'), fact('GCP', 'опыт исследований'), fact('4', 'ключевых направления команды')],
        form_title='Стать частью команды',
        form_lead='Расскажите о себе и возможном формате сотрудничества с CLINISS. В комментарии можно оставить ссылку на резюме, например на hh.ru.',
        default_lead_type='team',
        lead_types=('team', 'question', 'callback'),
    ),
    'employees-en': page(
        'employees-en',
        'en',
        'CLINISS / Team',
        'Team',
        'Team',
        'Our Team',
        'The center team includes doctors, quality specialists, clinical research staff, medical support, and business development specialists.',
        [
            {
                'title': 'CLINISS Specialists',
                'body': ['Employee cards have been migrated from Tilda into a structured format with photos and roles.'],
                'cards': TEAM_EN,
                'card_style': 'people',
            },
            {
                'title': 'Want to Become Part of the Team?',
                'body': ['Submit a request and we will contact you to discuss possible cooperation and open roles.'],
            },
        ],
        cta_label='Become Part of the Team',
        hero_image='site/img/graphics/proposal-banner.png',
        stats=[fact('9', 'specialists in profiles'), fact('GCP', 'clinical trial experience'), fact('4', 'key team areas')],
        form_title='Become Part of the Team',
        form_lead='Tell us about yourself and the possible cooperation format with CLINISS. You can add a link to your CV or profile in the comment.',
        default_lead_type='team',
        lead_types=('team', 'question', 'callback'),
    ),
    'missions': page(
        'missions',
        'ru',
        'CLINISS / Наша миссия',
        'Миссия',
        'Ценности',
        'Наша миссия',
        'Внести вклад в развитие медицины и улучшить здоровье людей.',
        [
            {
                'title': 'Миссия и ценности',
                'body': ['CLINISS строит работу вокруг открытости, честности, развития и уважения к человеку.'],
                'cards': [
                    card('Открытость', 'Наши двери открыты: мы доступны партнерам, клиентам, новым сотрудникам и добровольцам.'),
                    card('Настройка', 'Мы открыты новым идеям, готовы к экспериментам и умеем находить нестандартные решения.'),
                    card('Совершенствование', 'Мы учимся, развиваем навыки и используем современные научные и технологические подходы.'),
                    card('Человек', 'Главная ценность - добровольцы, пациенты, сотрудники, клиенты и партнеры.'),
                ],
                'image': media('site/img/graphics/cliniss-wave-brand.jpg', 'Фирменная графика CLINISS'),
            }
        ],
        hero_image='site/img/graphics/cliniss-wave-brand.jpg',
        form_title='Связаться по вопросам сотрудничества',
        form_lead='Напишите, если хотите обсудить партнерство, работу центра или участие в исследованиях.',
        default_lead_type='question',
        lead_types=('question', 'callback', 'proposal', 'volunteer'),
    ),
    'missions-en': page(
        'missions-en',
        'en',
        'CLINISS / Mission',
        'Mission',
        'Values',
        'Mission',
        "To contribute to the advancement of medicine and improve people's health.",
        [
            {
                'title': 'Mission and Values',
                'body': ['CLINISS builds its work around accessibility, openness, refinement, and respect for people.'],
                'cards': [
                    card('Accessibility', 'Our doors are open to partners, clients, employees, and volunteers.'),
                    card('Tuning', 'We stay open to new ideas, experiments, and unconventional solutions.'),
                    card('Refinement', 'We learn, improve skills, and use modern scientific and technological approaches.'),
                    card('Person', 'Our main value is the person: volunteers, patients, employees, clients, and partners.'),
                ],
                'image': media('site/img/graphics/cliniss-wave-brand.jpg', 'CLINISS brand graphic'),
            }
        ],
        hero_image='site/img/graphics/cliniss-wave-brand.jpg',
        form_title='Contact Us About Cooperation',
        form_lead='Write to discuss partnership, center operations, or participation in studies.',
        default_lead_type='question',
        lead_types=('question', 'callback', 'proposal', 'volunteer'),
    ),
    'system': page(
        'system',
        'ru',
        'CLINISS / Система качества',
        'Система качества',
        'Качество',
        'Система качества',
        'Система качества CLINISS развивается на основе международного стандарта ISO 9001:2015 и регуляторных требований.',
        [
            {
                'title': 'Цели системы качества',
                'body': [
                    'Система качества CLINISS имеет две взаимосвязанные цели: соответствовать нормативным требованиям и постоянно повышать эффективность и конкурентоспособность.',
                ],
                'bullets': ['Стандарты и регламенты', 'Контроль процессов', 'Планирование качества', 'Обеспечение качества', 'Контроль качества', 'Улучшение качества'],
                'cards': [
                    card('Отвечать требованиям', 'Регуляторные и нормативные требования учитываются в процедурах, документации и ежедневном контроле.'),
                    card('Повышать эффективность', 'Процессы регулярно пересматриваются, чтобы сохранять конкурентоспособность и устойчивое качество исследований.'),
                ],
                'image': media('site/img/photos/center-equipment.png', 'Контроль оборудования и условий хранения'),
            }
        ],
        hero_image='site/img/photos/center-equipment.png',
        form_title='Задать вопрос о системе качества',
        form_lead='Оставьте вопрос по стандартам, процедурам или требованиям к проведению исследований.',
        default_lead_type='question',
        lead_types=('question', 'proposal', 'callback'),
    ),
    'system-en': page(
        'system-en',
        'en',
        'CLINISS / Quality Management System',
        'Quality Management System',
        'Quality',
        'Quality Management System',
        'The CLINISS quality management system is developed around ISO 9001:2015 and regulatory requirements.',
        [
            {
                'title': 'Quality Goals',
                'body': [
                    'The CLINISS quality management system has two interconnected goals: meet regulatory requirements and continuously improve effectiveness and competitiveness.',
                ],
                'bullets': ['Standards and regulations', 'Process control', 'Quality planning', 'Quality assurance', 'Quality control', 'Quality improvement'],
                'cards': [
                    card('Meet Requirements', 'Regulatory requirements are reflected in procedures, documentation, and day-to-day control.'),
                    card('Improve Effectiveness', 'Processes are reviewed to maintain competitiveness and stable clinical trial quality.'),
                ],
                'image': media('site/img/photos/center-equipment.png', 'Equipment and storage condition control'),
            }
        ],
        hero_image='site/img/photos/center-equipment.png',
        form_title='Ask About Quality Management',
        form_lead='Leave a question about standards, procedures, or clinical trial requirements.',
        default_lead_type='question',
        lead_types=('question', 'proposal', 'callback'),
    ),
    'areaswork': page(
        'areaswork',
        'ru',
        'CLINISS / Направления работы',
        'Направления работы',
        'Услуги',
        'Направления работы',
        'Центр проводит широкий спектр научных исследований, направленных на развитие медицины и внедрение новых решений.',
        [
            {
                'title': 'Исследовательские направления',
                'body': [
                    'CLINISS ориентирован на широкий спектр научных исследований, направленных на совершенствование и развитие медицины.',
                    'Мы стремимся к созданию и внедрению решений, которые могут значительно улучшить качество жизни людей и дать новый импульс развитию медицинских технологий.',
                ],
                'cards': AREAS_RU,
                'card_style': 'compact',
                'image': media('site/img/photos/bioequivalence-lab.png', 'Лабораторная работа с образцами'),
            },
            {
                'title': 'Для добровольцев',
                'body': [
                    'Мы всегда ищем добровольцев для участия в передовых клинических исследованиях. Это возможность внести вклад в развитие медицины и помочь улучшить здоровье миллионов людей.',
                    'Заполните анкету или закажите обратный звонок, чтобы начать путь к участию в исследованиях.',
                ],
                'links': [
                    link('Узнать больше', '/volunteers', 'Раздел для добровольцев', external=False),
                    link('Заполнить анкету', '#lead-form', 'Форма на этой странице', external=False),
                ],
                'image': media('site/img/photos/volunteer-path.png', 'Путь добровольца в исследовании'),
                'image_position': 'left',
            },
        ],
        cta_label='Запросить предложение',
        hero_image='site/img/photos/research-hero.png',
        form_title='Запросить предложение',
        form_lead='Опишите интересующее направление, протокол или задачу, чтобы команда подготовила следующий шаг.',
        default_lead_type='proposal',
        lead_types=('proposal', 'study', 'question', 'callback'),
    ),
    'areaswork-en': page(
        'areaswork-en',
        'en',
        'CLINISS / Areas of Work',
        'Areas of Work',
        'Services',
        'Areas of Work',
        'The center conducts a broad range of scientific studies aimed at medical development and implementation of new solutions.',
        [
            {
                'title': 'Research Areas',
                'body': [
                    'CLINISS focuses on a broad range of scientific studies aimed at improving and developing medicine.',
                    'We work on solutions that can significantly improve quality of life and support the development of medical technologies.',
                ],
                'cards': AREAS_EN,
                'card_style': 'compact',
                'image': media('site/img/photos/bioequivalence-lab.png', 'Laboratory work with samples'),
            },
            {
                'title': 'For Volunteers',
                'body': [
                    'We invite volunteers to participate in advanced clinical studies and contribute to the future of medicine.',
                    'Fill out the form or request a callback to start your pathway toward participation.',
                ],
                'links': [
                    link('Learn more', '/volunteers-en', 'Volunteer section', external=False),
                    link('Fill out the form', '#lead-form', 'Form on this page', external=False),
                ],
                'image': media('site/img/photos/volunteer-path.png', 'Volunteer pathway in a study'),
                'image_position': 'left',
            },
        ],
        cta_label='Request a Proposal',
        hero_image='site/img/photos/research-hero.png',
        form_title='Request a Proposal',
        form_lead='Describe the area, protocol, or task of interest so the team can prepare the next step.',
        default_lead_type='proposal',
        lead_types=('proposal', 'study', 'question', 'callback'),
    ),
    'price': page(
        'price',
        'ru',
        'CLINISS / Прайс',
        'Прайс',
        'Стоимость',
        'Прайс',
        'Цены зависят от протокола, состава процедур, сроков и требований исследования.',
        [
            {
                'title': 'Коммерческое предложение',
                'body': [
                    'Центр готов предоставить подробную информацию об услугах и исследованиях. Мы предлагаем прозрачные и конкурентные условия, соответствующие высокому качеству и стандартам медицинских исследований.',
                    'Для детальной информации о расчетах, возможных скидках и составе работ свяжитесь с нами или запросите обратный звонок.',
                ],
                'bullets': ['Исследования биоэквивалентности', 'Ранние фазы', 'Эффективность и безопасность', 'Терапевтическая эквивалентность'],
                'cards': [
                    card('Расчет по протоколу', 'Стоимость зависит от дизайна исследования, числа периодов, процедур, длительности пребывания и требований к отчетности.'),
                    card('Коммерческое предложение', 'Команда подготовит предложение после уточнения задач, сроков, объема медицинских процедур и логистики образцов.'),
                ],
                'image': media('site/img/graphics/proposal-banner.png', 'Фирменный баннер CLINISS для коммерческого предложения'),
            }
        ],
        cta_label='Запросить коммерческое предложение',
        hero_image='site/img/graphics/proposal-banner.png',
        form_title='Запросить коммерческое предложение',
        form_lead='Оставьте вводные по исследованию: команда уточнит протокол, сроки, процедуры и логистику образцов.',
        default_lead_type='proposal',
        lead_types=('proposal', 'callback', 'question'),
    ),
    'price-en': page(
        'price-en',
        'en',
        'CLINISS / Price',
        'Price',
        'Pricing',
        'Price',
        'Pricing depends on the protocol, procedures, timelines, and study requirements.',
        [
            {
                'title': 'Commercial Proposal',
                'body': [
                    'The center is ready to provide detailed information about services and trials. We offer transparent and competitive conditions aligned with high medical research standards.',
                    'For detailed calculations, possible discounts, and scope of work, contact us or request a callback.',
                ],
                'bullets': ['Bioequivalence studies', 'Early phases', 'Efficacy and safety', 'Therapeutic equivalence'],
                'cards': [
                    card('Protocol-Based Estimate', 'Pricing depends on study design, number of periods, procedures, length of stay, and reporting requirements.'),
                    card('Commercial Proposal', 'The team prepares a proposal after clarifying objectives, timelines, medical procedures, and sample logistics.'),
                ],
                'image': media('site/img/graphics/proposal-banner.png', 'CLINISS proposal banner'),
            }
        ],
        cta_label='Request a Proposal',
        hero_image='site/img/graphics/proposal-banner.png',
        form_title='Request a Commercial Proposal',
        form_lead='Share initial study details: the team will clarify protocol, timeline, procedures, and sample logistics.',
        default_lead_type='proposal',
        lead_types=('proposal', 'callback', 'question'),
    ),
    'volunteers': page(
        'volunteers',
        'ru',
        'CLINISS / Для добровольцев',
        'Для добровольцев',
        'Добровольцам',
        'Хочешь стать добровольцем?',
        'Участие в клинических исследованиях помогает современной медицине и дает возможность проконтролировать состояние здоровья.',
        [
            {
                'title': 'Почему участвуют',
                'body': [
                    'Во время исследования у вас будет возможность проконтролировать и оценить состояние своего здоровья, познакомиться с новыми людьми и провести время с пользой.',
                    'Для здоровых добровольцев участие в клинических исследованиях - это не только возможность помочь современной медицине. Участие оплачивается, если это предусмотрено конкретным протоколом.',
                ],
                'image': media('site/img/photos/volunteer-path.png', 'Путь добровольца в клиническом исследовании'),
            },
            {
                'title': 'Часто задаваемые вопросы',
                'body': ['Мы собрали основные вопросы, которые добровольцы задают перед участием в исследованиях.'],
                'faq': VOLUNTEER_FAQ_RU,
            },
            {
                'title': 'Кому подходит участие',
                'body': [
                    'К участию приглашаются лица старше 18 лет без острых и хронических заболеваний, а также без противопоказаний по критериям конкретного протокола.',
                    'Перед включением доброволец проходит информированное согласие, медицинский осмотр и скрининг.',
                ],
                'bullets': ['Старше 18 лет', 'Без острых и хронических заболеваний', 'Без противопоказаний протокола', 'Беременные и кормящие женщины не участвуют', 'Информированное согласие', 'Медицинский скрининг'],
                'image': media('site/img/photos/outpatient-checkup.jpeg', 'Скрининг добровольца в CLINISS'),
                'image_position': 'left',
            },
            {
                'title': 'Как стать добровольцем',
                'body': [
                    'Достаточно заполнить анкету или заказать обратный звонок. Мы свяжемся с вами, уточним данные и расскажем о ближайших исследованиях.',
                    'Добровольцами могут стать лица старше 18 лет без острых и хронических заболеваний. Беременные и кормящие женщины не участвуют в исследованиях в нашем центре.',
                ],
                'bullets': ['Анкета', 'Обратный звонок', 'Информированное согласие', 'Скрининг', 'Участие по протоколу'],
            },
        ],
        cta_label='Заполнить анкету добровольца',
        hero_image='site/img/photos/volunteer-path.png',
        stats=[fact('18+', 'возраст добровольцев'), fact('3 мес.', 'обычный интервал участия'), fact('24-48 ч', 'частый формат пребывания')],
        form_title='Анкета добровольца',
        form_lead='Оставьте контакты, возраст и короткий комментарий о готовности участвовать. Менеджер расскажет о ближайших наборах и условиях скрининга.',
        default_lead_type='volunteer',
        lead_types=('volunteer', 'callback', 'study', 'question'),
    ),
    'volunteers-en': page(
        'volunteers-en',
        'en',
        'CLINISS / For Volunteers',
        'For Volunteers',
        'Volunteers',
        'Want to Become a Volunteer?',
        'Participation in clinical studies supports modern medicine and gives you an opportunity to check your health.',
        [
            {
                'title': 'Why People Participate',
                'body': [
                    'During a study you can check your health, meet new people, and spend time usefully.',
                    'For healthy volunteers, participation is also an opportunity to support modern medicine. Participation is compensated when provided by the study protocol.',
                ],
                'image': media('site/img/photos/volunteer-path.png', 'Volunteer pathway in a clinical study'),
            },
            {
                'title': 'FAQ',
                'body': ['Key questions volunteers ask before participating in clinical studies.'],
                'faq': VOLUNTEER_FAQ_EN,
            },
            {
                'title': 'Who Can Participate',
                'body': [
                    'Participation is open to people over 18 without acute or chronic diseases and without contraindications under a specific protocol.',
                    'Before enrollment, every volunteer goes through informed consent, medical examination, and screening.',
                ],
                'bullets': ['Over 18 years old', 'No acute or chronic diseases', 'No protocol contraindications', 'Pregnant and breastfeeding women do not participate', 'Informed consent', 'Medical screening'],
                'image': media('site/img/photos/outpatient-checkup.jpeg', 'Volunteer screening at CLINISS'),
                'image_position': 'left',
            },
            {
                'title': 'How to Become a Volunteer',
                'body': [
                    'Fill out a form or request a callback. We will contact you, clarify details, and tell you about upcoming studies.',
                    'Volunteers must be over 18 and free of acute or chronic diseases. Pregnant and breastfeeding women cannot participate in studies at the center.',
                ],
                'bullets': ['Form', 'Callback', 'Informed consent', 'Screening', 'Protocol participation'],
            },
        ],
        cta_label='Fill Out Volunteer Form',
        hero_image='site/img/photos/volunteer-path.png',
        stats=[fact('18+', 'volunteer age'), fact('3 mo.', 'typical interval'), fact('24-48 h', 'common stay format')],
        form_title='Volunteer Form',
        form_lead='Leave your contact details, age, and a short comment about your readiness to participate. A manager will explain current recruitment and screening conditions.',
        default_lead_type='volunteer',
        lead_types=('volunteer', 'callback', 'study', 'question'),
    ),
    'contacts': page(
        'contacts',
        'ru',
        'CLINISS / Контакты',
        'Контакты',
        'Контакты',
        'Контакты',
        'Вагжановский переулок, 9, 2 этаж, Тверь. Телефон: +7 (909) 157-86-18.',
        [
            {
                'title': 'Быстрые контакты',
                'body': [
                    'ООО «АРС Клинический Центр». Лицензия на осуществление медицинской деятельности Л041-01186-69/01327284 от 31.07.2024.',
                    'Адрес: 170100, г. Тверь, Вагжановский переулок, 9, 2 этаж.',
                ],
                'links': CONTACT_LINKS_RU,
                'facts': [
                    fact('10:00-13:00', 'прием граждан в последнюю среду месяца'),
                    fact('2 этаж', 'расположение центра'),
                    fact('122', 'горячая линия Минздрава Тверской области'),
                ],
                'image': media('site/img/photos/contacts-illustration.png', 'Иллюстрация контактов CLINISS'),
            },
            {
                'title': 'Адрес и визит в центр',
                'body': [
                    'Перед визитом на скрининг или встречу дождитесь подтверждения времени от менеджера центра.',
                    'Для вопросов по доступности и качеству медицинской помощи в регионе также работает единый номер горячей линии Министерства здравоохранения Тверской области 122.',
                ],
                'bullets': ['Тверь, Вагжановский переулок, 9', '2 этаж', 'Предварительное согласование визита', 'Связь по телефону, email и мессенджерам'],
                'map': CONTACT_MAP_RU,
            },
        ],
        cta_label='Оставить заявку',
        hero_image='site/img/photos/contacts-illustration.png',
        form_title='Напишите в CLINISS',
        form_lead='Выберите тип обращения, оставьте контакты, и команда центра вернется с ответом.',
        default_lead_type='question',
        lead_types=('question', 'callback', 'proposal', 'volunteer', 'review'),
    ),
    'contacts-en': page(
        'contacts-en',
        'en',
        'CLINISS / Contacts',
        'Contacts',
        'Contacts',
        'Contacts',
        '2nd floor, 9 Vagzhanovsky lane, Tver, Russian Federation. Phone: +7 (909) 157-86-18.',
        [
            {
                'title': 'Quick Contacts',
                'body': [
                    'ARS Clinical Center LLC. Medical activity license Л041-01186-69/01327284 dated 31.07.2024.',
                    'Address: 2nd floor, 9 Vagzhanovsky lane, Tver, Russian Federation, 170100.',
                ],
                'links': CONTACT_LINKS_EN,
                'facts': [
                    fact('10:00-13:00', 'public reception on the last Wednesday of each month'),
                    fact('2nd floor', 'center location'),
                    fact('122', 'Tver Region Ministry of Health hotline'),
                ],
                'image': media('site/img/photos/contacts-illustration.png', 'CLINISS contact illustration'),
            },
            {
                'title': 'Address and Visit',
                'body': [
                    'Please wait for a manager to confirm the time before coming for screening or a meeting.',
                    'The Tver Region Ministry of Health hotline 122 is also available for questions about access to care and quality of care in the region.',
                ],
                'bullets': ['Tver, 9 Vagzhanovsky lane', '2nd floor', 'Visit confirmed in advance', 'Contact by phone, email, or messengers'],
                'map': CONTACT_MAP_EN,
            },
        ],
        cta_label='Submit a Request',
        hero_image='site/img/photos/contacts-illustration.png',
        form_title='Contact CLINISS',
        form_lead='Choose the request type, leave your contact details, and the center team will reply.',
        default_lead_type='question',
        lead_types=('question', 'callback', 'proposal', 'volunteer', 'review'),
    ),
    'docs': page(
        'docs',
        'ru',
        'CLINISS / Нормативные документы',
        'Нормативные документы',
        'Документы',
        'Нормативные документы',
        'Раздел содержит сведения о контролирующих органах, лекарственном обеспечении, правилах записи добровольцев, подготовке к исследованиям, госпитализации и порядке оказания услуг.',
        [
            {
                'title': 'Контролирующие органы',
                'body': [
                    'Единый номер горячей линии Министерства здравоохранения Тверской области - 122. По нему можно задать вопросы о доступности и качестве медицинской помощи, обеспечении льготными лекарственными препаратами, диспансеризации и профилактических осмотрах. Короткий номер 122 действует во всех регионах страны.',
                    'Министерство здравоохранения Тверской области: 170100, г. Тверь, улица Ивана Седых, 8; тел./факс: (4822) 33-32-55; dep_zdrav@tverreg.ru.',
                    'Территориальный орган Росздравнадзора по Тверской области: (4822) 35-85-88; rzntver@reg69.roszdravnadzor.gov.ru; 170100, г. Тверь, ул. Советская, д. 35, корпус 1.',
                    'Управление Роспотребнадзора по Тверской области: 170034, г. Тверь, ул. Дарвина, д. 17; тел. (4822) 34-22-11; факс: (4822) 35-61-85, 32-06-20.',
                ],
            },
            {
                'title': 'Лекарственное обеспечение и лицензия',
                'body': [
                    'На странице сохранены внешние ссылки на перечни лекарственных препаратов, сведения о лицензии и документы организации.',
                ],
                'links': DOC_LINKS_RU,
                'images': [
                    media('site/img/documents/organization-structure.png', 'Организационная структура CLINISS'),
                ],
                'gallery_style': 'documents',
            },
            {
                'title': 'Правила участия и оказания услуг',
                'body': [
                    'Запись добровольцев на участие в клинических исследованиях осуществляется после заполнения анкеты на сайте или в официальных социальных сетях центра. После обработки данных менеджер связывается с кандидатом для уточнения деталей и назначения времени визита на скрининг.',
                    'В рамках клинических исследований в центре проводятся ЭКГ, забор биоматериала натощак и осмотры врачей-исследователей. Каждый протокол уникален, поэтому требования к подготовке могут различаться; подробные инструкции доброволец получает от координатора проекта.',
                    'На базе центра функционирует стационарное отделение для пребывания участников исследований. Сроки, порядок и условия госпитализации определяются исключительно протоколом конкретного клинического исследования.',
                    'Стандартный консультативный прием граждан вне рамок протоколов клинических исследований не ведется. Центр не оказывает платные медицинские услуги населению, не участвует в реализации программы ОМС и не ведет прием граждан по полисам обязательного медицинского страхования.',
                    'Все обследования, медицинские вмешательства и манипуляции выполняются только для лиц, включенных в программы клинических исследований, и проводятся бесплатно для участника за счет средств спонсора исследования.',
                ],
                'bullets': ['Запись после анкеты', 'Скрининг после связи с менеджером', 'Индивидуальная подготовка по протоколу', 'ЭКГ и забор биоматериала по программе исследования', 'Госпитализация только в рамках исследования', 'Плановая медицинская помощь вне исследований не оказывается', 'Платные медицинские услуги населению не оказываются', 'ОМС не ведется', 'Диспансеризация и профилактические осмотры населения не проводятся'],
            },
            {
                'title': 'Прием граждан и согласия',
                'body': [
                    'Прием граждан проводится в последнюю среду месяца с 10:00 до 13:00.',
                    'В соответствии с Федеральным законом № 323-ФЗ каждый гражданин имеет право на получение медицинской помощи в рамках программы государственных гарантий. Поскольку CLINISS не участвует в реализации территориальной программы государственных гарантий, по вопросам плановой медицинской помощи и диспансеризации рекомендуется обращаться в поликлиники по месту прикрепления.',
                    'На исходном сайте отдельно размещены политика об обработке персональных данных и информированное добровольное согласие на медицинское вмешательство. Эти внешние ссылки сохранены в новом разделе документов.',
                ],
                'links': [
                    link('Политика об обработке персональных данных', 'https://disk.yandex.ru/i/zNO3XYku2JzNeg', 'Яндекс.Диск'),
                    link('Информированное добровольное согласие на медицинское вмешательство', 'https://disk.yandex.ru/i/oEXu78YjBmLc4g', 'Яндекс.Диск'),
                    link('Политика конфиденциальности сайта', '/policy', 'Внутренняя страница', external=False),
                    link('Соглашение об обработке персональных данных', '/agreement', 'Внутренняя страница', external=False),
                ],
            },
        ],
        show_lead_form=False,
        hero_image='site/img/documents/organization-structure.png',
    ),
    'docs-en': page(
        'docs-en',
        'en',
        'CLINISS / Regulatory Documents',
        'Documents',
        'Documents',
        'Regulatory Documents',
        'This section contains regulatory authority details, medicine support links, volunteer enrollment rules, preparation requirements, hospitalization rules, and service information.',
        [
            {
                'title': 'Regulatory Authorities',
                'body': [
                    'The Ministry of Health hotline for the Tver Region is 122. It can be used for questions about access to care, quality of care, medicine support, preventive checkups, and scheduled examinations.',
                    'Tver Region Ministry of Health: 8 Ivan Sedykh St., Tver; phone/fax: (4822) 33-32-55; dep_zdrav@tverreg.ru.',
                    'Roszdravnadzor territorial body for the Tver Region: (4822) 35-85-88; rzntver@reg69.roszdravnadzor.gov.ru; 35 Sovetskaya St., building 1, Tver.',
                    'Rospotrebnadzor for the Tver Region: 17 Darvina St., Tver; phone: (4822) 34-22-11; fax: (4822) 35-61-85, 32-06-20.',
                ],
            },
            {
                'title': 'Medicine Support and License',
                'body': ['External regulatory links from the Russian page are preserved for public reference.'],
                'links': DOC_LINKS_EN,
                'images': [
                    media('site/img/documents/organization-structure.png', 'CLINISS organizational structure'),
                ],
                'gallery_style': 'documents',
            },
            {
                'title': 'Participation and Service Rules',
                'body': [
                    'Volunteer enrollment starts after a form is submitted on the site or through official social channels. A manager contacts the candidate to clarify details and schedule screening.',
                    'Within clinical trials, the center may perform ECG, fasting biomaterial collection, and examinations by investigators. Every protocol is unique, so preparation requirements may differ; detailed instructions are provided by the project coordinator.',
                    'The center has an inpatient department for study participants. Timing, procedure, and hospitalization conditions are determined only by the protocol of the specific clinical study.',
                    'The center does not provide routine outpatient consultations outside clinical trial protocols, does not provide paid medical services to the public, and does not participate in compulsory medical insurance programs.',
                    'All examinations and medical procedures are performed only for people enrolled in clinical trial programs and are free of charge for participants because they are funded by the study sponsor.',
                ],
                'bullets': ['Enrollment after form submission', 'Screening after manager contact', 'Protocol-specific preparation', 'ECG and biomaterial collection according to the study program', 'Hospitalization only within a study', 'No routine medical care outside studies', 'No paid medical services for the public', 'No compulsory medical insurance reception', 'No public preventive checkups'],
            },
            {
                'title': 'Public Reception and Consent Forms',
                'body': [
                    'Public reception is held on the last Wednesday of each month from 10:00 to 13:00.',
                    'Because CLINISS does not participate in the territorial state guarantees program, people seeking routine medical care or preventive checkups should contact clinics at their place of attachment.',
                    'The original site provides separate downloadable documents for the personal data processing policy and informed voluntary consent for medical intervention. These external links are preserved here.',
                ],
                'links': [
                    link('Personal Data Processing Policy', 'https://disk.yandex.ru/i/zNO3XYku2JzNeg', 'Yandex Disk'),
                    link('Informed Voluntary Consent for Medical Intervention', 'https://disk.yandex.ru/i/oEXu78YjBmLc4g', 'Yandex Disk'),
                    link('Site Privacy Policy', '/policy-en', 'Internal page', external=False),
                    link('Personal Data Processing Agreement', '/agreement-en', 'Internal page', external=False),
                ],
            },
        ],
        show_lead_form=False,
        hero_image='site/img/documents/organization-structure.png',
    ),
    'issledovaniya-bioekvivalentnosti': page(
        'issledovaniya-bioekvivalentnosti',
        'ru',
        'CLINISS / Исследования биоэквивалентности',
        'Исследования биоэквивалентности',
        'Исследования',
        'Исследования биоэквивалентности',
        'Исследования проводятся для сравнения фармакокинетического профиля исследуемого препарата с уже существующим препаратом и определения их биоэквивалентности.',
        [
            {
                'title': 'Что такое биоэквивалентность',
                'body': [
                    'Исследование проводится для сравнения фармакокинетического профиля исследуемого препарата с уже существующим препаратом и определения их биоэквивалентности.',
                    'CLINISS провел до 50 клинических исследований в области биоэквивалентности, эффективности, безопасности и терапевтической эквивалентности. Центр создает безопасную и комфортную среду для участников, использует современные технологии и соблюдает принципы GCP.',
                    'В России дженерики занимают значимую долю рынка лекарств, а их вывод на рынок тщательно регламентируется. Процедура одобрения и оборот таких лекарственных средств находятся под надзором Министерства здравоохранения и Росздравнадзора.',
                ],
                'facts': [fact('50', 'завершенных исследований'), fact('600', 'добровольцев успешно прошли исследование')],
                'image': media('site/img/photos/bioequivalence-lab.png', 'Лабораторный анализ биоэквивалентности'),
            },
            {
                'title': 'Путь добровольца',
                'body': ['Участие строится по протоколу исследования и включает несколько этапов от первичного отбора до завершения визитов.'],
                'cards': [
                    card('Рекрутинг', 'Поиск и привлечение добровольцев, информирование об исследовании и предварительный отбор по основным требованиям.'),
                    card('Скрининг', 'Комплексное медицинское обследование, анализы и сбор анамнеза для проверки критериев протокола и безопасности участия.'),
                    card('Госпитализация', 'Прибытие включенных добровольцев в центр, размещение и подготовка к активной части исследования.'),
                    card('Дозинг', 'Прием исследуемого препарата под строгим медицинским наблюдением, контроль состояния и сбор необходимых данных.'),
                    card('Амбулаторные визиты', 'Контрольные осмотры, дополнительные анализы и оценка состояния после выписки для формирования полной картины профиля препарата.'),
                ],
                'image': media('site/img/photos/bioequivalence-screening.png', 'Скрининг добровольцев'),
                'image_position': 'left',
            },
            {
                'title': 'Актуальные исследования',
                'body': [
                    'Наборы добровольцев зависят от активных протоколов. На сайте можно оставить заявку на участие, а менеджер уточнит возрастные критерии, график визитов, размер компенсации и статус набора.',
                    'Если набор по конкретному исследованию остановлен, кандидат может быть внесен в базу добровольцев и получить информацию о следующих подходящих исследованиях.',
                ],
                'bullets': ['Возрастные критерии зависят от протокола', 'График визитов сообщается перед скринингом', 'Компенсация определяется условиями исследования', 'Участие начинается только после информированного согласия и скрининга'],
            },
        ],
        cta_label='Запросить предложение',
        hero_image='site/img/photos/research-hero.png',
        stats=[fact('50', 'исследований'), fact('600', 'добровольцев'), fact('GCP', 'стандарты')],
        form_title='Запросить предложение по биоэквивалентности',
        form_lead='Опишите препарат, формат исследования или вопрос по протоколу, чтобы команда связалась с вами.',
        default_lead_type='proposal',
        lead_types=('proposal', 'study', 'question', 'callback'),
    ),
    'issledovaniya-bioekvivalentnosti-en': page(
        'issledovaniya-bioekvivalentnosti-en',
        'en',
        'CLINISS / Bioequivalence Studies',
        'Bioequivalence Studies',
        'Studies',
        'Bioequivalence Studies',
        'Bioequivalence studies compare the pharmacokinetic profile of an investigational medicine with an existing product and evaluate their bioequivalence.',
        [
            {
                'title': 'What Bioequivalence Means',
                'body': [
                    'The study compares the pharmacokinetic profile of the investigational medicine with an existing reference product and evaluates their bioequivalence.',
                    'CLINISS has conducted up to 50 clinical studies in bioequivalence, efficacy, safety, and therapeutic equivalence. The center creates a safe and comfortable environment for participants, uses modern technologies, and follows GCP principles.',
                    'Generic medicines represent a significant part of the pharmaceutical market, and their market entry is carefully regulated. Approval and circulation of these medicines are supervised by the Ministry of Health and Roszdravnadzor.',
                ],
                'facts': [fact('50', 'completed studies'), fact('600', 'volunteers successfully completed studies')],
                'image': media('site/img/photos/bioequivalence-lab.png', 'Bioequivalence laboratory analysis'),
            },
            {
                'title': 'Volunteer Pathway',
                'body': ['Participation follows a study protocol and includes several stages from initial recruitment to follow-up visits.'],
                'cards': [
                    card('Recruitment', 'Searching for volunteers, informing them about the study, and preliminary selection according to key requirements.'),
                    card('Screening', 'Comprehensive medical examination, tests, and history collection to confirm protocol criteria and participation safety.'),
                    card('Hospitalization', 'Arrival of enrolled volunteers at the center, accommodation, and preparation for the active study phase.'),
                    card('Dosing', 'Administration of the investigational product under strict medical supervision, health monitoring, and data collection.'),
                    card('Outpatient Visits', 'Follow-up examinations, additional tests, and post-discharge assessment to complete the medicine profile.'),
                ],
                'image': media('site/img/photos/bioequivalence-screening.png', 'Volunteer screening'),
                'image_position': 'left',
            },
            {
                'title': 'Current Studies',
                'body': [
                    'Volunteer recruitment depends on active protocols. A candidate can submit a participation request, and a manager will clarify age criteria, visit schedule, compensation, and recruitment status.',
                    'If recruitment for a specific study is closed, the candidate may be added to the volunteer database and informed about future suitable studies.',
                ],
                'bullets': ['Age criteria depend on the protocol', 'Visit schedule is explained before screening', 'Compensation is defined by study conditions', 'Participation starts only after informed consent and screening'],
            },
        ],
        cta_label='Request a Proposal',
        hero_image='site/img/photos/research-hero.png',
        stats=[fact('50', 'studies'), fact('600', 'volunteers'), fact('GCP', 'standards')],
        form_title='Request a Bioequivalence Proposal',
        form_lead='Describe the medicine, study format, or protocol question so the team can contact you.',
        default_lead_type='proposal',
        lead_types=('proposal', 'study', 'question', 'callback'),
    ),
    'policy': page(
        'policy',
        'ru',
        'Политика конфиденциальности',
        'Политика конфиденциальности',
        'Правовая информация',
        'Политика конфиденциальности',
        'Политика в отношении обработки персональных данных описывает цели, принципы, условия обработки и меры защиты персональных данных пользователей сайта CLINISS.',
        [
            {
                'title': 'Общие положения',
                'body': [
                    'Настоящая политика обработки персональных данных составлена в соответствии с требованиями Федерального закона от 27.07.2006 № 152-ФЗ «О персональных данных».',
                    'Оператором персональных данных является ООО «АРС Клинический Центр». Оператор считает соблюдение прав и свобод человека при обработке персональных данных одним из важных условий своей деятельности.',
                    'Политика применяется ко всей информации, которую Оператор может получить о посетителях веб-сайта https://cliniss.ru, включая сведения из форм обратной связи и технические данные использования сайта.',
                ],
            },
            {
                'title': 'Основные понятия',
                'body': [
                    'Персональные данные - любая информация, относящаяся прямо или косвенно к определенному или определяемому пользователю сайта.',
                    'Обработка персональных данных включает сбор, запись, систематизацию, накопление, хранение, уточнение, использование, передачу, обезличивание, блокирование, удаление и уничтожение персональных данных.',
                    'Автоматизированная обработка означает обработку персональных данных с помощью средств вычислительной техники. Обезличивание означает действия, после которых невозможно определить принадлежность данных конкретному пользователю без дополнительной информации.',
                ],
            },
            {
                'title': 'Права и обязанности Оператора',
                'body': [
                    'Оператор вправе получать от субъекта персональных данных достоверную информацию и документы, содержащие персональные данные.',
                    'Оператор обязан организовывать обработку персональных данных в порядке, установленном законодательством РФ, отвечать на обращения субъектов персональных данных и обеспечивать доступ к настоящей Политике.',
                    'Оператор принимает правовые, организационные и технические меры для защиты персональных данных от неправомерного или случайного доступа, уничтожения, изменения, блокирования, копирования, предоставления и распространения.',
                ],
            },
            {
                'title': 'Права пользователя',
                'body': [
                    'Пользователь вправе получать информацию, касающуюся обработки его персональных данных, требовать уточнения, блокирования или уничтожения данных, если они являются неполными, устаревшими, неточными, незаконно полученными или не являются необходимыми для заявленной цели обработки.',
                    'Пользователь вправе отозвать согласие на обработку персональных данных и направить требование о прекращении обработки. Пользователь также вправе обжаловать неправомерные действия или бездействие Оператора в уполномоченный орган или в суд.',
                    'Пользователь обязан предоставлять Оператору достоверные данные о себе и сообщать об их уточнении, обновлении или изменении.',
                ],
            },
            {
                'title': 'Принципы обработки',
                'body': [
                    'Обработка персональных данных осуществляется на законной и справедливой основе, ограничивается достижением конкретных, заранее определенных и законных целей.',
                    'Оператор не допускает обработки персональных данных, несовместимой с целями сбора, и не объединяет базы данных, обработка которых осуществляется в несовместимых целях.',
                    'Содержание и объем обрабатываемых персональных данных соответствуют заявленным целям. При обработке обеспечиваются точность, достаточность и актуальность персональных данных.',
                ],
            },
            {
                'title': 'Цели и категории данных',
                'body': [
                    'Персональные данные обрабатываются для информирования пользователя, обработки заявок и обращений, записи кандидатов на исследования, обратной связи, ведения внутреннего учета обращений, улучшения качества сайта и выполнения требований законодательства РФ.',
                    'К обрабатываемым данным могут относиться фамилия, имя, отчество, телефон, email, комментарии пользователя, сведения из форм, технические данные браузера, IP-адрес и cookie.',
                    'Типовые действия с данными: сбор, запись, систематизация, накопление, хранение, уточнение, использование, уничтожение и обезличивание.',
                ],
            },
            {
                'title': 'Условия обработки и передачи',
                'body': [
                    'Обработка персональных данных осуществляется с согласия субъекта персональных данных, а также в иных случаях, предусмотренных законодательством Российской Федерации.',
                    'Персональные данные пользователя не передаются третьим лицам, за исключением случаев, связанных с исполнением законодательства, оказанием услуг или исполнением обязательств по договору при наличии соответствующих оснований.',
                    'При обработке персональных данных Оператор обеспечивает конфиденциальность персональных данных.',
                ],
            },
            {
                'title': 'Хранение, отзыв согласия и актуальная версия',
                'body': [
                    'Срок обработки персональных данных определяется достижением целей, для которых они были собраны, если иной срок не предусмотрен договором или законодательством.',
                    'Пользователь может актуализировать персональные данные или отозвать согласие, направив уведомление на адрес info@arsclinic.ru с соответствующей пометкой.',
                    'Все изменения политики публикуются на сайте. Актуальная версия расположена по адресу https://cliniss.ru/policy.',
                ],
            },
        ],
        show_lead_form=False,
        hero_image='site/img/graphics/cliniss-wave-brand.jpg',
    ),
    'policy-en': page(
        'policy-en',
        'en',
        'Privacy Policy',
        'Privacy Policy',
        'Legal',
        'Privacy Policy',
        'This English reference version describes the purposes, principles, conditions, and safeguards for personal data processing on the CLINISS site.',
        [
            {
                'title': 'General Provisions',
                'body': [
                    'This personal data policy is based on the requirements of Russian Federal Law No. 152-FZ on Personal Data.',
                    'The personal data controller is ARS Clinical Center LLC. The controller treats respect for individual rights and freedoms in personal data processing as an important condition of its activity.',
                    'The policy applies to information the controller may receive from visitors of https://cliniss.ru, including feedback form data and technical site usage data.',
                ],
            },
            {
                'title': 'Key Terms',
                'body': [
                    'Personal data means any information directly or indirectly related to an identified or identifiable site user.',
                    'Processing includes collection, recording, systematization, accumulation, storage, clarification, use, transfer, depersonalization, blocking, deletion, and destruction of personal data.',
                    'Automated processing means processing with computer technology. Depersonalization means actions after which data cannot be attributed to a specific user without additional information.',
                ],
            },
            {
                'title': 'Controller Rights and Duties',
                'body': [
                    'The controller may receive accurate information and documents containing personal data from the data subject.',
                    'The controller must organize processing in accordance with Russian law, respond to data subject requests, and provide access to this policy.',
                    'The controller applies legal, organizational, and technical measures to protect personal data from unlawful or accidental access, destruction, modification, blocking, copying, provision, and distribution.',
                ],
            },
            {
                'title': 'User Rights',
                'body': [
                    'The user may receive information about personal data processing and request clarification, blocking, or deletion of data where data are incomplete, outdated, inaccurate, unlawfully obtained, or no longer necessary for the stated purpose.',
                    'The user may withdraw consent to personal data processing and request termination of processing. The user may also appeal unlawful actions or inaction to the authorized body or court.',
                    'The user must provide accurate data and notify the controller about clarification, updates, or changes.',
                ],
            },
            {
                'title': 'Processing Principles',
                'body': [
                    'Personal data are processed lawfully and fairly and only for specific, predetermined, and legitimate purposes.',
                    'The controller does not process data in ways incompatible with the collection purposes and does not merge databases processed for incompatible purposes.',
                    'The content and volume of processed personal data correspond to the stated purposes. Accuracy, sufficiency, and relevance are maintained during processing.',
                ],
            },
            {
                'title': 'Purposes and Data Categories',
                'body': [
                    'Personal data are processed to inform users, handle requests, enroll study candidates, provide feedback, maintain internal request records, improve the site, and comply with Russian law.',
                    'Processed data may include surname, name, patronymic, phone, email, user comments, form data, browser technical data, IP address, and cookies.',
                    'Typical processing actions include collection, recording, systematization, accumulation, storage, clarification, use, destruction, and depersonalization.',
                ],
            },
            {
                'title': 'Conditions and Transfer',
                'body': [
                    'Personal data are processed with the data subject consent and in other cases provided by Russian law.',
                    'User personal data are not transferred to third parties except where required by law, service provision, or contractual obligations with appropriate legal grounds.',
                    'The controller maintains confidentiality of personal data during processing.',
                ],
            },
            {
                'title': 'Storage, Withdrawal, and Current Version',
                'body': [
                    'The processing period is determined by the purposes for which data were collected unless another period is provided by contract or law.',
                    'The user may update personal data or withdraw consent by sending a notice to info@arsclinic.ru with the relevant subject note.',
                    'Changes to the policy are published on the site. The current version is available at https://cliniss.ru/policy-en.',
                ],
            },
        ],
        show_lead_form=False,
        hero_image='site/img/graphics/cliniss-wave-brand.jpg',
    ),
    'agreement': page(
        'agreement',
        'ru',
        'Соглашение об обработке персональных данных',
        'Соглашение',
        'Правовая информация',
        'Соглашение об обработке персональных данных',
        'Соглашение является публичной офертой и используется при отправке форм на сайте CLINISS, включая заявки, обратную связь и обращения добровольцев.',
        [
            {
                'title': 'Термины и согласие',
                'body': [
                    'Сайт - совокупность текстов, графических элементов, дизайна, изображений, программного кода, фото- и видеоматериалов и иных результатов интеллектуальной деятельности, размещенных по адресу https://cliniss.ru.',
                    'Администрация сайта - ООО «АРС Клинический Центр». Пользователь - любое лицо, осуществившее доступ к сайту, заполнившее формы обратной связи и принявшее условия настоящего соглашения.',
                    'Персональные данные - сведения, предоставляемые пользователем при заполнении форм на сайте, включая имя, номер телефона, адрес электронной почты, комментарии и иные данные, необходимые для обработки обращения.',
                    'Обработка персональных данных включает сбор, запись, систематизацию, накопление, хранение, уточнение, использование, передачу, обезличивание, блокирование, удаление и уничтожение.',
                ],
            },
            {
                'title': 'Общие положения',
                'body': [
                    'Присоединяясь к соглашению и оставляя данные на сайте cliniss.ru, пользователь подтверждает, что предоставляет достоверные данные о себе, ознакомился с соглашением в полном объеме и действует добровольно, по собственной воле и в своих интересах.',
                    'Пользователь выражает согласие на обработку своих персональных данных, а также соглашается с использованием файлов cookie и аналитических сервисов.',
                    'Согласие дается в соответствии с Федеральным законом № 152-ФЗ «О персональных данных».',
                ],
            },
            {
                'title': 'Цели обработки',
                'body': [
                    'Персональные данные используются для обработки заявок и обращений, записи кандидатов на исследования, обратной связи с пользователем, ведения внутренней базы обращений, информирования об услугах и исследованиях, улучшения качества сайта и выполнения требований законодательства РФ.',
                    'Если пользователь отправляет заявку на сотрудничество, добровольческую анкету, отзыв или вопрос, данные используются для связи с пользователем и подготовки ответа по выбранному сценарию обращения.',
                    'При наличии согласия пользователь может получать информационные сообщения по телефону, электронной почте, SMS, мессенджерам и иным средствам связи. Пользователь вправе отказаться от таких сообщений.',
                ],
            },
            {
                'title': 'Способы обработки и передача',
                'body': [
                    'Обработка персональных данных осуществляется с использованием средств автоматизации и без использования таких средств.',
                    'Администрация сайта вправе вносить персональные данные в электронные базы, реестры и внутренние системы учета обращений.',
                    'Допускается передача персональных данных третьим лицам без дополнительного согласия пользователя в случаях, когда это необходимо для оказания услуг, обработки обращения или предусмотрено законодательством РФ.',
                ],
            },
            {
                'title': 'Срок действия и отзыв согласия',
                'body': [
                    'Согласие на обработку персональных данных действует с момента их предоставления и до достижения целей обработки либо до отзыва пользователем.',
                    'Пользователь вправе отозвать согласие путем направления письменного обращения Администрации сайта. После получения обращения обработка прекращается в порядке и сроки, предусмотренные законодательством.',
                    'Администрация сайта вправе вносить изменения в соглашение в одностороннем порядке. Новая редакция вступает в силу с момента размещения на сайте, если иное не предусмотрено.',
                ],
            },
            {
                'title': 'Cookie и аналитика',
                'body': [
                    'Файлы cookie - это небольшие текстовые файлы, сохраняемые на устройстве пользователя при посещении сайта. Они позволяют запоминать настройки и улучшать пользовательский опыт.',
                    'На сайте могут использоваться обязательные, аналитические, функциональные и рекламные cookie при наличии соответствующих сервисов. Также могут применяться сервисы веб-аналитики, включая Яндекс.Метрику и аналогичные инструменты.',
                    'Пользователь может изменить настройки cookie в браузере. Отключение cookie может повлиять на работу отдельных функций сайта.',
                ],
            },
            {
                'title': 'Контактная информация',
                'body': [
                    'По вопросам обработки персональных данных пользователь может обратиться в ООО «АРС Клинический Центр» по адресу info@arsclinic.ru.',
                    'К соглашению применяется право Российской Федерации. Все споры подлежат разрешению в соответствии с действующим законодательством РФ.',
                    'Актуальная версия соглашения доступна по адресу https://cliniss.ru/agreement.',
                ],
            },
        ],
        show_lead_form=False,
        hero_image='site/img/graphics/cliniss-wave-brand.jpg',
    ),
    'agreement-en': page(
        'agreement-en',
        'en',
        'Personal Data Processing Agreement',
        'Agreement',
        'Legal',
        'Personal Data Processing Agreement',
        'This English reference page describes the consent used when forms, feedback, volunteer requests, and other inquiries are submitted on the CLINISS site.',
        [
            {
                'title': 'Terms and Consent',
                'body': [
                    'The site is the set of text, design elements, images, program code, photo and video materials, and other intellectual property located at https://cliniss.ru.',
                    'The site administration is ARS Clinical Center LLC. A user is any person who accesses the site, completes feedback forms, and accepts this agreement.',
                    'Personal data means information provided by the user in site forms, including name, phone number, email address, comments, and other data needed to handle the request.',
                    'Personal data processing includes collection, recording, systematization, accumulation, storage, clarification, use, transfer, depersonalization, blocking, deletion, and destruction.',
                ],
            },
            {
                'title': 'General Provisions',
                'body': [
                    'By joining the agreement and submitting data on cliniss.ru, the user confirms that the data are accurate, that the user has read the agreement in full, and that the user acts voluntarily and in their own interest.',
                    'The user consents to personal data processing and agrees to the use of cookies and analytics services.',
                    'Consent is given in accordance with Russian Federal Law No. 152-FZ on Personal Data.',
                ],
            },
            {
                'title': 'Processing Purposes',
                'body': [
                    'Personal data are used to handle requests and inquiries, enroll study candidates, provide feedback, maintain internal request records, inform users about services and studies, improve site quality, and comply with Russian law.',
                    'If the user submits a cooperation request, volunteer form, review, or question, the data are used to contact the user and prepare a response according to the selected request scenario.',
                    'With consent, the user may receive information messages by phone, email, SMS, messengers, and other communication channels. The user may opt out of such messages.',
                ],
            },
            {
                'title': 'Processing Methods and Transfer',
                'body': [
                    'Processing may be automated or non-automated.',
                    'The site administration may enter personal data into electronic databases, registers, and internal request accounting systems.',
                    'Personal data may be transferred to third parties without additional consent where this is necessary to provide services, handle a request, or comply with Russian law.',
                ],
            },
            {
                'title': 'Duration and Withdrawal',
                'body': [
                    'Consent applies from the moment data are submitted until processing purposes are achieved or consent is withdrawn by the user.',
                    'The user may withdraw consent by sending a written request to the site administration. Processing is then stopped according to the procedure and timing required by law.',
                    'The site administration may update this agreement unilaterally. The new version takes effect when published on the site unless otherwise stated.',
                ],
            },
            {
                'title': 'Cookies and Analytics',
                'body': [
                    'Cookies are small text files stored on the user device when visiting the site. They help remember settings and improve user experience.',
                    'The site may use required, analytical, functional, and advertising cookies where relevant services are present. Web analytics services, including Yandex Metrica and similar tools, may also be used.',
                    'Browser settings can be used to limit cookies, but this may affect some site functions.',
                ],
            },
            {
                'title': 'Contact Information',
                'body': [
                    'Questions about personal data processing can be sent to ARS Clinical Center LLC at info@arsclinic.ru.',
                    'This agreement is governed by the law of the Russian Federation. Disputes are resolved under applicable Russian law.',
                    'The current version is available at https://cliniss.ru/agreement-en.',
                ],
            },
        ],
        show_lead_form=False,
        hero_image='site/img/graphics/cliniss-wave-brand.jpg',
    ),
}

PAGE_ORDER = list(PAGES.keys())


def get_page(slug):
    return PAGES.get(slug or '')


def section_text(section):
    parts = [
        section.get('title', ''),
        ' '.join(section.get('body', [])),
        ' '.join(section.get('bullets', [])),
    ]
    for collection in ('facts', 'cards', 'faq', 'links'):
        for item in section.get(collection, []):
            parts.extend(str(value) for value in item.values())
    return ' '.join(parts)


def search_pages(query):
    normalized = query.strip().lower()
    if not normalized:
        return []

    results = []
    for item in PAGES.values():
        haystack = ' '.join(
            [
                item['title'],
                item['hero_title'],
                item['hero_lead'],
                ' '.join(section_text(section) for section in item['sections']),
            ]
        ).lower()
        if normalized in haystack:
            results.append(item)
    return results

