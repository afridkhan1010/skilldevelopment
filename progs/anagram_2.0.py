def anagram(str1, str2):
    x, y = [0] * 26, [0] * 26

    for char in str1:
        x[ord(char) - ord('a')] += 1

    for char in str2:
        y[ord(char) - ord('a')] += 1
    print(x)
    print(y)
    if x != y:
        print("Entered strings are not anagrams.")
    else:
        print("Entered strings are anagrams.")

if __name__ == '__main__':
    str1 = input("Enter string 1: ").lower()
    str2 = input("Enter string 2: ").lower()
    anagram(str1, str2)