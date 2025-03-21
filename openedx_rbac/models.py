"""
Database models for openedx_rbac.
"""
from django.db import models
from model_utils.models import TimeStampedModel


class Role(TimeStampedModel):
    """
    Represents a role within the system, used to assign permissions to users.

    .. pii: True
    .. pii_types: id
    .. pii_retirement: local_api
    """

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'<Role, ID: {self.id}, Name: {self.name}>'



class Permission(TimeStampedModel):
    """
    Defines specific permissions that can be assigned to roles within the system.

    .. pii: True
    .. pii_types: id
    .. pii_retirement: local_api
    """

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'<Permission, ID: {self.id}, Name: {self.name}>'

