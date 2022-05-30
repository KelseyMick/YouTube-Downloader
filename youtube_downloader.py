from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import time

root = Tk()
root.geometry('500x400')
root.title('YouTube Video Downloader')
root.configure(bg = 'lightgrey')
Label(root, text = "YouTube Video Downloader", font = 'arial 20 bold').pack()

label_dir = Label(root, text = 'Click to download')
label_dir.place(x=32,y=185)

Button(root, text="Choose download location", bg='lightgreen')

dir = StringVar()
pastelink = Entry(root, width=50, textvariable=dir)
pastelink.place(x=20, y=90)

#link = StringVar()
#Label(root, text = 'Link to video: ').place(x=160,y=60)
#link_enter = Entry(root, width = 70, textvariable = link).place(x=32,y=90)
  
def chooseDir():
    global path
    videoLoc = filedialog.askdirectory(title="Choose save location")
    path = videoLoc
    Label(root, text=path, bg='gray').place(x=10,y=300)

def download():
    link = (dir.get())
    video = YouTube(link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download(path)
    Label(root, text="Successfully downloaded: "+video.title, bg='gray').place(x=10,y=340)

Button(root, text = 'Save to:', command = chooseDir).place(x=180,y=230)
Button(root, text = 'Download', command = download).place(x=180,y=270)


root.mainloop()
