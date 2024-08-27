import requests

API_URL ="https://random-word-api.herokuapp.com/word"

def get_random_word():
    response = requests.get(API_URL)
    return response.json()[0]

def main():
    guessed_letters = []

    right_counter = 0
    wrong_counter = 0

    word = get_random_word()
    word_char_list = list(word)

    for letter in word_char_list:
        print("_", end=" ")
    print()

    while True:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("Letter already guessed")
        else:
            guessed_letters.append(guess)
            if guess in word_char_list:
                right_counter += 1
                print("Correct guess")
            else:
                wrong_counter += 1
                print("Wrong guess")
            print()


        for letter in word_char_list:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

        if right_counter == len(word_char_list):
            print("You won! 🎉")
            break
        elif wrong_counter == 5:
            print("You lost!")
            print(f"The word was: {word}! Better luck next time! 🍀")
            break


if __name__ == "__main__":
    main()
