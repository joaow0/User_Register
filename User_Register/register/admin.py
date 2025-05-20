from django.contrib import admin
from .models import AccountInfo 

class AccountInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'birthdate', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    ordering = ('-updated_at',)

    # This class customizes how the model appears in the Django admin interface.
    # 'list_display' defines the fields shown in the admin list view.
    # 'list_filter' adds filtering options on the right sidebar.
    # 'ordering' sets the default sorting order for records.

admin.site.register(AccountInfo, AccountInfoAdmin)
