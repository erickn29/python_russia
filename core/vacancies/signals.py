from django.db.models.signals import pre_save
from django.dispatch import receiver

from vacancies.models import StackTool


@receiver(pre_save, sender=StackTool)
def check_empty_expired_at(sender, instance, **kwargs):
    if instance.name:
        instance.name = instance.name.replace(" ", "_").lower()
