from PIL import Image
import os

original=r'C:\\faculdades\\etec\\2024-1\\técnicas de programação e algoritmos\\alunos\\'
new_place=r"C:\\faculdades\\etec\\2024-1\\técnicas de programação e algoritmos\\alunos\\pronto\\"
for file in os.listdir(original):
    filename=file
    im=Image.open(original+filename)
    left=787
    top=30
    right=787+129
    bottom=30+187
    image_ok = im.crop((left, top, right, bottom))
    image_ok.save(new_place+filename)