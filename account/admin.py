from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.roles.mixins import UserAdminMixin
from account.roles import operator, subadmin
from account.choices import UserRole
from account.models import (
    User,
    Region,
    City
)


class UserAdmin(UserAdminMixin, admin.ModelAdmin):
    def save_model(self, request, obj, form, change) -> None:
        new_password = form.data['password']
        if not change or \
            not self.get_object(request, obj.id).password == new_password:     
            obj.set_password(new_password)
        return super().save_model(request, obj, form, change)
    
    
admin.site.register(User, UserAdmin)
admin.site.register(Region)
admin.site.register(City)