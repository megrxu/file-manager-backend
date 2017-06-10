from django.apps import AppConfig

class FileConfig(AppConfig):
    name = 'file'

def read_fd(location_str):
    if not exists(location_str):
        return HttpResponse('Error')
    elif isfile(location_str):
        return read_file(location_str)
    elif isdir(location_str):
        return read_dir(location_str)


def read_dir(location_str):
    trash = []
    for item in DeletedFile.objects.all():
        trash.append(item.filename)
    if location_str == '/':
        response = []
    else:
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
                    'size': len(listdir(join(location_str, f)))
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

        one_file = RecentFiles(filename=location_str, date=datetime.now())
        one_file.save()

    return HttpResponse(response)


def delete_file(location_str):
    trash = []
    for item in DeletedFile.objects.all():
        trash.append(item.filename)

    if isfile(location_str) or isdir(location_str):
        if location_str not in trash:
            one_file = DeletedFile(filename=location_str, date=datetime.now())
            one_file.save()
            return HttpResponse('Deleted ' + location_str)
        else:
            return HttpResponse('Already deleted ' + location_str)
    else:
        return HttpResponse('No use')


def restore_file(location_str):
    trash = []
    print(location_str)

    if isfile(location_str) or isdir(location_str):
        for item in DeletedFile.objects.all():
            trash.append(item.filename)
            if (item.filename == location_str):
                item.delete()
                return HttpResponse('Restored ' + location_str)
    return HttpResponse('No use')


def remove_file(location_str):
    return HttpResponse(remove(location_str))


def edit_file(location_str, content):
    file_object = open(location_str, 'w')
    file_object.write(content)
    file_object.close()

    return HttpResponse(read_file(location_str))


def move_file(src_loc, dst_loc):
    if exists(src_loc) and exists(dst_loc):
        shutil.move(src_loc, dst_loc)
        return HttpResponse('Moved ' + src_loc + ' to ' + dst_loc)
    else:
        return HttpResponse('Error')


def copy_file(src_loc, dst_loc):
    if exists(src_loc) and exists(dst_loc):
        shutil.copy(src_loc, dst_loc)
        return HttpResponse('Copied ' + src_loc + ' to ' + dst_loc)
    else:
        return HttpResponse('Error')


def rename_file(location_str, name, new_name):
    rename(join(location_str, name), join(location_str, new_name))
    return HttpResponse(read_dir(location_str))
