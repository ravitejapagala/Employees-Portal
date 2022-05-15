from django.urls import path
from . import views
app_name = "demosampleapp"

urlpatterns = [
    path('',views.register_request,name = "register"),
    path('homepage',views.homepage,name = "homepage"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('fileupload',views.post_article,name = "fileupload"),
    path('allrecords',views.all_records,name = "allrecords")

]