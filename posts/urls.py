from django.conf.urls import url
from posts import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.post_list),
    url(r'^create/$', views.post_create),
    url(r'^detail/$', views.post_detail),
    url(r'^update/$', views.post_update),
    url(r'^delete/$', views.post_delete),
]