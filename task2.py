from os import path
import os
import re

def sub_task():
	f_input = input("input the filename>>")
	d_input = input("input the specific folder(option)(if no please enter q)>>")
	c_input = input("input the page>>")
	
	if path.exists(d_input) and d_input != "q":
		if not os.path.isdir(d_input):
			print(f"{d_input} is not a dir")
		else:
			f_input = path.join(d_input,f_input)
	elif d_input == "q":
		pass
	else:
		print(f"{d_input} is not exist!")
		return 
	
	if path.exists(f_input):
		if not os.path.isfile(f_input):
			print(f"{f_input} is not a file")
			return
	else:
		print(f"{f_input} is not exist!")
		
	
	
	if c_input.isdigit():
		cj = int(c_input)
		cp = cj * 25
		with open(f_input,"r") as fr:
			fs = fr.readlines()
		fs = fs[:cp]
		fw = open("Newfile.txt","at")
		for j in fs:
			n_t = l33t(j)
			fw.write(n_t)
		fw.close()
		with open("Newfile.txt","r") as fg:
			fgt = fg.read()
		c_w = len(fgt.split())
		c_c = len(re.findall("[a-zA-Z]",fgt))
		c_n = len(re.findall("[0-9]",fgt))
		
		print("success!")
		print(f"{cj} pages")
		print(f"{cp} lines")
		print(f"{c_w} words")
		print(f"{c_c} alphabetic characters")
		print(f"{c_n} numeric characters")
		
			
	else:
		print("wrong input!")
		
	

def l33t(text):
	texts = text.split()
	ntexts = []
	for item in texts:
		if item[-2:] == "er":
			nitem = item[:-2]
			nitem += "xor"
			ntexts.append(nitem)
		else:
			ntexts.append(item)
	ntext = " ".join(ntexts)

	ntext = ntext.replace("o","0").replace("O","0")
	ntext = ntext.replace("a","4").replace("A","4")
	ntext = ntext.replace("e","3").replace("E","3")
	ntext = ntext.replace("i","1").replace("I","1")
	

	return(ntext)
	
sub_task()