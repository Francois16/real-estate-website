from django.urls import path

# Views
from .views import property_add, property_detailview, property_listview

urlpatterns = [
    path("all/", property_listview, name="property_list"),
    path("details/<uuid:pk>/", property_detailview, name="property_detail"),
    path("add/", property_add, name="property_add"),
]
