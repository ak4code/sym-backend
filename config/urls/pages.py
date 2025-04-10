from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'SYMAdmin'
admin.site.site_title = 'SYMAdmin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
