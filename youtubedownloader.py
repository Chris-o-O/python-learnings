from tkinter import *
from tkinter import ttk
from media_downloader import MediaDownloader

def download(*args):
    try:
        url2 = str(url.get())
        video_downloader_instance = MediaDownloader()
        video_downloader_instance.set_save_path() #-> SAVE PATH -- e.g. r"C:\Users\USER\Downloads")
        video_downloader_instance.download_video(url2)
        downloadnotif.set("download complete!")
    except ValueError:
        downloadnotif.set("error !")
        pass


#setting up global window
root = Tk()
root.title("YT videos processing")
root.geometry('400x200')
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)

#setting up frame 1
mainframe = ttk.Frame(root, padding="8 8 16 16")
mainframe.grid(column=0, row=0) #sticky options=(N, W, E, S)

#setting up url variable
url = StringVar()
url_entry = ttk.Entry(mainframe,textvariable=url).grid(column=1, row=1)

#setting up 'download' function success notif label
downloadnotif = StringVar()
ttk.Label(mainframe,textvariable=downloadnotif).grid(column=2,row=2)

#setting up static widgets inside frame 1 
ttk.Label(mainframe, text="Youtube video: ").grid(column=0, row=1) 

ttk.Label(mainframe, text="option 1:").grid(column=0, row=2) 
ttk.Button(mainframe,text="download",command=download).grid(column=1,row=2)

#global format rules applicable for each widget inside frame 1 'mainframe'
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)


#setting up frame 2
#subframe = ttk.Frame(root, padding="3 3 12 12")
#subframe.grid(column=0, row=1) 
#ttk.Label(subframe, text="test it").grid(column=1, row=3) 

root.mainloop()
