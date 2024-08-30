from main.apps import MainConfig
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import main, ContactCreateView

app_name = MainConfig.name

urlpatterns = [
                  path("", main, name="main"),
                  path("contact_create/", ContactCreateView.as_view(), name="contact_create"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
