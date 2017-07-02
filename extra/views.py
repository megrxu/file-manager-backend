# from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from extra.models import RecentFiles
from file.models import DeletedFile
from django.contrib.auth import authenticate, login
import json
from django.http import HttpResponse, JsonResponse
import psutil


# Create your views here.
@csrf_exempt
# @login_required
def index(request):
    response = manage(request)
    return response


@csrf_exempt
def login_request(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    result = []
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        result.append({
            'status': 1,
            'user': username,
        })
    else:
        # Return an 'invalid login' error message.
        result.append({
            'status': 0,
            'user': username,
        })
    result = json.dumps(result)
    return HttpResponse(result)


def manage(request):
    if request.method == 'GET':
        action = request.GET.get('action')
        if (action == 'recentfiles'):
            return get_recent_files()
        elif (action == 'deletedfiles'):
            return get_deleted_files()
        elif (action == 'system'):
            return get_system_status()
        elif (action == 'check'):
            return check(request)
        else:
            return HttpResponse('index')


def get_recent_files():
    file_list = RecentFiles.objects.all()
    result = []
    for file in file_list:
        result.append({
            'filename': file.filename,
            'date': file.date
        })
    result = json.dumps(result)

    return HttpResponse(result)


def get_deleted_files():
    file_list = DeletedFile.objects.all()
    result = []
    for file in file_list:
        result.append({
            'filename': file.filename,
            'date': file.date
        })
    result = json.dumps(result)

    return HttpResponse(result)


def get_system_status():
    result = {
        'cpu': psutil.cpu_percent(),
        'ram': psutil.virtual_memory().percent
    }

    return JsonResponse(result)


@login_required
def check(request):
    return JsonResponse({
        'status': 1
    })


def manage_request(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    result = []
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        result.append({
            'status': 1,
            'user': username,
        })
    else:
        # Return an 'invalid login' error message.
        result.append({
            'status': 0,
            'user': username,
        })
    return HttpResponse(result)
