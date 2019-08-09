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
	p.confuseCount -= 1
	if p.confuseCount == 0:
		print(f"{p.name} snapped out of confusion!")
		
		p.isConfused = False
		return "move"
	else:
		print(f"{p.name} is confused!")
		playsound("sound\\confused.mp3")
		playsound("sound\\confused.mp3")
		playsound("sound\\confused.mp3")
		playsound("sound\\confused.mp3")
		if random.randint(0,10) % 2 != 0:
			#hurt itself
			return "hurt-itself"
		else:	
			return "move"

def checkCondition(p):
	status = ""

	if p.isAsleep:
		#check for sleep
		p.sleepFreezeCount -= 1
		if p.sleepFreezeCount == 0:
			print(f"{p.name} woke up!")
			p.isAsleep = False
			
			status =  "move"
		else:
			print(f"{p.name} is fast asleep!")
			
			status =  "wont"

	elif p.isFrozen:
		#check for freeze (Samsung 4 star)
		p.sleepFreezeCount -= 1
		if p.sleepFreezeCount == 0:
			print(f"{p.name} was defrosted!")
			p.isFrozen = False
			
			status =  "move"
		else:
			print(f"{p.name} is frozen solid!")
			
			status =  "wont"

	elif p.isParalysed:
		#check for paralysis
		if random.randint(0,10) % 2 != 0:
			#can't move
			print(f"{p.name} is paralysed! It can't move")
			playsound("sound\\paralyse.mp3")
			status =  "wont"

		elif p.isConfused:
			#check for confusion in paralysis
			status =  inConfusion(p)

		else:
			#free; no status problems
			status =  "move"
			
	elif p.isConfused:
		#check for confusion
		status =  inConfusion(p)
		if p.isPoisoned:
			status += " poison"
		elif p.isBurnt:
			status += " burn"
		elif p.isSeeded:
			status += " seed"

	else:
		#free; no status problems
		status =  "move"
		if p.isPoisoned:
			status += " poison"
		elif p.isBurnt:
			status += " burn"
		elif p.isSeeded:
			status += " seed"
	
	return status
