from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from os.path import isfile, isdir, join, getsize
import json
from file.trashbin import trash

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'GET':
        para_get = request.GET.get('location')

        files = []
        dirs = []

        for f in listdir(para_get):
            if isfile(join(para_get, f)):
                files.append({
                    'name': f,
                    'size': getsize(join(para_get,f))
                })
            elif isdir(join(para_get, f)):
                dirs.append({
                    'name': f,
                    'amount': len(listdir(join(para_get, f)))
                })
        json_str = json.dumps({
            'files': files,
            'dirs': dirs,
        })

        return HttpResponse(json_str)

    elif request.method == 'POST':
        para_get = request.POST.get('location')
        action = request.POST.get('action')

        if action == 'delete':
            trash.append(para_get)
            return HttpResponse('Moved ' + para_get + ' to trash bin.')

        return HttpResponse('No use')

