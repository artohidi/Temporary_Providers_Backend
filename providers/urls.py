"""providers URL Configuration

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
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from tracking.models import ProviderBasicInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderBasicInfo
        fields = ('id', 'first_name', 'last_name', 'cell_phone_number')


class UserViewSet(viewsets.ModelViewSet):
    queryset = ProviderBasicInfo.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'provider', UserViewSet)

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^tracking/', include('tracking.urls')),
                  url(r'^', include(router.urls)),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
