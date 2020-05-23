from django.contrib import admin
from .models import Page


# Register your models here.
class PagesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Page, PagesAdmin)