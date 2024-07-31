from .views import register, login_view, home_view, activate, logout_view, settings_view, password_reset_view
from django.urls import path

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('logout/', logout_view, name='logout'),
    path('settings/', settings_view, name='settings'),
    path('password_reset/', password_reset_view, name='password_reset')
]
