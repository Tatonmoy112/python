import qrcode
from PIL import Image
ipt=input("Enter link or text that you want to make into QR Code: ")
out_name=input("What name do you want to save QR Code: ")
design=qrcode.QRCode(version=1 , error_correction=qrcode.constants.ERROR_CORRECT_H , box_size=20 , border=6)
design.add_data(f"{ipt}")
design.make(fit=True)
img=design.make_image(fill_color="black",back_color="white")
img.save(f"{out_name}.png")

# #Normal way
# import qrcode
# ipt=input("Enter link or text that you want to make into QR Code: ")
# out_name=input("What name do you want to save QR Code: ")
# img=qrcode.make(f"{ipt}")
# img.save(f"{out_name}")