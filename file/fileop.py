from datetime import datetime
from os import listdir
from os.path import isdir, isfile, join, getsize
import json

from django.http import HttpResponse

from file.models import DeletedFile


def read_fd(location_str):
    if isfile(location_str):
        return read_file(location_str)
    elif isdir(location_str):
        return read_dir(location_str)


def read_dir(location_str):
    files = []
    dirs = []
    for f in listdir(location_str):
        if isfile(join(location_str, f)):
            files.append({
                'name': f,
                'size': getsize(join(location_str, f))
            })
        elif isdir(join(location_str, f)):
            dirs.append({
                'name': f,
                'amount': len(listdir(join(location_str, f)))
            })
    response = json.dumps({
        'files': files,
        'dirs': dirs,
    })

    return HttpResponse(response)


def read_file(location_str):
    location_str_lower = location_str.lower()

    if location_str_lower.endswith('.png') | location_str_lower.endswith('.jpg') | location_str_lower.endswith('.jpeg'):
        image_data = open(location_str, "rb").read()
        return HttpResponse(image_data, content_type="image")
    else:
        file_object = open(location_str)
        try:
            content = file_object.read()
        finally:
            file_object.close()
        response = json.dumps({
            'file': location_str,
            'size': getsize(location_str),
            'content': content
        })

    return HttpResponse(response)


def delete_file(location_str):
    trash = []
    for item in DeletedFile.objects.all():
        trash.append(item.filename)
    #
    # for item in  DeletedFile.objects.all():
    #     item.delete()

    if isfile(location_str) or isdir(location_str):
        if location_str not in trash:
            one_file = DeletedFile(filename=location_str, date=datetime.now())
            one_file.save()
            return HttpResponse('Deleted ' + location_str)
        else:
            return HttpResponse('Already deleted ' + location_str)
    else:
        return HttpResponse('No use')


def edit_file(location_str, content):
    file_object = open(location_str, 'w')
    file_object.write(content)
    file_object.close()

    return HttpResponse(read_file(location_str))
