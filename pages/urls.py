from django.urls import path

# Views
from .views import homeview

urlpatterns = [
    path("", homeview, name="home"),
]
