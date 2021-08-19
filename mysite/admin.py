from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (About, Comment)
# from .forms import (CustomUserCreationForm)


# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     add_form = CustomUserCreationForm

#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             'Other Information',
#             {
#                 'fields': (
#                     'address',
#                     'mobile_number',
#                 )
#             }
#         )
#     )


admin.site.register(About)
admin.site.register(Comment)
# admin.site.register(CustomUser, CustomUserAdmin)
