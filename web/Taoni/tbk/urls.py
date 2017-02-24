# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SubView.as_view()),
]
