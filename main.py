import os
import cv2
from cvzone .HandTrackingModule import HandDetector
import numpy as np

# variables
width, height = 1280, 720
folderPath = "presentation"

# camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Get the list of presentation images
pathImages = sorted(os.listdir(folderPath), key=len)
# print(pathImages)

# Variables
imgNumber = 0
hs, ws = int(120*1), int(213*1)
gestureThreshold = 300
buttonPressed = False
buttonCounter = 0
buttonDelay = 10
annotation = [[]]
annotationNumber = -1
annotationStart = False

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    # Import Images
    success, img = cap.read()
    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands, img = detector.findHands(img)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)

    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        lmList = hand['lmList']

        # Constrain values for easier drawing
        xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
        yVal = int(np.interp(lmList[8][1], [150, height-200], [0, height]))
        indexFinger = xVal, yVal

        if cy <= gestureThreshold:  # if the hand is at the height of the face
            annotationStart = False

            # Gesture 1 - left
            if fingers == [1, 0, 0, 0, 0]:
                annotationStart = False
                print("left")
                if imgNumber > 0:
                    buttonPressed = True
                    annotation = [[]]
                    annotationNumber = 0
                    imgNumber -= 1

            # Gesture 2 - right
            if fingers == [0, 0, 0, 0, 1]:
                annotationStart = False
                print("right")
                if imgNumber < len(pathImages)-1:
                    buttonPressed = True
                    annotation = [[]]
                    annotationNumber = 0
                    imgNumber += 1

        # Gesture 3 - Draw Pointer
        if fingers == [0, 1, 1, 0, 0]:
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotationStart = False

            # Gesture 4 - Draw Pointer
        if fingers == [0, 1, 0, 0, 0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber += 1
                annotation.append([])
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotation[annotationNumber].append(indexFinger)
        else:
            annotationStart = False

        # Gesture 5 - Erase
        if fingers == [0, 1, 1, 1, 0]:
            if annotation:
                if annotationNumber >= 0:
                    annotation.pop(-1)
                    annotationNumber -= 1
                    buttonPressed = True
    else:
        annotationStart = False

# Button press iterations
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False

    for i in range(len(annotation)):
        for j in range(len(annotation[i])):
            if j != 0:
                cv2.line(imgCurrent, annotation[i][j - 1], annotation[i][j], (0, 0, 200), 12)

# Adding webcam image on the slides
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w-ws:w] = imgSmall

    cv2.imshow("Image", img)
    cv2.imshow("slides", imgCurrent)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
