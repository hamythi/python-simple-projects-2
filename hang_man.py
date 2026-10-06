# simplified hang man

# answer = "morning"
# begin: input
# if wrong: 
# guess = 6
# if len(guess_lst) == 6
# --> lose --> exit
# if correct [m, o, r, n, i, g]:
# correct character : show
# if guess_list == answer:
#     done
# 
# option to exit game
# hint option
# cretae list of empty strings (number of char == len(answer)), when correct take out index from empty string and insert to char

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
    print(already)
    if "".join(already) == answer and wrong_guesses < 6:
        print("You won!")
        print(answer)
        break
if wrong_guesses >= 6:
    print("Game Over!")

        
        
#replace one by one:
#compare already list, if already in there then compare the index position, and move it to the next index
        
    