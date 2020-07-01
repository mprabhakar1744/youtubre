from pytube import*
from tkinter import *
from tkinter.filedialog import *

from tkinter.messagebox import *
from threading import *

file_size=0
def progress(stream=None,chunk=None,file_handle=None,remaining=None):

    file_download=(file_size-remaining)

    print('jnbjk',file_download)
    per=(file_download/file_size)*100
    dbtn.config(text="{:00.0f } % downloaded".format(per))

def startDownloder():
    global file_size
    try:
        url = urlField.get()
        print(url)

        dbtn.config(text="please wait....")
        dbtn.config(state=DISABLED)


        path_vedio_download = askdirectory()
        print(path_vedio_download)
        if path_vedio_download is None:
            return

        ob = YouTube(url,on_progress_callback=progress)
        '''strms=ob.streams.all()
        for s in strms:
            print(s)'''
        strm = ob.streams.first()


        file_size=strm.filesize
        print(file_size)
        vYitle.config(text=strm.title)

        vYitle.pack(side=TOP)
        strm.download(path_vedio_download)
        print("download")
        dbtn.config(text="start doownload")
        dbtn.config(state=NORMAL)
        showinfo("doenload finish","download sucess")

        urlField.delete(0,END)
        vYitle.pack_forget()


    except Exception as e:
        print(e)
        print("error")

def startDownloadThread():
    thread=Thread(target=startDownloder)
    thread.start()


main= Tk()
main.title("youtubr downloder")

main.iconbitmap('download (1).ico')
main.geometry('500x600')

file=PhotoImage(file='download.png')
headingicon=Label(main,image=file)
headingicon.pack(side=TOP)

urlField=Entry(main,font=("verdana",18),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)
dbtn=Button(main,text="start download",font=("verdana",18),relief='ridge',command=startDownloadThread)
dbtn.pack(side=TOP,pady=10)

vYitle=Label(main,text="video title")
vYitle.pack(side=TOP)
main.mainloop()
