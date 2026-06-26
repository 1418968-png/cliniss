from django.db import models


class Lead(models.Model):
    class LeadType(models.TextChoices):
        CALLBACK = 'callback', 'Заказать звонок'
        TEAM = 'team', 'Стать частью команды'
        PROPOSAL = 'proposal', 'Запросить коммерческое предложение'
        VOLUNTEER = 'volunteer', 'Анкета добровольца'
        REVIEW = 'review', 'Оставить отзыв'
        STUDY = 'study', 'Записаться на исследование'
        QUESTION = 'question', 'Задать вопрос'

    class Language(models.TextChoices):
        RU = 'ru', 'Русский'
        EN = 'en', 'English'

    class Status(models.TextChoices):
        NEW = 'new', 'Новая'
        IN_PROGRESS = 'in_progress', 'В работе'
        CLOSED = 'closed', 'Закрыта'
        ARCHIVED = 'archived', 'Архив'

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    lead_type = models.CharField(max_length=32, choices=LeadType.choices)
    language = models.CharField(
        max_length=2,
        choices=Language.choices,
        default=Language.RU,
    )
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=40)
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)
    source_path = models.CharField(max_length=255, blank=True)
    source_site = models.CharField(max_length=80, default='cliniss')
    consent = models.BooleanField(default=False)
    integration_key = models.CharField(max_length=120, blank=True)
    external_payload = models.JSONField(default=dict, blank=True)
    user_agent = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'

    def __str__(self):
        return f'{self.get_lead_type_display()} - {self.name}'
