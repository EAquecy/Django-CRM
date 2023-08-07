from django.urls import path
from . import views

urlpatterns = [
    #the name tag is like the id for the url. It represents it everywhere
    path('',views.home, name = 'home'),
    #path('',views.login_user, name = 'login'),
    path('logout/',views.logout_user, name = 'logout'),
    path('register/',views.register_user, name = 'register'),

]
