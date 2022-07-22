import random
print("Welcome to dice guessing game")
min=1
max=6
while True:
    number=int(input("Please enter a number between 1 and 6.Press 9 to exit"))
    if number==9:
        break
    elif 1<=number<=6:
        x=random.randint(min,max)
        if x==number:
            print("Congratulations!You won.")
        else:
            print("You didn't know.Number was ",x)
    else:
        print("You keyed wrong.Please enter a number between 1 and 6.Press 9 to exit")