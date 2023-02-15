import random

random_string=['afrid','tazneen','khan']
chosen_word=random.choice(random_string)
print(chosen_word)
lives=6

wordlen=len(chosen_word)
display=[]
for _ in range(wordlen):
    display+= "_"

end_of_game=False

while not end_of_game:
    user_guess=input('Enter the guess letter:')
    for position in range(wordlen):
        letter=chosen_word[position]
        if letter==user_guess:
            display[position]=letter

    if user_guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print('game lost')
  
    print(f"{''.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("won")