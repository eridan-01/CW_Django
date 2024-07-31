import smtplib

import pytz
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from newsletter.models import Mailing, Attempt


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    # Фильтруем рассылки, которые должны быть отправлены
    mailings = Mailing.objects.filter(
        start_time__lte=current_datetime,
        status=Mailing.STARTED
    )
    print("hello world")
    for mailing in mailings:
        # Проверяем последнюю попытку отправки
        last_attempt = Attempt.objects.filter(mailing=mailing).order_by('-attempt_time').first()
        if last_attempt:
            time_diff = current_datetime - last_attempt.attempt_time
            if mailing.periodicity == Mailing.DAILY and time_diff.days < 1:
                continue
            elif mailing.periodicity == Mailing.WEEKLY and time_diff.days < 7:
                continue
            elif mailing.periodicity == Mailing.MONTHLY and time_diff.days < 30:
                continue

        # Попытка отправить письмо
        try:
            send_mail(
                subject=mailing.message.subject,
                message=mailing.message.body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.clients.all()],
                fail_silently=False
            )
            # Запись успешной попытки
            Attempt.objects.create(
                mailing=mailing,
                status=Attempt.SUCCESS
            )
        except smtplib.SMTPException as e:
            # Запись неуспешной попытки
            Attempt.objects.create(
                mailing=mailing,
                status=Attempt.FAILED,
                server_response=str(e)
            )
