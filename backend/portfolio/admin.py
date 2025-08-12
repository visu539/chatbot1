from django.contrib import admin
from .models import Account, Holding, Transaction, SIP

admin.site.register(Account)
admin.site.register(Holding)
admin.site.register(Transaction)
admin.site.register(SIP)