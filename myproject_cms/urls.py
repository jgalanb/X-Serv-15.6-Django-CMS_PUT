from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject_cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?pages$', 'cms_put.views.obtener_lista_pages'),
    url(r'^(\d+)', 'cms_put.views.id_to_page'),
    url(r'/?(.*)', 'cms_put.views.name_to_page')
)
