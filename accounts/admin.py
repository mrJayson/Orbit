from django.contrib import admin
from .models import Account
from .forms import AccountAdminForm


class AccountAdmin(admin.ModelAdmin):
    form = AccountAdminForm


admin.site.register(Account, AccountAdmin)
