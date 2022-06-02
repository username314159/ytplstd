import os 
import glob
import subprocess

from pytube import YouTube, Playlist

url =input('Enter the playlist link you want to download: ')
pl = Playlist(url)
dest_path = input ('Please specify a saving destination: ')
print(f'Downloading playlist: {pl.title} to {os.path.join(os.getcwd(), dest_path)}/')

for url in pl:
    song = YouTube(url).streams.filter(only_audio=True).first().download(dest_path)
    out_name = song.replace("mp4", "mp3")
    print(f'Downloading and converting to mp3 song {song}')
    out = subprocess.Popen(['ffmpeg', '-i', f"{song}", '-acodec','libmp3lame', '-q:a', '2', f"{out_name}"])

for i in glob.glob(os.path.join(os.getcwd(),dest_path,"*.mp4")):
    try:
       os.chmod(i,0o777)
       os.remove(i)
    except OSError:
       pass
