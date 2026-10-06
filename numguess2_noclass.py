import random 
num = 9
count = 0
guess = int(input("take a guess: "))
hint1 = "number is from 0 to 9"
hint2 = "number is divisible to 3"
while True:
    while guess != num and count < 3:
        print("try again")
        guess = int(input("take a guess: "))
        count += 1
    if count == 3:
        clue = random.randint(1,2)
        if clue == 1:
            print(hint1)
        else:
            print(hint2)
        count = 0
    if guess == num:
        print("you're right")
        break
