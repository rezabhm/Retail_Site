"""retail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import re_path
from django.urls import include
#    path('^check/', include("retail_app1.urls")),

urlpatterns = [

    re_path(r'admin/', admin.site.urls),
    re_path(r'^', include("retail_app1.urls")),
    re_path(r'create_user/', include("retail_app1.urls")),
    re_path(r'accounts/', include("django.contrib.auth.urls")),
    re_path(r'^/accounts/login/home/', include("retail_app1.urls")),
    re_path(r'order/', include("retail_app1.urls")),
    re_path(r'product/(?P<id>[\w]*)/', include("retail_app1.urls")),
    re_path(r'^/comment/', include("retail_app1.urls")),
    re_path(r'profile/(?P<username>[\w]*)/', include("retail_app1.urls")),
    re_path(r'all_profile/', include("retail_app1.urls")),
    re_path(r'^order_query/', include("retail_app1.urls")),
    re_path(r'^order_query/state/', include("retail_app1.urls")),
    re_path(r'^order_query/group/', include("retail_app1.urls")),
    re_path(r'^order_query/name_EN/', include("retail_app1.urls")),
    re_path(r'^order_query/date/', include("retail_app1.urls")),

]
