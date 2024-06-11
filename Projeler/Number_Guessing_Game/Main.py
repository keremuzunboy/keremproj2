from random import randint
from art import logo 

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Kullanıcının tahminini gerçek cevaba göre kontrol etme işlevi.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The anwer was {answer}.")

# Zorluğu ayarlamak için işlev yapın.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard':")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
def game():
    #1 ile 100 arasında rastgele bir sayı seçme.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct anwer is {answer}")
    
    turns = set_difficulty()
    #Yanlış anlarlarsa tahmin etme işlevini tekrarlayın.
    guess = 0
    while guess != answer:
      print(f"you have {turns} attempts remaining to guess the number.")
      
      #Kullanıcının bir sayı tahmin etmesine izin ver.
      guess = int(input("Make a guess:"))
    
      #Dönüş sayısını takip et ve yanlış anlarlarsa 1 azalt.
      turns = check_answer(guess, answer, turns)
      if turns == 0:
        print("You've run out of guesses, you lose.")
        return
      elif guess != answer:
        print("Guess again.")
  

game()


