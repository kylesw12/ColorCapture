import cv2
from util import get_limits

yellow = [0, 255, 255] # Yellow in BGR
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower, upper = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lower, upper) # Create a mask for yellow objects

    cv2.imshow('frame', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()