import numpy as np
import cv2
import matplotlib.pyplot as plt
import seaborn
import matlab.engine

eng = matlab.engine.start_matlab()

image_path = 'path/to/image/'

image = cv2.imread(image_path)

image_gray = cv2.imread(image_path,0)




