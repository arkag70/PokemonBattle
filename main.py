from gui_class import *
from pokemon import *
import threading
from functions import *
from battle import *
import winsound as w


powerful = [0,1,2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7]
pauseTimer = True
stopTimer = False
toxic_count = 1
minutes = 5
seconds = 0
Score = [0,0]
change = 0
ice_ball = 0
roll_out = 0
fury_cutter = 1
basepow = [30,30,10]
hit_count = ["once","twice","three times","four times","five times"]
p = [Pokemon(random.randint(0,7)),Pokemon(random.randint(0,7))]
background_theme = ["sound\\magmatheme.wav","sound\\aquatheme.wav","sound\\finaltheme.wav","sound\\rayquaza.wav"]
moveset = pd.read_excel("moves.xlsx",sheet_name = "sheet1")
round = 0
disablity = 0

def display(text):
	remarkBox.insert(tk.END,text)
	remarkBox.yview(tk.END)

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

def updateHealth(i,remainingonbar,hp, bar,fullhp,deduct = 10,reason = "",effect = 1):
	f = 1
	displaymsg = False
	if reason == "":
		if effect >= 1 and effect <= 1.25:
			display(f"normal damage")
			playsound('sound\\normal.wav')
		elif effect < 1:
			display(f"not very effective damage")
			playsound('sound\\notvery.wav')
		elif effect > 1.25:
			display(f"super effective damage")
			playsound('sound\\super.wav')
			

	elif reason == "hurt itself in confusion!":
		playsound('sound\\normal.wav')
		displaymsg = True
	elif "recoil" in reason:
		playsound('sound\\normal.wav')
		displaymsg = True
	elif reason == "is hurt by burn!":
		playsound('sound\\burn.wav')
		displaymsg = True
	elif reason == "is hurt by poison!":
		playsound('sound\\poison.wav')
		displaymsg = True
	elif "LEECH SEED" in reason:
		playsound("sound\\seed1.wav")
		playsound("sound\\seed2.wav")
		displaymsg = True
		f = 1
	elif deduct < 0:
		playsound("sound\\seed3.wav")
		displaymsg = True
		f = -1
	if displaymsg == True:
		display(f"{p[i].name} {reason}")
	remainingonbar = int((hp - deduct)*bar["maximum"]/fullhp)
	if remainingonbar < 0:
		remainingonbar = 0
	elif remainingonbar > bar["maximum"]:
		remainingonbar = bar["maximum"]
	if i == 0:
		hp = first(remainingonbar,f)
	else:
		hp = second(remainingonbar,f)
	
	return hp
	
def checkStatus(p,n,index):
	#raise\lower attack defense speed normally or harshly or sharply
	move_name = p[n].move
	status = str(moveset[moveset['movename'] == move_name]["status"]).split()[1]
	stats = str(moveset[moveset['movename'] == move_name]["stats"]).split()[1]
	stats = stats.split(",")
	#stats related code
	if n == 0:
		power = int(firstdesc[index[n]][0])
	else:
		power = int(seconddesc[index[n]][0])

	if power == 0 or move_name in ["Overheat","Psycho Boost"]:
		if len(stats) == 1:
			display(applyStats(p,n,float(stats[0])))
		else:
			display(applyStats(p,n,float(stats[0])))
			display(applyStats(p,n,float(stats[1])))
	
	
	elif power > 0:
		if random.randint(1,11) <= 3:
			if len(stats) == 1:
				display(applyStats(p,n,float(stats[0])))
			else:
				display(applyStats(p,n,float(stats[0])))
				display(applyStats(p,n,float(stats[1])))
	
	
	#status related code
	if power == 0 or move_name in ['Outrage']:
		display(applyStatus(p,n,float(status)))
	else:
		if random.randint(1,11) < 3:
			display(applyStatus(p,n,float(status)))
	
	
def critical_hit(crit_factor):
	
	if random.randint(1,crit_factor) == 5:
		display("It's a critical hit!")
		return 1.5
	else:
		return 1.0
	


def startProgress(damageon,accuracy,n,index,effectiveness):
	willmove = 0
	global round,toxic_count
	round += 1
	display(f"Round {round}")
	remainingonbar = [int((p[n].hp - damageon[n])*Pbar[n]["maximum"]/p[n].HP),int((p[(n+1)%2].hp - damageon[(n+1)%2])*Pbar[(n+1)%2]["maximum"]/p[(n+1)%2].HP)]

	
	v,p[n].condition = checkCondition(p[n])
	display(v)
	
	if "move" in p[n].condition:
		health = int(str(moveset[moveset['movename'] == p[n].move]["health"]).split()[1])
		crit_factor = int(str(moveset[moveset['movename'] == p[n].move]["critical"]).split()[1])
		display(f"{p[n].name} used {p[n].move}")
		#check if it effects opponent
		if effectiveness[n] == 0:
			time.sleep(1)
			display(f"It doesn't effect {p[(n+1)%2].name}")
		else:
			#It effects and now check accuracy
			time.sleep(1)
			if random.randint(1,100) > accuracy[n]:
				#miss
				display(f"{p[n].name}'s attack missed!")
			else:
				#hit
				if damageon[(n+1)%2] == 0:
					if health == -50:
						if p[n].bellyDrum_Memento == False and p[n].hp > p[n].HP/2:
							p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = p[n].HP/2,reason = "",effect = 1)
							if p[n].hp <= 0:
								playsound("sound\\faint.wav")
								display(f"{p[n].name} fainted!")
								return -1*((n+1)%2 + 1)
							elif p[n].move == "Belly Drum":
								p[n].attack *= 4
								display(f"{p[n].name} maximized its attacks!")
								playsound("sound\\rise.wav")
							elif p[n].move == "Memento":
								p[(n+1)%2].attack *= 0.25
								display(f"{p[n].name} sharply lowered {p[(n+1)%2].name}'s attack!")
								playsound("sound\\fall.wav")
							p[n].bellyDrum_Memento = True
						else:
							display("But it Failed!")
					elif health == 50:
						p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = -1.0 * p[n].HP/2,reason = "regained health",effect = 1)
				else:
					#get type of hit (gain,recoil,hits)
					if health == 1000:
						crit = critical_hit(crit_factor)
						#tackle
						if p[n].move == "Magnitude":
							value = random.randint(1,10)
							p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = crit * value * damageon[(n+1)%2],reason = "",effect = effectiveness[n])
							display(f"Magnitude {value}")
						else:
							p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = crit * damageon[(n+1)%2],reason = "",effect = effectiveness[n])
					
					elif int(health/1000) >= 2:
						#multi hit moves - double or 2-5 times
						for i in range(random.randint(2,int(health/1000))):
							crit = critical_hit(crit_factor)
							p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = crit * damageon[(n+1)%2],reason = "",effect = effectiveness[n])

							if p[(n+1)%2].hp <= 0:
								#pokemon 2 fainted
								display(f"Hit {hit_count[i]}!")
								playsound("sound\\faint.wav")
								display(f"{p[(n+1)%2].name} fainted!")
								return -1*(n+1)
						#after loop
						display(f"Hit {hit_count[i]}!")

					elif health == 1100:
						#recoil
						crit = critical_hit(crit_factor)
						p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = crit * damageon[(n+1)%2],reason = "",effect = effectiveness[n])
						p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = crit * damageon[(n+1)%2] / 2,reason = "is hit with recoil!",effect = 1)
						if p[n].hp <= 0:
							#pokeom 1 fainted
							playsound("sound\\faint.wav")
							display(f"{p[n].name} fainted!")
							return -1*((n+1)%2 + 1)				
						

					elif health == 1010:
						#gain type
						crit = critical_hit(crit_factor)
						p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = crit * damageon[(n+1)%2],reason = "",effect = effectiveness[n])
						p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = -1.0 * crit * damageon[(n+1)%2] / 2,reason = "gained foe's energy!",effect = 1)	

					elif health == 1001:
						#gift type
						p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = -1.0 * damageon[(n+1)%2],reason = "gifted health to foe",effect = 1)
				
				checkStatus(p,n,index)

		if p[(n+1)%2].hp <= 0:
			#pokeom 2 fainted
			playsound("sound\\faint.wav")
			display(f"{p[(n+1)%2].name} fainted!")
			return -1*(n+1)
		else:
			#pokemon 2 did not faint
			v,p[(n+1)%2].condition = checkCondition(p[(n+1)%2])
			display(v)
			if "move" in p[(n+1)%2].condition:
				willmove = 1
			elif "hurt-itself" in p[(n+1)%2].condition:
				willmove = -1
			else:
				pass
	elif "hurt-itself" in p[n].condition:
		time.sleep(2)
		p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = 10,reason = "hurt itself in confusion!",effect = 1)
		if p[n].hp <= 0:
			#pokemon 1 fainted
			playsound("sound\\faint.wav")
			display(f"{p[n].name} fainted!")
			return -1*((n+1)%2 + 1)
		else:
			time.sleep(2)
			v,p[(n+1)%2].condition = checkCondition(p[(n+1)%2])
			display(v)
			if "move" in p[(n+1)%2].condition:
				willmove = 1
			elif "hurt-itself" in p[(n+1)%2].condition:
				willmove = -1
			else:
				pass
	elif "wont" in p[n].condition:
		time.sleep(2)
		v,p[(n+1)%2].condition = checkCondition(p[(n+1)%2])
		display(v)
		if "move" in p[(n+1)%2].condition:
			willmove = 1
		elif "hurt-itself" in p[(n+1)%2].condition:
			willmove = -1
		else:
			pass

	if willmove == 1:
		time.sleep(1)
		health = int(str(moveset[moveset['movename'] == p[(n+1)%2].move]["health"]).split()[1])
		crit_factor = int(str(moveset[moveset['movename'] == p[(n+1)%2].move]["critical"]).split()[1])
		display(f"{p[(n+1)%2].name} used {p[(n+1)%2].move}")
		#check if it effects opponent
		if effectiveness[(n+1)%2] == 0:
			time.sleep(1)
			display(f"It doesn't effect {p[n].name}")
		else:
			#It effects and now check accuracy
			time.sleep(1)
			if random.randint(1,100) > accuracy[(n+1)%2]:
				#miss
				display(f"{p[(n+1)%2].name}'s attack missed!")
			else:
				#hit
				if damageon[n] == 0:
					# zero powered move : ingrain, leech seed, recover, flail
					if health == -50:
						if p[(n+1)%2].bellyDrum_Memento == False and p[(n+1)%2].hp > p[(n+1)%2].HP/2:
							p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = p[(n+1)%2].HP/2,reason = "",effect = 1)
							if p[(n+1)%2].hp <= 0:
								playsound("sound\\faint.wav")
								display(f"{p[(n+1)%2].name} fainted!")
								return -1*(n+1)						
							elif p[(n+1)%2].move == "Belly Drum":
								p[(n+1)%2].attack *= 4
								display(f"{p[(n+1)%2].name} maximized its attack!")
								playsound("sound\\rise.wav")
							elif p[(n+1)%2].move == "Memento":
								p[n].attack *= 0.25
								display(f"{p[(n+1)%2].name} sharply lowered {p[n].name}'s attack!")
								playsound("sound\\fall.wav")
							p[(n+1)%2].bellyDrum_Memento == True
						else:
							display("But it Failed!")
					elif health == 50:
						p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = -1.0 * p[(n+1)%2].HP/2,reason = "regained health",effect = 1)
				else:
					#get type of hit (gain,recoil,hits)
					
					if health == 1000:
						crit = critical_hit(crit_factor)
						#tackle
						if p[(n+1)%2].move == "Magnitude":
							value = random.randint(1,10)
							p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = crit * value * damageon[n],reason = "",effect = effectiveness[(n+1)%2])
							display(f"Magnitude {value}")
						else:
							p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = crit * damageon[n],reason = "",effect = effectiveness[(n+1)%2])
					
					elif int(health/1000) >= 2:
						#multi hit moves - double or 2-5 times
						for i in range(random.randint(2,int(health/1000))):
							crit = critical_hit(crit_factor)
							p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = crit * damageon[n],reason = "",effect = effectiveness[(n+1)%2])
							if p[n].hp <= 0:
								#pokemon 2 fainted
								display(f"Hit {hit_count[i]}!")
								playsound("sound\\faint.wav")
								display(f"{p[n].name} fainted!")
								return -1*((n+1)%2 +1)
						#after loop
						display(f"Hit {hit_count[i]}!")

					elif health == 1100:
						#recoil
						crit = critical_hit(crit_factor)
						p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = crit * damageon[n],reason = "",effect = effectiveness[(n+1)%2])
						p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = crit * damageon[n] / 2,reason = "is hit with recoil!",effect = 1)
						if p[(n+1)%2].hp <= 0:
							#pokeom 2 fainted
							playsound("sound\\faint.wav")
							display(f"{p[(n+1)%2].name} fainted!")
							return -1*(n + 1)
							
					elif health == 1010:
						#gain type
						crit = critical_hit(crit_factor)
						p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = crit * damageon[n],reason = "",effect = effectiveness[(n+1)%2])
						p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = -1.0 * crit * damageon[n] / 2,reason = "gained foe's energy!",effect = 1)
					elif health == 1001:
						#gift type
						p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = -1.0 * damageon[n],reason = "gifted health to foe",effect = 1)
				
				checkStatus(p,(n+1)%2,index)

		if p[n].hp <= 0:
			#pokemon 1 fainted
			playsound("sound\\faint.wav")
			display(f"{p[n].name} fainted!")
			return -1*((n+1)%2 + 1)
		else:
			pass
	elif willmove == -1:
		time.sleep(2)
		p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = 10,reason = "hurt itself in confusion!",effect = 1)
		if p[(n+1)%2].hp <= 0:
			playsound("sound\\faint.wav")
			display(f"{p[(n+1)%2].name} fainted!")
			return -1*(n+1)
		else:
			pass
	if "poison" in p[n].condition:
		time.sleep(2)
		p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = int(0.125*p[n].HP),reason = "is hurt by poison!",effect = 1)
		if p[n].hp <= 0:
			#pokemon 1 fainted
			playsound("sound\\faint.wav")
			display(f"{p[n].name} fainted!")
			return -1*((n+1)%2 + 1)
		else:
			pass
	elif "toxic" in p[n].condition:
		time.sleep(2)
		p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = int(toxic_count*0.125*p[n].HP),reason = "is hurt by poison!",effect = 1)
		if p[n].hp <= 0:
			#pokemon 1 fainted
			playsound("sound\\faint.wav")
			display(f"{p[n].name} fainted!")
			toxic_count = 1
			return -1*((n+1)%2 + 1)
		else:
			toxic_count *= 2
	elif "burn" in p[n].condition:
		time.sleep(2)
		p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = int(0.125*p[n].HP),reason = "is hurt by burn!",effect = 1)
		if p[n].hp <= 0:
			#pokemon 1 fainted
			playsound("sound\\faint.wav")
			display(f"{p[n].name} fainted!")
			return -1*((n+1)%2 + 1)
		else:
			pass
	if "seed" in p[n].condition:
		time.sleep(2)
		p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = int(0.125*p[n].HP),reason = "health is sapped by LEECH SEED!",effect = 1)
		p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = int(-0.125*p[n].HP),reason = "gained foe's energy!!",effect = 1)
		if p[n].hp <= 0:
			#pokemon 1 fainted
			playsound("sound\\faint.wav")
			display(f"{p[n].name} fainted!")
			return -1*((n+1)%2 + 1)
		else:
			pass
	if "root" in p[n].condition and (p[n].hp < p[n].HP):
		time.sleep(2)
		p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = -5,reason = "absorbed nutrients with its roots!",effect = 1)
	
	if "poison" in p[(n+1)%2].condition:
		time.sleep(2)
		p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = int(0.125*p[(n+1)%2].HP),reason = "is hurt by poison!",effect = 1)
		if p[(n+1)%2].hp <= 0:
			#pokemon 1 fainted
			playsound("sound\\faint.wav")
			display(f"{p[(n+1)%2].name} fainted!")
			return -1*(n+1)
		else:
			pass
	elif "toxic" in p[(n+1)%2].condition:
		time.sleep(2)
		p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = int(toxic_count*0.125*p[(n+1)%2].HP),reason = "is hurt by poison!",effect = 1)
		if p[(n+1)%2].hp <= 0:
			#pokemon 1 fainted
			playsound("sound\\faint.wav")
			display(f"{p[(n+1)%2].name} fainted!")
			toxic_count = 1
			return -1*(n+1)
		else:
			toxic_count *= 2
	elif "burn" in p[(n+1)%2].condition:
		time.sleep(2)
		p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = int(0.125*p[(n+1)%2].HP),reason = "is hurt by burn!",effect = 1)
		if p[(n+1)%2].hp <= 0:
			#pokemon 1 fainted
			playsound("sound\\faint.wav")
			display(f"{p[(n+1)%2].name} fainted!")
			return -1*(n+1)
		else:
			pass
	if "seed" in p[(n+1)%2].condition:
		time.sleep(2)
		p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = int(0.125*p[(n+1)%2].HP),reason = "health is sapped by LEECH SEED!",effect = 1)
		p[n].hp = updateHealth(n,remainingonbar[n],p[n].hp, Pbar[n],p[n].HP,deduct = int(-0.125*p[(n+1)%2].HP),reason = "gained foe's energy!!",effect = 1)
		if p[(n+1)%2].hp <= 0:
			#pokemon 1 fainted
			playsound("sound\\faint.wav")
			display(f"{p[(n+1)%2].name} fainted!")
			return -1*(n+1)
		else:
			pass
	if "root" in p[(n+1)%2].condition and (p[(n+1)%2].hp < p[(n+1)%2].HP):
		time.sleep(2)
		p[(n+1)%2].hp = updateHealth((n+1)%2,remainingonbar[(n+1)%2],p[(n+1)%2].hp, Pbar[(n+1)%2],p[(n+1)%2].HP,deduct = -5,reason = "absorbed nutrients with its roots!",effect = 1)
	return 0



def start_fight_thread(event):
    startButton.config(state = tk.DISABLED)
    global fight_thread
    fight_thread = threading.Thread(target = fight) #args = (Pbar[0],Pbar[1],var1,var2))
    fight_thread.daemon = True
    fight_thread.start()
    root.after(20,check_fight_thread)

def Scorecheck(score,n):
	diff = score[(n+1)%2] - score[n]
	print(f"diff:{diff}")
	if diff >= 2:
		print(powerful[2*diff:])
		return random.choice(powerful[2*diff:])
	else:
		return random.randint(0,7)

def check_fight_thread():
    global disablity,Score

    if fight_thread.is_alive():
        root.after(20,check_fight_thread)
    else:
	    if disablity == -1:
		    Score[0] += 1
		    batch = Scorecheck(Score,1)
		    p[1] = Pokemon(batch)
		    reinit(1)

		    if p[0].hp <= 0:
			    Score[1] += 1
			    batch = Scorecheck(Score,0)
			    p[0] = Pokemon(batch)
			    reinit(0)
		    disablity = 0

	    elif disablity == -2:
		    Score[1] += 1
		    batch = Scorecheck(Score,0)
		    p[0] = Pokemon(batch)
		    reinit(0)
		    if p[1].hp <= 0:
			    Score[0] += 1
			    batch = Scorecheck(Score,1)
			    p[1] = Pokemon(batch)
			    reinit(1)
		    disablity = 0
			
	    if disablity == 0:
		    if stopTimer == True:
			    if Score[0] > Score[1]:
				    display("Congratulations! Player 1 wins!!!")
			    elif Score[0] < Score[1]:
				    display("Congratulations! Player 2 wins!!!")
			    else:
				    display("It's a tie!!!")
		    else:
			    reinit(abs(disablity) -1)
			    time.sleep(1)
			    startButton.config(state = "normal")
				
def ppUpdate(index):
	
	if firstdesc[index[0]][2] == '1':
		firstRadio[index[0]].configure(state = tk.DISABLED)
		for i in range(1,4):
			if firstRadio[(index[0]+i)%4]['state'] != "disabled":
				var1.set((index[0]+i)%4)
				break

	if seconddesc[index[1]][2] == '1':
		secondRadio[index[1]].configure(state = tk.DISABLED)
		for i in range(1,4):
			if secondRadio[(index[1]+i)%4]['state'] != "disabled":
				var2.set((index[1]+i)%4)
				break

	firstdesc[index[0]][2] = str(int(firstdesc[index[0]][2]) - 1)
	seconddesc[index[1]][2] = str(int(seconddesc[index[1]][2]) - 1)

	for i in range(4):
		firstRadioPP[i].configure(text = " PP: "+ firstdesc[i][2])
		secondRadioPP[i].configure(text = " PP: "+ seconddesc[i][2])

def checkEffect(p):
	move1Type = str(moveset[moveset["movename"] == p[0].move]['type']).split()[1]
	move2Type = str(moveset[moveset["movename"] == p[1].move]['type']).split()[1]
	val = getEffectiveness((move1Type,move2Type),((p[0].type1,p[1].type1),(p[0].type2,p[1].type2)))
	# val = getEffectiveness(("fire","grass"),(("fire","grass"),("fire","grass")))
	return val

def getFlail(p):

	fraction = p.hp/p.HP
	if fraction > 0.6875:
		return 20
	elif fraction > 0.3542:
		return 40
	elif fraction > 0.2083:
		return 80
	elif fraction > 0.1042:
		return 100
	elif fraction > 0.0417:
		return 150
	else:
		return 200

def getMovePower(p,index,desc):
	global ice_ball,roll_out,fury_cutter
	movepower = [0,0]
	for i in range(2):
		if p[i].move == "Ice Ball":
			roll_out = 0
			movepower[i] = basepow[0] * (1 + ice_ball)
			ice_ball  = (ice_ball + 1) % 5
		elif p[i].move == "Rollout":
			ice_ball = 0
			movepower[i] = basepow[1] * (1 + roll_out)
			roll_out  = (roll_out + 1) % 5
		elif p[i].move == "Fury Cutter":
			ice_ball = 0
			roll_out = 0
			movepower[i] = basepow[2] * fury_cutter
			if fury_cutter < 16:
				fury_cutter  = (fury_cutter * 2)

		elif p[i].move == "Flail":
			movepower[i] = getFlail(p[i])
		else:		#firstdesc[index1][0]
			movepower[i] = int(desc[i][index[i]][0])
	return movepower

			


def start_timer_thread():
    global timer_thread
    timer_thread = threading.Thread(target = countdown)
    timer_thread.daemon = True
    timer_thread.start()
    root.after(20,check_timer_thread)

def check_timer_thread():
    if timer_thread.is_alive():
        root.after(20,check_timer_thread)
    else:
    	pass

def countdown():
	global stopTimer,pauseTimer
	if pauseTimer == False:
		while True:
			if pauseTimer == True:
				break
			time.sleep(1)
			global minutes,seconds
			if seconds < 1:
				if minutes < 1:
					stopTimer = True				
					break
				else:
					seconds = 59
					minutes -= 1
			else:
				seconds -= 1
			if len(str(seconds)) == 1:
				timeLabel.config(text = f"0{minutes} : 0{seconds}")
			else:
				timeLabel.config(text = f"0{minutes} : {seconds}")
	else:
		pass

def fight():
	global stopTimer,pauseTimer,disablity
	stopTimer = False
	pauseTimer = False
	start_timer_thread()
	
	startButton.config(bg = "light green",text = "wait...")
	index1 = var1.get()
	index2 = var2.get()
	ppUpdate((index1,index2))

	p[0].move = firstmoves[index1]
	p[1].move = secondmoves[index2]

	movepower1,movepower2 = getMovePower(p,(index1,index2),(firstdesc,seconddesc))
	# if p[0].move == "Flail":
	# 	movepower1 = getFlail(p[0])
	# else:	
	# 	movepower1 = int(firstdesc[index1][0])
	# if p[1].move == "Flail":
	# 	movepower2 = getFlail(p[1])
	# else:
	# 	movepower2 = int(seconddesc[index2][0])

	accuracy = [int(p[0].acc[index1]),int(p[1].acc[index2])]
	maxA = p[0].maxAttack
	maxD = p[0].maxDefense
	effectiveness = checkEffect(p)
	#	damage on opponent = move-power * (normalize(self Attack) + (1 - normalize(opponent defense)))
	damageon = [0,0]
	damageon[0] = int((1.2*(p[1].attack/maxA)+0.5*(1-(p[0].defense/maxD)))*0.2*movepower2)*effectiveness[1]
	damageon[1] = int((1.2*(p[0].attack/maxD)+0.5*(1-(p[1].defense/maxD)))*0.2*movepower1)*effectiveness[0]

	# display(damageon[0],damageon[1])
	# # p[0].isParalysed = True
	# # p[1].isParalysed = True
	# # p[0].isPoisoned = True
	# # p[1].isPoisoned = True
	# # p[0].isBurnt = True
	# # p[1].isBurnt = True
	# p[0].isSeeded = True
	# # p[1].isSeeded = True
	# check speed to decide who'll go first
	if p[0].speed > p[1].speed:
		n = 0
	else:
		n = 1
	disablity = startProgress(damageon,accuracy,n,(index1,index2),(effectiveness))
	pauseTimer = True
	if stopTimer == False:
		startButton.config(bg = "green",text = "GO",fg = "white")
	else:
		startButton.config(bg = "light green",text = "GAME OVER",fg = "white")
	


'''
createLabel(canvas,row_ = 0,col_ = 0,padx_ = 2,pady_ = 2,text_ = "Label-Text",font_ = ("Calibri 12"))
createEntry(canvas,row_ = 0,col_ = 0,padx = 2,pady = 2,width_ = 50,bd_ = 2)
createButton(canvas,command_,text_ = "Button-Text",width_ = 5,bd_ = 2,font_ = ("Calibri 12"),row_ = 0,col_ = 0,padx = 2,pady = 2)
createRadioButton(canvas,text_ = "radio-item",variable_ = var,value_ = 1,row_ = 0, col_ = 0)
createImage(file_,canvas,row_ = 0,col_ = 0)
(orient_="horizontal",length_=200, mode_="determinate",row_ = 0, col_ = 1)
'''

def start_sound_thread():
    global sound_thread
    sound_thread = threading.Thread(target = loopSound)
    sound_thread.daemon = True
    sound_thread.start()
    root.after(20,check_sound_thread)

def check_sound_thread():
    if sound_thread.is_alive():
        root.after(100,check_sound_thread)
    else:
    	pass

def loopSound():
	file = random.choice(background_theme)
	w.PlaySound(file,w.SND_ASYNC | w.SND_LOOP)

def reinit(n):
	global firstpokeLabel,firstImg,secondpokeLabel,secondImg,firstpokeHP,secondpokeHP,Pbar,firstMoveLabel
	global secondMoveLabel,startButton,remarkBox,var1,var2,firstmoves,firstdesc,secondmoves,seconddesc
	global firstRadioPP,secondRadioPP,firstRadio,secondRadio,leftscore,rightscore
	global Score
	
	if n == 0:
		firstImg = pg.createImage(file_ = f"poke_png\\{p[0].rank} {p[0].name}.png",canvas = pg.firstleft,row_ = 1,col_ = 0)
		for i in range(4):
			firstRadio[i].configure(state = "normal")
		var1.set(0)
		print(f"poke_png\\{p[0].rank} {p[0].name}.png")
		Pbar[0] = pg.createProgress(pg.secondleft)
		firstpokeLabel.config(text = p[0].name)

		firstpokeHP.config(text = f"HP: {p[0].HP}/{p[0].HP}")
		moves = p[0].getMoves()
		firstmoves = [m.split(',')[0] for m in moves]
		firstdesc = [m.split(',')[1:] for m in moves]
		p[0].acc = [i[1] for i in firstdesc]
		var1 = tk.IntVar()
		var1.set(0)
		for i in range(4):
			firstRadio[i].config(text_ = firstmoves[i],variable_ = var1,value_ = i)
			firstRadioPP[i].config(text_ = " PP: "+ firstdesc[i][2])
		rightscore.config(text_ = f"score : {Score[1]}")

	if n == 1:
		secondImg = pg.createImage(file_ = f"poke_png\\{p[1].rank} {p[1].name}.png",canvas = pg.firstright,row_ = 1,col_ = 0)	
		for i in range(4):
			secondRadio[i].configure(state = "normal")
		var2.set(0)
		print(f"poke_png\\{p[1].rank} {p[1].name}.png")
		Pbar[1] = pg.createProgress(pg.secondright)
		secondpokeLabel.config(text = p[1].name)
		
		secondpokeHP.config(text = f"HP: {p[1].HP}/{p[1].HP}")
		moves = p[1].getMoves()
		secondmoves = [m.split(',')[0] for m in moves]
		seconddesc = [m.split(',')[1:] for m in moves]
		p[1].acc = [i[1] for i in seconddesc]
		var2 = tk.IntVar()
		var2.set(0)
		for i in range(4):
			secondRadio[i].config(text_ = secondmoves[i],variable_ = var2,value_ = i)
			secondRadioPP[i].config(text_ = " PP: "+ seconddesc[i][2])
		leftscore.config(text_= f"score : {Score[0]}")
	

	


def setup():
	global firstpokeLabel,firstImg,secondpokeLabel,secondImg,firstpokeHP,secondpokeHP,Pbar,firstMoveLabel
	global secondMoveLabel,startButton,remarkBox,var1,var2,firstmoves,firstdesc,secondmoves,seconddesc
	global firstRadioPP,secondRadioPP,firstRadio,secondRadio,leftscore,rightscore
	global timeLabel

	firstpokeLabel = pg.createLabel(pg.firstleft,text_ = p[0].name,bg_ = "#5a6d9c",color_="white")
	firstImg = pg.createImage(file_ = f"poke_png\\{p[0].rank} {p[0].name}.png",canvas = pg.firstleft,row_ = 1,col_ = 0)

	secondpokeLabel = pg.createLabel(pg.firstright,text_ = p[1].name,bg_ = "#5a6d9c",color_="white")
	secondImg = pg.createImage(file_ = f"poke_png\\{p[1].rank} {p[1].name}.png",canvas = pg.firstright,row_ = 1,col_ = 0)

	firstpokeHP = pg.createLabel(pg.secondleft,text_= f"HP: {p[0].HP}/{p[0].HP}",row_ = 0,col_ = 0,bg_ = "white")
	secondpokeHP = pg.createLabel(pg.secondright,text_= f"HP: {p[1].HP}/{p[1].HP}",row_ = 0,col_ = 0,bg_ = "white")
	Pbar = [pg.createProgress(pg.secondleft),pg.createProgress(pg.secondright)]


	firstMoveLabel = pg.createLabel(pg.thirdleft,text_ = "Moves",row_ = 0,col_ = 0,bg_ = "#5a6d9c")
	moves = p[0].getMoves()
	firstmoves = [m.split(',')[0] for m in moves]
	firstdesc = [m.split(',')[1:] for m in moves]
	p[0].acc = [i[1] for i in firstdesc]
	var1 = tk.IntVar()
	var1.set(0)
	firstRadio = []
	firstRadioPP = []
	for i in range(4):
		firstRadio.append(pg.createRadioButton(pg.thirdleft,text_ = firstmoves[i],variable_ = var1,value_ = i,row_ = i+1,col_ = 0,color_ = "black"))
		firstRadioPP.append(pg.createLabel(pg.thirdleft,text_ = " PP: "+ firstdesc[i][2],row_ = i+1,col_ = 1,font_ = "Calibri 12",bg_ = "#5a6d9c",color_ = "white"))

	secondMoveLabel = pg.createLabel(pg.thirdright,text_ = "Moves",row_ = 0,col_ = 0,bg_ = "#5a6d9c")
	moves = p[1].getMoves()
	secondmoves = [m.split(',')[0] for m in moves]
	seconddesc = [m.split(',')[1:] for m in moves]
	p[1].acc = [i[1] for i in seconddesc]
	var2 = tk.IntVar()
	var2.set(0)
	secondRadio = []
	secondRadioPP = []
	
	for i in range(4):
		secondRadio.append(pg.createRadioButton(pg.thirdright,text_ = secondmoves[i],variable_ = var2,value_ = i,row_ = i+1,col_ = 0,color_="black"))
		secondRadioPP.append(pg.createLabel(pg.thirdright,text_ = " PP: "+ seconddesc[i][2],row_ = i+1,col_ = 1,font_ = "Calibri 12",bg_ = "#5a6d9c",color_ = "white"))
	#canvas,row_ = 0,col_ = 0,padx_ = 2,pady_ = 2,text_ = "Label-Text",font_ = ("Calibri 12")
	if len(str(seconds)) == 1:
		txt = f"0{seconds}"
	else:
		txt = f"{seconds}"
	timeLabel = pg.createLabel(pg.bottom,row_ = 0,col_ = 1,padx_ = 10,text_ = f"0{minutes}:{txt}",bg_ = "#5a6d9c",color_ = "white")

	leftscore = pg.createLabel(pg.bottom,row_ = 1,col_ = 0,padx_ = 0,text_ = f"score : {Score[0]}",bg_ = "#5a6d9c",color_ = "white")
	startButton = pg.createButton(pg.bottom,text_ = "GO",command_ = lambda: start_fight_thread(None),row_= 1,col_=1)
	rightscore = pg.createLabel(pg.bottom,row_ = 1,col_ = 2,padx_ = 10,text_ = f"score : {Score[1]}",bg_ = "#5a6d9c",color_ = "white")
	remarkBox = pg.createListBox(pg.remark)


if __name__ == "__main__":
	root = tk.Tk()
	root.wm_iconbitmap("poke_png\\pokeico.ico")
	start_sound_thread()
	root.resizable(width=False, height=False)
	root.title("Pokemon Battle")
	pg = PokeGUI(root)
	setup()
	change += 1
	root.mainloop()
