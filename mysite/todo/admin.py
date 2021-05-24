from django.contrib import admin
from .models import TodoItem
from .views import update_data

admin.site.register(TodoItem)

# Register your models here.
