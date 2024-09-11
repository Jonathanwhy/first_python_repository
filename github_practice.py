import random

print("Welcome to wok, peipa, siza")

userchoice = input("wok, peipa, siza?\n")
computerchoice = random.choice(["wok","peipa","siza"])

win = 0
lose =0
def playgame(userchoice, computerchoice):
  
  print("You chose da " + userchoice + " and the computer chose de " + computerchoice)
  if userchoice == computerchoice:
    print("It a tie")
  elif (userchoice == "wok" and computerchoice == "peipa") or (userchoice == "peipa" and computerchoice == "siza") or (userchoice == "siza" and computerchoice == "wok"):
    print("You rost")
    global lose
    lose = lose +1
  else:
    print("You win!!!!!!11!")
    global win
    win = win+1
    
playgame(userchoice, computerchoice)

goagain = input("Best of tree?? (yes,no)\n")
if goagain == "yes":
  while win or lose <= 2:
    userchoice = input("wok, peipa, siza?\n")
    computerchoice = random.choice(["wok","peipa","siza"])
    playgame(userchoice, computerchoice)
    if win == 2:
      print("You win best of tree!!!!!!11!!1!")
      break
    if lose == 2:
      print("You rost best of tree")
      break