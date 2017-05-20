from django.views.decorators.csrf import csrf_exempt
from . import apps

from file import fileop


# Create your views here.


@csrf_exempt
def index(request):
    response = apps.manage(request)

    return response
