import pandas as pd

def sub_task1():
	df = pd.read_csv("Trails.csv",usecols=["OBJECTID","CONDITION"])
	d = {}
	for i,r in df.iterrows():
		d[r["CONDITION"]] = d.get(r["CONDITION"],[])
	for i,r in df.iterrows():
		d[r["CONDITION"]].append(r["OBJECTID"])
	print(d)

sub_task1()