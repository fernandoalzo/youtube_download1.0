import os
from os.path import basename
import youtube_dl
from zipfile import ZipFile
import shutil

class funciones():
    def download_vidoes_as_mp3(link_video):
        try:
            SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/temp'
            ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link_video])\
            
            return 0

        except:
            return 1

    def comprimir(directorio):
        with ZipFile('canciones.zip', 'w') as paquete_zip:
            for folderName, subfolders, filenames in os.walk(directorio):
                for f in filenames:
                    if f.endswith('.mp3'):
                        filePath = os.path.join(folderName, f)
                        paquete_zip.write(filePath, basename(filePath))

    def eliminar_archivos_usados(directorio):
        for folderName, subfolders, filenames in os.walk(directorio):
                for f in filenames:
                    filePath = os.path.join(folderName, f)
                    os.remove(filePath)

    def mover_archivos(*args):
        for i in args:
            shutil.move(i, "./temp")

    def eliminar_directorio(directorio):
        try:
            shutil.rmtree(directorio)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))