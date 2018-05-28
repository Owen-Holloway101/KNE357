import cv2
import numpy as np
from visionUtils import findBlocks

print (cv2.__version__)

print ("starting vision")

cap = cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,720)

#colour defs

#light green
greenLower = np.array([45, 103, 56],np.uint8)
greenUpper = np.array([114, 255, 255],np.uint8)

orangeLower = np.array([0, 103, 56],np.uint8)
orangeUpper = np.array([0, 255, 255],np.uint8)

pinkLower = np.array([86, 103, 56],np.uint8)
pinkUpper = np.array([196, 255, 255],np.uint8)

yellowLower = np.array([16, 103, 56],np.uint8)
yellowUpper = np.array([37, 255, 255],np.uint8)

frames = 0
greenCounts = 0
orangeCounts = 0
pinkCounts = 0
yellowCounts = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frames = frames + 1

    FILTER_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    greenXY = findBlocks(frame,FILTER_HSV,greenLower,greenUpper,"Green")
    orangeXY = findBlocks(frame,FILTER_HSV,orangeLower,orangeUpper,"Orange")
    pinkXY = findBlocks(frame,FILTER_HSV,pinkLower,pinkUpper,"Pink")
    yellowXY = findBlocks(frame,FILTER_HSV,yellowLower,yellowUpper,"Yellow")

    yOffset = 715
    yStepUp = 15
    ySteps = 0

    cv2.putText(frame,"Total Frames: %i" % (frames), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))

    if((greenXY[0] > 0.00) & (greenXY[1] > 0.00)):
        greenCounts = greenCounts + 1
        cv2.putText(frame, "Green Block Location: (X %i) (Y %i) reliability: %i" % (greenXY[0], greenXY[1],greenCounts/frames*100),(0, yOffset - yStepUp*ySteps), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        ySteps = ySteps + 1

    if((orangeXY[0] > 0.00) & (orangeXY[1] > 0.00)):
        orangeCounts = orangeCounts + 1
        cv2.putText(frame, "Orange Block Location: (X %i) (Y %i) reliability: %i" % (orangeXY[0], orangeXY[1],orangeCounts/frames*100),(0, yOffset - yStepUp*ySteps), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        ySteps = ySteps + 1

    if((pinkXY[0] > 0.00) & (pinkXY[1] > 0.00)):
        pinkCounts = pinkCounts + 1
        cv2.putText(frame, "Pink Block Location: (X %i) (Y %i) reliability: %i" % (pinkXY[0], pinkXY[1],pinkCounts/frames*100),(0, yOffset - yStepUp*ySteps), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        ySteps = ySteps + 1

    if((yellowXY[0] > 0.00) & (yellowXY[1] > 0.00)):
        yellowCounts = yellowCounts + 1
        cv2.putText(frame, "Yellow Block Location: (X %i) (Y %i) reliability: %i" % (yellowXY[0], yellowXY[1],yellowCounts/frames*100),(0, yOffset - yStepUp*ySteps), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        ySteps = ySteps + 1

    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
