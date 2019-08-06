import pandas as pd
import random
from moves import moveset
#filtered the file
#dataset1 = dataset[~dataset.Name.str.contains("Mega ")]

pokemons = []
def getData():
	dataset = pd.read_csv("poke.csv")
	return dataset.iloc[:386]

class Pokemon:
	def __init__(self):
		
		self.dataset = getData()
		for i in range(len(self.dataset)):
			pokemons.append(self.dataset.iloc[i])
		i = random.randint(0,386)

		self.name = pokemons[i]["name"]
		self.HP = int(pokemons[i]["hp"])
		self.type1 = pokemons[i]["type1"]
		self.type2 = pokemons[i]["type2"]
		self.attack = pokemons[i]["attack"]
		self.defense = pokemons[i]["defense"]
		self.speed = pokemons[i]["speed"]

		i += 1
		if len(str(i)) == 1:
			i = f"00{i}"
		elif len(str(i)) == 2:
			i = f"0{i}"
		self.rank = i
		print(self.rank,self.name)

	def fetchName(self):
		return self.name

	def fetchRank(self):
		return self.rank

	def fetchHP(self):
		return self.HP

	def fetchAttack(self):
		return self.attack

	def fetchDefense(self):
		return self.defense

	def fetchSpeed(self):
		return self.speed

	def getMoves(self):

		if self.type1 == self.type2:
			moves = []
			desc = []
			movlist = list(moveset[self.type1].items())
			for movename in movlist:
				moves.append(movename[0])
				desc.append(movename[1])
			together = list(zip(moves,desc))
			random.shuffle(together)
			moves[:],desc[:] = zip(*together)
			moves = moves[:4]
			desc = desc[:4]
				
		else:
			moves1 = []
			desc1 = []
			movlist1 = list(moveset[self.type1].items())
			for movename in movlist1:
				moves1.append(movename[0])
				desc1.append(movename[1])
			together1 = list(zip(moves1,desc1))
			random.shuffle(together1)
			moves1[:],desc1[:] = zip(*together1)
			moves1 = moves1[:2]
			desc1 = desc1[:2]

			moves2 = []
			desc2= []
			movlist2 = list(moveset[self.type2].items())
			for movename in movlist2:
				moves2.append(movename[0])
				desc2.append(movename[1])
			together2 = list(zip(moves2,desc2))
			random.shuffle(together2)
			moves2[:],desc2[:] = zip(*together2)
			moves2 = moves2[:2]
			desc2 = desc2[:2]

			moves = moves1 + moves2
			desc = desc1 + desc2
		#print(moves,desc)
		return moves,desc

# def hello():
# 	key, value = list(moveset["dark"].items())[5]
# 	print(key)

# hello()
