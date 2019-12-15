from django.conf.urls import url, include
from users.views import login, logout, profile, registration, profile, update
from users import url_reset

urlpatterns = [
    url(r'^login/', login, name="login"),
    url(r'^logout/', logout, name='logout'),
    url(r'^profile/', profile, name='profile'),
    url(r'^register/', registration, name='register'),
    url(r'^update/', update, name='update'),
    url(r'^password-reset/', include(url_reset)),
]