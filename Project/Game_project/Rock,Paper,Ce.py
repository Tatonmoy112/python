import random
print("Welcome to S,G,W Game..!!")
print("You have 3 option: S , G , W ")
predic=[['T','W','L'],['L','T','W'],['W','L','T']]
ipt=input("Enter your option: ").upper()
com=random.randint(0,2)
player={'S':0,'G':1,'W':2}[ipt]
com_pre=['S','G','W']
result=predic[com][player]
print(f"Your choice is {ipt} and Computer chose {com_pre[com]}")
if(result=='W'):
    print("You  ar win..")
elif(result=="L"):
    print("Game over..")
else:
    print("Draw")



# print("Welcome to S,G,W Game..!!")
# print("You have 3 option: S , G , W ")
# ipt=input("Enter your option: ").upper()
# # lst=[['S','G','W'],['R','P','C'],['R','P','C']]
# lst=['S','G','W']
# ran=random.choice(lst)
# if(ipt==ran):
#     print("Draw..")
# elif(ipt == "G" and ran == "S"):
#     print("You are win..")
# elif(ipt == "S" and ran == "W"):
#     print("You are win..")
# elif(ipt == "W" and ran == "G"):
#     print("You are win..")
# else:
#     print("Game over..")