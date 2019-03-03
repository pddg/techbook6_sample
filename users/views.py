from rest_framework import generics, permissions, response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    """独自のトークンを取得するView"""
    serializer_class = MyTokenObtainPairSerializer


class NoAuthRequiredView(generics.RetrieveAPIView):
    # 誰でも許可する
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return response.Response({'message': 'hello'})


class AuthRequiredView(generics.RetrieveAPIView):
    # ログインを必須とする
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return response.Response({'message': f'hello {request.user.username}'})
