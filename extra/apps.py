from django.apps import AppConfig
from django.http import HttpResponse


class ExtraConfig(AppConfig):
    name = 'extra'


def manage(request):
    if request.method == 'GET':
        action = request.GET.get('action')
        if (action == 'recentfiles'):
            return getRecentFiles()


def getRecentFiles():
    return HttpResponse('wadw')
