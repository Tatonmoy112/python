# import os, random
# if (not os.path.exists("PNG")):
#     os.mkdir("PNG")
# for i in range(10):
#     x=[]
#     a=['a','x','j','d','m','w']
#     x=a[random.randint(0,5)]+a[random.randint(0,5)]+a[random.randint(0,5)]+a[random.randint(0,5)]
#     os.mkdir(f"PNG/{x}.png")

import os
files=os.listdir("PNG")
i=1
for file in files:
    if file.endswith("txt"):
     os.rename(f"PNG/{file}",f"PNG/{i}.png")
    i+=1

files=os.listdir("PNG")
for file in files:
#    if file.endswith(".png"):
    print(file)