from django.urls import path
from . import views

app_name='searchcourse'

urlpatterns = [
    path('search', views.search, name='search'),
    path('select', views.select, name='select'),
]
