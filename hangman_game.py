import random

hangman = [
    # Initial empty stage
    r"""
    +---+
    |   |
        |
        |
        |
        |
    ==========""",
    
    # Head only
    r"""
    +---+
    |   |
    O   |
        |
        |
        |
    ==========""",
    
    # Head and torso
    r"""
    +---+
    |   |
    O   |
    |   |
        |
        |
    ==========""",
    
    # Head, torso, and one arm
    r"""
    +---+
    |   |
    O   |
   /|   |
        |
        |
    ==========""",
    
    # Head, torso, and both arms
    r"""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    ==========""",
    
    # Head, torso, both arms, and one leg
    r"""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    ==========""",
    
    # Final stage - complete hangman
    r"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ==========""",
]

word_list = ["berke", "zeynep", "nil"]
letter_list = []
word_hidden = []
condition = False
hangman_iterator = 0
chances = 6

def main():

    hide_word(get_word())

    get_letters()



def hide_word(word):
    global word_hidden
    global letter_list

    for letter in word:
        word_hidden.append("_ ")
        letter_list.append(letter)

def get_word():
    global word_list

    return random.choice(word_list)

def get_letters():
    global letter_list
    global word_hidden
    global condition
    global hangman_iterator
    global chances

    while "_ " in word_hidden and chances > 0:
        condition = False

        print(f"chances : {chances}")
        letter = input("  letter: ")

        for i in range(len(letter_list)):
            if letter == letter_list[i]:
                word_hidden[i] = letter
                condition = True
        
        if condition == False:
            try:
                print(hangman[hangman_iterator])
                hangman_iterator += 1
                chances -= 1
            except IndexError:
                print("YOU LOST")

            
        for ch in word_hidden:
            print(ch, end="")
    
    if chances == 0:
        print("YOU LOST")
    else:
        print("YOU WIN")


main()





