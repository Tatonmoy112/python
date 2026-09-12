import random

all_words = ["Tanvir","Ahmed","Tonmoy"]
word = random.choice(all_words).lower()
display = []
chances = 6

for i in range(len(word)):
    display += "_"

over=False

print("Welcome to Hangman Game!")
ipt = input("Do you want to start the game? (Yes/No) :")
print("---------------------------------------")
if ipt == "Yes" or ipt=="yes" or ipt =="y" or ipt=="Y":
    while not over:
        user_guess=input(f"{display} your chance remaning {chances}. Now enter a character: ")
        for pos in range(len(word)):
            i=word[pos]
            if i==user_guess:
                display[pos]=user_guess
        print(f"Result: {"".join(display).capitalize()}\n----------------------------------")
        if user_guess not in word:
            chances-=1
            if chances==0:
                over=True
                print("Game is over!")
        if "_" not in display:
            over=True
            print("You are win.")
elif ipt=='no' or ipt=='n' or ipt=='No' or ipt=='N':
    print("You quit the game.")
else:
    print("You enter invaild.\nPlease try again")