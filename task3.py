import re 

def unique_words(b):
	with open(b,"r") as f:
		ft = f.read()

	nt = ft.split()

	st = set(nt)
	st = tuple(st)
	return st
	
unique_words("Book1.txt")
