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

bush1_path = r"reference_images\bush1.PNG"
bush1_img = cv2.imread(bush1_path, cv2.IMREAD_UNCHANGED)

# Gets the width and height of our reference image so we can draw rectangles around matches 
w = bush1_img.shape[1]
h = bush1_img.shape[0]


with mss.mss() as sct:
    while True:       
      
        
        screen = np.array(sct.grab(main_monitor))    
            
        # Moved this line lower after modifying the screen with rectangles
        # img = cv2.resize(screen, (frameWidth, frameHeight))
        
        # cv2.imshow("Screen Recording", img)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break
        
        # Template matching for the bush on the screen        
        result = cv2.matchTemplate(screen, bush1_img, cv2.TM_CCOEFF_NORMED)
        
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        # Create rectangles around matches
        cv2.rectangle(screen, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
        img = cv2.resize(screen, (frameWidth, frameHeight))
        cv2.imshow('Rectangles', img)
        
        # Creates the heatmap and produces it in a new window
        # heatmap = cv2.resize(result, (frameWidth, frameHeight))
        # cv2.imshow('Heatmap', heatmap)
        
        
        
        # print(f'Max location: {max_loc} Max Val: {max_val}')
        
       
        
        
# Release the window and close it
cv2.destroyAllWindows()
