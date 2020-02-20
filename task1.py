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
	
sub_task2()