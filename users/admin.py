# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile


# Register your models here.
# Registering models for the admin site in one line using decorator
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # list_display sets the column fields you want to see in the Profile admin site=
    list_display = ('user', 'website', 'phone_number', 'profile_picture')
    # Set a link in the listed fields to get the detail of the profile
    list_display_links = ('user', 'website')
    list_editable = ('phone_number', 'profile_picture')

    # Enable search to the Profile admin site
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    # fieldsets lets you set and arrange the positions of the fields in the ADD or CHANGE interfaces
    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'profile_picture'),
            ),
        }),
        ('Additional Information', {
            'fields': (
                ('website', 'phone_number'),
                'biography',
            ),
        }),
        ('Other', {
            'fields': ('created', 'modified')
        })
    )

    readonly_fields = ('created', 'modified')


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (
        ProfileInline,
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
