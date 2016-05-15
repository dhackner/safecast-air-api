# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [

    url(
        regex=r'^upload$',
        view=csrf_exempt(views.UploadRawReadingView.as_view()),
        name='upload'
    ),
]

