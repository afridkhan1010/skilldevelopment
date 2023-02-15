"""
Program replace the numbers in the string into word representation
"""

units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
         "Seventeen", "Eighteen", "Nineteen"]
tens  = [0, 0, "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


inp_num=int(input("enter the number: "))
op_string=""
if inp_num>=0 and inp_num<=9:
    for i in units:



def ascii_to_int (num):
    """
    Convert ascii number into integer
    Args:
        num (str): number in ascii
    Returns:
        int: ascii equivalent integer
    """
    return int(ord(num) - ord('0'))


def num_in_word(str_num):
    """
    Replace the ascii numbers into word representation
    Args:
        str_num (str): number[s] in ascii
    Returns:
        str: word representation
    """
    # Get the number of digits
    digits = len(str_num)

    # Since we now have number of digits and we know the word representation start from the first
    # digit, get the max digit place in the given number.
    # Later we convert each digit to it's word format one after the other
    digit_place_max = 10 ** (digits - 1)

    # Run through each number and copy it's word representation
    # Todo this we use our word map to map the number with it's word representation
    word_rep = ""
    for digit in range (digits - 1):
        pos = ascii_to_int(str_num[digit])

        # Get the word from the respective word map
        # We have units, teens and tens, check at which digit place are we at and get the respective
        # word from the word map
        if (100 <= digit_place_max < 1000):
            word_rep += units[pos] + " Hundred"
        elif (10 <= digit_place_max < 100):
            # We need to consider below 2 cases
            # The number lies between 10 - 19
            # The number lies between 20 - 90
            # As the word representation for the above 2 cases are different. Consider the next
            # occurring number to know the exact number and where the number lies in the above 2
            # cases
            if str_num[digit] == '1':
                digit += 1
                digit_place_max /= 10
                pos = ascii_to_int(str_num[digit])
                word_rep += ' ' + teens[pos]
            else:
                pos = ascii_to_int(str_num[digit])
                word_rep += ' ' + tens[pos]
        else:
            pos = ascii_to_int(str_num[digit])
            word_rep += ' ' + units[pos]

        # Reduce digit place as we move to next digit
        digit_place_max /= 10
    return word_rep


def is_num (char):
    """
    Check if the given character is a number or not
    Args:
        char (str): character entered by user
    Returns:
        bool: True- if the character is number. Else, False
    """
    # Check if the character's ASCII value lies in numbers
    if ('0' <= char <= '9'):
        return True
    else:
        return False

def replace_num_to_word (string):
    """
    Replace the numbers in the string into it's equivalent word representation
    Args:
        string (string): read from user input
    Returns:
        str: word representation
    """
    # Split the string into words and run through each word
    words = string.split(' ')

    # Get the number of words in the string
    word_count = len(words)

    # Run through each word and scan for numbers
    out_str = ""
    for word in range (word_count):
        # Check if the word is a number or an alphabet
        if is_num(words[word][0]):
            # Replace number into it's equivalent word representation
            out_str += num_in_word(words[word]) + ' '
        else:
            out_str += words[word] + ' '

    return out_str


# Get the string from the user
string = input("Enter any string\n")

# Reserve space to occupy the result
out_str = replace_num_to_word(string)
print(out_str)


