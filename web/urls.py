from django.urls import path
from .views import *
urlpatterns = [
    path('',web_home,name='home'),
    path('cat/<str:pk>/',products,name='cat'),
     path('pro/<str:pk>/',view_product,name='pro'),
     path('shop/',shop,name='shop'),

]
