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
    )

    def __init__(self, *args, **kwargs):
        super(AddPropertyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            # We have a try/except block here because TextArea doesn't have an 'input_type'
            # This will cause an AttributeError in which case we just add the 'form-control'
            # class to it
            try:
                if visible.field.widget.input_type == "checkbox":
                    visible.field.widget.attrs["class"] = "form-check-input mb-3"
                else:
                    visible.field.widget.attrs["class"] = "form-control mb-3"
            except AttributeError:
                visible.field.widget.attrs["class"] = "form-control mb-3"


class AddPropertyImagesForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ("images",)

    images = forms.FileField(
        help_text="Please only add '.jpg' or '.png' image files",
        widget=forms.ClearableFileInput(
            attrs={
                "multiple": True,
            }
        ),
    )
