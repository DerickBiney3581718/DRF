from .permissions import IsStaffEditorPermission
from rest_framework.permissions import IsAdminUser

class StaffEditorPermissionMixin():
    permission_classes = [IsAdminUser, IsStaffEditorPermission]