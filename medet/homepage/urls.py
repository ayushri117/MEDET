from . import views
from  django.urls import path
from django.contrib import admin


urlpatterns=[
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("news_all/",views.news_all,name="news"),
    path("search_medicine/",views.search_med,name="search"),
    path("med_read_more/<id>/",views.read_more,name="med_read_more"),
    path("new_read_more/<id>/",views.new_read_more,name="new_read_more"),
    path("bookmark/<id>/",views.bookmark,name="bookmark"),
    path("remove_bookmark/<id>/",views.remove_bookmark,name="remove_bookmark")
]