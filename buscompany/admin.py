from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from buscompany.models import Salesperson, TerminalAgent, Manager, Customer

class SalespersonInline(admin.StackedInline):
    model = Salesperson
    can_delete = False
    verbose_name_plural = 'salespeople'

class TerminalAgentInline(admin.StackedInline):
    model = TerminalAgent
    can_delete = False
    verbose_name_plural = 'terminal agents'

class ManagerInline(admin.StackedInline):
    model = Manager
    can_delete = False
    verbose_name_plural = 'managers'

class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'customers'

class UserAdmin(UserAdmin):
    inlines = (SalespersonInline, TerminalAgentInline, ManagerInline, CustomerInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

