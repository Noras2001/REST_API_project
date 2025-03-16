# core/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    # Проверяем для нужных приложений
    if sender.name in ['auth', 'core']:
        roles = ['admin', 'manager', 'user']
        for role in roles:
            Group.objects.get_or_create(name=role)
