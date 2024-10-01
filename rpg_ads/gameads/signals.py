# gameads/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Reply


@receiver(post_save, sender=Reply)
def send_reply_notification(sender, instance, created, **kwargs):
    if created:

        ad_owner = instance.ad.author
        if ad_owner.email:
            send_mail(
                subject='Новый отклик на ваше объявление',
                message=f'У вас новый отклик от {instance.author.username} на объявление {instance.ad.title}.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[ad_owner.email],
            )
