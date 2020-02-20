import re 

def unique_words(b):
	with open(b,"r") as f:
		ft = f.read()

	nt = ft.split()

	st = set(nt)
	st = tuple(st)
	return st
	
#unique_words("Book1.txt")

def count_the_article(b):
	with open(b,"r") as f:
		ft = f.read()
		
	nt = re.findall("[a-zA-Z-]+",ft)
	
	l = ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
	c = 0
	for i in nt:
		if i in l:
			c += 1
	print(c)
	return c
	
#count_the_article("Book1.txt")

def sorted_words(b):
	with open(b,"r") as f:
		ft = f.read()
		
	nt = re.findall("[a-zA-Z-]+",ft)
	
	d = {}
	for i in nt:
		d[i] = d.get(i,0) + 1
	l=[]	
	for key, value in sorted(d.items(), key=lambda item: item[1],reverse=True):
		l.append(key)
		
	print(l)
	return l

sorted_words("Book1.txt")