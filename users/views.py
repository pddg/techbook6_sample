from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    """独自のトークンを取得するView"""
    serializer_class = MyTokenObtainPairSerializer
