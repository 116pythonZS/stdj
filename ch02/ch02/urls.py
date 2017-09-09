"""ch02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello),
    url(r'^currentTime$', views.current_time),
    url(r'^time/plus/(\d{1,2})$', views.hours_ahead),
    url(r'^custom$', views.customtemplate),
    url(r'^info$', views.display_meta),
    url(r"^search-form$", views.search_form),
    url(r"^search$", views.search),
    url(r'^contact-form$', views.contact),
    url(r'^contact2$', views.contact2),
]
