import random


print("welcome to Number Guessing Game!")
upper=int(input("Enter upper number: "))
lower=int(input("Enter lower number: "))
c_guess=random.randint(lower,upper)
count=0
while True:
    u_guess=int(input("Enter your guess number: "))
    if(u_guess==c_guess):
        count+=1
        break
    elif(u_guess>c_guess):
        count+=1
        print("You guessed too high!")
    elif(u_guess<c_guess):
        count+=1
        print("You guessed too small!")
    elif(u_guess>upper or u_guess<lower):
        count+=1
        print("You guessed out of limit!")
print(f"Congralations you did it in {count} try..")