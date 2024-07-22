from django.urls import path
from .views import RegisterView, CurrentUserView, imagePage
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('user/', CurrentUserView.as_view()),
    path('user/avatar/<str:image_title>/', imagePage)
]
