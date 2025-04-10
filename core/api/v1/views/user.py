from rest_framework import serializers, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User


class UserMeAPIView(APIView):
    """APIView для получения информации о текущем пользователе"""
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    class UserMeResponseSerializer(serializers.ModelSerializer):
        """Сериализатор данных о текущем пользователе"""

        followers_count = serializers.IntegerField(source='followers.count')
        following_count = serializers.IntegerField(source='following.count')

        class Meta:
            model = User
            fields = ['id', 'email', 'last_login', 'followers_count', 'following_count']

    def get(self, request: Request) -> Response:
        """Получение информации о текущем пользователе"""
        serializer = self.UserMeResponseSerializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
