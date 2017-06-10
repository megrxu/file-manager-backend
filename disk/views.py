from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from disk.models import Disk
import json
import psutil
from django.contrib.auth.decorators import login_required
from disk.blacklist import black_list


# Create your views here.

@login_required
@csrf_exempt
def index(request):

    if request.method == 'GET':
        # get the disks info
        get_disks()
        disk_list = Disk.objects.all()

        # read all disks
        result = []
        for disk in disk_list:
            result.append({
                'id': disk.id,
                'device': disk.disk_device,
                'mount_point': disk.disk_mountpoint,
                'size': disk.disk_size,
                'used_size': disk.disk_usedsize,
                'percent': disk.disk_percent,
                'is_shown': disk.disk_shown,
            })

        # encode the result to json
        id_get = int(request.GET.get('id', -1))

        if id_get >= 0:
            json_str = json.dumps(result[id_get])
        else:
            json_str = json.dumps(result)

        return HttpResponse(json_str)


def get_disks():

    for disk in Disk.objects.all():
        disk.delete()

    temp_id = 0
    for one_disk in psutil.disk_partitions():
        d = Disk(disk_device=one_disk.device, disk_size=psutil.disk_usage(one_disk.mountpoint).total,
                 disk_usedsize=psutil.disk_usage(one_disk.mountpoint).used,
                 disk_percent=psutil.disk_usage(one_disk.mountpoint).percent, disk_mountpoint=one_disk.mountpoint,
                 disk_id=temp_id, disk_mounted=1)
        d.id = temp_id
        if d.disk_device in black_list:
                d.disk_shown = 0
        d.save()
        temp_id += 1
    return
