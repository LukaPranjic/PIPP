from input import emotionFinder, incorporate
from paz.backend.image import show_image, load_image

boxes2D = emotionFinder("neo.png")
image = load_image("neo.png")

finalImage = incorporate(image, boxes2D)
show_image(finalImage)
quit()
