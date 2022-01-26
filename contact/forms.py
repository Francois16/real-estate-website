from django import forms


class ContactForm(forms.Form):

    SUBJECT_CHOICES = (
        (None, "-------"),
        ("PPM", "Property Portfolio Management"),
        ("RM", "Rental Management"),
        ("S", "Sell My Property"),
    )

    first_name = forms.CharField(max_length=55, required=True)
    last_name = forms.CharField(max_length=55, required=True)
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    email = forms.EmailField(max_length=255, required=True)
    message = forms.CharField(required=True, widget=forms.Textarea())
