import os
from PIL import Image

directory = "C:/Users/PaulE/Documents/DataSet/AbstractArt"

gen = (Image.open(os.path.join(directory, fichier_name)) for fichier_name in os.listdir(directory) if fichier_name.endswith(".jpg"))

def load_images(directory):
    liste_fichier = os.listdir(directory)
    for fichier_name in liste_fichier:
        if fichier_name.endswith(".jpg"):
            image_path_absolute = os.path.join(directory, fichier_name)
            image = Image.open(image_path_absolute)
            yield image
          
gen = load_images(directory)
for i, image in enumerate(gen):
    image_path_absolute = os.path.join(directory, "test", f"{i}.png")
    image.save(image_path_absolute)

C:/Users/PaulE/Documents/DataSet/AbstractArt \ test \ 1.png
C:/Users/PaulE/Documents/DataSet/AbstractArt / test / 1.png