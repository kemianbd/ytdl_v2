import os
from pytube import YouTube
import subprocess

class Convert:
    def __init__(self, yturl, vid, bit):
        self.yturl = yturl
        self.vid = vid
        self.bit = bit
        self.err = False

    def dl_convert(self):
        # Remove all files from download folder prior to new convert
        for root, directories, files in os.walk(self.dl_path):
            for filename in files:
                fp = os.path.join(root, filename)
                os.remove(fp)

        # Grab video from youtube
        # TODO Better error handling
        try:
            ytdl = YouTube(self.yturl)
        except:
            self.err = True
            print('File could not be downloaded, make sure the YouTube link is correct')

        # Get attributes of video
        ytitle = ytdl.title
        print('NOW DOWNLOADING: ' + ytitle + '\n')
        ytdl.streams.filter(file_extension='mp4').first().download(self.dl_path)

        # Clean title
        for badchar in ['\"', '#', '$', '%', '\'', '*', ',', '.', '/', ':',
                        ';', '<', '>', '?', '\\', '^', '|', '~', '\\\\']:
            if badchar in ytitle:
                ytitle = ytitle.replace(badchar, "")

        # Convert video to mp3
        command = f"ffmpeg -i \"{self.dl_path}" + f"{ytitle}" + ".mp4\"" f" -b:a {self.bit}" \
            f" -vn \"{self.dl_path}" + f"{ytitle}" + ".mp3\""
        subprocess.call(command, shell=True)

        # Delete video if not requested
        if self.vid == 0:
            os.remove(self.dl_path + ytitle + '.mp4')

        if not self.err:
            return 'All downloads complete'
        else:
            return 'At least one file did not download successfully'

    @property
    def yt_title(self):
        return YouTube(self.yturl).title

    @property
    def dl_path(self):
        return r"D:\Programming\ytdl_v2\files" + "\\"
