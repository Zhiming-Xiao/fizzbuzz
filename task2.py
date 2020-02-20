from os import path

def sub_task():
	f_input = input("input the filename>>")
	d_input = input("input the specific folder(option)(if no please enter q)>>")
	c_input = input("input the page>>")
	
	if path.exists(f_input):
		if not os.path.isfile(f_input):
			print("this is not a file")
	else:
		print("it is not exist!")
		
	if path.exists(d_input) and d_input != "q":
		if not os.path.isdir(d_input):
			print("this is not a dir")
	else:
		print("it is not exist!")
		
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
		
		print("success!")
		print(cj)
		print(cp)
		print(c_w)
		
			
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
	ntext = "".join(ntexts)

	ntext = ntext.replace("o","0").replace("O","0")
	ntext = ntext.replace("a","4").replace("A","4")
	ntext = ntext.replace("e","3").replace("E","3")
	ntext = ntext.replace("i","1").replace("I","1")
	
	return(ntext)
	
sub_task()