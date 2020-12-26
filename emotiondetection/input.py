import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from paz.backend.image import load_image
from analyzer import EmotionDetector

detect = EmotionDetector()


# """# Function expects a filepath. Returns Boxes of 2D rectangles. Also included is the estimated emotion"""
# def emotionFinder(filepath):
#     return detect(load_image(filepath))

"""Function expects a numpy array image. Returns Boxes of 2D rectangles. Also included is the estimated emotion"""
def emotionFinder(image):
    return detect(image)

"""Incorporates the given image (expected as numpy array) with given Boxes of 2D rectangles"""
def incorporate(image, boxes2D):
    return detect.install(image, boxes2D)
