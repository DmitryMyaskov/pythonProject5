from django.urls import path

from . import views
from .views import GetUsersData,Prints

urlpatterns = [
    path('', GetUsersData.getUserPost,name='home'),
    path('index',Prints.printUser,name='home'),
    path('about-us',Prints.printPost,name='about')
]

