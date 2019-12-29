from django.conf.urls import url, include
from .views import projects, housing, training

urlpatterns = [
    url(r'^$', projects, name="donation"),
    url(r'^housing/', housing, name="housing"),
    url(r'^training/', training, name="training"),

]
