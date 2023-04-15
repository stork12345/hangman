import random

def hangman():  
  lives = 4
  
  i = 0
  
  words = ["apple", "banana", "cherry", "orange", "watermelon", "grape", "strawberry", "blueberry", "mango", "pineapple", "lemon", "lime", "peach", "pear", "plum", "raspberry", "kiwi", "apricot", "pomegranate", "coconut"]
  wrongGuesses = []

  hangmanDrawing = [
        "-----"
        "    |"
        "    |"
        "    |"
        "    |"
        "  __|__",
          "-----"
        "o   |"
        "    |"
        "    |"
        "    |"
        "  __|__",
        "-----"
        "o   |"
        "i   |"
        "    |"
        "    |"
        "  __|__",
        "-----"
        "o   |"
        "i   |"
        "/\  |"
        "    |"
        "  __|__",
        "-----"
        " o   |"
        "/i\  |"
        " /\  |"
        "     |"
        "   __|__"
  ]
  
  word = words[random.randint(0, 3)]
  splitWord = list(word)
  
  if lives == 4:
      print(hangmanDrawing[0])
  
  dashes = ["_"] * len(splitWord)
  
  while dashes != splitWord:
      
      print(*dashes)
      guess = input("Guess a letter: ")
      
      if guess not in word:
          print("Wrong!")
          wrongGuesses.append(guess)
          lives -= 1
          print(wrongGuesses)
          print(hangmanDrawing[4 - lives])

          if lives == 0:
              print("You failed")
              break
  
      else:
          for i, letter in enumerate(splitWord):
              if letter == guess:
                  dashes[i] = guess
            

hangman()

while True:
  tryAgain = input("Do you want to play again? y/n")
  
  if tryAgain == "y":
      hangman()
  else:
      break  