#!/usr/bin/env python 
import os 
import subprocess

from pytube import YouTube, Playlist

url =input('Enter the playlist link you want to download:')
pl = Playlist(url)
dest_path = input ('Please specify a saving destination:')
print(f'Downloading: {pl.title} to {dest_path}')

for url in pl:
    YouTube(url).streams.filter(only_audio=True).first().download(dest_path)


