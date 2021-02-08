from django.urls import path
from app import views
urlpatterns=[
    path("",views.Sample_print.as_view(),name="sample"),
    path("login/",views.login.as_view(),name="login"),



]