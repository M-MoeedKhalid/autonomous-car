from django.urls import re_path
from carroutes import views

urlpatterns = [
    re_path(r'^routes/(?P<route>[\w\-]+)/$', views.CarRoutes.as_view(), name='routes'),
]
