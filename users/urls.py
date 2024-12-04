from django.conf import settings
from django.conf.urls.static import static

from .views import register, login_view, home_view, activate, logout_view, settings_view, password_reset_view, \
    post_a_review
from django.urls import path

urlpatterns = [
                  path('register/', register, name='register'),
                  path('login/', login_view, name='login'),
                  path('home/', home_view, name='home'),
                  path('activate/<uidb64>/<token>/', activate, name='activate'),
                  path('logout/', logout_view, name='logout'),
                  path('settings/', settings_view, name='settings'),
                  path('post-a-review/', post_a_review, name='post-a-review'),
                  path('password_reset/', password_reset_view, name='password_reset')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
