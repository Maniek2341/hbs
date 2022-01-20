from django.shortcuts import render
from django.views.generic import TemplateView

class HBSView(TemplateView):
    template_name = 'sites/index.html'