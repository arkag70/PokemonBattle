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

	def getMoves(self):
		moves = []
		if self.type1 == self.type2:
			print(self.type1,self.type2,"same type")
			for i in range(4):
				key, value = list(moveset[self.type1].items())[random.randint(0,10)]
				moves.append(key)
				
		else:
			print(self.type1,self.type2,"different types")
			for i in range(2):
				key, value = list(moveset[self.type1].items())[random.randint(0,10)]
				moves.append(key)
			for i in range(2):
				key, value = list(moveset[self.type2].items())[random.randint(0,10)]
				moves.append(key)
		print(moves)
		return moves

# def hello():
# 	key, value = list(moveset["dark"].items())[5]
# 	print(key)

# hello()
