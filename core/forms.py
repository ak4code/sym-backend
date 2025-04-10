from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    """Форма входа"""

    email = forms.EmailField(label='Email', max_length=255)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
                if not user.check_password(password):
                    raise forms.ValidationError('Неверный пароль')
                if not user.is_active:
                    raise forms.ValidationError('Этот аккаунт неактивен')
            except User.DoesNotExist:
                raise forms.ValidationError('Пользователь с таким email не найден')
        return cleaned_data
