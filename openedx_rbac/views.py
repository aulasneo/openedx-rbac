from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from bridgekeeper import perms

User = get_user_model()

class GetUserPermissions(viewsets.ModelViewSet):
    """
    API endpoint for managing users and their roles using Bridgekeeper.
    """

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def has_permission(self, request):
        """ Check if the user has a specific permission using Bridgekeeper """
        permission_codename = request.query_params.get('permission_codename')
        if not permission_codename:
            return Response({'error': 'Permission codename is required'}, status=400)
        
        # Verificar permiso usando Bridgekeeper
        has_perm = perms.check(request.user, permission_codename)
        
        return Response({'has_permission': has_perm})
