from django.views.generic.edit import CreateView

from .models import Resource

class ResourceCreateView(CreateView):
    model = Resource
    template_name = "app/base.html"
    fields = [
        "code_repository",
    ]

