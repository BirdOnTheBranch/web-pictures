from django.contrib import admin
from .models import Pages, Category


# Register your models here.
class PagesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Pages, PagesAdmin)
admin.site.register(Category, PagesAdmin)
