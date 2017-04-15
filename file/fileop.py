from os import listdir
from os.path import isdir, isfile, join, getsize
import json


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
        return 'is a txt file.'
