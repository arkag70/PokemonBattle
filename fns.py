import pandas as pd

#filtered the file
#dataset1 = dataset[~dataset.Name.str.contains("Mega ")]


def getData():
	dataset = pd.read_csv("data_final.csv")
	return dataset.iloc[:386]

def fight():
	pass
