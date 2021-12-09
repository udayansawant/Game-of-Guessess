import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("Hey there! Welcome to the Game of Guessess!")
    player_name = input("What's your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input("Alright ! Pick a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Now guess a number within the given range")
            if int(guess) == random_number:
                print("HUrray! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("Alright! See You Soon")
                    break
            elif int(guess) > random_number:
                print("Oh no! this ain't the right number  | Hint: It's a lower number")
                attempts += 1
            elif int(guess) < random_number:
                print("Oh no! this ain't the right number | Hint: It's a higher number")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("Amazing! See you later")
if __name__ == '__main__':
    start_game()