def roman_to_decimal(roman):
    roman_to_dec = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    decimal = 0
    prev = 0
    # print(reversed(roman))
    for char in reversed(roman):
        print(char)
        curr = roman_to_dec[char]

        if curr >= prev:
            decimal += curr
        else:
            decimal -= curr
        prev = curr
    return decimal

roman = input("Enter a Roman numeral: ").upper()
decimal = roman_to_decimal(roman)
print(f"The decimal equivalent of {roman} is {decimal}")