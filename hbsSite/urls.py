from django.urls import path
from django.views.generic import TemplateView

from hbsSite.views import HBSView, SystemView

urlpatterns = [
    path('', HBSView.as_view(), name='hbs'),
    path('o-systemie', SystemView.as_view(), name='system'),
    path('aebrxylwukyqsa7gaxohgafjfeo20p.html/', TemplateView.as_view(template_name="sites/aebrxylwukyqsa7gaxohgafjfeo20p.html")),
]