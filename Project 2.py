import random

words = ["apple","orange","mango","banana","grapes"]

word = random.choice(words)

name = input("Please enter your name: ")
print(f"Hello ",name,", today we will play a game of Guessing the fruit.")
print("I will tell you the letter which is in the middle and you will answer the fruit")
print("You will have 5 chances to do so, OK")
print("Let's get started!!")

middle_letter = word[2]
hint = word[0],word[-1]

chances = 5
hints = 2
guessed_letters = []

print(f"The letter which is in the middle is ",middle_letter)

for guess in range(chances):

    while True:
        letter = input("Guess a letter: ")

        if len(letter)==1:
            break
        else:
            print("Please guess one letter at a time")

    if letter.lower() in word:
        print("Yes! You have guessed the corrct letter, keep going!")
        guessed_letters.append(letter)

    else:
        print("No! That's the wrong letter guess something else!")

    if chances == 3:
        question = input("Do you want a hint?: ")

        if question.lower() == "yes":
            print(f"The first and last letter of the fruit is ",hint)
        else:
            print("Well you are very confident I guess")

print(f"You have guessed ",len(guessed_letters)," correctly")
print(f"They are ", guessed_letters)
full_word = input("With the help of this guess the whole word: ")

if full_word == word:
     print("Congrats you have guessed the correct fruit!")

else:
     print(f"Oh no that's the wrong answer, the correct answer is ",word)


