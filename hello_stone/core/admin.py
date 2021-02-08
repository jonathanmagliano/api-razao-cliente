from django.contrib import admin
from core.models import Client
from core.models import Seller

# Register models


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'creationDate', 'attDate', 'email', 'location')
    list_filter = ('role', 'creationDate', 'location')


class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'creationDate', 'attDate', 'email', 'location')
    list_filter = ('role', 'creationDate', 'location')


admin.site.register(Client, ClientAdmin)
admin.site.register(Seller, SellerAdmin)
