from django.conf.urls import patterns, include, url
from cart import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecomstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.show_cart, name="show_cart"),
)

