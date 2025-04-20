import pyautogui

ScreenX,ScreenY = pyautogui.size()



loopcount = 25
pyautogui.FAILSAFE = True
mouseX,mouseY = pyautogui.position()


for x in range(loopcount):
    firefoxpos = pyautogui.locateOnScreen("firefox.png",confidence=0.9)
    firefoxpos = pyautogui.center(firefoxpos)
    pyautogui.leftClick(firefoxpos)

    pyautogui.leftClick(138,23) #click first tab on firefox
    snippos = pyautogui.locateOnScreen("snippingtool.png",confidence=0.9)
    snippos = pyautogui.center(snippos)
    pyautogui.leftClick(snippos)
    pyautogui.sleep(0.5)

    newbuttonpos = pyautogui.locateOnScreen("newbutton.png",confidence=0.99)
    newbuttonpos = pyautogui.center(newbuttonpos)
    pyautogui.leftClick(newbuttonpos)


    pyautogui.moveTo(163,121)
    pyautogui.dragTo(1749,1000)


    pyautogui.sleep(0.7) 
    try:
        extractbuttonpos = pyautogui.locateOnScreen("extractbutton.png",confidence=0.8)
    except pyautogui.ImageNotFoundException:
        try:
            extractbuttonpos = pyautogui.locateOnScreen("extractbutton2.png",confidence=0.7)
        except pyautogui.ImageNotFoundException:
            extractbuttonpos = pyautogui.locateOnScreen("extractbutton3.png",confidence=0.7)

    
    extractbuttonpos = pyautogui.center(extractbuttonpos)
    pyautogui.leftClick(extractbuttonpos)
    pyautogui.sleep(2) 


    copybutton = pyautogui.locateOnScreen("copyallbutton2.png",confidence=0.9)

    copybutton = pyautogui.center(copybutton)
    pyautogui.leftClick(copybutton)
    pyautogui.sleep(0.7)


    pyautogui.leftClick(firefoxpos)
    pyautogui.sleep(0.25)
    pyautogui.press('right')



    notepad = pyautogui.locateOnScreen("notepad.png",confidence=0.9)
    notepad = pyautogui.center(notepad)
    pyautogui.leftClick(notepad)

    pyautogui.hotkey('ctrl','v')
    for x in range(3):
        pyautogui.press('enter')
