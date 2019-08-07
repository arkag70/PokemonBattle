from gui_class import *
from pokemon import *
import threading


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
	will1attack = False
	will2attack = False
	# if p1.isAsleep:
	# 	sleepturns -= 1
	# 	if sleepturns <= 0:
	# 		p1.isAsleep = False
	# 		print(f"{p1.name} woke up!")

	global round
	round += 1
	print(round)
	global hp1,hp2
	global startButton

	if n == 1:
		# first pokemon attacks first due to speed stat so effect on second pokemon
		if p1.isAsleep:
			print(f"{p1.name} is fast asleep!")
		elif p1.isFrozen:
			print(f"{p1.name} is frozen solid!")
		else:
			if p1.isParalysed:
				#check when it fails to move
				if random.randint(0,10) % 2 != 0:
					print(f"{p1.name} is paralysed! It can't move")
				else:
					#it can move
					#check for confusion
					if p1.isConfused:
						#it hurts itself
						if random.randint(0,10) % 2 != 0:
							print(f"{p1.name} is confused!")
							remaining1onbar = int((hp1-10)*firstPbar["maximum"]/fullhp1)
							if remaining1onbar < 0:
								remaining1onbar = 0
							time.sleep(1)
							hp1 = first(remaining1onbar)
							print("It hurt itself in confusion")
							if hp1 == 0:
								print(f"{p2.name} wins the round")
								return -2
							else:
								pass

						else:
							#it will attack
							print(f"{p1.name} is confused!")
							will1attack = True
					else:
						#not confused it will attack
						will1attack = True
			
			#not paralysed check for confusion
			elif p1.isConfused:
				#it hurts itself
				if random.randint(0,10) % 2 != 0:
					print(f"{p1.name} is confused!")
					remaining1onbar = int((hp1-10)*firstPbar["maximum"]/fullhp1)
					if remaining1onbar < 0:
						remaining1onbar = 0
					time.sleep(1)
					hp1 = first(remaining1onbar)
					print("It hurt itself in confusion")
					if hp1 == 0:
						print(f"{p2.name} wins the round")
						return -2
					else:
						pass

				else:
					#it will attack
					print(f"{p1.name} is confused!")
					time.sleep(1)
					will1attack = True
			else:
				#not confused it will attack
				will1attack = True

		if will1attack == True:
			remaining2onbar = int((hp2-damageon2)*secondPbar["maximum"]/fullhp2)
			time.sleep(1)
			print(f"{p1.name} used move")
			time.sleep(1)
			if remaining2onbar < 0:
				remaining2onbar = 0
			hp2 = second(remaining2onbar)

		if hp2 != 0:
			time.sleep(2)
			if p2.isAsleep:
				print(f"{p2.name} is fast asleep!")
			elif p2.isFrozen:
				print(f"{p2.name} is frozen solid!")
			else:
				if p2.isParalysed:
					#check when it fails to move
					if random.randint(0,10) % 2 != 0:
						#paralysed can't move
						print(f"{p2.name} is paralysed! It can't move")
					else:
						#paralysed but can move; check for confusion
						if p2.isConfused:
							print(f"{p2.name} is confused!")
							#it hurts itself
							if random.randint(0,10) % 2 != 0:
								remaining2onbar = int((hp2-10)*secondPbar["maximum"]/fullhp2)
								if remaining2onbar < 0:
									remaining2onbar = 0
								time.sleep(1)
								hp2 = second(remaining2onbar)
								print("It hurt itself in confusion")
								if hp2 == 0:
									print(f"{p1.name} wins the round")
									return -1
								else:
									pass

							else:
								#it will attack
								will2attack = True
						else:
							#not confused it will attack
							will2attack = True
				#not paralysed check for confusion
				elif p2.isConfused:
					#it hurts itself
					if random.randint(0,10) % 2 != 0:
						print(f"{p2.name} is confused!")
						remaining2onbar = int((hp2-10)*secondPbar["maximum"]/fullhp2)
						if remaining2onbar < 0:
							remaining2onbar = 0
						time.sleep(1)
						hp2 = second(remaining2onbar)
						print("It hurt itself in confusion")
						if hp2 == 0:
							print(f"{p1.name} wins the round")
							return -1
						else:
							pass
					else:
						#it will attack
						print(f"{p2.name} is confused!")
						time.sleep(1)
						will2attack = True
				else:
					#not confused it will attack
					will2attack = True


			if will2attack == True:
				remaining1onbar = int((hp1-damageon1)*firstPbar["maximum"]/fullhp1)
				time.sleep(1)
				print(f"{p2.name} used move")
				time.sleep(1)
				if remaining1onbar < 0:
					remaining1onbar = 0
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
		if p2.isAsleep:
			print(f"{p2.name} is fast asleep!")
		elif p2.isFrozen:
			print(f"{p2.name} is frozen solid!")
		else:
			if p2.isParalysed:
				#check when it fails to move
				if random.randint(0,10) % 2 != 0:
					print(f"{p2.name} is paralysed! It can't move")
				else:
					#it can move
					#check for confusion
					if p2.isConfused:
						#it hurts itself
						if random.randint(0,10) % 2 != 0:
							print(f"{p2.name} is confused!")
							remaining2onbar = int((hp2-10)*secondPbar["maximum"]/fullhp2)
							if remaining2onbar < 0:
								remaining2onbar = 0
							time.sleep(1)
							hp2 = second(remaining2onbar)
							print("It hurt itself in confusion")
							if hp2 == 0:
								print(f"{p1.name} wins the round")
								return -1
							else:
								pass

						else:
							#it will attack
							print(f"{p2.name} is confused!")
							will2attack = True
					else:
						#not confused it will attack
						will2attack = True
			
			#not paralysed check for confusion
			elif p2.isConfused:
				#it hurts itself
				if random.randint(0,10) % 2 != 0:
					print(f"{p2.name} is confused!")
					remaining2onbar = int((hp2-10)*secondPbar["maximum"]/fullhp2)
					if remaining2onbar < 0:
						remaining2onbar = 0
					time.sleep(1)
					hp2 = second(remaining2onbar)
					print("It hurt itself in confusion")
					if hp2 == 0:
						print(f"{p1.name} wins the round")
						return -1
					else:
						pass

				else:
					#it will attack
					print(f"{p2.name} is confused!")
					time.sleep(1)
					will2attack = True
			else:
				#not confused it will attack
				will2attack = True

		if will2attack == True:
			remaining1onbar = int((hp1-damageon1)*firstPbar["maximum"]/fullhp1)
			time.sleep(1)
			print(f"{p2.name} used move")
			time.sleep(1)
			if remaining1onbar < 0:
				remaining1onbar = 0
			hp1 = first(remaining1onbar)

		if hp1 != 0:
			time.sleep(2)
			if p1.isAsleep:
				print(f"{p1.name} is fast asleep!")
			elif p1.isFrozen:
				print(f"{p1.name} is frozen solid!")
			else:
				if p1.isParalysed:
					#check when it fails to move
					if random.randint(0,10) % 2 != 0:
						#paralysed can't move
						print(f"{p1.name} is paralysed! It can't move")
					else:
						#paralysed but can move; check for confusion
						if p1.isConfused:
							print(f"{p1.name} is confused!")
							#it hurts itself
							if random.randint(0,10) % 2 != 0:
								remaining1onbar = int((hp1-10)*firstPbar["maximum"]/fullhp1)
								if remaining1onbar < 0:
									remaining1onbar = 0
								time.sleep(1)
								hp1 = first(remaining1onbar)
								print("It hurt itself in confusion")
								if hp1 == 0:
									print(f"{p2.name} wins the round")
									return -2
								else:
									pass

							else:
								#it will attack
								will1attack = True
						else:
							#not confused it will attack
							will1attack = True
				#not paralysed check for confusion
				elif p1.isConfused:
					#it hurts itself
					if random.randint(0,10) % 2 != 0:
						print(f"{p1.name} is confused!")
						remaining1onbar = int((hp1-10)*firstPbar["maximum"]/fullhp1)
						if remaining1onbar < 0:
							remaining1onbar = 0
						time.sleep(1)
						hp1 = first(remaining1onbar)
						print("It hurt itself in confusion")
						if hp1 == 0:
							print(f"{p2.name} wins the round")
							return -2
						else:
							pass
					else:
						#it will attack
						print(f"{p1.name} is confused!")
						time.sleep(1)
						will1attack = True
				else:
					#not confused it will attack
					will1attack = True


			if will1attack == True:
				remaining2onbar = int((hp2-damageon2)*secondPbar["maximum"]/fullhp2)
				time.sleep(1)
				print(f"{p1.name} used move")
				time.sleep(1)
				if remaining2onbar < 0:
					remaining2onbar = 0
				hp2 = second(remaining2onbar)

			if hp2 == 0:
				print(f"{p1.name} wins the round")
				return -1
			else:
				pass
		else:
			print(f"{p2.name} wins the match")
			return -2
	#check poisoned or burnt
	time.sleep(2)
	if p1.isPoisoned or p1.isBurnt:
		remaining1onbar = int((hp1-10)*firstPbar["maximum"]/fullhp1)
		if remaining1onbar < 0:
			remaining1onbar = 0
		time.sleep(1)
		hp1 = first(remaining1onbar)
		if p1.isPoisoned:
			print(f"{p1.name} is hurt by poison")
		else:
			print(f"{p1.name} is hurt by burn")

		if hp1 == 0:
			print(f"{p2.name} wins the round")
			return -2
		else:
			pass
	if p2.isPoisoned or p2.isBurnt:
		remaining2onbar = int((hp2-10)*secondPbar["maximum"]/fullhp2)
		if remaining2onbar < 0:
			remaining2onbar = 0
		time.sleep(1)
		hp2 = second(remaining2onbar)
		if p2.isPoisoned:
			print(f"{p2.name} is hurt by poison")
		else:
			print(f"{p2.name} is hurt by burn")

		if hp2 == 0:
			print(f"{p1.name} wins the round")
			return -1
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
	# p1.isPoisoned = True
	# p2.isPoisoned = True
	p1.isBurnt = True
	p2.isBurnt = True
	# p1.isFrozen = True
	# p2.isFrozen = True
	
	# check speed to decide who'll go first
	if p1.HP > p2.HP:
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
