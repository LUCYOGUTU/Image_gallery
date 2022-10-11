from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from . models import Image


# class IndexView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["images"] = Image.objects.all()
#         return context

class IndexView(ListView):
    model = Image
    template_name = 'index.html'
    context_object_name = 'images'


class ImageView(CreateView):
    template_name = 'add_image.html'
    model = Image
    fields = '__all__' 
    success_url = '/'
