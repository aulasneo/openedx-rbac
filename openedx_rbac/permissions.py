from bridgekeeper import perms
from bridgekeeper.rules import is_staff, Attribute
from django.contrib.auth.models import Group

# Regla para verificar si un usuario es administrador
perms['is_admin'] = is_staff

# Regla para verificar si un usuario tiene el flag is_superuser
def is_superuser(user):
    return user.is_superuser

perms['is_superuser'] = is_superuser

# Regla para verificar si un usuario pertenece a un grupo específico
def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

perms['is_manager'] = lambda user: is_in_group(user, 'Manager')
perms['is_instructor'] = lambda user: is_in_group(user, 'Instructor')
perms['is_api_admin'] = lambda user: is_in_group(user, 'API Access Request Approvers')