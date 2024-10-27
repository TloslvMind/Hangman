from random import choice

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/\n''')


status = ['''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
 / \\ |
      |
=========''']

word_list = ['camel', 'raccoon', 'crocodile', 'president', 'efficiency', 'currency']

guess_word = choice(word_list)
len_word = len(guess_word)
count = 0
underscores = ['_'] * len_word
while count < len_word and '_' in underscores:
    print(f"Word to guess: {''.join(underscores)}")
    letter = input("Guess a letter: ").lower()
    if letter in guess_word:
        for i in range(len_word):
            if guess_word[i] == letter:
                    underscores[i] = letter
    else:
        print(f"You guessed {letter}, that's not in the word. You lose a life.")
        print(status[count])
        count += 1
    print(f"\n****************************{len_word - count}/{len_word} LIVES LEFT****************************")

if '_' not in underscores:
    print(f"Congratulations! You guessed the word correctly. -->> {guess_word}")
else:
    print(f"***********************IT WAS {guess_word}! YOU LOSE!************************")