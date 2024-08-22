import random
import hangman_arts
import hangman_words

print(hangman_arts.logo)

lives = 6

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess " + placeholder)

game_over = False
correct_letters = []


while not game_over:
    print(f"*******You have {lives}/6 left*******")
    guess = input("Guess the letter").lower()
    
    display = ""
    
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"


    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word")
        
        if lives == 0:
            game_over = True
            print(f"*******Word was {chosen_word}, YOU LOSE!*******")
    
    if "_" not in display:
        game_over = True
        print("*******Congratulations! You WON!*******")

    print(f"Word to guess " + display)

    print(hangman_arts.stages[lives])