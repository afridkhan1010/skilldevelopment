num=int(input("enter the number:" ))
div=int(input("enter the divisor" ))
def divisible(num,div):
    if num % div ==0:
        return "number is perfectly divisible"
    else:
        return "not divisible"

print(divisible(num,div))
