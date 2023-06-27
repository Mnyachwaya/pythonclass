import random

# Creating the random words
WORDS = ['bull', 'horse', 'chicken', 'dog' ,'cat', 'mouse', 'frog']

HANGMAN = '''-----'''

MAX_WRONG = len(HANGMAN) - 1

word = random.choice (WORDS)
print(word)

#Creating dashes for the word
current_guess = "-" * len(word)

print (current_guess)

#Wrong guess counter
wrong_guesses = 0

# Used letters Tracker
used_letters = []

#PLAY THE GAME
print("Welcome to Hangman")
print ("Try to guess the word")


#To allow there to be many playing turns
while wrong_guesses < MAX_WRONG and current_guess != word:
    #print (HANGMAN[wrong_guesses])
    print ("You have used the following letters: ", used_letters)
    print ("So far, the word is: ", current_guess)
    break


#User input
guess = input("Enter your letter guess: ")
guess = guess.lower()

#Check if letter has already been used
while guess in used_letters:
    print ('Letter has already been used', guess)
    guess = input("Enter your letter guess: ")
    guess = guess.lower()

#Adding the list of used letters
used_letters.append(guess)
print (used_letters)

#Check guess
if guess in word: 
    print ('You have guessed correctly!')


#CHECK THIS TO USE IN V1
#give a new version of the word with mixed letters and dashes
new_current_guess = ""
for letter in range(len(word)):
    if guess == word [letter]:
        new_current_guess += guess
    else:
        new_current_guess += current_guess [letter]
#print (new_current_guess)
    current_guess = new_current_guess
else: 
    print ('Sorry, that was incorrect') 
    wrong_guesses +=1

#End the game 
if wrong_guesses == MAX_WRONG:
    print (HANGMAN[wrong_guesses]) 
    print ("You have been hanged!")
    print ("The correct word was", word)
else:
    print("You have won")



