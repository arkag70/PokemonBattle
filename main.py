from gui_class import *
import fns
import random
'''
createLabel(self,canvas,row_ = 0,col_ = 0,padx_ = 2,pady_ = 2,text_ = "Label-Text",font_ = ("Calibri 12"))
createEntry(canvas,row_ = 0,col_ = 0,padx = 2,pady = 2,width_ = 50,bd_ = 2)
createButton(canvas,command_,text_ = "Button-Text",width_ = 5,bd_ = 2,font_ = ("Calibri 12"),row_ = 0,col_ = 0,padx = 2,pady = 2)
createRadioButton(canvas,text_ = "radio-item",variable_ = var,value_ = 1,row_ = 0, col_ = 0)
createImage(file_,canvas,row_ = 0,col_ = 0)
'''
dataset = fns.getData()
pokemons = []
for i in range(len(dataset)):
	pokemons.append(dataset.iloc[i]["Name"])
i1 = random.randrange(len(pokemons))
pokeleft = pokemons[i1]
i1 += 1
if len(str(i1)) == 1:
	i1 = f"00{i1}"
elif len(str(i1)) == 2:
	i1 = f"0{i1}"

i2 = random.randrange(len(pokemons))
pokeright = pokemons[i2]
i2 += 1
if len(str(i2)) == 1:
	i2 = f"00{i2}"
elif len(str(i2)) == 2:
	i2 = f"0{i2}"



print(f"{i1}: {pokeleft}, {i2}: {pokeright}")

if __name__ == "__main__":

	root = tk.Tk()
	root.title("Pokemon Battle")
	pg = PokeGUI(root)

	firstpokeLabel = pg.createLabel(pg.firstleft,text_ = pokeleft)
	firstImg = pg.createImage(file_ = f"poke_png\\{i1} {pokeleft}.png",canvas = pg.firstleft,row_ = 1,col_ = 0)
	secondpokeLabel = pg.createLabel(pg.firstright,text_ = pokeright)
	secondImg = pg.createImage(file_ = f"poke_png\\{i2} {pokeright}.png",canvas = pg.firstright,row_ = 1,col_ = 0)

	firstpokeHP = pg.createLabel(pg.secondleft,text_= "201/201")
	secondpokeHP = pg.createLabel(pg.secondright,text_= "195/195")

	firstMoveLabel = pg.createLabel(pg.thirdleft,text_ = "Moves",row_ = 0,col_ = 0)
	firstmoves = ["Quick Attack","Slash","Double Kick","Blaze Kick"]
	firstRadio = []
	var = tk.IntVar()
	for i in range(4):
		firstRadio.append(pg.createRadioButton(pg.thirdleft,text_ = firstmoves[i],variable_ = var,value_ = i+1,row_ = i+1,col_ = 0))


	secondMoveLabel = pg.createLabel(pg.thirdright,text_ = "Moves",row_ = 0,col_ = 0)
	secondmoves = ["Pound","Leaf Blade","Pursuit","Agility"]
	secondRadio = []
	var = tk.IntVar()
	for i in range(4):
		secondRadio.append(pg.createRadioButton(pg.thirdright,text_ = secondmoves[i],variable_ = var,value_ = i+1,row_ = i+1,col_ = 0))


	startButton = pg.createButton(pg.bottom,text_ = "GO",command_ = fns.fight)

	root.mainloop()