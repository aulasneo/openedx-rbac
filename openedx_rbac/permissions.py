from bridgekeeper import perms
from bridgekeeper.rules import is_staff, blanket_rule

perms['is_staff'] = is_staff

perms['is_superuser'] = blanket_rule(lambda user, obj=None: user.is_superuser)