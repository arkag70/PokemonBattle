from gui_class import *
import threading


p1 = Pokemon()
p2 = Pokemon()
fullhp1 = p1.HP
fullhp2 = p2.HP
hp1 = fullhp1
hp2 = fullhp2
round = 0
disablity = 0
def second(remaining2onbar):
	s = ttk.Style()
	while(secondPbar["value"] > remaining2onbar):
		secondPbar["value"] -= 1
		if secondPbar["value"] <= 37:
			s.configure("red.Horizontal.TProgressbar", foreground='red')
			secondPbar.configure(style="red.Horizontal.TProgressbar",value = secondPbar["value"])
		elif secondPbar["value"] <= 75:
			s.configure("yellow.Horizontal.TProgressbar", foreground='yellow')
			secondPbar.configure(style="yellow.Horizontal.TProgressbar",value = secondPbar["value"])

		val = int(secondPbar["value"]*fullhp2/secondPbar["maximum"])
		secondpokeHP.config(text = f"HP: {val}/{fullhp2}")
		time.sleep(0.05)
	return val

def first(remaining1onbar):
	while(firstPbar["value"] > remaining1onbar):
		firstPbar["value"] -= 1
		val = int(firstPbar["value"]*fullhp1/firstPbar["maximum"])
		firstpokeHP.config(text = f"HP: {val}/{fullhp1}")
		time.sleep(0.05)
	return val	

def startProgress(damageon1,damageon2,n):
	global round
	round += 1
	print(round)
	global hp1,hp2
	global startButton
	remaining1onbar = int((hp1-damageon1)*firstPbar["maximum"]/fullhp1)
	remaining2onbar = int((hp2-damageon2)*secondPbar["maximum"]/fullhp2)

	if remaining1onbar < 0:
		remaining1onbar = 0
	if remaining2onbar < 0:
		remaining2onbar = 0

	if n == 1:
		# first pokemon attacks first due to speed stat so effect on second pokemon
		print(f"{p1.name} used move")
		time.sleep(1)
		hp2 = second(remaining2onbar)
		if hp2 != 0:
			time.sleep(2)
			print(f"{p2.name} used move")
			time.sleep(1)
			hp1 = first(remaining1onbar)
			if hp1 == 0:
				print(f"{p2.name} wins the round")
				return -2
			else:
				pass
		else:
			print(f"{p1.name} wins the match")
			return -1

	if n == 2:
		# second pokemon attacks first due to speed stat so effect on first pokemon
		print(f"{p2.name} used move")
		time.sleep(1)
		hp1 = first(remaining1onbar)
		if hp1 != 0:
			time.sleep(2)
			print(f"{p1.name} used move")
			time.sleep(1)
			hp2 = second(remaining2onbar)
			if hp2 == 0:
				print(f"{p1.name} wins the round")
				return -1
			else:
				pass
		else:
			print(f"{p2.name} wins the match")
			return -2
	return 0


def start_fight_thread(event):
    startButton.config(state = tk.DISABLED)
    global fight_thread
    fight_thread = threading.Thread(target = fight) #args = (firstPbar,secondPbar,var1,var2))
    fight_thread.daemon = True
    fight_thread.start()
    root.after(20,check_fight_thread)

def check_fight_thread():
    if fight_thread.is_alive():
        root.after(20,check_fight_thread)
    else:
    	if disablity < 0:
    		pass
    	else:
        	startButton.config(state = "normal")

def fight():
	global disablity
	damageon2 = 40
	damageon1 = 45
	disablity = startProgress(damageon1,damageon2,1)
	# check speed to decide who'll go first


	#check for sleep or freeze; if yes then skip to next player or end turn if player2
	#


'''
createLabel(canvas,row_ = 0,col_ = 0,padx_ = 2,pady_ = 2,text_ = "Label-Text",font_ = ("Calibri 12"))
createEntry(canvas,row_ = 0,col_ = 0,padx = 2,pady = 2,width_ = 50,bd_ = 2)
createButton(canvas,command_,text_ = "Button-Text",width_ = 5,bd_ = 2,font_ = ("Calibri 12"),row_ = 0,col_ = 0,padx = 2,pady = 2)
createRadioButton(canvas,text_ = "radio-item",variable_ = var,value_ = 1,row_ = 0, col_ = 0)
createImage(file_,canvas,row_ = 0,col_ = 0)
(orient_="horizontal",length_=200, mode_="determinate",row_ = 0, col_ = 1)
'''
if __name__ == "__main__":
	
	root = tk.Tk()
	root.title("Pokemon Battle")
	pg = PokeGUI(root)

	firstpokeLabel = pg.createLabel(pg.firstleft,text_ = p1.name)
	firstImg = pg.createImage(file_ = f"poke_png\\{p1.rank} {p1.name}.png",canvas = pg.firstleft,row_ = 1,col_ = 0)

	secondpokeLabel = pg.createLabel(pg.firstright,text_ = p2.name)
	secondImg = pg.createImage(file_ = f"poke_png\\{p2.rank} {p2.name}.png",canvas = pg.firstright,row_ = 1,col_ = 0)

	firstpokeHP = pg.createLabel(pg.secondleft,text_= f"HP: {fullhp1}/{fullhp1}",row_ = 0,col_ = 0)
	firstPbar = pg.createProgress(pg.secondleft)
	secondpokeHP = pg.createLabel(pg.secondright,text_= f"HP: {fullhp2}/{fullhp2}",row_ = 0,col_ = 0)
	secondPbar = pg.createProgress(pg.secondright)

	firstMoveLabel = pg.createLabel(pg.thirdleft,text_ = "Moves",row_ = 0,col_ = 0)
	firstmoves = p1.getMoves()[0]
	firstdesc = p1.getMoves()[1]
	firstRadio = []
	var1 = tk.IntVar()
	firstRadio1 = pg.createRadioButton(pg.thirdleft,text_ = firstmoves[0],variable_ = var1,value_ = 0,row_ = 1,col_ = 0)
	firstRadio2 = pg.createRadioButton(pg.thirdleft,text_ = firstmoves[1],variable_ = var1,value_ = 1,row_ = 2,col_ = 0)
	firstRadio3 = pg.createRadioButton(pg.thirdleft,text_ = firstmoves[2],variable_ = var1,value_ = 2,row_ = 3,col_ = 0)
	firstRadio4 = pg.createRadioButton(pg.thirdleft,text_ = firstmoves[3],variable_ = var1,value_ = 3,row_ = 4,col_ = 0)


	secondMoveLabel = pg.createLabel(pg.thirdright,text_ = "Moves",row_ = 0,col_ = 0)
	secondmoves = p2.getMoves()[0]
	seconddesc = p2.getMoves()[1]
	secondRadio = []
	var2 = tk.IntVar()
	secondRadio1 = pg.createRadioButton(pg.thirdright,text_ = secondmoves[0],variable_ = var2,value_ = 0,row_ = 1,col_ = 0)
	secondRadio2 = pg.createRadioButton(pg.thirdright,text_ = secondmoves[1],variable_ = var2,value_ = 1,row_ = 2,col_ = 0)
	secondRadio3 = pg.createRadioButton(pg.thirdright,text_ = secondmoves[2],variable_ = var2,value_ = 2,row_ = 3,col_ = 0)
	secondRadio4 = pg.createRadioButton(pg.thirdright,text_ = secondmoves[3],variable_ = var2,value_ = 3,row_ = 4,col_ = 0)

	
	startButton = pg.createButton(pg.bottom,text_ = "GO",command_ = lambda: start_fight_thread(None))

	remarkLabel = pg.createLabel(pg.remark,row_ = 0,col_ = 0,padx_ = 2,pady_ = 2,text_ = "Label-Text",font_ = ("Calibri 12"))

	root.mainloop()
