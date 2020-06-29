from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "space"
urlpatterns=[
    url('^$',views.homepage,name = 'homepage'),
    url(r'^search', views.search_product, name='search'),
    url(r'^about', views.about, name = 'about'),
    url(r'^contact', views.contact, name = 'contact'),
    url(r'category/(\d+)',views.filter_by_category,name ='category'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)