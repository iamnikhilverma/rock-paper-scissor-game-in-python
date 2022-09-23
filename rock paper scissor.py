from logging import error
from pickle import TRUE
import random

def gamewin(comp,you,galat):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return TRUE
        elif you == 's':
            return False
        else:
            return galat

    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
        else:
            return galat

    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False
        else:
            return galat
print("Computer choosed : Rock, paper,scissor")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'r'
elif randNo==2:
    comp = 'p'
elif randNo == 3:
        comp = 's'
you = input("Your turn's: Rock (r) paper(p) scissor(s) ?")
galat = ()
a = gamewin(comp,you,galat)
print(f"computer choosed : {comp}")
print(f"You choosed : {you}")
    
if a == None:
    print("The game is tie!")
elif a==galat:
    print(f"{you} is invalid command")
elif a:
    print("You win")
else:
    print("you lose")