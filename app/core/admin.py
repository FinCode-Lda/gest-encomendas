from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from import_export.admin import ImportExportMixin
from users.models import User
from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


class ServicoAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price'
    ]



admin.site.register(User, UserAdmin)
admin.site.register(models.Servico, ServicoAdmin)
admin.site.register(models.Carga)
admin.site.register(models.CategoriaCarga)
admin.site.register(models.Notificacao)
admin.site.register(models.Remetente)
admin.site.register(models.Receptor)
admin.site.register(models.Rota)
admin.site.register(models.TarifaPeso)
admin.site.register(models.TarifaVolume)
admin.site.register(models.Transportador)
admin.site.register(models.Viatura)
