from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.views.static import serve
 

urlpatterns = [
    # Examples:
    # url(r'^$', 'museos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'appmuseos.views.mylog'),
    url(r'^logout$', logout, {'next_page':'/'}),
    url(r'^logout$', 'appmuseos.views.main'),    
    url(r'^like$', 'appmuseos.views.like'),            
    url(r'^$', 'appmuseos.views.main'),
    url(r'^museos$', 'appmuseos.views.list_museum'),
    url(r'^about$', 'appmuseos.views.information'),
    url(r'^museo/(\d+)', 'appmuseos.views.museum'),
    url(r'^style.css$', 'appmuseos.views.style'),
    url(r'^print.css$', 'appmuseos.views.pri'),
    url(r'static/(.*)$', serve, {'document_root': 'sfiles'}),
    url(r'^.*/config$', 'appmuseos.views.configuration'),
    url(r'^(.*)$', 'appmuseos.views.user_page'),
    
]
