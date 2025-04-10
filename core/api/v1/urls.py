from django.urls import path

from core.api.v1.views import UserMeAPIView

urlpatterns = [
    path('me/', UserMeAPIView.as_view())
]