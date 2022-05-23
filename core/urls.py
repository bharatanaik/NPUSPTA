# NPUSPTA main urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import StaticViewSitemap



sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
