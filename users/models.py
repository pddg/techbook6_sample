from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """ユーザモデル操作用のマネージャ"""

    def create_user(self, username: 'str', email: 'str', password: 'str', **extra_fields) -> 'User':
        """ユーザを作成するメソッド"""
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username: 'str', email: 'str', password: 'str', **extra_fields):
        """管理ユーザを作成するメソッド"""
        admin_attrs = {"is_superuser": True, "is_staff": True, "is_active": True}
        for key, val in admin_attrs.items():
            extra_fields[key] = val
        return self.create_user(username=username, email=email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ユーザのモデル"""
    username = models.CharField(max_length=64, unique=True, verbose_name='ユーザ名')
    email = models.EmailField(max_length=255, unique=True, verbose_name='メールアドレス')
    # ユーザがアクティベーション済みかどうか
    is_active = models.BooleanField(default=False)
    # 管理ユーザかどうか
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # 自作のマネージャを登録
    objects = UserManager()
    # ユーザ名として使うフィールドを明示
    USERNAME_FIELD = 'username'
    # ユーザ作成時の必須項目
    REQUIRED_FIELDS = ('email', 'password')
