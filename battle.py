import random
import time
'''
											pokemon
								   				|
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
		if random.randint(0,10) % 2 != 0:
			#hurt itself
			return "hurt-itself"
		else:	
			return "move"

def checkCondition(p):

	if p.isAsleep:
		#check for sleep
		p.sleepFreezeCount -= 1
		if p.sleepFreezeCount == 0:
			print(f"{p.name} woke up!")
			p.isAsleep = False
			
			return "move"
		else:
			print(f"{p.name} is fast asleep!")
			
			return "wont"

	elif p.isFrozen:
		#check for freeze (Samsung 4 star)
		p.sleepFreezeCount -= 1
		if p.sleepFreezeCount == 0:
			print(f"{p.name} was defrosted!")
			p.isFrozen = False
			
			return "move"
		else:
			print(f"{p.name} is frozen solid!")
			
			return "wont"

	elif p.isParalysed:
		#check for paralysis
		if random.randint(0,10) % 2 != 0:
			#can't move
			print(f"{p.name} is paralysed! It can't move")
			return "wont"

		elif p.isConfused:
			#check for confusion in paralysis
			return inConfusion(p)

		else:
			#free; no status problems
			return "move"
			
	elif p.isConfused:
		#check for confusion
		return inConfusion(p)

	else:
		#free; no status problems
		return "move"