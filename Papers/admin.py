from django.contrib import admin
from Papers.models import *

# Register your models here.

admin.site.register(Category)
class PaperImageAdmin(admin.StackedInline):
    model = Paper_Image

class PaperAdmin(admin.ModelAdmin):
    inlines = [PaperImageAdmin]

admin.site.register(Paper_Model,PaperAdmin)
admin.site.register(Paper_Image)