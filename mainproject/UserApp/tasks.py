from celery import shared_task
from .models import CustomUserRegistration
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_mail_to_us():
    users = CustomUserRegistration.objects.values( )
    send_mail()
