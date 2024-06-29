import rest_framework_simplejwt.authentication
from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from app.views.Login import RegisterView
from app.views.Login import Loginview
from app.views.Login import LogoutView


urlpatterns = [
    path("api/", include("app.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh", TokenObtainPairView.as_view()),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', Loginview.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name = "logout")
]
