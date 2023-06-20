from django.urls import path
from .views import *
urlpatterns = [
    path('',empty),
    path('pi/',home),
    path('li/',location),
    path('pm/',movement),
    path('upi/',edit_product_id),
    path('uli/',edit_location_id),
    path('upm/',edit_pro_movement),
    path('v/',view),


    path('product_id/',add_product_id),
    path('location_id/',add_loction_id),
    path('movement/',add_product_movement),
    path('update_pro_id/',edit_pro),
    path('update_location/',edit_location),
    path('update_movement/',edit_movement),    
    path('display/',views)

]