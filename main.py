from gui_class import *
from pokemon import *
from battle import *
import threading

p = [Pokemon(),Pokemon()]
background_theme = ["sound\\magmatheme.mp3","sound\\aquatheme.mp3","sound\\finaltheme.mp3"]
sleepturns = random.randint(1,5)
round = 0
disablity = 0
# p[0].isAsleep = True
# p[0].sleepFreezeCount = 2
# p[1].isAsleep = True
# p[1].sleepFreezeCount = 2

# p[0].isConfused = True
# p[1].isConfused = True
# p[0].confuseCount = 2
# p[1].confuseCount = 2

def second(remainingonbar):
	s = ttk.Style()
	s.theme_use('default')
	while(Pbar[1]["value"] > remainingonbar):
		Pbar[1]["value"] -= 1
		if Pbar[1]["value"] <= 37:
			s.configure("s.Horizontal.TProgressbar", foreground='red', background='red')
			Pbar[1].configure(style="s.Horizontal.TProgressbar")
		elif Pbar[1]["value"] <= 75:
			s.configure("s.Horizontal.TProgressbar",foreground='yellow', background='yellow')
			Pbar[1].configure(style="s.Horizontal.TProgressbar")
		else:
			s.configure("s.Horizontal.TProgressbar",foreground='green', background='green')
			Pbar[1].configure(style="s.Horizontal.TProgressbar")

		val = int(Pbar[1]["value"]*p[1].HP/Pbar[1]["maximum"])
		secondpokeHP.config(text = f"HP: {val}/{p[1].HP}")
		time.sleep(0.05)
	return val

def first(remainingonbar):
	s = ttk.Style()
	s.theme_use('default')
	while(Pbar[0]["value"] > remainingonbar):
		Pbar[0]["value"] -= 1
		if Pbar[0]["value"] <= 37:
			s.configure("f.Horizontal.TProgressbar", foreground='red', background='red')
			Pbar[0].configure(style="f.Horizontal.TProgressbar")
		elif Pbar[0]["value"] <= 75:
			s.configure("f.Horizontal.TProgressbar",foreground='yellow', background='yellow')
			Pbar[0].configure(style="f.Horizontal.TProgressbar")
		else:
			s.configure("f.Horizontal.TProgressbar",foreground='green', background='green')
			Pbar[0].configure(style="f.Horizontal.TProgressbar")

		val = int(Pbar[0]["value"]*p[0].HP/Pbar[0]["maximum"])
		firstpokeHP.config(text = f"HP: {val}/{p[0].HP}")
		time.sleep(0.05)
	return val

def updateHealth(i,remainingonbar,hp, bar,fullhp,deduct = 10,reason = ""):

	displaymsg = False
	if reason == "":
		playsound('sound\\normal.mp3')
	elif reason == "hurt itself in confusion!":
		playsound('sound\\normal.mp3')
		displaymsg = True
	elif reason == "is hurt by burn!":
		playsound('sound\\burn.mp3')
		displaymsg = True
	elif reason == "is hurt by poison!":
		playsound('sound\\poison.mp3')
		playsound('sound\\poison.mp3')
		displaymsg = True

	remainingonbar = int((hp - deduct)*bar["maximum"]/fullhp)
	if remainingonbar < 0:
		remainingonbar = 0
	if i == 0:
		hp = first(remainingonbar)
	else:
		hp = second(remainingonbar)

	if displaymsg == True:
		print(f"{p[i].name} {reason}")
	return hp
	

def startProgress(damageon,n):
	willmove = 0
	global round
	round += 1
	print(round)

	# remainingonbar[1] = int((p[1].hp - damageon2)*Pbar[1]["maximum"]/p[1].HP)
	# remainingonbar[0] = int((p[0].hp - damageon1)*Pbar[0]["maximum"]/p[0].HP)
	remainingonbar = [int((p[0].hp - damageon[0])*Pbar[0]["maximum"]/p[0].HP),int((p[1].hp - damageon[1])*Pbar[1]["maximum"]/p[1].HP)]

	#from here
	p[n].condition = checkCondition(p[n])
	#pokemon 1 attacks first
	if "move" in p[n].condition:
		# time.sleep(1)
		print(f"{p[n].name} used {p[n].move}")
		time.sleep(1)
		p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = damageon[(n+1)%2],reason = "")
		if p[(n+1)%2].hp == 0:
			#pokeom 2 fainted
			playsound("sound\\faint.mp3")
			print(f"{p[(n+1)%2].name} fainted!")
			return -1
		else:
			#pokemon 2 did not faint
			p[(n+1)%2].condition = checkCondition(p[(n+1)%2])
			if "move" in p[(n+1)%2].condition:
				willmove = 1
			elif "hurt-itself" in p[(n+1)%2].condition:
				willmove = -1
			else:
				pass
	elif "hurt-itself" in p[n].condition:
		time.sleep(2)
		p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = 10,reason = "hurt itself in confusion!")
		if p[n].hp == 0:
			#pokemon 1 fainted
			playsound("sound\\faint.mp3")
			print(f"{p[n].name} fainted!")
			return -2
		else:
			time.sleep(2)
			p[(n+1)%2].condition = checkCondition(p[(n+1)%2])
			if "move" in p[(n+1)%2].condition:
				willmove = 1
			elif "hurt-itself" in p[(n+1)%2].condition:
				willmove = -1
			else:
				pass
	elif "wont" in p[n].condition:
		time.sleep(2)
		p[(n+1)%2].condition = checkCondition(p[(n+1)%2])
		if "move" in p[(n+1)%2].condition:
			willmove = 1
		elif "hurt-itself" in p[(n+1)%2].condition:
			willmove = -1
		else:
			pass

	if willmove == 1:
		# time.sleep(1)
		print(f"{p[(n+1)%2].name} used {p[(n+1)%2].move}")
		time.sleep(1)
		p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = damageon[n],reason = "")
		if p[n].hp == 0:
			#pokemon 1 fainted
			playsound("sound\\faint.mp3")
			print(f"{p[n].name} fainted!")
			return -2
		else:
			pass
	elif willmove == -1:
		time.sleep(2)
		p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = 10,reason = "hurt itself in confusion!")
		if p[(n+1)%2].hp == 0:
			playsound("sound\\faint.mp3")
			print(f"{p[(n+1)%2].name} fainted!")
			return -1
		else:
			pass
	if "poison" in p[n].condition:
		time.sleep(2)
		p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = 10,reason = "is hurt by poison!")
		if p[n].hp == 0:
			#pokemon 1 fainted
			playsound("sound\\faint.mp3")
			print(f"{p[n].name} fainted!")
			return -2
		else:
			pass
	elif "burn" in p[n].condition:
		time.sleep(2)
		p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = 10,reason = "is hurt by burn!")
		if p[n].hp == 0:
			#pokemon 1 fainted
			playsound("sound\\faint.mp3")
			print(f"{p[n].name} fainted!")
			return -2
		else:
			pass
	if "poison" in p[(n+1)%2].condition:
		time.sleep(2)
		p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = 10,reason = "is hurt by poison!")
		if p[(n+1)%2].hp == 0:
			#pokemon 1 fainted
			playsound("sound\\faint.mp3")
			print(f"{p[(n+1)%2].name} fainted!")
			return -1
		else:
			pass
	elif "burn" in p[(n+1)%2].condition:
		time.sleep(2)
		p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = 10,reason = "is hurt by burn!")
		if p[(n+1)%2].hp == 0:
			#pokemon 1 fainted
			playsound("sound\\faint.mp3")
			print(f"{p[(n+1)%2].name} fainted!")
			return -1
		else:
			pass
	return 0



def start_fight_thread(event):
    startButton.config(state = tk.DISABLED)
    global fight_thread
    fight_thread = threading.Thread(target = fight) #args = (Pbar[0],Pbar[1],var1,var2))
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
	p[0].isParalysed = True
	p[1].isParalysed = True
	# p[0].isPoisoned = True
	# p[1].isPoisoned = True
	# p[0].isBurnt = True
	# p[1].isBurnt = True
	
	
	# check speed to decide who'll go first
	if p[0].speed > p[1].speed:
		n = 0
	else:
		n = 1
	disablity = startProgress((damageon1,damageon2),n)
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
	# w2.PlaySound('poke_music.wav', w2.SND_ASYNC | w2.SND_NOSTOP)
	file = random.choice(background_theme)
	playsound(file,False)

	root = tk.Tk()
	root.title("Pokemon Battle")
	pg = PokeGUI(root)

	firstpokeLabel = pg.createLabel(pg.firstleft,text_ = p[0].name)
	firstImg = pg.createImage(file_ = f"poke_png\\{p[0].rank} {p[0].name}.png",canvas = pg.firstleft,row_ = 1,col_ = 0)

	secondpokeLabel = pg.createLabel(pg.firstright,text_ = p[1].name)
	secondImg = pg.createImage(file_ = f"poke_png\\{p[1].rank} {p[1].name}.png",canvas = pg.firstright,row_ = 1,col_ = 0)

	firstpokeHP = pg.createLabel(pg.secondleft,text_= f"HP: {p[0].HP}/{p[0].HP}",row_ = 0,col_ = 0)
	# Pbar[0] = pg.createProgress(pg.secondleft)
	secondpokeHP = pg.createLabel(pg.secondright,text_= f"HP: {p[1].HP}/{p[1].HP}",row_ = 0,col_ = 0)
	Pbar = [pg.createProgress(pg.secondleft),pg.createProgress(pg.secondright)]
	# Pbar[1] = pg.createProgress(pg.secondright)

	firstMoveLabel = pg.createLabel(pg.thirdleft,text_ = "Moves",row_ = 0,col_ = 0)
	firstmoves = p[0].getMoves()[0]
	firstdesc = p[0].getMoves()[1]
	firstRadio = []
	var1 = tk.IntVar()
	firstRadio1 = pg.createRadioButton(pg.thirdleft,text_ = firstmoves[0],variable_ = var1,value_ = 0,row_ = 1,col_ = 0)
	firstRadio2 = pg.createRadioButton(pg.thirdleft,text_ = firstmoves[1],variable_ = var1,value_ = 1,row_ = 2,col_ = 0)
	firstRadio3 = pg.createRadioButton(pg.thirdleft,text_ = firstmoves[2],variable_ = var1,value_ = 2,row_ = 3,col_ = 0)
	firstRadio4 = pg.createRadioButton(pg.thirdleft,text_ = firstmoves[3],variable_ = var1,value_ = 3,row_ = 4,col_ = 0)


	secondMoveLabel = pg.createLabel(pg.thirdright,text_ = "Moves",row_ = 0,col_ = 0)
	secondmoves = p[1].getMoves()[0]
	seconddesc = p[1].getMoves()[1]
	secondRadio = []
	var2 = tk.IntVar()
	secondRadio1 = pg.createRadioButton(pg.thirdright,text_ = secondmoves[0],variable_ = var2,value_ = 0,row_ = 1,col_ = 0)
	secondRadio2 = pg.createRadioButton(pg.thirdright,text_ = secondmoves[1],variable_ = var2,value_ = 1,row_ = 2,col_ = 0)
	secondRadio3 = pg.createRadioButton(pg.thirdright,text_ = secondmoves[2],variable_ = var2,value_ = 2,row_ = 3,col_ = 0)
	secondRadio4 = pg.createRadioButton(pg.thirdright,text_ = secondmoves[3],variable_ = var2,value_ = 3,row_ = 4,col_ = 0)

	
	startButton = pg.createButton(pg.bottom,text_ = "GO",command_ = lambda: start_fight_thread(None))

	remarkLabel = pg.createLabel(pg.remark,row_ = 0,col_ = 0,padx_ = 2,pady_ = 2,text_ = "Label-Text",font_ = ("Calibri 12"))

	root.mainloop()
