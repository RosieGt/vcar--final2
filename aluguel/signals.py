from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Perfil

@receiver(post_save, sender=User)
def criar_user(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(nome=instance.username, user=instance)