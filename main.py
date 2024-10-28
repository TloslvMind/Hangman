from random import choice
from images import logo, status
from words import word_list

print(logo)



guess_word = choice(word_list)
len_word = len(guess_word)
lives = 0
underscores = ['_'] * len_word
while lives < len_word and '_' in underscores:
    print(f"Word to guess: {''.join(underscores)}")
    letter = input("Guess a letter: ").lower()
    if letter in guess_word:
        for i in range(len_word):
            if guess_word[i] == letter:
                    underscores[i] = letter
    else:
        print(f"You guessed {letter}, that's not in the word. You lose a life.")
        if lives + 1 == len_word:
            print(status[-1])
        elif len(status) < lives + 2:
            print(status[-2])
        else:
            print(status[lives])
        lives += 1
    print(f"\n**************************** {len_word - lives}/{len_word} LIVES LEFT****************************")

if '_' not in underscores:
    print(f"Congratulations! You guessed the word correctly. -->> {guess_word}")
else:
    print(f"***********************IT WAS {guess_word}! YOU LOSE!************************")