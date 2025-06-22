import random
word_list = ["aardvark", "baboon", "camel"]
print("Welcome To Hangman")
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_to_guess = random.choice(word_list)  # determining the word
word = list(word_to_guess)
copy_word=list(word_to_guess)
length_of_string = len(word_to_guess)
no_of_lives = 7
user_guessed_word = ""
track_of_guessed_word=[]
result = False
user_input = []
final_output=" "
for j in range(0,length_of_string):
    user_input.insert(j,"-")

print(f"You have to guess {length_of_string} words: ",user_input)
while no_of_lives > 0 and copy_word != user_input:
    user_guessed_word = input("Enter the guessed word: ")
    for i in range(0, length_of_string):
        if word==user_input:
            break

        if i < length_of_string and user_guessed_word == word[i] :
            user_input[i]=word[i]
            track_of_guessed_word.insert(i,word[i])
            word[i]=" "
            final_output=" ".join(word)
            print(user_input)
            result=True
            break

        elif i == length_of_string - 1 and user_guessed_word != word[i]:
            no_of_lives -= 1
            print(f"The remaining lives: {no_of_lives}")
            print(stages[no_of_lives])

if result == True:
    print("Congratulation! You have guessed the word right")
else:
    print("Try again")






