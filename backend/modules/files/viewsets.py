from rest_framework import authentication, permissions, viewsets

from .models import FileUploaded
from .serializers import FileUploadedSerializer


class FileUploadedViewSet(viewsets.ModelViewSet):
    serializer_class = FileUploadedSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = FileUploaded.objects.all()
