
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Banner


@receiver(signal=pre_save, sender=Banner)
def update_banner_last_update_time(sender, instance, **kwargs):
    if instance.pk is not None:
        instance.updated_at = timezone.now()
    return instance
