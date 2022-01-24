from django.urls import path


from .views import contact_view, _send_email

urlpatterns = [
    path("contact-us/", contact_view, name="contact"),
    path("send-email/", _send_email, name="send-email"),
]
