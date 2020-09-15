from django.contrib import admin
from .models import Publication


class PublicationAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["title", "date"]}),
        ("Image", {"fields": ["image"]}),
        ("Content", {"fields": ["content"]}),
        ("Author", {"fields": ["author"]})
    ]


admin.site.register(Publication, PublicationAdmin)
