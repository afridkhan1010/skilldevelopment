string="i am good boy"
# l=string.split()

# op=''

# for i in l:
#     op=i+" "+op
# print(op)
def reverse_words(s):
    words = []
    current_word = ''
    for c in s:
        # If c is a space, add current_word to words and reset it to an empty string
        if c == ' ':
            if current_word:
                words.append(current_word)
                current_word = ''
        else:
            # Append the current character to current_word
            current_word += c
    # Add the final word to the list if it exists
    print("final word", current_word)
    if current_word:
        words.append(current_word)
    print(words)
    reversed_string = ''
    # Append words to the reversed string in reverse order
    # for i in range(len(words) - 1, -1, -1):
    #     reversed_string += words[i] + ' '
    for i in words:
        reversed_string=i+" "+reversed_string

    return reversed_string.strip()

# example usage
s = "the quick brown fox"
print(reverse_words(s)) # "fox brown quick the"
