from django.contrib import admin

# Register your models here.
from business_api import models

admin.site.register(models.Business)
admin.site.register(models.BusinessFeedItem)