##  Hangman Game (Python CLI Version)
This is a simple command-line Hangman game implemented in Python. The player is tasked with guessing a randomly selected word from a predefined list within a limited number of attempts (lives). The game provides feedback after each guess and visually updates the word being guessed.

## 🎯 Features
Random word selection from a fixed list.
Player has 4 lives to guess the word.
Word progress is shown after each correct guess.
Tracks guessed letters and reveals correct positions.
Displays a victory or defeat message based on the result.

## 🧠 Game Logic
The word to guess is chosen at random from the word_list.
The player inputs one letter at a time.
Correct guesses reveal the letter in its correct position(s).
Incorrect guesses reduce the player's lives.
The game ends when the player guesses the entire word correctly or runs out of lives.

## 🛠️ Technologies Used
Python 3

## Standard libraries:
random

## 📦 Sample Word List
python
Copy
Edit
word_list = ["aardvark", "baboon", "camel"]
## 🚀 How to Run
Make sure you have Python installed.

Save the script as hangman.py.

Run the game in your terminal:

bash
Copy
Edit
python hangman.py
##  Sample Output
![image](https://github.com/user-attachments/assets/03049c47-e0f2-483e-8017-8b59d97a8e5f)
![image](https://github.com/user-attachments/assets/d5f6350c-48d3-4bcc-b046-0291807e39f7)



🤝 Contributing
Feel free to fork this repo, improve the logic, add new features, or extend the word list.
