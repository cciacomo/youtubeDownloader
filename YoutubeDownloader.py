from pytube import YouTube, Playlist
import os


def ChangeExtension(file_path, new_extension):
    base_name, _ = os.path.splitext(file_path)
    new_file_path = base_name + "." + new_extension
    os.rename(file_path, new_file_path)



def DownloadVideo(link, dirPath) -> None:
    Video = YouTube(link)
    Video.streams.get_highest_resolution().download(dirPath)



def DownloadAudio(link, dirPath) -> None:
    index = -1
    Audio = YouTube(link)
    Audio.streams.get_audio_only().download(dirPath)
    name = Audio.title
    name = name.replace('.','')
    name = name.replace("'", "")
    name = name.replace(':', '')
    name = name.replace('?','')
    name = name.replace('"','')
    name = name.replace(';','')
    name = name.replace(',','')
    filePath = dirPath + '/' + name + '.mp4'
    ChangeExtension(filePath, 'wav')



def DownloadPlaylist(link, downloader, dirPath) -> None:
    pl = Playlist(link)
    for videos in pl.video_urls:
            downloader(videos, dirPath)
