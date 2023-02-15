def int_to_word(num):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if num < 20:
        return ones[num]
    elif num < 100:
        return tens[num//10] + (ones[num%10] if num%10 != 0 else "")
    else:
        return ""

num = int(input("Enter a number between 1 and 100: "))
result = int_to_word(num)

if result:
    print(f"The word representation of {num} is '{result}'")
else:
    print("The number is outside the range of 1-100.")