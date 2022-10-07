from django.urls import path
from .views import Indexview

urlpatterns = [
    path("inicio/", Indexview.as_view(), name="Inicio"), #path("endereço/", minhaview, name="nomedaurl")
]