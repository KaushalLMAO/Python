import random
print("Welcome to Dice Game")
data = [1,2,3,4,5,6]
score = 0
imp = str(input("Press p to play: ")).lower()
user_input = int(input("Enter your choice: "))
while user_input >= 6 or user_input <= 1:
    print("Choose between 1 to 6")
    user_input = int(input("Enter your choice: "))
bot_output = random.choice(data)
if bot_output == user_input:
    print(f" player wins on first try")
    score += 2
else:
     print("Wrong, second try")
     user_input = int(input("Enter your choice: "))
     if user_input == bot_output:
       print("Player wins on second try")
       score += 1
     else:
      print(f"Bot chose {bot_output}, Bot wins")
      score = 0
print(f"Score: {score}")