
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Contact

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    # verbose_name_plural = 'Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

# Unregister the original User admin
admin.site.unregister(User)

# Register the new User admin with profile inline
admin.site.register(User, UserAdmin)
admin.site.register(Contact)
admin.site.register(UserProfile)