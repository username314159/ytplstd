#!/bin/sh
for f in *.mp4
do
       	ffmpeg -i "$f" -acodec libmp3lame -q:a 2 "${f%.*}.mp3"
done
