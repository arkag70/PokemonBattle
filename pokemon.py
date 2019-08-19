import pandas as pd
import random
# from moves import moveset
#filtered the file
#dataset1 = dataset[~dataset.Name.str.contains("Mega ")]

pokemons = []
def getData():
	global maxAttack,maxDefense
	dataset = pd.read_csv("poke.csv")
	datasheet = dataset.iloc[:385]
	print(datasheet.tail(1))
	return dataset

class Pokemon:
	def __init__(self):
		
		self.dataset = getData()
		for i in range(len(self.dataset)):
			pokemons.append(self.dataset.iloc[i])
		i = random.randint(0,386)
		self.maxAttack = max(self.dataset['attack'])
		self.maxDefense = max(self.dataset['defense'])
		self.name = pokemons[i]["name"]
		#max HP
		self.HP = int(pokemons[i]["hp"])
		#current HP
		self.hp = int(pokemons[i]["hp"])
		self.type1 = pokemons[i]["type1"]
		self.type2 = pokemons[i]["type2"]
		self.attack = pokemons[i]["attack"]
		self.defense = pokemons[i]["defense"]
		self.speed = pokemons[i]["speed"]
		self.isAsleep = False
		self.sleepFreezeCount = 0
		self.confuseCount = 0
		self.isFrozen = False
		self.isParalysed = False
		self.isConfused = False
		self.isPoisoned = False
		self.isBurnt = False
		self.isSeeded = False
		self.isRooted = False
		self.condition = "wont"
		self.move = "Move"
		self.acc = [0,0,0,0]

		i += 1
		if len(str(i)) == 1:
			i = f"00{i}"
		elif len(str(i)) == 2:
			i = f"0{i}"
		self.rank = i
		print(self.rank,self.name)

	def getMoves(self):
		moveset = pd.read_excel("moves.xlsx",sheet_name = "sheet1")
		movelist = []
		if self.type1 == self.type2:
			#list all type1 moves
			data = moveset[moveset["type"] == self.type1]
			for i in range(len(data)):
				attributes = ""
				attributes += str(data.iloc[i]['movename'])+","+str(data.iloc[i]['power'])+","+str(data.iloc[i]['accuracy'])+","+str(data.iloc[i]['pp'])+","+str(data.iloc[i]['type'])
				movelist.append(attributes)
		else:
			data1 = moveset[moveset["type"] == self.type1]
			data2 = moveset[moveset["type"] == self.type2]

			for i in range(len(data1)):
				attributes = ""
				attributes += str(data1.iloc[i]['movename'])+","+str(data1.iloc[i]['power'])+","+str(data1.iloc[i]['accuracy'])+","+str(data1.iloc[i]['pp'])+","+str(data1.iloc[i]['type'])
				movelist.append(attributes)
			for i in range(len(data2)):
				attributes = ""
				attributes += str(data2.iloc[i]['movename'])+","+str(data2.iloc[i]['power'])+","+str(data2.iloc[i]['accuracy'])+","+str(data2.iloc[i]['pp'])+","+str(data2.iloc[i]['type'])
				movelist.append(attributes)

			
		random.shuffle(movelist)
		movelist = movelist[:4]
		return movelist[:4]
