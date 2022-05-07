from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import BlogPost


@receiver(post_save, sender=BlogPost)
def send_title(sender, instance, created, **kwargs):
    if created:
        print(instance.title)
    