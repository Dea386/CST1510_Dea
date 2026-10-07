"""""""""""
Define a function `add(n1, n2)` that returns `n1 + n2`.
2. Define a function `subtract(n1, n2)` that returns `n1 - n2`.
3. Define a function `multiply(n1, n2)` that returns `n1 * n2`.
4. Define a function `divide(n1, n2)` that returns `n1 / n2`.
5. Use `input()` to ask for the first number. Convert it with `float()` and
   store it in `n1`.
6. Create a variable `keep_going` and set it to `True`.
7. Start a `while keep_going:` loop.
8. Inside the loop, ask for an operator (`+ - * /`) and store it in
   `operator`.
9. Ask for the second number, convert it with `float()`, and store it in `n2`.
10. Use `if`/`elif` to call the matching function and store the answer in
    `result`. For example, if `operator == "+"`, then `result = add(n1, n2)`.
11. Print the calculation and the result.
12. Ask the user: `"Type 'y' to continue with the result, or 'n' to start over:"`
13. If they type `"y"`, set `n1 = result`.
14. Otherwise, ask for a new first number and store it in `n1`.
"""""""""""""""""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2 

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

n1 = float(input("What's the first number?  "))

keep_going = True 

while keep_going: 
    operator = input(" Pick an operator (+ - * /):")

n1 = float(input("What's the second number?  "))

if operator == "+":
    result = add( n1, n2)
elif operator == "-":
    result = subtract(n1, n2)
elif operator == "*":
    result = multiply(n1, n2)
elif operator == "/":
    result = divide(n1, n2)
else:
    print("Invalid operator.")
    continue

print(f"{n1} {operator} {n2} = {result}")

choice = input(f"Type 'y' to continue calculating with {result}, or 'n' to start over")

if choice.lower() == "y":
    n1 = result
else:
    n1 = float(input("Whats the first nunmber? "))


""""1. At the top of your file, write `import random`.
2. Define a function called `get_computer_choice()`.
3. Inside it, create a variable `number` and set it to `random.randint(0, 2)`.
4. Use `if`/`elif`/`else` to check `number`:
   - if it is `0`, return `"rock"`
   - if it is `1`, return `"paper"`
   - otherwise, return `"scissors"`
5. Define a function called `decide_winner(user_choice, computer_choice)`.
6. Inside it, if `user_choice` equals `computer_choice`, return `"draw"`.
7. Add an `elif` that returns `"user"` if the user wins
   (rock beats scissors, paper beats rock, scissors beats paper).
8. Add an `else` that returns `"computer"`.
9. Outside the functions, use `input()` to ask the user for their choice
   and store it in a variable called `user_choice`.
10. Call `get_computer_choice()` and store the result in `computer_choice`.
11. Print the computer's choice.
12. Call `decide_winner(user_choice, computer_choice)` and store the result
    in `winner`.
13. Print who won."""


import random 

def get_computer_choice():
    number = random.randint(0,2)
    if number == 0:
        return "rock"
    elif number == 1:
        return"paper"
    else:
        return "scissors"


def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif ( user_choice == "rock" and computer_choice == "scissors") or \
         ( user_choice == "paper" and computer_choice == "rock") or \
         ( user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

user_choice = input("enter rock, paper, or scissors "). lower()

computer_choice = get_computer_choice()

print(f"Computer chose: {computer_choice}")

winner = decide_winner(user_choice, computer_choice)

if winner == "draw":
    print("Its a draw")
elif winner == "user":
    print("You won")
else:
    print("Computer won!")


         