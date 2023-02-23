'''In this code, we use the cv2.VideoCapture() function to 
open the camera. We then use a while loop to continuously 
capture frames from the camera using the camera.read() method. 
We show each frame in a window using the cv2.imshow() function,
and wait for a key event using the cv2.waitKey() method. If 
the 'q' key is pressed, we break out of the loop and release 
the camera using the camera.release() method, and destroy the 
window using the cv2.destroyAllWindows() method.'''


import cv2

camera = cv2.VideoCapture(0) # open the camera

while True:
    # capture each frame
    ret, frame = camera.read()

    # show the frame in a window
    cv2.imshow("Camera", frame)

    # wait for a key event
    key = cv2.waitKey(1)

    # if 'q' is pressed, break the loop
    if key == ord('q'):
        break

# release the camera and destroy the window
camera.release()
cv2.destroyAllWindows()
