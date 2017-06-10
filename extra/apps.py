from django.apps import AppConfig
from django.http import HttpResponse


class ExtraConfig(AppConfig):
    name = 'extra'


def manage(request):
    if request.method == 'GET':
        action = request.GET.get('action')
        if (action == 'recentfiles'):
            return getRecentFiles()
        else:
            return HttpResponse('index')


def getRecentFiles():
    return HttpResponse('getRecentFiles')
