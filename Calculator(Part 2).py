import tkinter
from tkinter import *
from tkinter import messagebox
import webbrowser

root = tkinter.Tk()
root.geometry("250x400+1050+90")
root.resizable(0,0)
root.title("Basic Calculator - By Techno Feed")



val = ""
A = 0
operator = ""




def btn_0_clkd():
	global val
	val = val + "0"
	data.set(val)

def btn_1_clkd():
	global val
	val = val + "1"
	data.set(val)

def btn_2_clkd():
	global val
	val = val + "2"
	data.set(val)

def btn_3_clkd():
	global val
	val = val + "3"
	data.set(val)

def btn_4_clkd():
	global val
	val = val + "4"
	data.set(val)

def btn_5_clkd():
	global val
	val = val + "5"
	data.set(val)

def btn_6_clkd():
	global val
	val = val + "6"
	data.set(val)

def btn_7_clkd():
	global val
	val = val + "7"
	data.set(val)

def btn_8_clkd():
	global val
	val = val + "8"
	data.set(val)

def btn_9_clkd():
	global val
	val = val + "9"
	data.set(val)

def C_clkd():
	global A
	global operator
	global val
	val = ""
	A = 0
	operator = ""
	data.set(val)

def plus_clkd():
	global A
	global operator
	global val
	A = int(val)
	operator = "+"
	val = val + "+"
	data.set(val)

def min_clkd():
	global A
	global operator
	global val
	A = int(val)
	operator = "-"
	val = val + "-"
	data.set(val)

def mul_clkd():
	global A
	global operator
	global val
	A = int(val)
	operator = "*"
	val = val + "*"
	data.set(val)

def div_clkd():
	global A
	global operator
	global val
	A = int(val)
	operator = "/"
	val = val + "/"
	data.set(val)

def result():
	global A
	global operator
	global val
	val1 = val
	if operator == "+":
		x = int(val1.split("+")[1])
		c = A + x
		data.set(c)
		val = str(c)
	elif operator == "-":
		x = int(val1.split("-")[1])
		c = A - x
		data.set(c)
		val = str(c)
	elif operator == "*":
		x = int(val1.split("*")[1])
		c = A * x
		data.set(c)
		val = str(c)
	elif operator == "/":
		x = int(val1.split("/")[1])
		if x == 0:
			messagebox.showerror("Error","You cannot Divide by 0")
			A = ""
			val = ""
			data.set(val)
		else:
			c = int (A / x)
			data.set(c)
			val = str(c)




def youtube():
	webbrowser.open("https://bit.ly/technofeed", new = 1)

def whatsapp():
	webbrowser.open("https://bit.ly/technofeedwa", new = 1)

def instagram():
	webbrowser.open("https://bit.ly/technofeedig", new = 1)




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
	command = btn_1_clkd,
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
	command = btn_2_clkd,
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
	command = btn_3_clkd,
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
	command = plus_clkd
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
	command = btn_4_clkd,
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
	command = btn_5_clkd,
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
	command = btn_6_clkd,
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
	command = min_clkd,
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
	command = btn_7_clkd,
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
	command = btn_8_clkd,
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
	command = btn_9_clkd,
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
	command = mul_clkd,
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
	command = C_clkd,
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
	command = btn_0_clkd,
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
	command = result,
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
	command = div_clkd,
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
	command = youtube
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
	command = whatsapp
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
	command = instagram
	)
btn3.pack(side = LEFT, expand = True, fill = "both")


root.mainloop()