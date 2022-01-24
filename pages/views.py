from django.shortcuts import render


def homeview(request):
    template_name = "pages/index.html"
    context = {}

    return render(request, template_name, context)


def property_portfolio_management(request):
    template_name = "pages/services/property_portfolio_management.html"
    context = {}

    return render(request, template_name, context)


def property_rentals(request):
    template_name = "pages/services/property_rentals.html"
    context = {}

    return render(request, template_name, context)
