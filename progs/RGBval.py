# hexval='0x102030'
# print(type(hexval))
# str_len=len(hexval)
# if str_len==7:
#     r_hex=hexval[2:3]


num = 0X102030
print(type(num))
b_num = (bin(num)) 
temp= (bin(0xFF)) 
print(b_num)
print(temp)
b=b_num and temp
print(b)
g = ((bin(num)>> 8) & 0xFF)
print(g)
r = ((num>>16) & 0xFF)
print(r)



r = ((r*31)/255) 
print(r)
g = ((g*31)/255)
print(g)
b = ((b*31)/255)
print(b)
num =0
num |= (r<<11)
print(num)
num |= (g<<6)
print(num)
num |= b



