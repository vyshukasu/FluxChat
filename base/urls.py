'''from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.lobby),
    path('room/', views.room),
    path('get_token/', views.getToken),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/',views.user_logout , name='user_logout'),
]'''
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.my_login, name='my_login'), 
     path('register/',views.register,name='register'), # Redirect to login initially
    path('room/', views.room, name='room'),
    path('get_token/', views.getToken, name='get_token'),

    path('create_member/', views.createMember, name='create_member'),
    path('get_member/', views.getMember, name='get_member'),
    path('delete_member/', views.deleteMember, name='delete_member'),

    path('lobby/', views.lobby, name='lobby'),  # Lobby page
    
    #path('user_logout/', views.user_logout, name='user_logout'),  # Logout page
]
