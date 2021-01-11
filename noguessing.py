import random
print("no. guessing game")

number = random.randint(1,9)
chances = 0
print("guess a no. between 1 and 9")

while chances < 5:
    guess = int(input("enter your guess: "))

    if guess == number :
        print("congo u won")
        break
    elif guess < number :
        print("your guess wasa to low")
    else :
        print("your guess was high enough")
    chances+=1
if not chances<5 :
    print("you lose. the no. is ",number)
