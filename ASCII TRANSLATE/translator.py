import datatranslate
user_input = input("Enter a word: ")
for letter in user_input:
        print(datatranslate.values[letter], end="")