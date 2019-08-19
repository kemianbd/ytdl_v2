import os
from pytube import YouTube
import moviepy.editor as mp
import time


def dl_convert(yturl, dlpath, vid, bit):

    # Split entries
    ytget = yturl.splitlines()

    # Loop through all URLs
    err_cnt = 0
    for i in range(0, len(ytget)):

        # Skip blank line
        if ytget[i] == "":
            continue

        # Grab video from youtube
        try:
            ytdl = YouTube(ytget[i])
        except:
            err_cnt += 1
            print('File', i+1, 'could not be downloaded, make sure the YouTube link is correct')
            continue

        # Get attributes of video
        ytitle = ytdl.title
        print('NOW DOWNLOADING: ' + ytitle + '\n')
        ytdl.streams.filter(file_extension='mp4').first().download(dlpath)

        # Clean title
        for badchar in ['\"', '#', '$', '%', '\'', '*', ',', '.', '/', ':',
                        ';', '<', '>', '?', '\\', '^', '|', '~', '\\\\']:
            if badchar in ytitle:
                ytitle = ytitle.replace(badchar, "")

        # Convert video to mp3
        print('\n')
        clip = mp.VideoFileClip(dlpath + '\\' + ytitle + '.mp4')
        clip.audio.write_audiofile(dlpath + '\\' + ytitle + '.mp3', bitrate=bit)
        clip.reader.close()
        clip = None
        time.sleep(2)

        # Delete video if not requested
        if vid == 0:
            os.remove(dlpath + '\\' + ytitle + '.mp4')

    if err_cnt == 0:
        return 'All downloads complete'
    else:
        return 'At least one file did not download successfully'
