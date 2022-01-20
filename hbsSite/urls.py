from django.urls import path
from hbsSite.views import HBSView

urlpatterns = [
    path('', HBSView.as_view(), name='hbs'),
]