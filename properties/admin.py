from atexit import register
from django.contrib import admin

# Models
from .models import PropertyFeature, Property, PropertyImage


class PropertyImageInline(admin.StackedInline):
    model = PropertyImage
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "property_status")

    inlines = [
        PropertyImageInline,
    ]


admin.site.register(PropertyImage)
admin.site.register(PropertyFeature)
