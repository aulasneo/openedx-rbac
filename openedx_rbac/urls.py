from django.urls import path
from .views import CheckUserPermission

urlpatterns = [
    path('user-permissions/', CheckUserPermission.as_view(), name='user-permissions'),
]
