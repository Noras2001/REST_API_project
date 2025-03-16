# core/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group

class RoleAccessTests(TestCase):
    def setUp(self):
        # Создаем группы
        self.admin_group, _ = Group.objects.get_or_create(name='admin')
        self.manager_group, _ = Group.objects.get_or_create(name='manager')
        self.user_group, _ = Group.objects.get_or_create(name='user')
        
        # Создаем тестовых пользователей
        self.admin_user = User.objects.create_user(
            username='admin_user',
            password='Password123'
        )
        self.admin_user.groups.add(self.admin_group)
        
        self.manager_user = User.objects.create_user(
            username='manager_user',
            password='Password123'
        )
        self.manager_user.groups.add(self.manager_group)
        
        self.regular_user = User.objects.create_user(
            username='regular_user',
            password='Password123'
        )
        self.regular_user.groups.add(self.user_group)
        
        # Клиент для тестирования HTTP-запросов
        self.client = Client()
    
    def test_admin_access_dashboard(self):
        # Логин под пользователем admin
        self.client.login(username='admin_user', password='Password123')
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 200, "Пользователь с ролью admin должен иметь доступ к админ-панели.")
    
    def test_manager_no_access_dashboard(self):
        # Логин под пользователем manager
        self.client.login(username='manager_user', password='Password123')
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 403, "Пользователь с ролью manager не должен иметь доступ к админ-панели.")
    
    def test_regular_user_no_access_dashboard(self):
        # Логин под пользователем regular_user
        self.client.login(username='regular_user', password='Password123')
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 403, "Пользователь с ролью user не должен иметь доступ к админ-панели.")

# python manage.py test
