from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from . import apps
from django.contrib.auth import authenticate, login
import json



# from django.http import HttpResponse


# Create your views here.
@csrf_exempt
# @login_required
def index(request):
    response = apps.manage(request)

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
