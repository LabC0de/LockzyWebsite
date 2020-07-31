from django.contrib import admin

# Register your models here.
from .models import ContentTable, Article

admin.site.register(ContentTable)
admin.site.register(Article)