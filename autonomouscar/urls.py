"""autonomouscar URL Configuration

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
from django.urls import re_path
from django.conf.urls import include
from carroutes import views
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    re_path(r'^api/v1/autonomous-car/', include('carroutes.urls')),

]
schema_view = get_swagger_view(title='Autonomous Car API Documentation', patterns=urlpatterns)

# This separation is done to separate primary application urls from helpers ones
urlpatterns = urlpatterns + [
    re_path(r'^$', schema_view),
    re_path(r'^.*/$', views.Error404.as_view(), name='error404')
]

