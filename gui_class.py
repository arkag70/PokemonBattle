import tkinter as tk
from tkinter import ttk
import time

class PokeGUI:

	def __init__(self,canvas):
		self.master = tk.Frame(canvas)
		self.master.grid(row = 0,column = 0)
		self.firstleft = tk.Frame(self.master,highlightbackground="black", highlightthickness=1,background = "#f0ead6")
		self.firstleft.grid(row = 0,column = 0)

		self.firstright = tk.Frame(self.master,highlightbackground="black", highlightthickness=1,background = "#f0ead6")
		self.firstright.grid(row = 0,column = 1)

		self.secondleft = tk.Frame(self.master,highlightbackground="black", highlightthickness=1)
		self.secondleft.grid(row = 1,column = 0)

		self.secondright = tk.Frame(self.master,highlightbackground="black", highlightthickness=1)
		self.secondright.grid(row = 1,column = 1)

		self.thirdleft = tk.Frame(self.master,highlightbackground="black", highlightthickness=1)
		self.thirdleft.grid(row = 2,column = 0)

		self.thirdright = tk.Frame(self.master,highlightbackground="black", highlightthickness=1)
		self.thirdright.grid(row = 2,column = 1)

		self.bottom = tk.Frame(self.master)
		self.bottom.grid(row = 3,column = 0)

		self.remark = tk.Frame(self.master)
		self.remark.grid(row = 4,column = 0)

	def createLabel(self,canvas,row_ = 0,col_ = 0,padx_ = 2,pady_ = 2,text_ = "Label-Text",font_ = ("Calibri 12 bold")):
		self.label = tk.Label(canvas,text = text_,font=font_,background = "#f0ead6")
		self.label.grid(row = row_,column = col_,padx = padx_, pady = pady_)
		return self.label

	# def createEntry(self,canvas,row_ = 0,col_ = 0,padx = 2,pady = 2,width_ = 50,bd_ = 2):
	# 	self.entry = tk.Entry(canvas,width = width_,bd = bd_)
	# 	self.entry.grid(row = row_,column = col_,padx = padx_, pady = pady_)
	# 	return self.entry

	def createButton(self,canvas,command_,text_ = "Button-Text",width_ = 5,bd_ = 3,font_ = ("Calibri 12")):
		self.button = tk.Button(canvas,text = text_,command = command_,width = width_,bd = bd_,font = font_)
		self.button.grid(row = 0,column = 0,sticky = tk.W + tk.E)
		return self.button

	def createRadioButton(self,canvas,variable_,text_ = "radio-item",value_ = 1,row_ = 0, col_ = 0):
		self.radio = tk.Radiobutton(canvas,text = text_,variable = variable_,value = value_)
		self.radio.grid(row = row_,column = col_,sticky = "W")
		return self.radio

	def createImage(self,file_,canvas,row_ = 0,col_ = 0):
		photo = tk.PhotoImage(file=file_)
		imglabel= tk.Label(canvas,image = photo,background = "#f0dd8e")
		imglabel.image = photo
		imglabel.grid(row = row_,column = col_)
		return imglabel
	
	def createProgress(self,canvas,orient_="horizontal",length_=150, mode_="determinate",row_ = 0, col_ = 1):
		s = ttk.Style()
		s.theme_use('default')
		s.configure("Horizontal.TProgressbar", foreground='green', background='green')
		self.pbar = ttk.Progressbar(canvas,orient = orient_,length = length_, mode = mode_)
		self.pbar.grid(row = row_, column = col_)
		self.pbar["maximum"] = length_
		self.pbar["value"] = length_
		return self.pbar







