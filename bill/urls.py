from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from management.admin import admin_site

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', admin_site.urls)
]
