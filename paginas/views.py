from django.views.generic import TemplateView

# Create your views here.

class Indexview(TemplateView): #heranção de templateview
    template_name = "index.html"
