from django.conf.urls import patterns, include, url
from catalog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecomstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name="catalog_home"),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.show_category, name="catalog_category"),
    url(r'^product/(?P<product_slug>[-\w]+)/$', views.show_product, name="catalog_product"),
    
)
