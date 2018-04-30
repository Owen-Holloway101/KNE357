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
greenLower = np.array([51, 60, 60],np.uint8)
greenUpper = np.array([84, 255, 255],np.uint8)

orangeLower = np.array([0, 155, 79],np.uint8)
orangeUpper = np.array([35, 255, 255],np.uint8)

pinkLower = np.array([79, 138, 80],np.uint8)
pinkUpper = np.array([183, 255, 255],np.uint8)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    FILTER_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    greenXY = findBlocks(frame,FILTER_HSV,greenLower,greenUpper,"Green")
    orangeXY = findBlocks(frame,FILTER_HSV,orangeLower,orangeUpper,"Orange")
    pinkXY = findBlocks(frame,FILTER_HSV,pinkLower,pinkUpper,"Pink")
    
    yOffset = 715
    yStepUp = 15
    ySteps = 0
    
    if((greenXY[0] > 0.00) & (greenXY[1] > 0.00)):
        cv2.putText(frame, "Green Block Location: (X %i) (Y %i) " % (greenXY[0], greenXY[1]),(0, yOffset - yStepUp*ySteps), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        ySteps = ySteps + 1
    
    if((orangeXY[0] > 0.00) & (orangeXY[1] > 0.00)):
        cv2.putText(frame, "Orange Block Location: (X %i) (Y %i) " % (orangeXY[0], orangeXY[1]),(0, yOffset - yStepUp*ySteps), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        ySteps = ySteps + 1
        
    if((pinkXY[0] > 0.00) & (pinkXY[1] > 0.00)):
        cv2.putText(frame, "Pink Block Location: (X %i) (Y %i) " % (pinkXY[0], pinkXY[1]),(0, yOffset - yStepUp*ySteps), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        ySteps = ySteps + 1
        
    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
