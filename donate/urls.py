from django.conf.urls import url
from .views import view_donate, amount_to_donate, adjust_donation

urlpatterns = [
    url(r'^$', view_donate, name='view_donate'),
    url(r'^add/(?P<id>\d+)', amount_to_donate, name='amount_to_donate'),
    url(r'^adjust/(?P<id>\d+)', adjust_donation, name='adjust_donation'),
]
