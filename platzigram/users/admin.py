"""User admin classes"""
#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#Our Models
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk','user','phone_number','webside','picture') #Campos de la tabla
    list_display_links = ('pk','user') #Link de referencía
    list_editable = ('webside','phone_number','picture') #Canpos editables

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )   #Buscador

    list_filter = ('created',
                  'modified',
                 'user__is_active',
                 'user__is_staff') #Creacion de filtros

    fildsets = (
        ('Profile',{
            'fields':((('user','picture'),
                    ('phone_number','webside'),)
            ),
        }),
        ('Extra info',{
            'fields':((('webside', 'phone_number'),
                    ('biography'),)
            )
        }),
        ('Metadata',{
            'fields':(('created','modified'),)
        })
    )

    readonty_fields = ('created','modified','user') #Para que no editen los campos

class ProfileInLine(admin.StackedInline): #Es la la parte en donde creamos un usuarios
                                          #Pasamos los datos de profile a la de Add User
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


