"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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


from django.urls import path

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.mainindexpage),
    url(r'^hotel/', include("hotel.urls")),
    url(r'^manager/', include("manager.urls")),
    url(r'^user/', include("user.urls")),

    #url(r'^paypal/', include(" paypal.standard.ipn.urls"))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)