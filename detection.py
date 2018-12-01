from pynput.keyboard import Key, Controller
import numpy as np 
import cv2

#######################
### SETUP CONSTANTS ###
#######################

# Thresholds before sensing inputs
x_threshold = 50
y_threshold = 50

# The keys to press
key_x_below_threshold = Key.right    # x < x_threshold
key_x_above_threshold = Key.left   # x > x_threshold
key_y_below_threshold = Key.down    # y < y_threshold
key_y_above_threshold = Key.up      # y > y_threshold

############################
### FUNCTION DEFINITIONS ###
############################

# Converts screen coordinates to cartesian coordinates
def cartesian_coordinates(sx, sy, fw, fh):
    cx = sx - (fw/2)
    cy = (fh/2) - sy
    return (cx, cy)

# Gets the midpoint of a box
def middle_of_box (x,y,w,h):
    mx = x + (w/2)
    my = y + (h/2)
    return mx, my

########################
### MAIN CODE MODULE ###
########################

def main():
    wait_for_inputs = 100

    # Keyboard Controller for inputs
    keyboard = Controller()

    # Haar Cascade for face detction
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

    # The webcam capture
    cap = cv2.VideoCapture(0)
    f_width = cap.get(3)
    f_height = cap.get(4)

    while(True):

        ret, frame = cap.read()

        # Detect the faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x,y,w,h) in faces:
            # Convert to cartesian
            mx, my = middle_of_box(x,y,w,h)
            cx, cy = cartesian_coordinates(mx,my,f_width,f_height)
            print(cx, cy)
            
            # Control the inputs based on the position of the face
            if (wait_for_inputs == 0):
                if (cx < -x_threshold):
                    keyboard.press(key_x_below_threshold)
                elif (cx > x_threshold):
                    keyboard.press(key_x_above_threshold)
                if (cy < -y_threshold):
                    keyboard.press(key_y_below_threshold)
                elif (cy > y_threshold):
                    keyboard.press(key_y_above_threshold)

            # Draw a rectangle at the face
            rect_color = (255,0,0)
            stroke = 2
            end_x = x + w
            end_y = y + h
            cv2.rectangle(frame, (x,y), (end_x,end_y), rect_color, stroke)
        
        if (wait_for_inputs > 0):
            wait_for_inputs -=1

        # The web cam frame
        cv2.imshow('WebCam',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When done, exit cleanly
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()