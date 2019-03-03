from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class CurrentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """独自のペイロードを付加する"""

    @classmethod
    def get_token(cls, user):
        # 継承元のメソッドを利用してデフォルトのトークンを生成
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # 新しい情報を付加する
        token['is_active'] = user.is_active
        return token
