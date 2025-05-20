from . import views
from django.urls import path

urlpatterns = [
    path('', views.new_account, name='new_account'),
    path('activate_account/', views.activate_account, name='activate_account'),

]

