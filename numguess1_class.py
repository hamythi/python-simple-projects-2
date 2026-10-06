import random

class GuessNum():
    def guess(self, num = 9):
        count = 0
        guessed_num = int(input("take a guess: "))
        while guessed_num != num and count < 2:
            print("Try again!")
            count += 1
            guessed_num = int(input("take a guess: "))
        if count == 2:
            GuessNum.ask(self)
            GuessNum.guess(self)
        if guessed_num == num:
           print("You're correct!")
    def ask(self, asked = 0):
        hint1 = "number is from 0 to 9"
        hint2 = "number is divisible to 3"
        clue = random.randint(1,2)
        if clue == 1:
            print(hint1)
        else:
            print(hint2)
    def quit_game(self):
        print(f"correct number was {num}\n See you next time!")
game = GuessNum()
game.guess()

        
            
