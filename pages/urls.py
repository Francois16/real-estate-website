from django.urls import path

# Views
from .views import homeview, property_portfolio_management, property_rentals

urlpatterns = [
    path("", homeview, name="home"),
    path("services/property-rentals/", property_rentals, name="rentals"),
    path(
        "services/property-portfolio-management/", property_portfolio_management, name="portfolio_management"
    ),
]
