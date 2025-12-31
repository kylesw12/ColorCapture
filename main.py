import cv2
from PIL import Image
from util import get_limits

yellow = [0, 255, 255] # Yellow in BGR
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower, upper = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lower, upper) # Create a mask for yellow objects

    mask_ = Image.fromarray(mask) # convert from np array to a PILLOW image
    bbox = mask_.getbbox() # function from PILLOW to get bounding box of non-zero regions in the mask

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5) # Draw rectangle around detected object

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()