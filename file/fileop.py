import datetime
from os import listdir
from os.path import isdir, isfile, join, getsize
import json

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
    json_str = json.dumps({
        'files': files,
        'dirs': dirs,
    })

    return json_str


def read_file(location_str):
    if location_str.endswith('.txt'):
        
        file_object = open(location_str)
        try:
            content = file_object.read()
        finally:
            file_object.close()
        return json.dumps({
            'file': location_str,
            'size': getsize(location_str),
            'content': content
        })


def delete_file(location_str):
    trash = []
    for item in DeletedFile.objects.all():
        trash.append(item.filename)
    if location_str not in trash:
        one_file = DeletedFile(filename=location_str, date=datetime.now())
        one_file.save()
        return 'Deleted ' + location_str


def edit_file(location_str, content):
    file_object = open(location_str, 'w')
    file_object.write(content)
    file_object.close()

    return read_file(location_str)
