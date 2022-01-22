from operator import attrgetter
from random import vonmisesvariate
from signal import valid_signals
from django import forms


# Models
from .models import Property, PropertyImage, PropertyFeature


class AddPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"

    features = forms.ModelMultipleChoiceField(
        queryset=PropertyFeature.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="",
    )


class AddPropertyImagesForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ("images",)

    images = forms.FileField(
        help_text="Please only add '.jpg' or '.png' image files",
        label="",
        widget=forms.ClearableFileInput(
            attrs={
                "multiple": True,
            }
        ),
    )


class PropertySearchForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = (
            "property_type",
            "property_status",
            "province",
        )
