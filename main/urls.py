
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('form/',views.project_form , name='form'),
    path('search/',views.search, name='search'),
    path('email/',views.email , name='email'),

]
