from django.shortcuts import render


def homeview(request):
    template_name = "pages/index.html"
    context = {}

    return render(request, template_name, context)
