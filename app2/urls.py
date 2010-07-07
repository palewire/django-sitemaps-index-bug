from app2.sitemaps import FakeSitemap
from django.conf.urls.defaults import *


# Sitemaps
sitemaps = {
    'fake': FakeSitemap,
}

urlpatterns = patterns('django.contrib.sitemaps.views',
    url(r'^sitemap\.xml$', 'index', {
        'sitemaps': sitemaps
        }, name='app2-sitemap'),

    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {
        'sitemaps': sitemaps
        }, name='app2-sitemap-section'),
)
