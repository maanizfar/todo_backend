from django.urls import path, re_path, include
from rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('', include('allauth.urls')),
    path('', include('django.contrib.auth.urls'))
]
