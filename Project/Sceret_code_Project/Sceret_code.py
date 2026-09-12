st=input("Enter your string: ")
coding=input("1 for Coding or 0 for Decoding: ")
import random

words=st.split(" ")
coding=True if (coding=="1") else False
if(coding):
    nwords=[]
    n=["xyz","abc","hdf","wld","jas","vqp"]
    for word in words:
        if(len(word)>=3):
            stwords=random.choice(n)+word[1:]+word[0]+random.choice(n)
            nwords.append(stwords)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stwords=word[3:-3]
            stwords=stwords[-1]+stwords[:-1]
            nwords.append(stwords)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))