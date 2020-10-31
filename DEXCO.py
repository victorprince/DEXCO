from tkinter import*
from tkinter import ttk
import matplotlib.pyplot as plt
import language_check
from tkinter import filedialog
from pdf2image import*
import numpy as np
from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)
import re
import os,io
from google.cloud import vision
from google.cloud.vision import types
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r"ENTER THE TOKEN FILE LOCATION HERE(JSON FILE,AUTH TOKEN)"
client=vision.ImageAnnotatorClient()
tool = language_check.LanguageTool('en-US')
marks=0
total=0
gm=0;
class backend:
    qno=[]
    kw=[]
    count=0
    marks=0
    gm=0
    km=0
    ans=""
    anslist=[]
    def textfile(self,filename):
        global total
        keylist=[]
        keyfile=open(filename,"r")
        for i in keyfile.readlines():
            keylist.append(i.lower() )
        global qno
        global kw
        global gm
        qno=[]
        kw=[]
        gm=0
        for i in keylist:
            qno.append([float(s) for s in re.findall(r'-?\d+\.?\d*',i )])
        for i in keylist:
            res=re.findall(r'\w+',i)
            kw.append(res)
        for i in kw:
            if(i[1]=="grammar"):
                index=kw.index(i)
                gm=qno[index][1]
                del kw[index]
                del qno[index]
                break
        if(gm==0):
            gm=0.25
        for i in qno:

            total+=i[1]
    def pdfile(self,filename):
        global count
        images_from_path=convert_from_path(filename,poppler_path=r"C:\Program Files\poppler-0.68.0\bin")
        count=0
        for page in images_from_path:
            page.save("ans"+str(count)+".jpeg", 'JPEG')
            count+=1
    def convert(self):
        i=0
        global ans
        ans=''
        imagefile=""
        for i in range(count):
            imagefile="ans"+str(i)+".jpeg"
            with io.open(imagefile,'rb') as ifile:
                content=ifile.read()
            image=vision.types.Image(content=content)
            response=client.document_text_detection(image=image)
            dtext=response.full_text_annotation.text
            ans+=dtext
            matches=tool.check(dtext)
            for mistake in matches:
            
                i+=1
        global gm
        gm=i*gm
    def calc(self):
        global km
        global ans
        global anslist
        global marks
        km=0
        kt=0
        lt=[]
        anslist=[]
        ans=ans.lower()
        ans=ans.split()
        temp=[]
        for i in ans:
            if(i=='#'):
                anslist.append(temp)
                temp=[]
            else:
                temp.append(i)
        for i in range(0,len(qno)):
            templ=kw[i][1:len(kw[i])-1]
            qn=int(kw[i][0])

            m=anslist[qn-1]
            for j in range(0,len(m)):
                for l in templ:
                    if(l in m[j]):
                        km+=qno[i][1]
        marks=km-gm
    def m(self):
        global marks
        print(marks)

    def deli(self):
        s=""
        for i in range(0,count):
            s="ans"+str(i)+".jpeg"
            os.remove(s)
b=backend()
root=Tk()
root.title("DEXCO-An answer paper evaluating software")
root['bg']="lightgrey"
root.geometry("800x350")
S=Scrollbar(root)
frame=Frame(root)
frame2=Frame(root,background="lightgrey")
frame3=Frame(root,background="lightgrey")
frame4=Frame(root,background="lightgrey")
frame5=Frame(root,background="lightgrey")
choice=0
var=IntVar()
var2=IntVar()
type=""
root.iconbitmap(r'C:\Users\Home\Downloads\circled-d.ico')
def screen1():
    frame.pack()
    frame['bg']="lightgrey"
    ilabel=Label(frame,text="DEXCO",bg="lightgrey")
    ilabel.configure(font="Impact 40 underline")
    about=Text(frame,height=5,width=60,font=("Times",18))
    ebutton=Button(frame,text="EXIT",relief=RAISED,command=root.quit)
    nbutton=Button(frame,text="NEXT",relief=RAISED,command=screen2)
    aboutstring="DEXCO-An open source answer paper evaluating software developed with the help of python.This software is capable of correcting handwritten papers,printed text papers and can check for grammatical errors,keyword errors and so on.."
    about.insert(END,aboutstring)
    statusbar=Label(frame,text="*V1KK1", bd=2, relief=SUNKEN, anchor=E,bg="lightgrey")
    dlabel1=Label(frame,bg="lightgrey")
    dlabel2 = Label(frame,bg="lightgrey")
    dlabel3 = Label(frame,bg="lightgrey")
    dlabel4 = Label(frame,bg="lightgrey")
    ilabel.grid(row=0,column=2,columnspan=3)
    about.grid(row=1,column=2,columnspan=3)
    dlabel1.grid(row=2,column=4)
    dlabel4.grid(row=3, column=4)
    dlabel3.grid(row=4, column=4)
    dlabel2.grid(row=5, column=4)
    dlabel3.grid(row=7, column=4)
    ebutton.grid(row=6,column=0)
    nbutton.grid(row=6,column=5)
    statusbar.grid(sticky=W,row=8,column=4,columnspan=3)
def screen2():
    frame.destroy()
    var1 = IntVar()
    var2=IntVar()
    frame2.pack(fill='both', expand=True)
    label=Label(frame2,text="Choose a text file containing the keywords/valuepoints ",bg="lightgrey")
    bbutton=Button(frame2,text="Browse",command=tfile)
    label2=Label(frame2,text="Choose your File",bg="lightgrey")
    label2.config(font=("Times", 15))
    dlabel1=Label(frame2,bg="lightgrey")
    dlabel2 = Label(frame2,bg="lightgrey")
    dlabel3 = Label(frame2,bg="lightgrey")
    dlabel4 = Label(frame2, bg="lightgrey")
    ebutton = Button(frame2, text="EXIT", relief=RAISED, command=root.quit)
    alabel=Label(frame2,text="Select the type of answer sheet",bg="lightgrey")
    pv=Checkbutton(frame2, text="Printed Version", variable=var1,command=button)
    hv=Checkbutton(frame2, text="Handwritten Version", variable=var2,command=button)
    nbutton = Button(frame2, text="NEXT", relief=RAISED, command=screen3)
    label.pack()
    label.configure(font="Fixedsys 16 underline")
    dlabel1.pack()
    label2.pack()
    label2.configure(font="Fixedsys 15 underline")
    bbutton.pack()
    dlabel2.pack()
    alabel.pack()
    alabel.configure(font="Fixedsys 12 underline")
    dlabel3.pack()
    pv.pack()
    dlabel4.pack()
    hv.pack()
    nbutton.pack(side=RIGHT)
    ebutton.pack(side=RIGHT)
    frame2.mainloop()
def button():
    global type
    if(var.get()):
        type="p"
    if(var2.get()):
        type="h"
def tfile():
    filename=filedialog.askopenfilename(initialdir="Documents",title="Select your text file",filetypes=(("text files","*.txt"),("all files","*.*")))
    label=Label(root,text=filename)
    b.textfile(filename)
def screen3():
    frame2.destroy()
    frame3.pack(fill='both', expand=True)
    label = Label(frame3, text="Choose the answer script", bg="lightgrey")
    label3=Label(frame3,bg="lightgrey")
    label.pack()
    label.configure(font="Fixedsys 25 underline")
    label3.pack(side=TOP)
    label2=Label(frame3,text=" Choose the pdf answer sheet",bg="lightgrey")
    bbutton = Button(frame3, text="Browse", command=pfile)
    label2.config(font=("Fixedsys", 17))
    dlabel2 = Label(frame3, bg="lightgrey")
    dlabel3 = Label(frame3, bg="lightgrey")
    dlabel4 = Label(frame3, bg="lightgrey")
    ebutton = Button(frame3, text="EXIT", relief=RAISED, command=root.quit)
    nbutton = Button(frame3, text="NEXT", relief=RAISED, command=screen4)
    dlabel3.pack(side=TOP)
    dlabel2.pack(side=TOP)
    dlabel4.pack(side=TOP)
    label2.pack(side=TOP)
    bbutton.pack(side=TOP)
    nbutton.pack(side=RIGHT)
    ebutton.pack(side=RIGHT)
def pfile():
    filename = filedialog.askopenfilename(initialdir="Documents", title="Select your text file",
                                          filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    b.pdfile(filename)
progressbar=ttk.Progressbar(frame4, orient=HORIZONTAL,
                           length=500, mode='determinate')
def graph():
    xnames=["Grammar","Keywords"]
    y_pos=np.arange(2)
    yaxis=[gm,marks]
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Mark Distribution')
    plt.bar(y_pos,yaxis,tick_label=xnames,
            width=0.5, color=['green', 'red'])
    plt.show()
def score():
    global marks
    global total
    global gm
    print(gm)
    t=Text(frame4,height=2,width=14)
    s=str(marks)+"/"+str(total)
    t.insert(END,s)
    label=Label(frame4,bg="lightgrey")
    lbutton=Button(frame4,text="SHOW GRAPH",relief=RAISED,command=graph)
    ebutton=Button(frame4, text="EXIT", relief=RAISED, command=root.quit)
    label.pack()
    t.pack()
    lbutton.pack()
    ebutton.pack(side=RIGHT)
def correct():
    progressbar['value']=20
    b.convert()
    b.calc()
    progressbar['value']=60
    b.deli()
    progressbar['value']=130
    sbutton=Button(frame4,text="DISPLAY MARKS",relief=RAISED,command=score)
    dlabel2=Label(frame4, bg="lightgrey")
    dlabel3=Label(frame4, bg="lightgrey")
    dlabel4=Label(frame4, bg="lightgrey")
    dlabel3.pack(side=TOP)
    dlabel2.pack(side=TOP)
    dlabel4.pack(side=TOP)
    sbutton.pack(side=TOP)
def screen4():
    frame3.destroy()
    frame4.pack(fill='both', expand=True)
    label=Label(frame4,text="DEXCO", bg="lightgrey")
    pbutton=Button(frame4,text="START EVALUATING",relief=RAISED,command=correct)
    label.pack()
    label.configure(font="Fixedsys 40 underline")
    progressbar.pack()
    pbutton.pack()
screen1()
root.mainloop()
