import random
print("Welcome to Rock Paper Sissors")
print("Press x for rock, y for paper and z for sissors")
user_input = str(input("Enter your choice: ")).lower()
while user_input == "":
      user_input = str(input("Enter your choice: ")).lower()
      print("Choose x,y,z")
bot_play = ["rock","paper","sissor"]
bot_output = random.choice(bot_play)
if bot_output == "rock" and user_input == "z" :
    print(f"Bot choose {bot_output}, Bot wins")
elif bot_output == "paper" and user_input == "x":
     print(f"Bot choose {bot_output}, Bot wins")
elif bot_output == "sissor" and user_input == "y":
      print(f"Bot choose {bot_output}, Bot wins")
elif bot_output =="rock" and user_input == "y":
     print(f"Player wins, bot choose {bot_output}")
elif bot_output == "paper" and user_input =="z":
       print(f"Player wins, bot choose {bot_output}")
elif bot_output == "sissor" and user_input =="x":
       print(f"Player wins, bot choose {bot_output}")
