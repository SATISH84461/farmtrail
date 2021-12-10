from django.urls import path
from . import views

app_name = 'land'
urlpatterns = [
    path("",views.index,name = "index"),
    path("create_listing",views.create_listings, name="create_listing"),
    path("land_details/<str:g_id>",views.land_details,name="land_details"),
]