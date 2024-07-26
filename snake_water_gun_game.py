import  random

computer=random.choice([-1,0,1])
youstr=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
player1=input("Enter your name: ")
player=youDict[youstr]

print(f"{player1} chose {reverseDict[player]}\nComputer chose {reverseDict[computer]}")

if(computer==player):
    print("Draw between you and computer")
else:
    if(computer==-1 or player==1):
        print(f"{player1} win!")
    elif(computer==-1 or player==0):
        print(f"{player1} lose!")
    elif(computer==1 or player==-1):
        print(f"{player1} lose!")
    elif(computer==1 or player==0):
        print(f"{player1} win!")
    elif(computer==0 or player==-1):
        print(f"{player1} win!") 
    elif(computer==0 or player==1):
        print(f"{player1} lose!")
    else:
        print(f"{player1} entered something wrong!")