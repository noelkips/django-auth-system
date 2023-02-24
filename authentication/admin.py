from django.contrib import admin
from .models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('mobile', 'first_name', 'last_name', 'email')


    
admin.site.register(UserAccount, UserAccountAdmin)

