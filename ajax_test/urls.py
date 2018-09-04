from django.contrib import admin
from django.urls import include, path
from django.views.generic import base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
]
