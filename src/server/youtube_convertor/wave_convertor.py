from pytube import YouTube
from scipy.io import wavfile
import os
import subprocess

class WaveConvertor(object):
    def get_wave(self, youtube_url):
        '''
        return wave data extracted from youtube url
        parameters -
            youtube_url : str
                Address of youtube
        returns -
            rate : int
                rate of wave
            data : numpy.ndarray
                sequencial data of wave 
        '''
        filename = "test"
        self.__download_mp4_from_youtube_url(youtube_url, filename)
        filepath = "cache/" + filename
        self.__convert_mp4_to_wav(filepath)
        return self.__read_wav(filepath)

    def __download_mp4_from_youtube_url(self, youtube_url, filename):
        '''
        private method
        create mp4 file downloaded from youtube url
        paramters -
            youtube_url : str
                Address of youtube
            filename : str
                file name to create
        '''
        print("download start")
        YouTube(youtube_url).streams.first().download(output_path="cache", filename=filename)
        print("download finished")

    def __convert_mp4_to_wav(self, filename):
        '''
        private method
        convert mp4 file to wav file using subprocess call - ffmpeg
        parameters -
            filename : str
                file name to convert
        '''
        subprocess.call(["ffmpeg", "-i", filename + ".mp4", filename + ".wav"])
        print("converted mp4 to wav")

    def __read_wav(self, filename):
        '''
        private method
        read wav file and return
        parameters -
            filename : str
                file name to read
        returns -
            wave : youtube_convertor.Wave
                wave data instance
        '''
        rate, data = wavfile.read(filename + ".wav")
        print("read wav file - " + filename)
        self.__delete_cache_file(filename)
        print("delete cache file - " + filename)
        return data
      
    def __delete_cache_file(selfm, filename):
        os.remove(filename + ".mp4")
        os.remove(filename + ".wav")
