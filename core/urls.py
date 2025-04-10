from django.urls import path

from core.views import home_page, login_page, logout_page

app_name = 'core'

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]