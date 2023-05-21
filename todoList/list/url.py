from django.contrib import admin
from django.urls import path
from list import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('addEvent',views.addEvent,name='addEvent'),
    path('deleteEvent/<int:deleteId>',views.deleteEvent,name="deleteEvent"),
    path('updateEvent/<int:updateId>', views.updateEvent,name="updateEvent"),
    path('search', views.search,name="search"),

]
