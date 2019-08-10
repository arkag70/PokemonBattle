from gui_class import *
from pokemon import *
from battle import *
import winsound
import threading

p = [Pokemon(),Pokemon()]
background_theme = ["sound\\magmatheme.wav","sound\\aquatheme.wav","sound\\finaltheme.wav","sound\\rayquaza.wav"]
moveset = pd.read_excel("moves.xlsx",sheet_name = "sheet1")
round = 0
disablity = 0
# # p[0].isFrozen = True
# # p[0].sleepFreezeCount = 3
# # p[1].isFrozen = True
# p[1].sleepFreezeCount = 3

# p[0].isConfused = True
# p[1].isConfused = True
# p[0].confuseCount = 2
# p[1].confuseCount = 2

def second(remainingonbar,f):
	s = ttk.Style()
	s.theme_use('default')
	while(True):
		Pbar[1]["value"] -= f
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

		if f == 1:
			if Pbar[1]["value"] < remainingonbar + 1:
				break
		elif f == -1:
			if Pbar[1]["value"] > remainingonbar - 1:
				break
	return val

def first(remainingonbar,f):
	s = ttk.Style()
	s.theme_use('default')
	while(True):
		Pbar[0]["value"] -= f
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

		if f == 1:
			if Pbar[0]["value"] < remainingonbar + 1:
				break
		elif f == -1:
			if Pbar[0]["value"] > remainingonbar - 1:
				break
	return val

def updateHealth(i,remainingonbar,hp, bar,fullhp,deduct = 10,reason = ""):
	f = 1
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
	elif "LEECH SEED" in reason:
		playsound("sound\\seed1.mp3")
		playsound("sound\\seed2.mp3")
		displaymsg = True
		f = 1
	elif "gained HP" in reason:
		playsound("sound\\seed3.mp3")
		f = -1
	if displaymsg == True:
		print(f"{p[i].name} {reason}")

	remainingonbar = int((hp - deduct)*bar["maximum"]/fullhp)
	if remainingonbar < 0:
		remainingonbar = 0
	if i == 0:
		hp = first(remainingonbar,f)
	else:
		hp = second(remainingonbar,f)

	return hp
	
def checkStatus(p,n):
	#raise\lowe attack defense speed normally or harshly or sharply
	pass


def startProgress(damageon,accuracy,n):
	willmove = 0
	global round
	round += 1
	print(round)

	# remainingonbar[1] = int((p[1].hp - damageon2)*Pbar[1]["maximum"]/p[1].HP)
	# remainingonbar[0] = int((p[0].hp - damageon1)*Pbar[0]["maximum"]/p[0].HP)
	remainingonbar = [int((p[n].hp - damageon[n])*Pbar[n]["maximum"]/p[n].HP),int((p[(n+1)%2].hp - damageon[(n+1)%2])*Pbar[(n+1)%2]["maximum"]/p[(n+1)%2].HP)]

	#from here
	p[n].condition = checkCondition(p[n])
	#pokemon 1 attacks first
	if "move" in p[n].condition:
		# time.sleep(1)
		if random.randint(1,100) < accuracy[n]:
			if damageon[(n+1)%2] != 0:
				print(f"{p[n].name} used {p[n].move}")
				time.sleep(1)
				p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = damageon[(n+1)%2],reason = "")
				checkStatus(p,n)
			else:
				#check stats update from moves.xlsx	
				checkStatus(p,n)
		else:
			print(f"{p[n].name}'s attack missed!")
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
		if random.randint(1,100) < accuracy[(n+1)%2]:
			if damageon[n] != 0:
				print(f"{p[(n+1)%2].name} used {p[(n+1)%2].move}")
				time.sleep(1)
				p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = damageon[n],reason = "")
				checkStatus(p,n)
			else:
				checkStatus(p,n)
		else:
			print(f"{p[(n+1)%2].name}'s attack missed!")
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
	if "seed" in p[n].condition:
		time.sleep(2)
		p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = 10,reason = "health is sapped by LEECH SEED!")
		p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = -10,reason = "gained HP!")
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
	if "seed" in p[(n+1)%2].condition:
		time.sleep(2)
		p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = 10,reason = "health is sapped by LEECH SEED!")
		p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = -10,reason = "gained HP!")
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
	index1 = var1.get()
	index2 = var2.get()
	p[0].move = firstmoves[index1]
	p[1].move = secondmoves[index2]
	print(firstmoves[index1],firstdesc[index1])
	print(secondmoves[index2],seconddesc[index2])
	
	movepower1 = int(firstdesc[index1][0])
	movepower2 = int(seconddesc[index2][0])
	accuracy = [int(firstdesc[index1][1]),int(seconddesc[index2][1])]

	print(movepower1,movepower2)
	maxA = p[0].maxAttack
	maxD = p[0].maxDefense
	effectiveness1 = 1
	effectiveness2 = 1


	#	damage on opponent = move-power * (normalize(self Attack) + (1 - normalize(opponent defense)))
	damageon = [0,0]
	damageon[0] = int(((p[1].attack/maxA)+(1-(p[0].defense/maxD)))*0.1*movepower2)*effectiveness1
	damageon[1] = int(((p[0].attack/maxD)+(1-(p[1].defense/maxD)))*0.1*movepower1)*effectiveness2

	print(damageon[0],damageon[1])
	# # p[0].isParalysed = True
	# # p[1].isParalysed = True
	# # p[0].isPoisoned = True
	# # p[1].isPoisoned = True
	# # p[0].isBurnt = True
	# # p[1].isBurnt = True
	# # p[0].isSeeded = True
	# # p[1].isSeeded = True
	
	
	# check speed to decide who'll go first
	if p[0].speed > p[1].speed:
		n = 0
	else:
		n = 1
	disablity = startProgress(damageon,accuracy,n)
	


'''
createLabel(canvas,row_ = 0,col_ = 0,padx_ = 2,pady_ = 2,text_ = "Label-Text",font_ = ("Calibri 12"))
createEntry(canvas,row_ = 0,col_ = 0,padx = 2,pady = 2,width_ = 50,bd_ = 2)
createButton(canvas,command_,text_ = "Button-Text",width_ = 5,bd_ = 2,font_ = ("Calibri 12"),row_ = 0,col_ = 0,padx = 2,pady = 2)
createRadioButton(canvas,text_ = "radio-item",variable_ = var,value_ = 1,row_ = 0, col_ = 0)
createImage(file_,canvas,row_ = 0,col_ = 0)
(orient_="horizontal",length_=200, mode_="determinate",row_ = 0, col_ = 1)
'''
if __name__ == "__main__":
	
	file = random.choice(background_theme)
	winsound.PlaySound(file, winsound.SND_ASYNC | winsound.SND_NOSTOP | winsound.SND_LOOP)

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
	moves = p[0].getMoves()
	firstmoves = [m.split(',')[0] for m in moves]
	firstdesc = [m.split(',')[1:] for m in moves]
	firstRadio = []
	var1 = tk.IntVar()
	firstRadio1 = pg.createRadioButton(pg.thirdleft,text_ = firstmoves[0],variable_ = var1,value_ = 0,row_ = 1,col_ = 0)
	firstRadio2 = pg.createRadioButton(pg.thirdleft,text_ = firstmoves[1],variable_ = var1,value_ = 1,row_ = 2,col_ = 0)
	firstRadio3 = pg.createRadioButton(pg.thirdleft,text_ = firstmoves[2],variable_ = var1,value_ = 2,row_ = 3,col_ = 0)
	firstRadio4 = pg.createRadioButton(pg.thirdleft,text_ = firstmoves[3],variable_ = var1,value_ = 3,row_ = 4,col_ = 0)


	secondMoveLabel = pg.createLabel(pg.thirdright,text_ = "Moves",row_ = 0,col_ = 0)
	moves = p[1].getMoves()
	secondmoves = [m.split(',')[0] for m in moves]
	seconddesc = [m.split(',')[1:] for m in moves]
	secondRadio = []
	var2 = tk.IntVar()
	secondRadio1 = pg.createRadioButton(pg.thirdright,text_ = secondmoves[0],variable_ = var2,value_ = 0,row_ = 1,col_ = 0)
	secondRadio2 = pg.createRadioButton(pg.thirdright,text_ = secondmoves[1],variable_ = var2,value_ = 1,row_ = 2,col_ = 0)
	secondRadio3 = pg.createRadioButton(pg.thirdright,text_ = secondmoves[2],variable_ = var2,value_ = 2,row_ = 3,col_ = 0)
	secondRadio4 = pg.createRadioButton(pg.thirdright,text_ = secondmoves[3],variable_ = var2,value_ = 3,row_ = 4,col_ = 0)

	
	startButton = pg.createButton(pg.bottom,text_ = "GO",command_ = lambda: start_fight_thread(None))

	# remarkLabel = pg.createLabel(pg.remark,row_ = 0,col_ = 0,padx_ = 2,pady_ = 2,text_ = "Label-Text",font_ = ("Calibri 12"))

	root.mainloop()
