alphabets = "abcdefghijklmnopqrstuvwxyz"

def get_char_pos (char):

    return alphabets.find(char.lower()) + 1

pos = get_char_pos(input("Enter any alphabet\n"))
print("Alphabet position is " + str(pos))