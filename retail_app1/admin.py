from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.product)
admin.site.register(models.user)
admin.site.register(models.order)
admin.site.register(models.comment)
