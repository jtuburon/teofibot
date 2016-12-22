from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^control$', views.control, name='control'),
    url(r'^render$', views.render_device, name='control')
]