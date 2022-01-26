from email import message
from django.shortcuts import redirect, render
from django.contrib import messages

# Forms
from .forms import ContactForm


def contact_view(request):
    template_name = "contact/contact-us.html"
    context = {"form": ContactForm}

    return render(request, template_name, context)


def _send_email(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            print("Sending E-mail is not implemented.")
            messages.add_message(
                request, messages.SUCCESS, "Thank you for contacting us! We will be in touch shortly."
            )
            return redirect("home")
