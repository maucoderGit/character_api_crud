"""API urls file"""
# Django
from django.urls import path
from .views import CharacterView

app_name = 'characters'
urlpatterns = [
    path('characters/', CharacterView.as_view(), name='crud'),
    path('characters/<int:id>', CharacterView.as_view(), name='options')
]

