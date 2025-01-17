from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Введите электронную почту клиента"
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        help_text="Введите фамилию клиента"
    )

    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        help_text="Введите имя клиента"
    )

    middle_name = models.CharField(
        max_length=50,
        verbose_name="Отчество",
        help_text="Введите отчество клиента (при наличии)",
        **NULLABLE
    )

    comment = models.TextField(
        verbose_name="Комментарий",
        help_text="Введите комментарий",
        **NULLABLE
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец"
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        permissions = [
            ('can_view_client', 'Может просматривать клиентов сервиса'),
        ]


class Message(models.Model):
    subject = models.CharField(
        max_length=255,
        verbose_name="Тема сообщения",
        help_text="Введите тему сообщения"
    )

    body = models.TextField(
        verbose_name="Содержание сообщения",
        help_text="Введите содержание сообщения"
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец"
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        permissions = [
            ('cannot_change_message', 'Не может изменять сообщения'),
        ]


class Mailing(models.Model):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'

    PERIODICITY_CHOICES = [
        (DAILY, 'Раз в день'),
        (WEEKLY, 'Раз в неделю'),
        (MONTHLY, 'Раз в месяц'),
    ]

    CREATED = 'created'
    STARTED = 'started'
    COMPLETED = 'completed'

    STATUS_CHOICES = [
        (CREATED, 'Создана'),
        (STARTED, 'Запущена'),
        (COMPLETED, 'Завершена'),
    ]

    start_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="Время запуска",
        help_text="Время запуска рассылки"
    )

    periodicity = models.CharField(
        max_length=10,
        choices=PERIODICITY_CHOICES,
        verbose_name="Периодичность",
        help_text="Периодичность рассылки"
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=CREATED,
        verbose_name="Статус",
        help_text="Статус рассылки"
    )

    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
    )

    clients = models.ManyToManyField(
        Client
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец"
    )

    def __str__(self):
        return f"Mailing {self.pk} - {self.status}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        permissions = [
            ('can_view_mailing', 'Может просматривать рассылки'),
            ('can_disable_mailing', 'Может отключать рассылки'),
            ('cannot_edit_mailing', 'Не может редактировать рассылки'),
            ('cannot_manage_mailing', 'Не может управлять списком рассылок'),
            ('cannot_change_mailing', 'Не может создавать рассылки'),
        ]


class Attempt(models.Model):
    SUCCESS = 'success'
    FAILED = 'failed'

    STATUS_CHOICES = [
        (SUCCESS, 'Успешно'),
        (FAILED, 'Не успешно'),
    ]

    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE
    )

    attempt_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время попытки",
        help_text="Время попытки отправки письма"
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        verbose_name="Статус попытки",
        help_text="Статус попытки отправки письма"
    )

    server_response = models.TextField(
        **NULLABLE,
        verbose_name="Ответ сервера",
        help_text="Ответ сервера при попытке отправки письма"
    )

    def __str__(self):
        return f"Attempt {self.pk} - {self.status}"

    class Meta:
        verbose_name = "Попытка отправки"
        verbose_name_plural = "Попытки отправки"
