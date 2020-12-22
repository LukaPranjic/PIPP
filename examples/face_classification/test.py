from paz.backend.image import load_image#, show_image, write_image
from input import EmotionDetector

def emotion(filepath)
    detect = EmotionDetector()
    # you can now apply it to an image (numpy array)
    #images = load_image('neo.png')
    return detect(load_image(filepath))
    #predictions = detect(images)
    # show_image(predictions)
    #write_image("faceClassification.png", predictions)
