from django.urls import path
from templeapp import views

urlpatterns = [
   
    path('',views.addtem),
    path('add/',views.addfest),
    path('addv/',views.addvazhi),
    path('vitem/',views.vitem),
    path('vifes/',views.vifest),
    path('vivazhi/',views.vivazhi),
    path('update/(?P<pk>\w+)',views.temupdate,name="update"),
    path('delete/(?P<pk>\w+)',views.temdelete,name="delete"),
    path('festup/(?P<pk>\w+)',views.festupdate,name="festup"),
    path('festdel/(?P<pk>\w+)',views.festdelete,name="festdel"),
    path('vazhiup/(?P<pk>\w+)',views.vazhiupdate,name="vazhiup"),
    path('vazhidel/(?P<pk>\w+)',views.vazhidelete,name="vazhidel"),

    
]

