# core/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import UserRegistrationForm
from .decorators import group_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
            # Получаем выбранную роль и добавляем пользователя в соответствующую группу
            selected_role = form.cleaned_data.get('role')
            group = Group.objects.get(name=selected_role)
            user.groups.add(group)
            messages.success(request, 'Регистрация прошла успешно. Теперь вы можете войти.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def home(request):
    return render(request, 'core/home.html')

@group_required(allowed_groups=['admin'])
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')




@group_required(allowed_groups=['admin'])
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

