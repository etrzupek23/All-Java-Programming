"""
This program is a rock paper scissors game where the user will play against computer.
User will select rock, paper or scissors.
The computer will randomly select rock, paper or scissors.
Rock beats scissor, paper beats rock, scissors beats paper.
Written by the Wonderful, Amazing Introduction to Programming and Hardware class.
November 12, 2019
"""
from random import randint
from time import sleep

options = ["R","P","S"]
loserSkSkSk = "sksks and I oops, you lose!!!! BOOOOOO"
winnerOwO = "OwO You won! Yay! You're very lucky! Woohooo! Very cool thank you! "

# function that decides winner
def decidethewinner(userChoice, computerChoice):
  print("You selected %s. " % userChoice)
  print("The computer is selecting...")
  sleep(1)
  print("The computer selected: " + computerChoice)

# determine index of userchoice
  userChoiceIndex = options.index(userChoice)
  computerChoiceIndex = options.index(computerChoice)

# rules that determine a winner use
  if userChoiceIndex == computerChoiceIndex:
    print ("It's a tie!")
  elif userChoiceIndex == 0 and computerChoiceIndex == 2:
    print(winnerOwO)
  elif userChoiceIndex == 1 and computerChoiceIndex == 0:
    print(winnerOwO)
  elif userChoiceIndex == 2 and computerChoiceIndex == 1:
    print(winnerOwO)
  elif userChoiceIndex > 2:
    print ("--ERROR--")
  else:
    print (loserSkSkSk)

# function that starts and plays the game
def playRPS():
  print ("Welcome to the game of Rock, Paper, Scissors by your favorite block 3 class introduction to computer science class! :P")
  userChoice = input("Choose R for rock, P for paper or S for scissors: ")
  sleep(1)
  userChoice = userChoice.upper()
  computerChoice = options[randint(0,len(options)-1)]
  decidethewinner(userChoice, computerChoice)

playRPS()
