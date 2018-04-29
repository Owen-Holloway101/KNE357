import cv2
import numpy as np

print (cv2.__version__)

print ("starting vision")

cap = cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,720)

#colour defs
greenLower = np.array([82, 42, 19],np.uint8)
greenUpper = np.array([215, 204, 204],np.uint8)

yellowLower = np.array([29, 86, 6],np.uint8)
yellowUpper = np.array([229, 255, 100],np.uint8)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    FILTER_GREEN = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FILTER_YELLOW = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mask_green = cv2.inRange(FILTER_GREEN, greenLower, greenUpper)
    mask_green = cv2.erode(mask_green, None, iterations=2)
    mask_green = cv2.dilate(mask_green, None, iterations=2)

    mask_yellow = cv2.inRange(FILTER_YELLOW, yellowLower, yellowUpper)
    mask_yellow = cv2.erode(mask_yellow, None, iterations=2)
    mask_yellow = cv2.dilate(mask_yellow, None, iterations=2)

    cntsgreen = cv2.findContours(mask_green.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    cntsyellow = cv2.findContours(mask_yellow.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    #print("found %i green box(s) found %i yellow box(s)" % (len(cntsgreen),len(cntsyellow)),end="\r")

    if len(cntsgreen) > 0:
        c = max(cntsgreen, key=cv2.contourArea)
        M = cv2.moments(c)
        #print(M)


    # Display the resulting frame
    cv2.imshow('frame',mask_green)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
