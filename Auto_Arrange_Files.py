from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json


fullName = []
programs = ["exe","msi","D:/Downloads/programs"]
audios = ["mp3","wav","wma","webm","D:/Downloads/audios"]
videos = ["mp4","m4p","m4v","mov","flv","avchd","webm","D:/Downloads/videos"]
images = ["png","jpg","jpeg","tiff","gif","bmp","D:/Downloads/images"]
imgFiles = ["iso","D:/Downloads/Img Files"]
zips = ["zip","rar","7z","D:/Downloads/Zips"]


class Myhandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            fullName = filename.split('.')
            extention = fullName[-1]
            print(fullName)
            if extention in programs:
                folder_destination = programs[-1]

            if extention in audios:
                folder_destination = audios[-1]

            if extention in videos:
                folder_destination = videos[-1]

            if extention in images:
                folder_destination = images[-1]

            if extention in imgFiles:
                folder_destination = imgFiles[-1]

            if extention in zips:
                folder_destination = zips[-1]

            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)
        

folder_to_track = "D:/Downloads/Drop"
event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()