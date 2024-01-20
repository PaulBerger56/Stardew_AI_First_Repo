import cv2
import mss
import numpy as np

# Grabs the monitors
monitors = mss.mss().monitors
'''
I have a multi monitor setup.  monitors[1] seems to isolate only my main monitor.
monitors[0] grabs both of my monitor's displays as one large monitor. 
Theoretically monitors[0] should work fine for a single monitor setup.
'''

main_monitor = monitors[1]

frameWidth = int(main_monitor['width'] * 0.5)
frameHeight = int(main_monitor['height'] * 0.5)

with mss.mss() as sct:
    while True:       
      
        
        screen = np.array(sct.grab(main_monitor))    
            
        
        img = cv2.resize(screen, (frameWidth, frameHeight))
        
        cv2.imshow("Result", img)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break
        
        
# Release the window and close it
cv2.destroyAllWindows()
