from django.conf.urls import url, include
from .views import payment

urlpatterns = [
    url(r'^$', payment, name="payment")
]
