def guessing_game_2():

    min = 0
    max = 1000

    print("Think a number between 1 and 1000 and let me guess it.")
    while True:
        guess = int((max-min)/2) + min
        print("Guess: ", guess)
        while True:
            feedback = input("press 1 if I guessed your number\n"
                             "press 2 if I didn't guess your number\n")
            if feedback in ["1", "2"]:
                break

        if feedback == "1":
            print("I WON! Easy job")
            break

        while True:
            feedback = input("press 1 if my guess is higher\n"
                             "press 2 if my guess is not higher\n")
            if feedback in ["1", "2"]:
                break

        if feedback == "1":
            max = guess
            continue

        while True:
            feedback = input("press 1 if my guess is lower\n"
                             "press 2 if my guess is not lower\n")
            if feedback in ["1", "2"]:
                break

        if feedback == "1":
            min = guess
            continue
        if feedback == "2":
            print("Do not try to cheat me!")

guessing_game_2()
