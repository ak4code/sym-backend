from django.urls import path, include

urlpatterns = [
    path('', include('config.urls.pages')),
    path('api/', include('config.urls.api')),
]