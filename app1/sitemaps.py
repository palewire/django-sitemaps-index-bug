from django.contrib.sitemaps import Sitemap

class FakeSitemap(Sitemap):
    limit=5
    def items(self):
        return [Fakepage("/app1/%s" % str(i)) for i in range(0,100)]


class Fakepage:
    def __init__(self, url):
         self.url = url
    def get_absolute_url(self):
        return self.url

