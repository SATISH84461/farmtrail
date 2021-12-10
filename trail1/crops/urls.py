from django.urls import path
from . import views


app_name = 'crops'
urlpatterns = [
    path("",views.index,name = "index"),
    path("create_listing",views.create_listings, name="create_listing"),
    path("my_listing",views.my_listing,name="my_listing"),
    path("crops_details/<str:g_id>",views.crops_details,name="crop_details"),
]