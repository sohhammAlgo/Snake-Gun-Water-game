import random
import sys

l1 = [1,-1,0]
computer = random.choice(l1)

you = input("Enter your choice:")
youDict = {"Snake":1,
           "Water":-1,
           "Gun":0}

if youDict[you] == computer:
    print("Its a draw!")
    sys.exit()
elif youDict[you]==1 and computer==-1:
    print("You win!")
    sys.exit()
elif youDict[you]==-1 and computer==0:
    print("You win!")
    sys.exit()
elif youDict[you]==0 and computer==1:
    print("You win!")
    sys.exit()
else:
    print("You lose!")
    sys.exit()
