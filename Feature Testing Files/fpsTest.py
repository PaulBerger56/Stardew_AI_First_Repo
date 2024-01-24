import cv2
import mss
import numpy as np



bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
bush1_path = r"reference_images\bush1.PNG"
bush1_img = cv2.imread(bush1_path, cv2.IMREAD_UNCHANGED)

log1_path = r"reference_images\log1.PNG"
log1_img = cv2.imread(log1_path, cv2.IMREAD_UNCHANGED)

w = bush1_img.shape[1]
h = bush1_img.shape[0]

log_1_w = log1_img.shape[1]
log_1_h = log1_img.shape[0]

sct = mss.mss()

while True:
    sct_img = sct.grab(bounding_box)
    img = np.array(sct_img)
    
    # bush 1 
    bush_1_result = cv2.matchTemplate(img, bush1_img, cv2.TM_CCOEFF_NORMED)        
    bush_1_min_val, bush_1_max_val, bush_1_min_loc, bush_1_max_loc = cv2.minMaxLoc(bush_1_result)
    
    bush_1_threshold = .48
    bush_1_yloc, bush_1_xloc = np.where(bush_1_result >= bush_1_threshold)
    
    log_1_result = cv2.matchTemplate(img, log1_img, cv2.TM_CCOEFF_NORMED)
    log_1_min_val, log_1_max_val, log_1_min_loc, log_1_max_loc = cv2.minMaxLoc(log_1_result)
    
    log_1_threshhold = .48
    log_1_yloc, log_1_xloc = np.where(log_1_result >= log_1_threshhold)
        
    rectangles = []
    for (x, y) in zip(bush_1_xloc, bush_1_yloc):
        # puts two rectangles to avoid issues
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])
        
    for (x, y) in zip(log_1_xloc, log_1_yloc):
        # puts two rectangles to avoid issues
        rectangles.append([int(x), int(y), int(log_1_w), int(log_1_h)])
        rectangles.append([int(x), int(y), int(log_1_w), int(log_1_h)])        
    
            
    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    
    for (x, y, w, h) in rectangles:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,255), 2)
    
    scaled_img = cv2.resize(img, (960, 540))
    cv2.imshow('Screen Capture', np.array(scaled_img))
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
    
    
       
cv2.destroyAllWindows()