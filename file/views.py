from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from file import fileop


# @login_required
@csrf_exempt
def index(request):
    response = ''
    if request.method == 'GET':
        location_str = request.GET.get('location')
        response = fileop.read_fd(location_str)

    elif request.method == 'POST':
        location_str = request.POST.get('location')
        action = request.POST.get('action')

        # for item in DeletedFile.objects.all():
        #     item.delete()

        if action == 'delete':
            response = fileop.delete_file(location_str)
        elif action == 'restore':
            response = fileop.restore_file(location_str)
        elif action == 'edit':
            content_str = request.POST.get('content')
            response = fileop.edit_file(location_str, content_str)

        elif action == 'move':
            dst_loc = request.POST.get('dst')
            response = fileop.move_file(location_str, dst_loc)
        elif action == 'copy':
            dst_loc = request.POST.get('dst')
            response = fileop.copy_file(location_str, dst_loc)
        elif action == 'rename':
            file = request.POST.get('dst')
            response = fileop.rename(location_str, file)
    else:
        response = HttpResponse('No use')

    return response
