num = int("00010111",2) 
print(num)
toggler = 1 
for _ in range(8): 
	num = num ^ toggler 
	toggler <<= 1	 
num += 1 
print(bin(num)) 