from PIL import Image
import os

original=r'C:\\Livros\\arq2\\'
new_place=r"C:\Livros\arq2\\trimmed\\"
for file in os.listdir(original):
    filename=file
    im=Image.open(original+filename)
    left=138
    top=93
    right=left+(917-left)
    bottom=top+(1183-top)
    image_ok = im.crop((left, top, right, bottom))
    image_ok.save(new_place+filename)