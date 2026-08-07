

from django.urls import path
from . import views

urlpatterns = [
   path("", views.Home, name="home"),
#    path("login", views.Home, name="home"),
   path("logout/", views.logout_user, name="logout"),
   path('record/<int:pk>', views.customer_record, name='record'),
   path('client/<int:pk>', views.detail_record, name='client'),
   path('add_record/', views.add_record, name='add_record'),
   path("register/", views.register_user, name="register"),
   path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
   path('delete_client/<int:pk>', views.delete_client, name='delete_client'),
   path('update_record/<int:pk>', views.update_record, name='update_record'),
   path('update_record/<int:pk>', views.update_record, name='update_record'),
   path('update_client/<int:pk>', views.update_client, name='update_client'),
   path('add_client/', views.add_client, name='add_client'),
   path('show_client/', views.show_client, name='show_client'),
   path("calculate/",views.CalculateView,  name="calculate")



]
