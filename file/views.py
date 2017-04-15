from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from os.path import isfile, isdir
from datetime import datetime
from file.models import DeletedFile

from file import fileop

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'GET':
        location_str = request.GET.get('location')

        if isfile(location_str):
            return HttpResponse(fileop.read_file(location_str))

        elif isdir(location_str):
            return HttpResponse(fileop.read_dir(location_str))

    elif request.method == 'POST':
        location_str = request.POST.get('location')
        action = request.POST.get('action')

        # for item in DeletedFile.objects.all():
        #     item.delete()

        trash = []
        for item in DeletedFile.objects.all():
            trash.append(item.filename)

        if action == 'delete':
            if location_str not in trash:
                one_file = DeletedFile(filename=location_str, date=datetime.now())
                one_file.save()
                return HttpResponse(DeletedFile.objects.all())

        return HttpResponse('No use')
