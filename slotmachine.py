import random
icons = ["⭐", "🍒", "🍊", "🍋", "🍉", "🍇"]
print("Welcome to the Slot Machine Game")
balance = 100
play = str(input("Enter X to play: ")).upper()
print(f"Your balance is ${balance}")
while balance >0 and play == "X":
    in_play = str(input("Enter S to spin or anything else to stop:").upper())
    if in_play != "S":
        play = str(input("Enter X to play or Anything else to quit: ")).upper()
        if play != "X":
            print("Thanks for playing")
            exit()
    else:
        results = [random.choice(icons) for i in range(3)]
       
        if play != "X":
            print("Enter X to play or Q to quit")
            play = str(input("Enter X to play and Q to quit:")).upper()
        else:
            print(results)
            if(results[0] != results[1] != results[2]):
                balance -= 10
                print("You lost $10")
            elif( results[0] == results[1] == results[2]):
                balance += 50
                print("You won $50")
            elif(results[0] == results[1] or results[1] == results[2] or results[0] == results[2]):
                balance += 20   
                print("You won $20")
            print(f"Your balance is ${balance}")
