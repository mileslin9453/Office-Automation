import tkinter as tk
from tkinter import messagebox,filedialog
import os
import ftplib

window = tk.Tk()
window.title("//~~信查理得永生~~//")
window.geometry('300x200') # Size 200, 200
window.attributes('-topmost', True) # bring window in front of other windwos

def hello():
    try:
        ftp = ftplib.FTP()
        ftp.connect('192.168.100.206',21)
        ftp.login(user='pe',passwd='gigape')
        ftp.cwd('/home/rt_location')
        os.chdir(fp[0])
        f = open(fp[1],'rb')
        ftp.storlines('STOR ' + fp[1], f)
        f.close()
        ftp.quit()
        messagebox.showinfo("恭喜",fp[1]+" 已上傳!!!")
    except:
        messagebox.showinfo("Error","帥哥，請夾檔先!!!")

def browsefunc():
    try:
        global filename
        filename = filedialog.askopenfilename(
            initialdir="E:/%s",
            filetypes=[('Text files','*.txt')])
        global fp
        fp = os.path.split(filename)    # split file path
        f = open(filename)
        messagebox.showinfo('Information',fp[1]+' 檔案被選取!!!\n'
                                    '接下請上傳!!!')
    except:
        messagebox.showinfo('Error','搞什麼東西~')


uploadbutton = tk.Button(window,text='Upload',command=hello,height=5,width=20)
uploadbutton.pack(side='bottom')

browsebutton = tk.Button(window,text="Browse",command=browsefunc,height=5,width=20)
browsebutton.pack(side='top')

window.mainloop()
