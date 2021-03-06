from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.homepage, name = 'homepage'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^Image/(\d+)',views.Image,name ='Image')
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
