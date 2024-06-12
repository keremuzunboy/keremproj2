import random

from replit import clear

from art import logo, vs
from game_data import data

#Bu fonksiyon, veri setinden rastgele bir hesap seçer.
def get_random_account():
  """Get data from random account"""
  return random.choice(data)

#Bu fonksiyon, seçilen hesabın bilgilerini düzgün bir biçimde formatlar.
def format_data(account):
  """Format account into printable format: name, descripton and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return(f" {name}, a {description}, from {country}")

#Bu fonksiyon, kullanıcının tahminini kontrol eder ve doğruysa True, yanlışsa False döndürür.
def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
#Bu fonksiyon, oyunun ana döngüsünü kontrol eder. Kullanıcıya iki hesap arasında kimin daha fazla takipçisi olduğunu tahmin etme şansı verir. Kullanıcının tahmini doğruysa, skorları artar. Yanlışsa, oyun sona erer.
def game():
  print(logo)
  score = 0
  game_should_couontinues = True
  account_a = get_random_account()
  account_b = get_random_account()
  
  while game_should_couontinues:
    account_a = account_b
    account_b = get_random_account()
    
    while account_a == account_b:
      account_b = get_random_account()
    
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]    
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_couontinues = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()      
