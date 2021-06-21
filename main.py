from tkinter import *
from pytube import YouTube
from tkinter import ttk
from tkinter import filedialog

FolderName = ""


def onclick(event):
    fadeText = url_entry.get()
    if fadeText == "Enter URL here":
        url_entry.delete(0, END)
        url_entry.configure(fg="#000000")
    else:
        pass


def openLocation():
    """file location"""
    global FolderName
    FolderName = filedialog.askdirectory()
    if (len(FolderName) > 1):
        locationError.config(text=FolderName, fg="green")

    else:
        locationError.config(text="Please Choose Folder", fg="red")


def DownloadVideo():
    choice = ytdChoices.get()
    url = url_entry.get()

    if (len(url) > 1):
        ytdError.config(text="")
        yt = YouTube(url)

        if (choice == Qchoices[0]):
            select = yt.streams.filter(progressive=True).first()
        elif (choice == Qchoices[1]):
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()
        elif (choice == Qchoices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Paste Link Again!", fg="red")

    select.download(FolderName)
    ytdError.config(text="Download complete", fg="green")


root = Tk()
root.geometry("600x300")
root.resizable(0, 0)
root.title("YT Downloader")


TitleLabel = Label(root, text="YT Downloader", font=("Lato", 16, "bold"))
TitleLabel.pack(pady=5)

global Link
Link = StringVar()
url_entry = Entry(root, textvariable="Link",)
url_entry.configure(bd=0, highlightbackground="grey", highlightthickness=1, fg="grey")
url_entry.place(x=5, y=50, width=480, height=35)

url_entry.insert(0, "Enter URL here")
url_entry.bind("<FocusIn>", onclick)


downloadBtn = Button(root, text="Download", command=DownloadVideo)
downloadBtn.configure(bd=0, bg="#E0471B", fg="#ffffff", width=20, height=2, font=("Roboto", 10, "bold"))
downloadBtn.pack(pady=60)

Location = Button(root, text="Select Path", command=openLocation)
Location.configure(bd=0, bg="#202020", fg="#ffffff", width=20, height=2, font=("Roboto", 10, "bold"))
Location.place(x=217, y=150)

locationError = Label(root, text="Error Message of Path", fg="red")
locationError.place(x=217, y=200)

ytdError = Label(root, text="Error Message of download", fg="red")
ytdError.place(x=217, y=230)


Qchoices = ["720p", "144p", "Only Audio"]
ytdChoices = ttk.Combobox(root, values=Qchoices)
ytdChoices.place(x=495, y=50, height=35, width=100)


root.mainloop()
