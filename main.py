from gui_class import *
from pokemon import *
from battle import *
import threading
import winsound as w2
from playsound import playsound

p1 = Pokemon()
p2 = Pokemon()
fullhp1 = p1.HP
fullhp2 = p2.HP
hp1 = fullhp1
hp2 = fullhp2
sleepturns = random.randint(1,5)
round = 0
disablity = 0

def second(remaining2onbar):
	s = ttk.Style()
	s.theme_use('default')
	while(secondPbar["value"] > remaining2onbar):
		secondPbar["value"] -= 1
		if secondPbar["value"] <= 37:
			s.configure("s.Horizontal.TProgressbar", foreground='red', background='red')
			secondPbar.configure(style="s.Horizontal.TProgressbar")
		elif secondPbar["value"] <= 75:
			s.configure("s.Horizontal.TProgressbar",foreground='yellow', background='yellow')
			secondPbar.configure(style="s.Horizontal.TProgressbar")
		else:
			s.configure("s.Horizontal.TProgressbar",foreground='green', background='green')
			secondPbar.configure(style="s.Horizontal.TProgressbar")

		val = int(secondPbar["value"]*fullhp2/secondPbar["maximum"])
		secondpokeHP.config(text = f"HP: {val}/{fullhp2}")
		time.sleep(0.05)
	return val

def first(remaining1onbar):
	s = ttk.Style()
	s.theme_use('default')
	while(firstPbar["value"] > remaining1onbar):
		firstPbar["value"] -= 1
		if firstPbar["value"] <= 37:
			s.configure("f.Horizontal.TProgressbar", foreground='red', background='red')
			firstPbar.configure(style="f.Horizontal.TProgressbar")
		elif firstPbar["value"] <= 75:
			s.configure("f.Horizontal.TProgressbar",foreground='yellow', background='yellow')
			firstPbar.configure(style="f.Horizontal.TProgressbar")
		else:
			s.configure("f.Horizontal.TProgressbar",foreground='green', background='green')
			firstPbar.configure(style="f.Horizontal.TProgressbar")

		val = int(firstPbar["value"]*fullhp1/firstPbar["maximum"])
		firstpokeHP.config(text = f"HP: {val}/{fullhp1}")
		time.sleep(0.05)
	return val	

def startProgress(damageon1,damageon2,n):
	will1move = 0
	will2move = 0
	global round
	round += 1
	print(round)
	global hp1,hp2
	
	if n == 1:
		p1.condition = checkCondition(p1)
		#pokemon 1 attacks first
		if p1.condition == "move":
			time.sleep(1)
			print(f"{p1.name} used {p1.move}")
			time.sleep(1)
			remaining2onbar = int((hp2-damageon2)*secondPbar["maximum"]/fullhp2)
			if remaining2onbar < 0:
				remaining2onbar = 0
			playsound('NH.wav')
			hp2 = second(remaining2onbar)
			if hp2 == 0:
				#pokeom 2 fainted
				print(f"{p2.name} fainted!")
				return -1
			else:
				#pokemon 2 did not faint
				p2.condition = checkCondition(p2)
				if p2.condition == "move":
					will2move = 1
				elif p2.condition == "hurt-itself":
					will2move = -1
				else:
					pass
		elif p1.condition == "hurt-itself":
			time.sleep(2)
			remaining1onbar = int((hp1-10)*firstPbar["maximum"]/fullhp1)
			if remaining1onbar < 0:
				remaining1onbar = 0
			playsound('NH.wav')
			hp1 = first(remaining1onbar)
			print(f"{p1.name} hurt itself in confusion")
			if hp1 == 0:
				#pokemon 1 fainted
				print(f"{p1.name} fainted!")
				return -2
			else:
				time.sleep(2)
				p2.condition = checkCondition(p2)
				if p2.condition == "move":
					will2move = 1
				elif p2.condition == "hurt-itself":
					will2move = -1
				else:
					pass
		elif p1.condition == "wont":
			time.sleep(2)
			p2.condition = checkCondition(p2)
			if p2.condition == "move":
				will2move = 1
			elif p2.condition == "hurt-itself":
				will2move = -1
			else:
				pass

		if will2move == 1:
			time.sleep(1)
			print(f"{p2.name} used {p2.move}")
			time.sleep(1)
			remaining1onbar = int((hp1-damageon1)*firstPbar["maximum"]/fullhp1)
			if remaining1onbar < 0:
				remaining1onbar = 0
			playsound('NH.wav')
			hp1 = first(remaining1onbar)
			if hp1 == 0:
				#pokemon 1 fainted
				print(f"{p1.name} fainted!")
				return -2
			else:
				pass
		elif will2move == -1:
			time.sleep(2)
			remaining2onbar = int((hp2-10)*secondPbar["maximum"]/fullhp2)
			if remaining2onbar < 0:
				remaining2onbar = 0
			playsound('NH.wav')
			hp2 = second(remaining2onbar)
			print(f"{p2.name} hurt itself in confusion")
			if hp2 == 0:
				print(f"{p2.name} fainted!")
				return -1
			else:
				pass

	elif n == 2:
		p2.condition = checkCondition(p2)
		#pokemon 2 attacks first
		if p2.condition == "move":
			time.sleep(1)
			print(f"{p2.name} used {p2.move}")
			time.sleep(1)
			remaining1onbar = int((hp1-damageon1)*firstPbar["maximum"]/fullhp1)
			if remaining1onbar < 0:
				remaining1onbar = 0
			playsound('NH.wav')
			hp1 = first(remaining1onbar)
			if hp1 == 0:
				#pokeom 1 fainted
				print(f"{p1.name} fainted!")
				return -2
			else:
				#pokemon 1 did not faint
				p1.condition = checkCondition(p1)
				if p1.condition == "move":
					will1move = 1
				elif p1.condition == "hurt-itself":
					will1move = -1
				else:
					pass
		elif p2.condition == "hurt-itself":
			time.sleep(2)
			remaining2onbar = int((hp2-10)*secondPbar["maximum"]/fullhp2)
			if remaining2onbar < 0:
				remaining2onbar = 0
			playsound('NH.wav')
			hp2 = second(remaining2onbar)
			print(f"{p2.name} hurt itself in confusion")
			if hp2 == 0:
				#pokemon 2 fainted
				print(f"{p2.name} fainted!")
				return -1
			else:
				time.sleep(2)
				p1.condition = checkCondition(p1)
				if p1.condition == "move":
					will1move = 1
				elif p1.condition == "hurt-itself":
					will1move = -1
				else:
					pass
		elif p2.condition == "wont":
			time.sleep(2)
			p1.condition = checkCondition(p1)
			if p1.condition == "move":
				will1move = 1
			elif p1.condition == "hurt-itself":
				will1move = -1
			else:
				pass

		if will1move == 1:
			time.sleep(1)
			print(f"{p1.name} used {p1.move}")
			time.sleep(1)
			remaining2onbar = int((hp2-damageon2)*secondPbar["maximum"]/fullhp2)
			if remaining2onbar < 0:
				remaining2onbar = 0
			playsound('NH.wav')
			hp2 = second(remaining2onbar)
			if hp2 == 0:
				#pokemon 2 fainted
				print(f"{p2.name} fainted!")
				return -1
			else:
				pass
		elif will1move == -1:
			time.sleep(2)
			remaining1onbar = int((hp1-10)*firstPbar["maximum"]/fullhp1)
			if remaining1onbar < 0:
				remaining1onbar = 0
			playsound('NH.wav')
			hp1 = first(remaining1onbar)
			print(f"{p1.name} hurt itself in confusion")
			if hp1 == 0:
				print(f"{p1.name} fainted!")
				return -2
			else:
				pass
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
	damageon2 = 20
	damageon1 = 15
	# p1.isParalysed = True
	# p2.isParalysed = True
	# p1.isConfused = True
	# p2.isConfused = True
	# p1.confuseCount = 2
	# p2.confuseCount = 2
	# p1.isPoisoned = True
	# p2.isPoisoned = True
	# p1.isBurnt = True
	# p2.isBurnt = True
	# p1.isFrozen = True
	# p1.sleepFreezeCount = 2
	# p2.isFrozen = True
	# p2.sleepFreezeCount = 2
	
	# check speed to decide who'll go first
	if p1.speed > p2.speed:
		n = 1
	else:
		n = 2
	disablity = startProgress(damageon1,damageon2,n)
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
	w2.PlaySound('poke_music.wav', w2.SND_ASYNC | w2.SND_NOSTOP)

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
