import random

word_list = ["Hello", "Three", "Dictionary", "Pepperoni"]


def main():
    word_index = random.randint(0, len(word_list)-1)
    secret_word = word_list[word_index]
    guesses = ''
    turns = 6
    while turns > 0:
        failed_guesses = 0
        for letter in secret_word:
            if letter in guesses:
                print(letter)
            else:
                print("-")
                failed_guesses += 1
        if failed_guesses == 0:
            won()
            break
        current_guess = input("Guess a letter:")
        guesses += current_guess
        if current_guess not in secret_word:
            turns -= 1
            print("Wrong guess")
            print("You have " + str(turns) + " guesses left")
            if turns == 0:
                lose()


def won():
    new_word = ""
    print("You won")
    play_again = input("Do you want to play again: ")
    if play_again == "yes" or play_again == "Yes":
        new_word_choice = input("Would you like to add a new word?")
        if new_word_choice == "yes" or new_word == "Yes":
            addword()
        main()


def lose():
    new_word = ""
    print("You lost")
    play_again = input("Do you want to play again: ")
    if play_again == "yes" or play_again == "Yes":
        new_word_choice = input("Would you like to add a new word?")
        if new_word_choice == "yes" or new_word == "Yes":
            addword()
        main()


def addword():
    new_word = input("Choose a new word")
    word_list.append(new_word)
    main()


main()
