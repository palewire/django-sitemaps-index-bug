from app1.sitemaps import FakeSitemap
from django.conf.urls.defaults import *


# Sitemaps
sitemaps = {
    'fake': FakeSitemap,
}

urlpatterns = patterns('django.contrib.sitemaps.views',
    url(r'^sitemap\.xml$', 'index', {
        'sitemaps': sitemaps
        }, name='app1-sitemap'),

    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {
        'sitemaps': sitemaps
        }, name='app1-sitemap-section'),
)
