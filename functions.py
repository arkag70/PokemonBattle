from pokemon import *
from playsound import playsound
import random
import time



	
def applyStats(p,n,stats):
	statmsg = ""
	if stats == 0:
		pass
	#attack
	if stats == 1:
		p[n].attack *= 1.25
		statmsg = f"{p[n].name}'s attack rose!"
	elif stats == 1.25:
		p[n].attack *= 1.5
		statmsg = f"{p[n].name}'s attack sharply rose!"
	elif stats == 1.5:
		p[(n+1)%2].attack *= 1.25
		statmsg = f"{p[(n+1)%2].name}'s attack rose!"
	elif stats == 1.75:
		p[(n+1)%2].attack *= 1.5
		statmsg = f"{p[(n+1)%2].name}'s attack sharply rose!"
	elif stats == -1:
		p[n].attack *= 0.8
		statmsg = f"{p[n].name}'s attack fell!"
	elif stats == -1.25:
		p[n].attack *= 0.67
		statmsg = f"{p[n].name}'s attack harshly fell!"
	elif stats == -1.5:
		p[(n+1)%2].attack *= 0.8
		statmsg = f"{p[(n+1)%2].name}'s attack fell!"
	elif stats == -1.75:
		p[(n+1)%2].attack *= 0.67
		statmsg = f"{p[(n+1)%2].name}'s attack harshly fell!"
	#defense
	elif stats == 2:
		p[n].defense *= 1.25
		statmsg = f"{p[n].name}'s defense rose!"
	elif stats == 2.25:
		p[n].defense *= 1.5
		statmsg = f"{p[n].name}'s defense sharply rose!"
	elif stats == 2.5:
		p[(n+1)%2].defense *= 1.25
		statmsg = f"{p[(n+1)%2].name}'s defense rose!"
	elif stats == 2.75:
		p[(n+1)%2].defense *= 1.5
		statmsg = f"{p[(n+1)%2].name}'s defense sharply rose!"
	elif stats == -2:
		p[n].defense *= 0.8
		statmsg = f"{p[n].name}'s defense fell!"
	elif stats == -2.25:
		p[n].defense *= 0.67
		statmsg = f"{p[n].name}'s defense harshly fell!"
	elif stats == -2.5:
		p[(n+1)%2].defense *= 0.8
		statmsg = f"{p[(n+1)%2].name}'s defense fell!"
	elif stats == -2.75:
		p[(n+1)%2].defense *= 0.67
		statmsg = f"{p[(n+1)%2].name}'s defense harshly fell!"
	#speed
	elif stats == 3:
		p[n].speed *= 1.25
		statmsg = f"{p[n].name}'s speed rose!"
	elif stats == 3.25:
		p[n].speed *= 1.5
		statmsg = f"{p[n].name}'s speed sharply rose!"
	elif stats == 3.5:
		p[(n+1)%2].speed *= 1.25
		statmsg = f"{p[(n+1)%2].name}'s speed rose!"
	elif stats == 3.75:
		p[(n+1)%2].speed *= 1.5
		statmsg = f"{p[(n+1)%2].name}'s speed sharply rose!"
	elif stats == -3:
		p[n].speed *= 0.8
		statmsg = f"{p[n].name}'s speed fell!"
	elif stats == -3.25:
		p[n].speed *= 0.67
		statmsg = f"{p[n].name}'s speed harshly fell!"
	elif stats == -3.5:
		p[(n+1)%2].speed *= 0.8
		statmsg = f"{p[(n+1)%2].name}'s speed fell!"
	elif stats == -3.75:
		p[(n+1)%2].speed *= 0.67
		statmsg = f"{p[(n+1)%2].name}'s speed harshly fell!"
	elif stats == 4:
		p[n].attack *= 1.25
		p[n].defense *= 1.25
		p[n].attack *= 1.25
		statmsg = f"{p[n].name}'s attack, defense and speed rose!"
	elif stats == 4.25:
		p[n].attack *= 1.5
		p[n].defense *= 1.5
		p[n].attack *= 1.5
		statmsg = f"{p[n].name}'s attack, defense and speed sharply rose!"
	elif stats == 4.5:
		p[(n+1)%2].attack *= 1.25
		p[(n+1)%2].defense *= 1.25
		p[(n+1)%2].attack *= 1.25
		statmsg = f"{p[(n+1)%2].name}'s attack, defense and speed rose!"
	elif stats == 4.75:
		p[(n+1)%2].attack *= 1.25
		p[(n+1)%2].defense *= 1.25
		p[(n+1)%2].attack *= 1.25
		statmsg = f"{p[(n+1)%2].name}'s attack, defense and speed sharply rose!"
	elif stats == -4:
		p[n].attack *= 0.8
		p[n].defense *= 0.8
		p[n].attack *= 0.8
		statmsg = f"{p[n].name}'s attack, defense and speed fell!"
	elif stats == -4.25:
		p[n].attack *= 0.67
		p[n].defense *= 0.67
		p[n].attack *= 0.67
		statmsg = f"{p[n].name}'s attack, defense and speed harshly fell!"
	elif stats == -4.5:
		p[(n+1)%2].attack *= 0.8
		p[(n+1)%2].defense *= 0.8
		p[(n+1)%2].attack *= 0.8
		statmsg = f"{p[(n+1)%2].name}'s attack, defense and speed fell!"
	elif stats == -4.75:
		p[(n+1)%2].attack *= 0.67
		p[(n+1)%2].defense *= 0.67
		p[(n+1)%2].attack *= 0.67
		statmsg = f"{p[(n+1)%2].name}'s attack, defense and speed harshly fell!"
	#accuracy
	elif stats == 5:
		p[n].acc = [int(i)+5 for i in p[n].acc]
		statmsg = f"{p[n].name}'s accuracy rose!"
	elif stats == 5.25:
		p[n].acc = [int(i)+10 for i in p[n].acc]
		statmsg = f"{p[n].name}'s accuracy sharply rose!"
	elif stats == 5.5:
		p[(n+1)%2].acc = [int(i)+5 for i in p[(n+1)%2].acc]
		statmsg = f"{p[(n+1)%2].name}'s accuracy rose!"
	elif stats == 5.75:
		p[(n+1)%2].acc = [int(i)+10 for i in p[(n+1)%2].acc]
		statmsg = f"{p[(n+1)%2].name}'s accuracy sharply rose!"
	elif stats == -5:
		p[n].acc = [int(i)-5 for i in p[n].acc]
		statmsg = f"{p[n].name}'s accuracy fell!"
	elif stats == -5.25:
		p[n].acc = [int(i)-10 for i in p[n].acc]
		statmsg = f"{p[n].name}'s accuracy harshly fell!"
	elif stats == -5.5:
		p[(n+1)%2].acc = [int(i)-5 for i in p[(n+1)%2].acc]
		statmsg = f"{p[(n+1)%2].name}'s accuracy fell!"
	elif stats == -5.75:
		p[(n+1)%2].acc = [int(i)-10 for i in p[(n+1)%2].acc]
		statmsg = f"{p[(n+1)%2].name}'s accuracy harshly fell!"

	if stats > 0:
		playsound("sound\\rise.wav")
	elif stats < 0:
		playsound("sound\\fall.wav")
	return statmsg

def applyStatus(p,n,status):
	time.sleep(1)
	statusmsg = ""
	poke = p[(n+1)%2]
	if status == 1.0:
		if (not poke.isParalysed) and (not poke.isPoisoned) and (not poke.isBadlyPoisoned) and (not poke.isBurnt) and (not poke.isAsleep) and (not poke.isFrozen):
			statusmsg = f"{poke.name} became paralysed!"
			poke.isParalysed = True
			playsound("sound\\paralyse.wav")
		else:
			if not poke.isParalysed:
				statusmsg = f"{poke.name} already has a status problem!"
	elif status == 2.0:
		if (not poke.isParalysed) and (not poke.isPoisoned) and (not poke.isBadlyPoisoned) and (not poke.isBurnt) and (not poke.isAsleep) and (not poke.isFrozen):
			statusmsg = f"{poke.name} is poisoned!"
			poke.isPoisoned = True
			playsound("sound\\poison.wav")
		else:
			if not poke.isPoisoned:
				statusmsg = f"{poke.name} already has a status problem!"
	elif status == 2.5:
		if (not poke.isParalysed) and (not poke.isPoisoned) and (not poke.isBadlyPoisoned) and (not poke.isBurnt) and (not poke.isAsleep) and (not poke.isFrozen):
			statusmsg = f"{poke.name} is badly poisoned!"
			poke.isBadlyPoisoned = True
			playsound("sound\\poison.wav")
			playsound("sound\\poison.wav")
		else:
			if not poke.isBadlyPoisoned:
				statusmsg = f"{poke.name} already has a status problem!"
	elif status == 3.0:
		if (not poke.isParalysed) and (not poke.isPoisoned) and (not poke.isBadlyPoisoned) and (not poke.isBurnt) and (not poke.isAsleep) and (not poke.isFrozen):
			statusmsg = f"{poke.name} is burnt!"
			poke.isBurnt = True
			playsound("sound\\burn.wav")
		else:
			if not poke.isBurnt:
				statusmsg = f"{poke.name} already has a status problem!"
	elif status == 4.0:
		if (not poke.isConfused):
			statusmsg = f"{poke.name} became confused!"
			poke.isConfused = True
			poke.confuseCount = random.randint(2,5)
			playsound("sound\\confused.wav")
			playsound("sound\\confused.wav")
	elif status == -4.0:
		if (not p[n].isConfused):
			statusmsg = f"{p[n].name} became confused!"
			p[n].isConfused = True
			p[n].confuseCount = random.randint(2,5)
			playsound("sound\\confused.wav")
			playsound("sound\\confused.wav")
	elif status == 5.0:
		if (not poke.isParalysed) and (not poke.isPoisoned) and (not poke.isBurnt) and (not poke.isBadlyPoisoned) and (not poke.isAsleep) and (not poke.isFrozen):
			statusmsg = f"{poke.name} went to sleep!"
			poke.isAsleep = True
			poke.sleepFreezeCount = random.randint(2,5)
			playsound("sound\\burn.wav")
		else:
			if not poke.isAsleep:
				statusmsg = f"{poke.name} already has a status problem!"
	elif status == 6.0:
		if (not poke.isParalysed) and (not poke.isPoisoned) and (not poke.isBadlyPoisoned) and (not poke.isBurnt) and (not poke.isAsleep) and (not poke.isFrozen):
			statusmsg = f"{poke.name} became frozen!"
			poke.isFrozen = True
			poke.sleepFreezeCount = random.randint(2,5)
			playsound("sound\\freeze.wav")
		else:
			if not poke.isFrozen:
				statusmsg = f"{poke.name} already has a status problem!"
	elif status == 7.0:
		if (not poke.isSeeded):
			statusmsg = f"{poke.name} was seeded!"
			poke.isSeeded = True
			playsound("sound\\seed1.wav")
		else:
			statusmsg = f"{poke.name} is already seeded!"
	elif status == 8.0:
		if (not p[n].isRooted):
			statusmsg = f"{p[n].name} planted its roots!"
			p[n].isRooted = True
			playsound("sound\\roots.wav")
			playsound("sound\\roots.wav")
		else:
			statusmsg = "But it failed!"
	elif status == -10.0:
		if poke.isSeeded or poke.isFrozen or poke.isAsleep or poke.isConfused or poke.isBurnt or poke.isPoisoned or poke.isParalysed:
			poke.isParalysed = False
			poke.isPoisoned = False
			poke.isBurnt = False
			poke.isConfused = False
			poke.isAsleep = False
			poke.isFrozen = False
			poke.isSeeded = False
			statusmsg = f"{poke.name} was healed of all status problems!"
			playsound("sound\\seed3.wav")
		else:
			statusmsg = f"But it failed!"
	time.sleep(1)
	return statusmsg

def getEffectiveness(mtype,types):
	val = [0,0]
	for i in range(2):
		#bug
		if mtype[i] == "bug":
			for j in range(2):
				if types[j][(i+1)%2] in ["dark","psychic","grass"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["fighting","flying","poison","steel","ghost","fire","fairy"]:
					val[i] += 0.5
				else:
					val[i] += 1
			val[i] /= 2
		#normal
		elif mtype[i] == "normal":
			for j in range(2):
				if types[j][(i+1)%2] == "ghost":
					val[i] = 0
					break
				elif types[j][(i+1)%2] in ["steel","rock"]:
					val[i] += 0.5
				else:
					val[i] += 1
			val[i] /= 2

		#fire
		elif mtype[i] == "fire":
			for j in range(2):
				if types[j][(i+1)%2] in ["ice","grass","bug","steel"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["water","fire","rock","dragon"]:
					val[i] += 0.5
				else:
					val[i] += 1
			val[i] /= 2

		#water
		elif mtype[i] == "water":
			for j in range(2):
				if types[j][(i+1)%2] in ["fire","ground","rock"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["water","grass","dragon"]:
					val[i] += 0.5
				else:
					val[i] += 1
			val[i] /= 2

		#electric
		elif mtype[i] == "electric":
			for j in range(2):
				if types[j][(i+1)%2] in ["water","flying"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["electric","dragon","grass"]:
					val[i] += 0.5
				elif types[j][(i+1)%2] in ["ground"]:
					val[i] = 0
					break
				else:
					val[i] += 1
			val[i] /= 2

		#grass
		elif mtype[i] == "grass":
			for j in range(2):
				if types[j][(i+1)%2] in ["water","ground","rock"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["fire","grass","dragon","poison","flying","bug","steel"]:
					val[i] += 0.5
				else:
					val[i] += 1
			val[i] /= 2

		#ice
		elif mtype[i] == "ice":
			for j in range(2):
				if types[j][(i+1)%2] in ["grass","ground","flying"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["fire","steel","water","ice"]:
					val[i] += 0.5
				else:
					val[i] += 1
			val[i] /= 2

		#fighting
		elif mtype[i] == "fighting":
			for j in range(2):
				if types[j][(i+1)%2] in ["normal","rock","ice","dark","steel"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["poison","flying","bug","psychic","fairy"]:
					val[i] += 0.5
				elif types[j][(i+1)%2] == "ghost":
					val[i] = 0
					break
				else:
					val[i] += 1
			val[i] /= 2

		#poison
		elif mtype[i] == "poison":
			for j in range(2):
				if types[j][(i+1)%2] in ["grass","fairy"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["poison","ground","rock","ghost"]:
					val[i] += 0.5
				elif types[j][(i+1)%2] == "steel":
					val[i] = 0
					break
				else:
					val[i] += 1
			val[i] /= 2
		
		#ground
		elif mtype[i] == "ground":
			for j in range(2):
				if types[j][(i+1)%2] in ["fire","electric","poison","rock","steel"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["grass","bug"]:
					val[i] += 0.5
				elif types[j][(i+1)%2] == "flying":
					val[i] = 0
					break
				else:
					val[i] += 1
			val[i] /= 2

		#flying
		elif mtype[i] == "flying":
			for j in range(2):
				if types[j][(i+1)%2] in ["grass","fight","bug"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["electric","steel","rock"]:
					val[i] += 0.5
				else:
					val[i] += 1
			val[i] /= 2

		#psychic
		elif mtype[i] == "psychic":
			for j in range(2):
				if types[j][(i+1)%2] in ["fighting","poison"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["psychic","steel"]:
					val[i] += 0.5
				elif types[j][(i+1)%2] == "dark":
					val[i] = 0
					break
				else:
					val[i] += 1
			val[i] /= 2

		#bug
		elif mtype[i] == "bug":
			for j in range(2):
				if types[j][(i+1)%2] in ["grass","psychic","dark"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["poison","fire","fighting","flying","ghost","steel","fairy"]:
					val[i] += 0.5
				else:
					val[i] += 1
			val[i] /= 2

		#rock
		elif mtype[i] == "rock":
			for j in range(2):
				if types[j][(i+1)%2] in ["fire","ice","flying","bug"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["fighting","ground","steel"]:
					val[i] += 0.5
				else:
					val[i] += 1
			val[i] /= 2

		#ghost
		elif mtype[i] == "ghost":
			for j in range(2):
				if types[j][(i+1)%2] in ["psychic","ghost"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["dark"]:
					val[i] += 0.5
				elif types[j][(i+1)%2] == "normal":
					val[i] = 0
					break
				else:
					val[i] += 1
			val[i] /= 2

		#dragon
		elif mtype[i] == "dragon":
			for j in range(2):
				if types[j][(i+1)%2] in ["dragon"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["steel"]:
					val[i] += 0.5
				elif types[j][(i+1)%2] == "fairy":
					val[i] = 0
					break
				else:
					val[i] += 1
			val[i] /= 2

		#dark
		elif mtype[i] == "dark":
			for j in range(2):
				if types[j][(i+1)%2] in ["psychic","ghost"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["fighting","dark","fairy"]:
					val[i] += 0.5
				else:
					val[i] += 1
			val[i] /= 2

		#steel
		elif mtype[i] == "steel":
			for j in range(2):
				if types[j][(i+1)%2] in ["ice","rock","fairy"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["steel","fire","water","electric"]:
					val[i] += 0.5
				else:
					val[i] += 1
			val[i] /= 2

		#fairy
		elif mtype[i] == "fairy":
			for j in range(2):
				if types[j][(i+1)%2] in ["fighting","dragon","dark"]:
					val[i] += 2
				elif types[j][(i+1)%2] in ["fire","poison","steel"]:
					val[i] += 0.5
				else:
					val[i] += 1
			val[i] /= 2
	return val

