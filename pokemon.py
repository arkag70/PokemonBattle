import pandas as pd
import random
# from moves import moveset
#filtered the file
#dataset1 = dataset[~dataset.Name.str.contains("Mega ")]

base = [0,290,320,385,435,480,505,570,1000]
pokemons = []

dataset = pd.read_excel("poke.xlsx",sheet_name = "poke")
datasheet = dataset.iloc[:386]
data = []
for i in range(8):
	data.append(datasheet[(datasheet["base_total"] > base[i]) & (datasheet["base_total"] < base[i+1])])

class Pokemon:
	def __init__(self,batch = random.randint(0,7)):

		self.dataset = data[batch]
		self.pokemon = self.dataset.sample()
		print(f"batch : {batch}")
		print(f"{str(self.pokemon.name).split()[1]}:{str(self.pokemon.base_total).split()[1]}")
		self.maxAttack = max(self.dataset['attack'])
		self.maxDefense = max(self.dataset['defense'])
		self.name = str(self.pokemon["name"]).split()[1]
		#max HP
		self.HP = int(str(self.pokemon["hp"]).split()[1])
		#current HP
		self.hp = self.HP
		self.type1 = str(self.pokemon["type1"]).split()[1]
		self.type2 = str(self.pokemon["type2"]).split()[1]
		self.attack = int(str(self.pokemon["attack"]).split()[1])
		self.defense = int(str(self.pokemon["defense"]).split()[1])
		self.speed = int(str(self.pokemon["speed"]).split()[1])
		self.isAsleep = False
		self.sleepFreezeCount = 0
		self.confuseCount = 0
		self.isFrozen = False
		self.isParalysed = False
		self.isConfused = False
		self.isPoisoned = False
		self.isBadlyPoisoned = False
		self.isBurnt = False
		self.isSeeded = False
		self.isRooted = False
		self.condition = "wont"
		self.move = "Move"
		self.acc = [0,0,0,0]
		self.bellyDrum_Memento = False

		i = int(str(self.pokemon["pokedex_number"]).split()[1])
		if len(str(i)) == 1:
			i = f"00{i}"
		elif len(str(i)) == 2:
			i = f"0{i}"
		self.rank = i

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
