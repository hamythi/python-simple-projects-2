answer = "mondayy" #use .index to get index in string
already = ["","","","","","", ""]
wrong_guesses = 0

while "".join(already) != answer and wrong_guesses < 6:
    guess = input("Guess a character: ")
    if guess in answer and guess not in already:
        print(f"Yes, there is a(n) {guess}")
        index = 0 #put here to go back to 0 for every guess
        count = answer.count(guess)
        while index < len(answer) and count != 0:
            if guess == answer[index]:
                already[index] = guess #already.pop(index)
                count -= 1
            index += 1
    if guess not in answer and guess in already:
        print("Already got that one!")
    if guess not in answer and guess not in already:
        print(f"Nope, there's no {guess}")
        wrong_guesses += 1
        if wrong_guesses == 1:
            print("     O     ")
        elif wrong_guesses == 2:
            print("     O     ")
            print("    /")
        elif wrong_guesses == 3:
            print("     O     ")
            print("    /|")
        elif wrong_guesses == 4:
            print("     O     ")
            print("    /|\\")
        elif wrong_guesses == 5:
            print("     O     ")
            print("    /|\\")
            print("    /")
        elif wrong_guesses == 6:
            print("     O     ")
            print("    /|\\")
            print("    / \\")
    print(already)
    if "".join(already) == answer and wrong_guesses < 6:
        print("You won!")
        print(answer)
        break
if wrong_guesses >= 6:
    print("Game Over!")