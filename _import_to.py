#!python3
'''Designed to be used as a share extension.
Import files into Pythonista app.'''

import appex
import os
import console
import shutil
import urllib.request


def import_from_file(fname, fpath, basepath):
    i = 2
    fname_ori = fname.split('.')[0]
    fname_ext = '.'+fname.split('.')[-1]
    write_path = os.path.join(basepath, fname)
    while os.path.exists(write_path):
        fname = fname_ori + '('+str(i)+')' + fname_ext
        write_path = os.path.join(basepath, fname)
        i += 1

    shutil.copy(fpath, write_path)
    console.hud_alert('Imported as: '+fname)


def import_from_text(fname, fpath, basepath):
    i = 2
    fname_ori = fname.split('.')[0]
    fname_ext = '.'+fname.split('.')[-1]
    write_path = os.path.join(basepath, fname)
    while os.path.exists(write_path):
        fname = fname_ori + '('+str(i)+')' + fname_ext
        write_path = os.path.join(basepath, fname)
        i += 1

    try:
        with open(fpath) as r:
            content = r.read()
    except:
        content = fpath
    with open(write_path, 'w') as w:
        w.write(content)
    console.hud_alert('Imported as: '+fname)


def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return

    basepath = os.path.expanduser('~/Documents/')
    fpath = appex.get_file_path()
    if fpath:
        fname = os.path.split(fpath)[1]
        try:
            import_from_file(fname, fpath, basepath)
        except:
            fpath = appex.get_text()
            if os.path.isfile(fpath):
                fname = os.path.split(fpath)[1]
                import_from_text(fname, fpath, basepath)
    elif appex.get_text():
        fpath = appex.get_text()
        resp = console.alert('Import file as..', 'Choose File Extension',
                             '.py', '.txt', '.pyui', hide_cancel_button=False)
        if resp == 1:
            fname = 'imported.py'
        elif resp == 2:
            fname = 'imported.txt'
        elif resp == 3:
            fname = 'imported.pyui'
        import_from_text(fname, fpath, basepath)
    else:
        console.hud_alert('Not a file!', icon='error')

if __name__ == '__main__':
    main()

