from django.contrib import admin

from MVTLucinaApp.models import *

# Register your models here.

class FamiliaConvivienteAdmin(admin.ModelAdmin):
    
    list_display = ('nombre','nacimiento', 'edad', 'parentezco')
    
class FamiliaExtendidaAdmin(admin.ModelAdmin):
    
    list_display = ('nombre','nacimiento', 'edad', 'parentezco')
    
admin.site.register(FamiliarConviviente, FamiliaConvivienteAdmin)
admin.site.register(FamiliarExtendida, FamiliaExtendidaAdmin)

# admin, admin
