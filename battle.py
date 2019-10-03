import random
import time
from playsound import playsound
'''
											pokemon
								   				|													check for burn, poison separately
		   ---------------------------------------------------------------------------------
		  |			   	  |						|						  |					|
		sleep			frozen				confusion					paralysed		  free
		  |				  |					//		\\					//		\\			|
		wont			wont			move	hurt-itself	 		confusion	wont	   move
															   		//		\\
																  move	  hurt-itself
'''
def inConfusion(p):
	val = ""
	p.confuseCount -= 1
	if p.confuseCount == 0:
		val = f"{p.name} snapped out of confusion!"
		time.sleep(1)
		p.isConfused = False
		return val,"move"
	else:
		val = f"{p.name} is confused!"
		time.sleep(1)
		playsound("sound\\confused.wav")
		playsound("sound\\confused.wav")
		if random.randint(0,10) % 2 != 0:
			#hurt itself
			return val,"hurt-itself"
		else:	
			return val,"move"

def checkCondition(p):
	status = ""
	val = ""
	if p.isSeeded:
		status += "seed"
		
	if p.isAsleep:
		#check for sleep
		p.sleepFreezeCount -= 1
		if p.sleepFreezeCount == 0:
			val = f"{p.name} woke up!"
			p.isAsleep = False
			time.sleep(1)
			status += "move"
		else:
			val = f"{p.name} is fast asleep!"
			
			status += "wont"

	elif p.isFrozen:
		#check for freeze (Samsung 4 star)
		p.sleepFreezeCount -= 1
		if p.sleepFreezeCount == 0:
			val = f"{p.name} was defrosted!"
			p.isFrozen = False
			time.sleep(1)
			status += "move"
		else:
			playsound("sound\\freeze.wav")
			val = f"{p.name} is frozen solid!"
			
			status += "wont"

	elif p.isParalysed:
		#check for paralysis
		if random.randint(0,10) % 2 != 0:
			#can't move
			val = f"{p.name} is paralysed! It can't move"
			playsound("sound\\paralyse.wav")
			status += "wont"

		elif p.isConfused:
			#check for confusion in paralysis
			v,s = inConfusion(p)
			val += v
			status += s

		else:
			#free; no status problems
			status += "move"
			
	elif p.isConfused:
		#check for confusion
		v,s = inConfusion(p)
		val += v
		status += s
		if p.isPoisoned:
			status += " poison"
		elif p.isBadlyPoisoned:
			status += " toxic"
		elif p.isBurnt:
			status += " burn"
		elif p.isSeeded:
			status += " seed"
		if p.isRooted:
			status += " root"

	else:
		#free; no status problems
		status += "move"
		if p.isPoisoned:
			status += " poison"
		elif p.isBadlyPoisoned:
			status += " toxic"
		elif p.isBurnt:
			status += " burn"
		elif p.isBurnt:
			status += " seed"
		if p.isRooted:
			status += " root"
	
	return val,status
