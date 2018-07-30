answer=23
question="What number am I thinking of ?"
print("lets play a simple game")
while True:
    guess=int(input(question))
    if(guess<answer):
        print("A little higher")
    elif(guess>answer):
        print("A little lower")
    else:
        print("Hurray you got it !")
        break;
