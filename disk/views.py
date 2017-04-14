from django.http import HttpResponse
from disk.models import Disk
import json
import psutil
from django.contrib.auth.decorators import login_required
from disk.blacklist import black_list

@login_required
# Create your views here.
def index(request):

    if request.method == 'GET':
        # get the disks info
        get_disks()
        disk_list = Disk.objects.all()

        # read all disks
        result = []
        for disk in disk_list:
            result.append({
                'id': disk.disk_id,
                'device': disk.disk_device,
                'mount point': disk.disk_mountpoint,
                'mounted': disk.disk_mounted,
                'size': disk.disk_size,
                'used_size': disk.disk_usedsize,
                'percent': disk.disk_percent,
                'is shown': disk.disk_shown,
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
        disk.disk_mounted = 0;
        disk.save()

    temp_id = 0
    for one_disk in psutil.disk_partitions():
        for disk in Disk.objects.all():
            if disk.disk_device == one_disk.device:
                disk.delete()
                d = Disk(disk_device=one_disk.device, disk_size=psutil.disk_usage(one_disk.mountpoint).total, disk_usedsize=psutil.disk_usage(one_disk.mountpoint).used, disk_percent=psutil.disk_usage(one_disk.mountpoint).percent, disk_mountpoint=one_disk.mountpoint, disk_id=temp_id, disk_mounted=1)
            else:
                d = Disk(disk_device=one_disk.device, disk_size=psutil.disk_usage(one_disk.mountpoint).total, disk_usedsize=psutil.disk_usage(one_disk.mountpoint).used, disk_percent=psutil.disk_usage(one_disk.mountpoint).percent, disk_mountpoint=one_disk.mountpoint, disk_id=temp_id, disk_mounted=1)
            if d.disk_device in black_list:
                d.disk_shown = 0
        temp_id += 1
        d.save()
    return
