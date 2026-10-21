
---

## Blackjack, Object-Oriented

**Uses:** classes, `__init__`, methods, `self`

import random


class Hand:

  def __init__(self):
    
    self.cards = []

  def add_card(self):
   
    cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards_list)
    self.cards.append(card)

  def score(self):
    if sum(self.cards) == 21 and len(self.cards) == 2:
      return 0  # 0 represents Blackjack in this rule set

    current_score = sum(self.cards)
    if 11 in self.cards and current_score > 21:
      self.cards.remove(11)
      self.cards.append(1)
      current_score = sum(self.cards)

    return current_score


def compare(user_score, computer_score):

  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"


def play_game():
  print("\n" * 5)
  print(" Welcome to Object-Oriented Blackjack!")


  user_hand = Hand()
  computer_hand = Hand()

  is_game_over = False

  for _ in range(2):
    user_hand.add_card()
    computer_hand.add_card()

  while not is_game_over:
    user_score = user_hand.score()
    computer_score = computer_hand.score()

    print(f"   Your cards: {user_hand.cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_hand.cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input(
          "Type 'y' to get another card, type 'n' to pass: "
      )
      if user_should_deal == "y":
        user_hand.add_card()
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_hand.add_card()
    computer_score = computer_hand.score()

  print(f"   Your final hand: {user_hand.cards}, final score: {user_hand.score()}")
  print(
      f"   Computer's final hand: {computer_hand.cards}, final score:"
      f" {computer_hand.score()}"
  )
  print(compare(user_hand.score(), computer_hand.score()))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()