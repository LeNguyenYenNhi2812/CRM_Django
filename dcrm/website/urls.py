from . import views 
from django.urls import path

urlpatterns = [
   path('',views.home,name='home'),
#    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('record/<int:pk>',views.record_pk,name='record_pk'),
    path('delete_record/<int:pk>',views.delete_record_pk,name='delete_record_pk'),
    path('add_record/',views.add_record,name='add_record'),

]