# Week 7 — Extra Practice Projects



## Hangman

import random

word_list = ["apple", "banana", "server", "console", "python", "record"]

chosen_word = random.choice(word_list)

display = ["_"] * len(chosen_word)
print(" ".join(display))

lives = 6
guessed = []

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed:
        print(f"You already guessed '{guess}'.")
        continue
    guessed.append(guess)

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"'{guess}' is not in the word. Lives left: {lives}")

    print(" ".join(display))

if "_" not in display:
    print("You win!")
else:
    print(f"You lose. The word was {chosen_word}.")




