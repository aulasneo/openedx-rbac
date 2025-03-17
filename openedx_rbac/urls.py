"""
URLs for openedx_rbac.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from openedx_rbac.views import GetUserPermissions

router = DefaultRouter()
router.register(r'user-permissions', GetUserPermissions, basename='user-permissions')

urlpatterns = [
    path('', include(router.urls)),
]
