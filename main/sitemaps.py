# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse
from main.views import PAGES
from main.urls import urlpatterns


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        ITEM_LIST = []
       
        for url in urlpatterns:
            if url.name != "page":
                ITEM_LIST.append((f"main:{url.name}",{}))

        for slug in PAGES.keys():
            ITEM_LIST.append(('main:page', {"slug":slug}))
        return ITEM_LIST

    def location(self, name):
        return reverse(name[0], kwargs=name[1])
