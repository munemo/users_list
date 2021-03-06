"""m_tv URL Configuration

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
from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from forms import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'bookings', views.BookingViewSet)
router.register(r'slotts', views.SlottViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.index, name="index"),
    #url(r'^users/$', views.users, name="users"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
