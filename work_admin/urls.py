from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_work_admin, name='work_admin'),
]