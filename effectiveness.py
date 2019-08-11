

def getEffectiveness(mtype,types):
	print(mtype,types)
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

