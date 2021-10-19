"""
In this game, we enter some number of stick, one of person and computer can start the game.
So, one can choose either 1 or 2 or 3 stick and last one who pick the sticks, win the game.
"""

import random
n=int(input("enter number (>4): "))
kk=n
p=random.choice([0,1])
if(p==0):
    print("you start the game\n")
else:
    print("computer start the game\n")
while(kk>0):
    # computer
    if(p==1):
        if(kk==1):
            aa=1
            kk=kk-aa
            p=0
            print("computer choose: ",aa)
            print("rest: ",kk)
            print("\n")
            if(kk==0):
                print("computer win")
        elif(kk==2):
            aa=random.choice([1,2])
            kk=kk-aa
            p=0
            print("computer choose: ",aa)
            print("rest: ",kk)
            print("\n")
            if(kk==0):
                print("computer win")
        else:    
            aa=random.choice([1,2,3])
            kk=kk-aa
            p=0
            print("computer choose: ",aa)
            print("rest: ",kk)
            print("\n")
            if(kk==0):
                print("computer win")
    # you
    else: #if(bb ==1 or bb == 2 or bb== 3):
        if(kk==1):
            bb=int(input("As only 1 left, you can choose only 1: "))
            if(bb==1):
                kk=kk-bb
                p=1
                print("you choose: ",bb)
                print("rest: ",kk)
                print("\n")
                if(kk==0):
                    print("you win")
            else:
                print("please enter valid choose\n")
                p=0
        elif(kk==2):
            bb=int(input("As 2 left, so you can choose 1 or 2: "))
            if(bb==1 or bb==2):
                kk=kk-bb
                p=1
                print("you choose: ",bb)
                print("rest: ",kk)
                print("\n")
                if(kk==0):
                    print("you win")
            else:
                print("please enter valid choose\n")
                p=0
        else:
            bb=int(input("enter your choose(1 or 2 or 3): "))
            if(bb ==1 or bb == 2 or bb== 3):
                kk=kk-bb
                p=1
                print("you choose: ",bb)
                print("rest: ",kk)
                print("\n")
                if(kk==0):
                    print("you win")
            else:
                print("enter valid choice\n")
                p=0

