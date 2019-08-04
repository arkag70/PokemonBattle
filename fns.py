import pandas as pd
import random
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
