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
			pokemons.append(self.dataset.iloc[i]["name"])
		i1 = random.randint(0,386)
		self.name = pokemons[i1]
		i1 += 1
		if len(str(i1)) == 1:
			i1 = f"00{i1}"
		elif len(str(i1)) == 2:
			i1 = f"0{i1}"
		self.rank = i1
		print(self.rank,self.name)

	def fetchName(self):
		return self.name

	def fetchRank(self):
		return self.rank



def fight():
	pass
