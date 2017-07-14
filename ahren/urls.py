#ahren/urls.py
from django.conf.urls import url
from ahren import views 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$',views.home),
    url(r'^gallery/$', views.gallery),
    url(r'^Add/$', views.add),
    url(r'^AddPost/$', views.addPost),
    url(r'^Delete/$', views.delete),
    url(r'^DeletePost/$', views.deletePost),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)