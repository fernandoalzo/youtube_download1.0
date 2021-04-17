import os
import youtube_dl

class funciones():
    def download_vidoes_as_mp3(link_video):
        SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Descargas'
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
            ydl.download([link_video])