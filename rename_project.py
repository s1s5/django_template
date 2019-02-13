#!/usr/bin/env python
import os
import itertools
import glob
import shutil

def replace_file(filename, from_string, to_string):
    contents = open(filename, 'r').read()
    contents = contents.replace(from_string, to_string)
    open(filename, 'w').write(contents)


def main(new_project_name, port):
    ignore = [
        'rename_project.py'
        'readme.md',
        'LICENSE',
        '__pycache__',
    ]
    
    replace_file('docker-compose.override.yml', '42040:8000', '{}:8000'.format(port))

    for filename in itertools.chain(glob.glob('*'), glob.glob('**/*')):
        if os.path.isdir(filename):
            continue
        for j in ignore:
            if j in filename:
                continue
        replace_file(filename, 'djtemplate', new_project_name)

    shutil.move('djtemplate', new_project_name)


if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
