from django.contrib import admin
from Products.models import Production, Suppliers, Supply, Bid

admin.site.register(Suppliers)
admin.site.register(Production)
admin.site.register(Supply)
admin.site.register(Bid)