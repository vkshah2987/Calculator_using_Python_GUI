import tkinter
from tkinter import *
from tkinter import messagebox
import webbrowser

root = tkinter.Tk()
root.geometry("250x400+1050+90")
root.resizable(0,0)
root.title("Basic Calculator - By Techno Feed")





photo1 = PhotoImage(file = r"C:\Users\SHAH\Pictures\Saved Pictures\YouTube.png")
photoimage1 = photo1.subsample(30,30)

photo2 = PhotoImage(file = r"C:\Users\SHAH\Pictures\Saved Pictures\WhatsApp.png")
photoimage2 = photo2.subsample(40,40)

photo3 = PhotoImage(file = r"C:\Users\SHAH\Pictures\Saved Pictures\Instagram.png")
photoimage3 = photo3.subsample(60,60)




data = StringVar()
lbl = Label(
	root,
	text ="Label",
	anchor = SE,
	font = ("Verdana", 20),
	textvariable = data,
	bg = "#FFFFFF",
	fg = "#000000"
	)
lbl.pack(expand = True, fill = "both")



btnrow1 = Frame(root, bg = "#F49F1C")
btnrow1.pack(expand = True, fill = "both",)

btnrow2 = Frame(root, bg = "#F49F1C")
btnrow2.pack(expand = True, fill = "both",)

btnrow3 = Frame(root, bg = "#F49F1C")
btnrow3.pack(expand = True, fill = "both",)

btnrow4 = Frame(root, bg = "#F49F1C")
btnrow4.pack(expand = True, fill = "both",)

btnrow5 = Frame(root, bg = "#F49F1C")
btnrow5.pack(expand = True, fill = "both",)






btn1 = Button(
	btnrow1,
	text = "1",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn1.pack(side = LEFT,expand = True, fill= "both")

btn2 = Button(
	btnrow1,
	text = "2",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn2.pack(side = LEFT,expand = True, fill= "both")

btn3 = Button(
	btnrow1,
	text = "3",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn3.pack(side = LEFT,expand = True, fill= "both")

btn4 = Button(
	btnrow1,
	text = "+",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn4.pack(side = LEFT,expand = True, fill= "both")







btn1 = Button(
	btnrow2,
	text = "4",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn1.pack(side = LEFT,expand = True, fill= "both")

btn2 = Button(
	btnrow2,
	text = "5",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn2.pack(side = LEFT,expand = True, fill= "both")

btn3 = Button(
	btnrow2,
	text = "6",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn3.pack(side = LEFT,expand = True, fill= "both")

btn4 = Button(
	btnrow2,
	text = "-",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn4.pack(side = LEFT,expand = True, fill= "both")







btn1 = Button(
	btnrow3,
	text = "7",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn1.pack(side = LEFT,expand = True, fill= "both")

btn2 = Button(
	btnrow3,
	text = "8",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn2.pack(side = LEFT,expand = True, fill= "both")

btn3 = Button(
	btnrow3,
	text = "9",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn3.pack(side = LEFT,expand = True, fill= "both")

btn4 = Button(
	btnrow3,
	text = "*",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn4.pack(side = LEFT,expand = True, fill= "both")







btn1 = Button(
	btnrow4,
	text = "C",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn1.pack(side = LEFT,expand = True, fill= "both")

btn2 = Button(
	btnrow4,
	text = "0",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn2.pack(side = LEFT,expand = True, fill= "both")

btn3 = Button(
	btnrow4,
	text = "=",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn3.pack(side = LEFT,expand = True, fill= "both")

btn4 = Button(
	btnrow4,
	text = "/",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	bg = "#F49F1C",
	fg = "#FFFFFF",
	)
btn4.pack(side = LEFT,expand = True, fill= "both")







btn1 = Button(
	btnrow5,
	text = "Youtube",
	image = photoimage1,
	compound = LEFT,
	font = ("Verdana", 8),
	relief = GROOVE,
	border = 0,
	bg = "#2F2F2B",
	fg = "#FF742B",
	height = 0,
	width = 5,
	)
btn1.pack(side = LEFT, expand = True, fill = "both")

btn2 = Button(
	btnrow5,
	text = "Whatsapp",
	image = photoimage2,
	compound = LEFT,
	font = ("Verdana", 8),
	relief = GROOVE,
	border = 0,
	bg = "#2F2F2B",
	fg = "#FF742B",
	height = 0,
	width = 5,
	)
btn2.pack(side = LEFT, expand = True, fill = "both")

btn3 = Button(
	btnrow5,
	text = "Instagram",
	image = photoimage3,
	compound = LEFT,
	font = ("Verdana", 8),
	relief = GROOVE,
	border = 0,
	bg = "#2F2F2B",
	fg = "#FF742B",
	height = 0,
	width = 5,
	)
btn3.pack(side = LEFT, expand = True, fill = "both")


root.mainloop()