from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.db.models import Count
from django.db.models import Sum
from .models import Asset,scan,ip_port,increase,decrease,notification
#展示端口列表
def index(request):
    return render(request,'index.html')
#展示资产列表
def asset(request):
    return render(request,'asset.html')

