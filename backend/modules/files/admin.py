from django.contrib import admin

from .models import FileUploaded


class FileUploadedAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "created_at", "updated_at", "size"]
    search_fields = ["user", "title"]
    list_filter = ["user", "created_at", ]


admin.site.register(FileUploaded)
