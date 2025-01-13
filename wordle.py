import random
import time

words = ["JAVA",
         "PYTHON",
         "JAVASCRIPT",
         "BEDROCK",
         "COPY",
         "PEN"
         ]
tries = 5
word = random.choice(words)
print(word)
print("Please enter a word.")
if word == "JAVA":
    print("Hint: A programming language")
    print("The word has 4 letters.")
    print("The word starts with J.")
elif word == "PYTHON":
   print("Hint: A programming language")
   print("The word has 6 letters.")
   print("The word starts with P.")
   print("The word ends with N.")

elif word == "JAVASCRIPT":  
    print("Hint: A programming language")
    print("The word has 10 letters.")
    print("The word starts with J.")
    print("The word ends with T.")

elif word == "BEDROCK": 
    print("Hint: A type of rock")
    print("The word has 7 letters.")
    print("The word starts with B.")
    print("The word ends with K.")
    print("It is a minecraft edition.")

elif word == "COPY":
    print("Hint: A type of action")
    print("The word has 4 letters.")
    print("The word starts with C.")
    print("You do this and paste.")
elif word == "PEN":
    print("Hint: A writing tool")
    print("The word has 3 letters.")
    print("The word starts with P.")
    print("You use this to write.")
while tries > 1 :
 print(f"You have {tries} tries left.")
 user_input = str(input("Enter a letter: ")).upper()
 if word == user_input:
    print("You guessed the word!")
    
    exit()
        
 else:
    print("Wrong word. Try again.")
    if user_input in word:
       print("You have a correct letter in the word.")
    else:
       print("Nothing is right")
    user_input = str(input("Enter a letter: ")).upper()
 
 tries  = tries -1    

print(f"Your tries are over. The word was {word}")