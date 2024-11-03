# Module
import cv2
import random
import os
from os.path import join as jn

# Data Definitions
PATH = "./images"
DEST_PATH = "./resImages"

for folder in os.listdir(PATH):
    targetFolder = jn(PATH, folder)
    for file in os.listdir(targetFolder):
        relativePathFile = jn(targetFolder, file)

        # resize the image
        img = cv2.imread(relativePathFile, cv2.IMREAD_UNCHANGED)
        res_img = cv2.resize(img, (28, 28))

        # rename the image
        newFileName = "28_" + file
        newImageName = jn(DEST_PATH, folder, newFileName)
        cv2.imwrite(newImageName, res_img)

        # save the image

# Code