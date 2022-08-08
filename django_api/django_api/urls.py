"""Django main url file."""
# Django
from django.contrib import admin
from django.urls import path, include
# Python


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]
