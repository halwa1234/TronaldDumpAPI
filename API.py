import tkinter
from tkinter import *
import PIL
from PIL import Image, ImageTk

import requests
import json
import tkinter

def Rand():
    url='https://api.whatdoestrumpthink.com/api/v1/quotes/random'

    r=requests.get(url)

    #print(r.status_code)
    message=r.json()['message']
    return(message)


def Personal(name):
    url='https://api.whatdoestrumpthink.com/api/v1/quotes/personalized'

    parameters={
    'q':name
    }

    r=requests.get(url,params=parameters)

    info=json.loads(r.content)
    #print(r.status_code)
    message=r.json()['message']
    nickname=r.json()['nickname']

    #print(message,nickname)
    #print(json.dumps(info,indent=2))
    return(message)

#............GUI...............
def refresh():
    if r.get()==1:
        name.insert(0,"Enter name")
        name.configure(state="disabled")
    else:
        name.configure(state="normal")


def code():
    if r.get()==1:
        text=Rand()
    elif r.get()==2:
        text=Personal(name.get())

    quote.configure(text=text)


#............GUI Interface..............
root=Tk()
root.geometry("750x450")
root.title('Trump says...')

#root.iconbitmap('@tronaldDump.xbm')
mainFrame=LabelFrame(root, text="Trump says...", width=600, height=350)
mainFrame.grid(row=0,column=0,padx=(50,50), pady=(50,50))

#Radio buttons
radioFrame=LabelFrame(mainFrame, text="select", width=175, height=150)
radioFrame.grid(row=0,column=2, padx=(20,20), pady=(15,20))
r=IntVar()
a=Radiobutton(radioFrame, text="random text", variable=r, value=1, command=refresh)
a.grid(row=0, column=0, sticky=E)
a.select()
Radiobutton(radioFrame, text="Text with you name", variable=r, value=2, command=refresh).grid(row=1, column=0, sticky=E)

name=Entry(radioFrame,width=30)
name.grid(row=2, column=0, sticky=E)
name.insert(0,"Enter name")
name.configure(state="disabled")


#pic
pic=ImageTk.PhotoImage(Image.open('trump2.jpg'))
pic_label=Label(mainFrame, image=pic)
pic_label.grid(row=0, column=0, padx=(20,0), pady=(15,15), columnspan=2)


#Quote
quote_text="Tronald Dump says dumb things."

quote=Label(mainFrame, text=quote_text, relief=RIDGE, height=5)
quote.grid(row=1, column=0, columnspan=3, padx=(20,20), pady=(10,10), sticky=W+E)

generate=Button(mainFrame, text="Generate Quote", border=1, command=code)
generate.grid(row=2, column=1, padx=(20,0), pady=(10, 10))

root.mainloop()
