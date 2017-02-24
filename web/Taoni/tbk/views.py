# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from django.views import View

class BaseView(View):
	hello_text="你好,世界~"
	def get(self, request):
		# <view logic>
		return HttpResponse(self.hello_text)

class SubView(BaseView):
	hello_text="Hello World~"

def index(request):
	name = "Haolo"
	return render(request, 'index.html', locals())