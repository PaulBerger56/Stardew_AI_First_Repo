import pyautogui, time, pydirectinput, cv2

def main():
    
    print(cv2.getVersionMajor())
    
    # Initialized PyAutoGui
    pyautogui.FAILSAFE = True
    
    # Countdown timer
    print("Starting", end="")
    for i in range(0, 5):
        print(".", end="")
        time.sleep(1)
    print("\nGo")
    
    # Do anything in game to check inputs
    # IDE must be in Administrator mode to press keys in game
    pydirectinput.keyDown(key='a')
    time.sleep(1.2)
    pydirectinput.keyUp(key='a')
    
    pydirectinput.keyDown(key='s')
    time.sleep(1)
    pydirectinput.keyUp(key='s')
    
    pydirectinput.keyDown(key='w')
    time.sleep(1)
    pydirectinput.keyUp(key='w')
    
    pydirectinput.keyDown(key='x')
    time.sleep(1.5)
    pydirectinput.keyUp(key='x')
    
    pydirectinput.keyDown(key='w')
    time.sleep(.2)
    pydirectinput.keyUp(key='w')
    
    pydirectinput.keyDown(key='d')
    time.sleep(1.2)
    pydirectinput.keyUp(key='d')
    
    
    
    
    
    
    # Done
    print("Done")
    
    
    
if __name__ == "__main__":
    main()
    
   