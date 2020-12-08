from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import re_path

My_app = "retail_app1"

urlpatterns= [

    re_path(r"/accounts/login/home/", views.user_created, name="refresh"),
    re_path(r"^home/" , views.index ,name="home"),
    re_path(r"^check/", views.check),
    re_path(r"^create_user/", views.createuser , name="sign-in"),
    re_path(r"^finish/", views.user_created , name="user_created"),
    re_path(r"^order/", views.order , name="order"),
    re_path(r'product/(?P<id>[\w]*)/', views.product_explain ),
    re_path(r"^comment/", views.UserComment , name="comment"),
    re_path(r"profile/(?P<username>[\w]*)/", views.UserProfile , name="UserProfile"),
    re_path(r"all_profile/", views.AllProfile, name="UserProfile"),

]

""" re_path(r'^order_query/', views.order_query),
    re_path(r'^order_query/state/', views.order_query_state),
    re_path(r'^order_query/group/', views.order_query_group),
    re_path(r'^order_query/name_EN/', views.order_query_name_EN),
    re_path(r'^order_query/date/', views.order_query_date ),
"""


