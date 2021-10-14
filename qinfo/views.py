from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http import HttpResponse
from .models import QueueInfo
from .models import QueueInfoFilter
from .tables import QueueTable
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

@csrf_exempt
def handleQueuInfo(request):
    data = json.loads(request.body)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(data)
    for i in data["data"]:
        result = QueueInfo.objects.filter(name=i['id'])
        if result.exists():
            qinfo = QueueInfo.objects.get(name=i['id'])
        else:
            qinfo = QueueInfo()
        qinfo.name = i['id']
        qinfo.queue = i['queue']
        qinfo.timestamp = timestamp
        qinfo.state = "OK"
        qinfo.save()
    
    return HttpResponse("OK")

def index(request):
    filter = QueueInfoFilter(request.GET, queryset=QueueInfo.objects.all())
    #RequestConfig(request, paginate={"per_page": 20}).configure(filter)

    #check state
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for i in QueueInfo.objects.all():
        diff = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S') - datetime.strptime(i.timestamp, '%Y-%m-%d %H:%M:%S')
        if diff.total_seconds() > 60:
            print("name:",i.name," client timeout!")
            i.state = "TIMEOUT!"
            i.save()
    return render(request, 'htmlfile/qinfo.html', {'filter': filter })
