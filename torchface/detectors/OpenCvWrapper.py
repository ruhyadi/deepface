"""OpenCV Face Detection Wrapper"""

from genericpath import isfile
from pathlib import Path
import cv2
import os
import pandas as pd
from torchface.detectors import FaceDetector

def build_model():

    detector = {}

    detector["face_detector"] = build_cascade('haarcascade')
    detector["eye_detector"] = build_cascade('haarcascade_eye')

    return detector

def build_cascade(model_name: str = "haarcascade"):
    """Build cascade classifier"""
    opencv_path = get_opencv_path()

    assert model_name in ["haarcascade", "haarcascade_eye"], "Model name not supported"

    if model_name == "haarcascade":
        face_detector_path = opencv_path / "haarcascade_frontalface_default.xml"
        if os.path.isfile(face_detector_path) != True:
            raise ValueError("Confirm that opencv is installed on your environment! Expected path ", face_detector_path, " violated.")
        
        face_detector = cv2.CascadeClassifier(face_detector_path)
        return face_detector
    elif model_name == "haarcascade_eye":
        eye_detector_path = opencv_path / "haarcascade_eye.xml"
        if os.path.isfile(eye_detector_path) != True:
            raise ValueError("Confirm that opencv is installed on your environment! Expected path ", eye_detector_path, " violated.")
        
        eye_detector = cv2.CascadeClassifier(eye_detector_path)
        return eye_detector

def detect_face(detector, img, align = True):
    """Detect face"""
    resp = []
    detected_face = None
    img_region = [0, 0, img.shape[0], img.shape[1]]

    faces = []

    return 0

def get_opencv_path() -> Path:
    """Get opencv library path"""
    opencv_home = cv2.__file__
    folders = opencv_home.split(os.path.sep)[0:-1]

    path = Path(folders[0])
    for folder in folders[1:]:
        path = path / folder

    return path / "data"

if __name__ == "__main__":

    path = get_opencv_path()

    print(path)