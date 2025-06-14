"""
URL configuration for hirehub_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

# from ats import views as ats_views # No longer needed for handlers if using string paths

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ats/', include('ats.urls')),  # Include URLs from the ATS application
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = 'ats.views.custom_bad_request'
handler403 = 'ats.views.custom_permission_denied'
handler404 = 'ats.views.custom_page_not_found'
handler500 = 'ats.views.custom_server_error'
