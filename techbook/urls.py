"""techbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from djoser.urls import base, jwt

from users.views import MyTokenObtainPairView, NoAuthRequiredView, AuthRequiredView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(base)),
    # 先に登録した方が優先される
    path('auth/jwt/create/', MyTokenObtainPairView.as_view()),
    path('auth/', include(jwt)),
    # 認証が不要なView
    path('hello/', NoAuthRequiredView.as_view()),
    # 認証が必要なView
    path('hello_with_auth/', AuthRequiredView.as_view())
]
