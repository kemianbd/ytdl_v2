import os
from pytube import YouTube
import moviepy.editor as mp
import time


class Convert:
    def __init__(self, yturl, dlpath, vid, bit):
        self.yturl = yturl
        self.dlpath = dlpath
        self.vid = vid
        self.bit = bit
        self.err = False

    def dl_convert(self):

        # Grab video from youtube
        try:
            ytdl = YouTube(self.yturl)
        except:
            self.err = True
            print('File could not be downloaded, make sure the YouTube link is correct')

        # Get attributes of video
        ytitle = ytdl.title
        print('NOW DOWNLOADING: ' + ytitle + '\n')
        ytdl.streams.filter(file_extension='mp4').first().download(self.dlpath)

        # Clean title
        for badchar in ['\"', '#', '$', '%', '\'', '*', ',', '.', '/', ':',
                        ';', '<', '>', '?', '\\', '^', '|', '~', '\\\\']:
            if badchar in ytitle:
                ytitle = ytitle.replace(badchar, "")

        # Convert video to mp3
        print('\n')
        clip = mp.VideoFileClip(self.dlpath + '\\' + ytitle + '.mp4')
        clip.audio.write_audiofile(self.dlpath + '\\' + ytitle + '.mp3', bitrate=self.bit)
        clip.reader.close()
        clip = None
        time.sleep(2)

        # Delete video if not requested
        if self.vid == 0:
            os.remove(self.dlpath + '\\' + ytitle + '.mp4')

        if not self.err:
            return 'All downloads complete'
        else:
            return 'At least one file did not download successfully'

    @property
    def yt_title(self):
        return YouTube(self.yturl).title
