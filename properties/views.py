from distutils.log import error
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.db.models import Q

# models
from .models import Property
from .helpers import save_photos

# Forms
from .forms import AddPropertyForm, AddPropertyImagesForm, PropertySearchForm


def property_listview(request):
    template_name = "property/list.html"

    if request.method == "POST":
        search_form = PropertySearchForm(request.POST)

        if search_form.is_valid():
            data = search_form.cleaned_data
            properties = Property.objects.filter_from_form(data)

    else:
        properties = Property.objects.filter().all().order_by("-created_at")

        # Search form
        search_form = PropertySearchForm()

    recent_properties = Property.objects.all().reverse()[:5]

    # Pagination
    paginator = Paginator(properties, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # End pagination

    context = {
        "properties": page_obj,
        "recent_properties": recent_properties,
        "search_form": search_form,
    }

    return render(request, template_name, context)


def property_detailview(request, pk):
    template_name = "property/detail.html"

    property = Property.objects.get(id=pk)

    context = {
        "property": property,
    }

    return render(request, template_name, context)


def property_add(request):
    template_name = "property/add.html"

    if request.method == "POST":
        form = AddPropertyForm(request.POST, request.FILES)
        image_form = AddPropertyImagesForm(request.POST, request.FILES)

        images = request.FILES.getlist("images")

        if form.is_valid() and image_form.is_valid():
            property = form.save()
            # Create, link and save all images to the property object
            save_photos(property=property, photos=images)

            return redirect("property_list")
        else:
            raise Exception("Form was not valid")
    else:
        form = AddPropertyForm()
        image_form = AddPropertyImagesForm()

    context = {
        "form": form,
        "image_form": image_form,
    }

    return render(request, template_name, context)
