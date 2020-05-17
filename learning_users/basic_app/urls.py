from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'basic_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('', views.index,name='index'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('special/', views.special,name='special'),
    path('logout/', views.user_logout, name='logout'),
]
