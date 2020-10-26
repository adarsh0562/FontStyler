from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
root = Tk()
__font = ["Times New Roman", "Wide Latin""Rockwell Extra Bold", "Segoe UI Semibold", "MV Boli",
          "Matura MT Script Capitals", "Microsoft Sans Serif""Gill Sans Ultra Bold", "Cooper Black", "Algerian",
          "Goudy Stout", "Corbel", "Arial black", "Calibri", "Berlin Sans FB Demi"]
__size = [8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
__weight = ["bold", "italic", "normal"]

text = Text(root)
text.pack(expand=YES, fill=BOTH)
font_family= "times new roman"
font_size = 8
font_weight = "normal"

def __fontStyle(*event):
    global __font, __size, __weight,font_family,font_size,font_weight,text
    window = Toplevel()
    window.minsize(height=400, width=410)
    window.maxsize(height=400, width=410)


    Label(window).grid(row=0, column=0)
    Label(window, text="Font :").grid(row=0, column=1,sticky="W")
    Label(window).grid(row=0, column=2)
    Label(window, text="Font Style :").grid(row=0, column=3,sticky="W")
    Label(window).grid(row=0, column=4)
    Label(window, text="Size :").grid(row=0, column=5,sticky="W")
    t1 = Entry(window, width=30)
    t1.grid(row=1, column=1)
    t1.insert(0, font_family)

    t2 = Entry(window)
    t2.grid(row=1, column=3)
    t2.insert(0, font_weight)

    t3 = Entry(window, width=10)
    t3.grid(row=1, column=5)
    t3.insert(0, font_size)

    def CurSelet_lbox(evt):
        try:
            font_family = lbox.get(lbox.curselection())
            t1.delete(0,END)
            t1.insert(0,font_family)
            myFont.configure(family=font_family)
        except TclError:
            return

    def CurSelet_lbox2(evt):
        try:
            font_weight = lbox2.get(lbox2.curselection())
            t2.delete(0,END)
            t2.insert(0,font_weight)
            myFont.configure(weight=font_weight)

        except TclError:
            return

    def CurSelet_lbox3(evt):
        try:
            font_size = int(lbox3.get(lbox3.curselection()))
            t3.delete(0,END)
            t3.insert(0,font_size)
            myFont.configure(size=font_size)
        except TclError:
            return

    def click_OK():
        text.config(font=myFont)
        window.destroy()

    myFont = tkFont.Font(family=font_family, size=font_size, weight=font_weight)
    lbox = Listbox(window, width=30, height=8)
    lbox.grid(row=2, column=1)
    lbox.bind('<<ListboxSelect>>', CurSelet_lbox)

    lbox2 = Listbox(window, height=8)
    lbox2.grid(row=2, column=3)
    lbox2.bind('<<ListboxSelect>>', CurSelet_lbox2)
    lbox3 = Listbox(window, width=10, height=8)
    lbox3.grid(row=2, column=5)
    lbox3.bind('<<ListboxSelect>>', CurSelet_lbox3)
    label_frame = LabelFrame(window, text="Sample", width=50, height=30)
    label_frame.grid(row=3, column=2, columnspan=4, sticky="E",
                     padx=5, pady=10, ipadx=70, ipady=30)
    sample = Label(label_frame, text="AaBbYyZz",font=myFont)
    sample.place(x=60, y=25)
    #sample["text"] = myFont

    b1=ttk.Button(window,text="OK", width=12, command=click_OK)
    b1.grid(row=4,column=3,pady=80)
    b2=ttk.Button(window,text="Cancel", width=12,command=lambda: window.destroy())
    b2.grid(row=4,column=4,columnspan=3,pady=80)
    for font in __font:
        lbox.insert(END,font)
    for weight in __weight:
        lbox2.insert(END,weight)
    for size in __size:
        lbox3.insert(END,size)
    window.update()

menubar = Menu(root)
formatMenu = Menu(menubar, tearoff=0)
formatMenu.add_command(label="FontStyle", command=__fontStyle)
menubar.add_cascade(label="Format", menu=formatMenu)
root.config(menu=menubar)

root.mainloop()
