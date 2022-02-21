from django.contrib import admin
from Users.models import Users, Workers, Administration


admin.site.register(Users)
admin.site.register(Workers)
admin.site.register(Administration)