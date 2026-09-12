email=input("Enter your email for check it's valid or not: ")
k=0
if len(email)>=6:
    if email[0].isalpha():
        if "@" in email and email.count("@")==1:
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==" ":
                        k+=1
                    elif i.isalpha():
                        if i==i.upper():
                            k+=1
                    elif i.isdigit():
                        continue
                    elif i == "@" or i == "." or i == "_":
                        continue
                    else:
                        k+=1
                if k>0:
                    print("Wrong Email")
                elif(k==0):
                    print("Valid Email.")
            else:
                print("Wrong Email")
        else:
            print("Wrong Email")
    else:
        print("Wrong Email")
else:
    print("Wrong Email")
