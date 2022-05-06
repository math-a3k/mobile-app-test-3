from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FileUploadedViewSet

router = DefaultRouter()
router.register("files_uploaded", FileUploadedViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
