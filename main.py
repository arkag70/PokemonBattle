from gui_class import *
import threading

def startProgress(pbar):
		if pbar["value"] >= 0:
			pbar["value"] -= 1
			time.sleep(0.1)

def start_fight_thread(event):
    #startButton.config(state = DISABLED)
    global fight_thread
    fight_thread = threading.Thread(target = fight, args = (firstPbar,secondPbar))
    fight_thread.daemon = True
    fight_thread.start()
    root.after(20,check_fight_thread)
#---------------------------------------------------------------------------------------------------#

def check_fight_thread():
    if fight_thread.is_alive():
        root.after(20,check_fight_thread)
    else:
        pass

def fight(bar1,bar2):
	for i in range(60):
		startProgress(bar2)


'''
createLabel(self,canvas,row_ = 0,col_ = 0,padx_ = 2,pady_ = 2,text_ = "Label-Text",font_ = ("Calibri 12"))
createEntry(canvas,row_ = 0,col_ = 0,padx = 2,pady = 2,width_ = 50,bd_ = 2)
createButton(canvas,command_,text_ = "Button-Text",width_ = 5,bd_ = 2,font_ = ("Calibri 12"),row_ = 0,col_ = 0,padx = 2,pady = 2)
createRadioButton(canvas,text_ = "radio-item",variable_ = var,value_ = 1,row_ = 0, col_ = 0)
createImage(file_,canvas,row_ = 0,col_ = 0)
(orient_="horizontal",length_=200, mode_="determinate",row_ = 0, col_ = 1)
'''
if __name__ == "__main__":

	p1 = Pokemon()
	p2 = Pokemon()
	
	hp1 = p1.fetchHP()
	hp2 = p2.fetchHP()
	
	root = tk.Tk()
	root.title("Pokemon Battle")
	pg = PokeGUI(root)

	firstpokeLabel = pg.createLabel(pg.firstleft,text_ = p1.fetchName())
	firstImg = pg.createImage(file_ = f"poke_png\\{p1.fetchRank()} {p1.fetchName()}.png",canvas = pg.firstleft,row_ = 1,col_ = 0)

	secondpokeLabel = pg.createLabel(pg.firstright,text_ = p2.fetchName())
	secondImg = pg.createImage(file_ = f"poke_png\\{p2.fetchRank()} {p2.fetchName()}.png",canvas = pg.firstright,row_ = 1,col_ = 0)

	
	firstpokeHP = pg.createLabel(pg.secondleft,text_= f"HP: {hp1}/{p1.fetchHP()}",row_ = 0,col_ = 0)
	firstPbar = pg.createProgress(pg.secondleft)
	secondpokeHP = pg.createLabel(pg.secondright,text_= f"HP: {hp2}/{p2.fetchHP()}",row_ = 0,col_ = 0)
	secondPbar = pg.createProgress(pg.secondright)

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


	startButton = pg.createButton(pg.bottom,text_ = "GO",command_ = lambda: start_fight_thread(None))

	root.mainloop()