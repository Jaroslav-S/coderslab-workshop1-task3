# function "guessing game 2" definition
def guessing_game_2():

# minimum and maximum initialized
    min = 0
    max = 1000

# code to do the job
    print("Think a number between 1 and 1000 and let me guess it.")

# guessing while loop to run until the user is not guessed
    while True:
        guess = int((max-min)/2) + min # guessing formula
        print("Guess: ", guess) # prints computer guess based on formula

# while loop to get correct feedback
        while True:
            feedback = input("press 1 if I guessed your number\n"
                             "press 2 if I didn't guess your number\n")
            if feedback in ["1", "2"]: # break the loop if correct feedback
                break

        if feedback == "1": # correct guess breaks the guessing loop
            print("I WON! Easy job")
            break

# while loop to get correct feedback
        while True:
            feedback = input("press 1 if my guess is higher\n"
                             "press 2 if my guess is not higher\n")
            if feedback in ["1", "2"]: # break the loop if correct feedback
                break

        if feedback == "1": # guess is set as max in case it is higher than number to guess
            max = guess
            continue

# while loop to get correct feedback
        while True:
            feedback = input("press 1 if my guess is lower\n"
                             "press 2 if my guess is not lower\n")
            if feedback in ["1", "2"]: # break the loop if correct feedback
                break

        if feedback == "1": # guess is set as min in case it is lower than number to guess
            min = guess
            continue
        if feedback == "2": # cheater warning in case guess is NOT < AND NOT > AND NOT ==
            print("Do not try to cheat me!")

guessing_game_2()
