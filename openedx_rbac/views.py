from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from bridgekeeper import perms

User = get_user_model()

class CheckUserPermission(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.query_params.get('user_id')
        permission_name = request.query_params.get('permission_name')

        if not user_id or not permission_name:
            return Response({'error': 'Se requieren user_id/permission_name'}, status=400)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=404)

        if permission_name in perms:
            has_perm = perms[permission_name].is_possible_for(user)
            return Response({'has_permission': has_perm})
        else:
            return Response({'error': 'Permiso no encontrado'}, status=400)
