import requests
from PIL import Image
from io import BytesIO
from tqdm import tqdm
option=["1.Image","2.File,exe,mp3,movie"]
print(f"Welcome to TAT Download Manager.\nWhich kind of file you want to dwonload?\n{option[0]}\n{option[1]}")
opi=int(input("Input your answer: "))

if(opi==1):
    print(f"You choose {option[opi-1]} this option.")
    url=input("Input your image url : ")
    output=input("What name do you want to save the image? ")
    r=requests.get(url)
    i=Image.open(BytesIO(r.content))
    with open(f"{output}.jpg","wb") as fp:
        i.save(fp)
elif(opi==2):
    print(f"You choose {option[opi-1]} this option.")
    url=input("Input your File,exe,mp3,movie url : ")
    output=input("What name do you want to save the image? Add extenstion like(.exe, .mp3, .mp4, .wav) ")
    r=requests.get(url , stream=True)
    totalBytes=int(r.headers["Content-Length"])
    Byte_Rec=0
    progress_bar=tqdm(total=totalBytes,unit='iB',unit_scale=True)
    with open(f"{output}.","wb") as fp:
        for chunk in r.iter_content(chunk_size=128):
            progress_bar.update(128)   
            fp.write(chunk)
            Byte_Rec+=128
        progress_bar.close()