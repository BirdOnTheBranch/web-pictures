from django.contrib import admin

from .models import Page


class PagesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'slug', 'likes')


admin.site.register(Page, PagesAdmin)
