from django.contrib.sitemaps import Sitemap 
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    i18n = True

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated