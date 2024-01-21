import cv2
import mss
import numpy as np

bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
bush1_path = r"reference_images\bush1.PNG"
bush1_img = cv2.imread(bush1_path, cv2.IMREAD_UNCHANGED)

w = bush1_img.shape[1]
h = bush1_img.shape[0]

sct = mss.mss()

while True:
    sct_img = sct.grab(bounding_box)
    img = np.array(sct_img)
    
    result = cv2.matchTemplate(img, bush1_img, cv2.TM_CCOEFF_NORMED)        
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    threshold = .50
    yloc, xloc = np.where(result >= threshold)
        
    rectangles = []
    for (x, y) in zip(xloc, yloc):
        # puts two rectangles to avoid issues
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])
            
    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    
    for (x, y, w, h) in rectangles:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,255), 2)
    
    scaled_img = cv2.resize(img, (960, 540))
    cv2.imshow('Screen Capture', np.array(scaled_img))
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
    
    
       
cv2.destroyAllWindows()