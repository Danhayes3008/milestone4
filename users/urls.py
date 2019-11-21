from django.conf.urls import url, include
from users.views import Login, logout, profile, registration

urlpatterns = [
    url(r'^login/', Login, name="login"),
    url(r'^logout/', logout, name='logout'),
    url(r'^profile/', profile, name='profile'),
    url(r'^register/', registration, name='register')
]