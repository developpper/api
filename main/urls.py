"""nss URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from rest_framework.authtoken import views

from django.conf.urls import url

from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),

    path('api/', include('api.urls')),
    path('api/nss/', include('api.nss.urls')),
    path('api/notes/', include('api.notes.urls')),
    path('api/users/', include('api.users.urls')),
    path('api/freestyle/', include('api.freestyle.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'NSS Admin Panel'                    # default: "Django Administration"
admin.site.index_title = 'NSS Admin Panel'                 # default: "Site administration"
admin.site.site_title = 'NSS Admin Panel'
