import cv2
import numpy as np

print (cv2.__version__)

print ("starting vision")

cap = cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,720)

#colour defs
greenLower = np.array([0, 0, 62],np.uint8)
greenUpper = np.array([180, 180, 180],np.uint8)

yellowLower = np.array([29, 86, 6],np.uint8)
yellowUpper = np.array([229, 255, 100],np.uint8)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    FILTER_YELLOW = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mask_green = cv2.inRange(frame, greenLower, greenUpper)
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
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cntsgreen, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)


    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
