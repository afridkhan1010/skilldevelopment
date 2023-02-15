def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 

dec_val = 5
     
    # Calling function
DecimalToBinary(dec_val)

def decimalToBinary(n):
    return bin(n).replace("0b", "")
   
# Driver code
if __name__ == '__main__':
    print(decimalToBinary(8))
    print(decimalToBinary(18))
    print(decimalToBinary(7))

def dec2bin(number: int):
    ans = ""
    if ( number == 0 ):
        return 0
    while ( number ):
        print(number&1)
        print(number>>1)
        ans += str(number&1)
        number = number >> 1
     
    ans = ans[::-1]
 
    return ans

number = 6
print(f"The binary of the number {number} is {dec2bin(number)}")

def d2b(num):
    bin_num=''
    while(num>0):
        bin_digit=str(num%2)
        print(bin_digit)
        bin_num=bin_num+bin_digit
        print("bin num:" , bin_num)
        num=num//2
        print(num)
    return bin_num
num=6
print(d2b(num))