from django.contrib import admin
from Products.models import Production, Suppliers, Bid, Supply

admin.site.register(Suppliers)
admin.site.register(Production)
admin.site.register(Supply)
admin.site.register(Bid)