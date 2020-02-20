import pandas as pd

def sub_task1():
	df = pd.read_csv("Trails.csv",usecols=["OBJECTID","CONDITION"])
	d = {}
	for i,r in df.iterrows():
		d[r["CONDITION"]] = d.get(r["CONDITION"],[])
	for i,r in df.iterrows():
		d[r["CONDITION"]].append(int(r["OBJECTID"]))
	print(d)

#sub_task1()

def sub_task2():
	df = pd.read_csv("Trails.csv",usecols=["OBJECTID","INST_YEAR"])
	d = {}
	for i,r in df.iterrows():
		if r["INST_YEAR"] >= 2000:
			iy = f"Installation Year for this {int(r['INST_YEAR'])}"
			d[iy] = d.get(iy,[])
	for i,r in df.iterrows():
		if r["INST_YEAR"] >= 2000:
			iy = f"Installation Year for this {int(r['INST_YEAR'])}"
			d[iy].append(int(r["OBJECTID"]))
	print(d)
	
#sub_task2()

def sub_task3():
	df = pd.read_csv("Trails.csv",usecols=["OBJECTID","LIGHT","STATUS","WALKING","BIKING"])
	count_light = 0
	count_act = 0
	count_wb = 0
	for i,r in df.iterrows():
		if r["LIGHT"] == "Yes":
			count_light += 1
		if r["STATUS"] == "ACTIVE":
			count_act += 1
		if r["WALKING"] == "Yes" and r["BIKING"] == "Yes":
			count_wb += 1
	
	print(f"There are {count_light} have lighting")
	print(f"There are {count_act} currently Active")
	print(f'There are {count_wb} both "Walking" and have "Biking"')
	
sub_task3()