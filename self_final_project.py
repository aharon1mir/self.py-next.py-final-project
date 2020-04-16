#!/usr/bin/python3


"""
I assume that I don't need any documention for these function 
cause the instructions for the above function are taken form the website.
                       good luck :) and thank you. (I had so much fun)
@author: Aharon Mirsky
@version: 1.121256

"""

MESSAGE = '''please insert:
             A) path for the file (which contain the words)
             B) index (for which word of the above file)
           '''
MAX_TRIES = 7

HANGMAN_PHOTOS = {
0:        
"""
 +---+
  |   |
      |
      |
      |
      |
=========
""",
1:
"""
+---+
  |   |
  O   |
      |
      |
      |
=========
""",
2:
"""
+---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
3:
"""
+---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
4:
"""
 +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
5:
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
6:
"""
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""               
 } 
    


def check_win(secret_word, old_letters_guessed):
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True 

def show_hidden_word(secret_word, old_letters_guessed):
    s = ''
    for char in secret_word:
        if char not in old_letters_guessed:
           s += '_'
        else:
            s += str(char)
    return s

def check_valid_input(letter_guessed, old_letters_guessed):
    if  len(letter_guessed) == 1 and 65 <= ord(letter_guessed) <= 122 \
    and letter_guessed not in old_letters_guessed:
        return True
    return False

def try_update_letter_guessed(letter_guessed, old_letter_guessed):
    letter_guessed = letter_guessed.lower()
    if check_valid_input(letter_guessed, old_letter_guessed):
        old_letter_guessed.append(letter_guessed)
        return True
    print('X \n%s' % ''.join(old_letter_guessed))
    return False

def choose_word(file_path, index):
    index = int(index)
    file = open(str(file_path),'r')
    file_content = file.read()
    words = file_content.split(' ')
    file.close()
    #return len(words), words[index]; if you want to keep it ;)
    return words[index]    

def welcome():
    print("""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/

   
""",6)
    print(MESSAGE)


def main():
    welcome()
    file_path = input('A:')
    index = input('B:')
    secret_word = choose_word(file_path, index)
    old_letters_guessed = list()
    num_of_tries = 0
    print(HANGMAN_PHOTOS[num_of_tries])
    while num_of_tries < 7:
        if check_win(secret_word, old_letters_guessed):
            print("WIN \nyou really good;)")
            exit(0)
        guess = input('please insert your guess_letter here:')
        while not try_update_letter_guessed(guess, old_letters_guessed):
            guess = input('please insert your input here:')
        if guess not in secret_word:
            print(':(')
            num_of_tries += 1
            if num_of_tries == 7:
                print("LOSE")
                exit(1)
            print(HANGMAN_PHOTOS[num_of_tries])
        print('your guess: %s' % show_hidden_word(secret_word, old_letters_guessed))
    
if __name__=="__main__":
    main()
    
