from django.contrib import admin

from .models import FileUploaded


class FileUploadedAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "created_at", "updated_at", "size"]
    list_select_related = ["user", ]
    list_filter = ["user", "created_at", ]
    search_fields = ["user", "title"]


admin.site.register(FileUploaded, FileUploadedAdmin)
