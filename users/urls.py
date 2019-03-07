from django.urls import path

from .views import MyTokenObtainPairView, NoAuthRequiredView, AuthRequiredView

urlpatterns = [
    # 認証が不要なView
    path('hello/', NoAuthRequiredView.as_view()),
    # 認証が必要なView
    path('hello_with_auth/', AuthRequiredView.as_view())
]
