from . import views
from django.urls import path

urlpatterns = [
    path('', views.class_type_list, name='classes'),
]