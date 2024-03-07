from django.urls import path
from userapp import views

urlpatterns = [
   
    path('',views.vtem,name='vtem'),
    path('vfest/',views.vfest,name='vfest'),
    path('vvazhi/',views.vvazhi,name='vvazhi'),
    path('index/',views.index,name='index'),
    path('home/',views.home,name='home'),
	path('login/',views.loginview,name="login"),
	path('logout',views.logout_view),
	path('sign_up/',views.sign_up,name="signup")
   
   
]

