# Import the random module in the next line.
import random
# Create the count_rock, 'count_paper and count_scissors variables and set their initial values equal to 0.
count_rock = 0
count_paper = 0
count_scissors = 0

# Create the update_counts() function.
def update_counts(user_input):
  global count_rock, count_paper, count_scissors
  if (user_input == 0):
    count_rock += 1
  elif (user_input == 1):
    count_paper += 1
  elif (user_input == 2):
    count_scissors += 1

# Create the predict() function.
def predict():
  # Uncomment the lines below.
  if count_rock > count_paper and count_rock > count_scissors:
    pred = 0
  if count_rock < count_paper and count_paper > count_scissors:
    pred = 1
  if count_scissors > count_paper and count_rock < count_scissors:
    pred = 1

# Create the player_score and comp_score variables.
player_score = 0
comp_score = 0

# Create the update_scores() function.
def update_scores(user_input):
  global player_score, comp_score
  # Rock wins over scissors, scissors win over paper and paper wins over rock.
  pred = predict()
  if user_input == 0:
    if pred == 0:
      print("\nYou played ROCK, computer played ROCK.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 1:
      print("\nYou played ROCK, computer played PAPER.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played ROCK, computer played SCISSORS.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
  elif user_input == 1:
    if pred == 0:
      print("\nYou played PAPER, computer played ROCK.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 1:
      print("\nYou played PAPER, computer played PAPER.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played PAPER, computer played SCISSORS.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
  elif user_input == 2:
    if pred == 0:
      print("\nYou played SCISSORS, computer played ROCK.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 1:
      print("\nYou played SCISSORS, computer played PAPER.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played SCISSORS, computer played SCISSORS.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)

# 1. Create a list: ['0', '1', '2'] and store it in the variable called valid_entries, i.e, valid_entries = ['0', '1', '2']
valid_entries = ["0", "1", "2"]
# 2. Create an infinite while loop. Inside the loop, create a variable called user_input to store the input taken by the player.
while True:
  user_input = input("Enter 0 for rock, 1 for paper, or 2 for scissors: ")
  # 3. Use the input() function to take input from a player.
  # Inside the input() function, write the Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: statement to show it as a message to a player.
  while (user_input not in valid_entries):
  # 4. Write another while loop to check whether the input provided by a player exists in the valid_entries list or not.
    print("Invalid Input!")
    user_input = input("Enter 0 for rock, 1 for paper, or 2 for scissors: ")
    # 5. If the input provided by a player does not exist in the valid_entries list, then print Invalid Input! message.
    # In the next line, rewrite the user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ") statement.
  user_input = int(user_input)
  # 6. Now, outside the inner while loop, convert the user_input value to an integer value using the int() function.
  update_scores(user_input)
  # 7. Call the update_scores() function with the user_input as an input to update the scores of the computer and the player.
  update_counts(user_input)
  # 8. Call the update_counts() function with the user_input as an input to update the counts of the inputs provided by the player.
  if (comp_score == 10):
    print("Computer Won")
  elif (player_score == 10):
    print("You won")
