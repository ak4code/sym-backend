from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from core.forms import LoginForm


@login_required
def home_page(request):
    """Домашняя страница"""
    return TemplateResponse(request, 'core/pages/home.html', {})


def login_page(request):
    """Страница авторизации"""
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('core:home')
            else:
                form.add_error(None, 'Ошибка аутентификации')
    else:
        context['form'] = LoginForm()
    return TemplateResponse(request, 'core/pages/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('core:login')