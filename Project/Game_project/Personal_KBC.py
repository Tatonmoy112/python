import os
os.mkdir("data")

for i in range(1,101):
    os.mkdir(f"data/Day {i}")

qus_ans=[
    ["What is the capital city of bd?","Dhaka","Ctg","Rajshahi","Cox's Bazar",1],
    ["What is the small city of bd?","Dhaka","Ctg","Rajshahi","Cox's Bazar",4],
    ["What is the clean city of bd?","Dhaka","Ctg","Rajshahi","Cox's Bazar",3]
]

lvl=[1000,10000,100000]

for j in range(0,len(qus_ans)):
    question=qus_ans[j]
    print(f"Question for TK.{lvl[j]}")
    print(f"Question is {question[0]}")
    print(f"A.{question[1]}           B.{question[2]}")
    print(f"C.{question[3]}           D.{question[4]}")
    reply=int(input("Enter your answer :"))


    if(reply<0 or reply>4):
        raise ValueError("Input correct answer")
    if(reply==question[5]):
        print(f"Your answer is correct.Congs you win {lvl[j]} Tk right now..")
    else:
        print("your answer is wrong.. sorry next time try..")