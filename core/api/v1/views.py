from rest_framework import serializers, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User


class UserMeAPIView(APIView):
    """APIView для получения информации о текущем пользователе"""
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    class UserMeResponseSerializer(serializers.ModelSerializer):
        """Сериализатор данных о текущем пользователе"""

        class Meta:
            model = User
            fields = ['id', 'email', 'last_login']

    def get(self, request: Request) -> Response:
        """Получение информации о текущем пользователе"""
        serializer = self.UserMeResponseSerializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
