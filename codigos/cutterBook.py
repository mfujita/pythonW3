from PIL import Image
import os

original=r'C:\Livros\Arquitetura e organizacao de computadores\\'
new_place=r"C:\Livros\Arquitetura e organizacao de computadores\\trimmed\\"
for file in os.listdir(original):
    filename=file
    im=Image.open(original+filename)
    left=270
    top=202
    right=left+540
    bottom=top+724
    image_ok = im.crop((left, top, right, bottom))
    image_ok.save(new_place+filename)