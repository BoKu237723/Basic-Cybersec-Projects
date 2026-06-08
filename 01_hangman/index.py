import random

print("Welcome to Hangman!")

num = 1
words = ["hacker", "bounty", "random"]

secret_word = random.choice(words)
print(secret_word)
display_word = []

for lett in secret_word:
    display_word += "_"

while True: 
    guess = input("Guess a letter: ").lower()

    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
        else:
            pass
    
    if guess not in secret_word:
        num += 1
        print("Guess Left: ", 10 - num)
        if num >= 10:
            print("You Loser")
            print("GAME OVER!")
            break
    
    print(display_word)

    if "_" not in display_word:
        print("You Win!")
        break
    