from django.conf.urls import url
from .views import gcd_view
from .views import prime_view


urlpatterns = [
    url(r'^gcd/(?P<left>[0-9]+)/(?P<right>[0-9]+)$', gcd_view),
    url(r'^prime/(?P<n>[0-9]+)$', prime_view),
]
