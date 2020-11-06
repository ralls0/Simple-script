#! /usr/bin/python3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import sys
import platform
import time

path = '/home/marco/Scaricati' if platform.system() == 'Linux' else '/Users/marco/Downloads'
img = '/img'
video = '/video'
zp = '/zip'
pdf = '/pdf'

class MyHandelr(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(path=path):
            try:
                name, extension = file.split('.')
            except:
                continue
            base_path = path+'/'+file
            if extension in ['mp4', 'mov']:
                os.rename(base_path, path+video+'/'+file)
            if extension in ['png', 'jpeg', 'jpg']:
                os.rename(base_path, path+img+'/'+file)
            if extension == 'pdf':
                os.rename(base_path, path+pdf+'/'+file) 
            if extension in ['zip', 'rar', 'gz', 'tar']:
                os.rename(base_path, path+zp+'/'+file)       

if __name__ == "__main__":
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MyHandelr()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
