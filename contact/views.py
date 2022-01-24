from django.shortcuts import redirect, render


# Forms
from .forms import ContactForm


def contact_view(request):
    template_name = "contact/contact-us.html"
    context = {"form": ContactForm}

    return render(request, template_name, context)


def _send_email(request):

    if request.method == "POST":
        print("sending mail")
        return redirect("home")
