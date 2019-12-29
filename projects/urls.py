from django.conf.urls import url, include
from .views import projects

urlpatterns = [
    url(r'^$', projects, name="donation"),
]
