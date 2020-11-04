from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('parse_input/', views.parse_input, name='parse_input'),
]
