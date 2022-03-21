import random
from google.colab import output

def difficulties(level): # take input from user and return no of guesses based on input
  if level == "easy":
   return 10
  else:
   return 5

def play_game():

  x = random.randint(0,100)

  no_of_guess = difficulties(input("Enter the difficulty! easy or hard\n"))

  while no_of_guess:
    guessed_number = int(input("Guess the number\n"))
    if guessed_number > x:
      print("Too high")
      no_of_guess-=1
    elif guessed_number < x:
      print("Too low")
      no_of_guess-=1
    elif guessed_number == x:
      print("You win")

  if no_of_guess == 0:
    print(f"You loose, you are out of guesses, the correct number is {x}")

while input("Do you wanna play guessing game? y or n\n")=="y":
  output.clear()
  play_game()
