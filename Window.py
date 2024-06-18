from tkinter import *
from tkinter.filedialog import askdirectory
from YoutubeDownloader import *

def AskDir():
    pathDir = askdirectory()
    return pathDir

def checkType(link) -> str:
    if 'https://www.youtube.com/watch?v=' in link or 'https://youtu.be/' in link:
        return 'video'
    elif 'https://www.youtube.com/playlist?list=' in link:
        return 'playlist'
    else:
        return 'error'

def checkVideoOrAudio():
    selection = VideoOrAudio.curselection()
    if selection:
        text = VideoOrAudio.get(VideoOrAudio.curselection())
        if text == 'Video':
            return DownloadVideo
        elif text == 'Audio':
            return DownloadAudio
    else:
        return Error

def DownloadClick():
    pathDir = AskDir()
    link = LinkEntry.get()
    type = checkType(link)
    func = checkVideoOrAudio()
    if func is not Error:
        if type == 'video':
            func(link, pathDir)
            SuccessLabel.config(text='Video Downloaded Successfully!')
        elif type == 'playlist':
            DownloadPlaylist(link, func, pathDir)
            SuccessLabel.config(text='Playlist Downloaded Successfully!')
        else:
            Error('Link Error')
    else:
        func('Type not chosen')

def Error(type):
    SuccessLabel.config(text=type)

Window = Tk()
Window.title('YouTube Downloader')
Window.geometry("800x500")

LogoLabel = Label(Window,
               text='Youtube Downloader',
               fg='#1c3323',
               font=('Segoe UI', 20)
              )
LogoLabel.pack()

LinkLabel = Label(Window,
                  font=('Segoe UI', 10),
                  text='Link:')
LinkLabel.place(x=10, y=40)
LinkEntry = Entry(Window,
                  font=('Segoe UI', 10),
                  width=50)
LinkEntry.place(x=10, y=65)

VideoOrAudio = Listbox(Window,
                  font=('Segoe UI', 10),
                  width=5
                  )
VideoOrAudio.insert(1, 'Video')
VideoOrAudio.insert(2, 'Audio')
VideoOrAudio.config(height=VideoOrAudio.size())

VideoOrAudio.place(x=10,y=105)

DowloadButton = Button(Window,
                       text='Download',
                       command=DownloadClick,
                       padx=10,
                       pady=5
                       )
DowloadButton.place(x = 10, y = 155)

SuccessLabel = Label(Window,
                     font=('Segoe UI', 10))
SuccessLabel.place(x = 10, y = 185)

Window.mainloop()
