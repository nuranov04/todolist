"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from todo.views import (
    todoView,
    create_todo,
    delete_data,
    update_data
)
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoView, name='index'),
    path('create_todo/', create_todo, name='create-todo'),
    path('delete_todo/<int:id>/', delete_data, name='delete-todo'),
    path('update_todo/<int:id>', update_data, name='update-todo'),
]
