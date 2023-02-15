val=int(input('enter the value between 0-100:'))
roundoffto=int(input('enter the value to be rounded off'))

def roundval(val,roundoff):
    temp=val % roundoffto   

    if val<roundoff:
        return roundoffto
    elif (val%roundoffto)<(roundoffto/2):
            
        return val-temp
    else:
            
        return val+(roundoffto-temp)

print(roundval(val,roundoffto))