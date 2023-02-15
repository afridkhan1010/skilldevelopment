n=1900

if(n%400==0 ):
    print('leapyear')

elif n%100==0:
    print('not a leap year')
elif n%4==0:
    print('leap year')
else:
    print('not not')