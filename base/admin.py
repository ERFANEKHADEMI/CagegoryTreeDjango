from django.contrib.admin import ModelAdmin, register
from .models import TreeCategory

@register(TreeCategory)
class GeneralInformationFilesAdmin(ModelAdmin):
    list_display = ('name', 'parent', )