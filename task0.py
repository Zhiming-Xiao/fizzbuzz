def B_f():
	for i in range(1,101):
		t = str(i)+"->"
		if not i % 3:
			t += "Fizz"
		if not i % 5:
			t += "Buzz"
		print(t)
		
B_f()