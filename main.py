from gui_class import *
'''
createLabel(self,canvas,row_ = 0,col_ = 0,padx_ = 2,pady_ = 2,text_ = "Label-Text",font_ = ("Calibri 12"))
createEntry(canvas,row_ = 0,col_ = 0,padx = 2,pady = 2,width_ = 50,bd_ = 2)
createButton(canvas,command_,text_ = "Button-Text",width_ = 5,bd_ = 2,font_ = ("Calibri 12"),row_ = 0,col_ = 0,padx = 2,pady = 2)
createRadioButton(canvas,text_ = "radio-item",variable_ = var,value_ = 1,row_ = 0, col_ = 0)
createImage(file_,canvas,row_ = 0,col_ = 0)
'''

if __name__ == "__main__":

	root = tk.Tk()
	root.title("Pokemon Battle")
	pg = PokeGUI(root)

	p1 = Pokemon()
	p2 = Pokemon()

	firstpokeLabel = pg.createLabel(pg.firstleft,text_ = p1.fetchName())
	firstImg = pg.createImage(file_ = f"poke_png\\{p1.fetchRank()} {p1.fetchName()}.png",canvas = pg.firstleft,row_ = 1,col_ = 0)

	secondpokeLabel = pg.createLabel(pg.firstright,text_ = p2.fetchName())
	secondImg = pg.createImage(file_ = f"poke_png\\{p2.fetchRank()} {p2.fetchName()}.png",canvas = pg.firstright,row_ = 1,col_ = 0)

	firstpokeHP = pg.createLabel(pg.secondleft,text_= "201/201")
	secondpokeHP = pg.createLabel(pg.secondright,text_= "195/195")

	firstMoveLabel = pg.createLabel(pg.thirdleft,text_ = "Moves",row_ = 0,col_ = 0)
	firstmoves = ["Quick Attack","Slash","Double Kick","Blaze Kick"]
	firstRadio = []
	var = tk.IntVar()
	for i in range(4):
		firstRadio.append(pg.createRadioButton(pg.thirdleft,text_ = firstmoves[i],variable_ = var,value_ = i+1,row_ = i+1,col_ = 0))


	secondMoveLabel = pg.createLabel(pg.thirdright,text_ = "Moves",row_ = 0,col_ = 0)
	secondmoves = ["Pound","Leaf Blade","Pursuit","Agility"]
	secondRadio = []
	var = tk.IntVar()
	for i in range(4):
		secondRadio.append(pg.createRadioButton(pg.thirdright,text_ = secondmoves[i],variable_ = var,value_ = i+1,row_ = i+1,col_ = 0))


	startButton = pg.createButton(pg.bottom,text_ = "GO",command_ = fight)

	root.mainloop()