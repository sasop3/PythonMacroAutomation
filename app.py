import pyautogui

ScreenX,ScreenY = pyautogui.size()



pyautogui.FAILSAFE = True
mouseX,mouseY = pyautogui.position()
for x in range(30):
    firefoxpos = pyautogui.locateOnScreen("firefox.png")
    firefoxpos = pyautogui.center(firefoxpos)
    pyautogui.leftClick(firefoxpos)

    pyautogui.leftClick(138,23) #click first tab on firefox
    snippos = pyautogui.locateOnScreen("snippingtool.png")
    snippos = pyautogui.center(snippos)
    pyautogui.leftClick(snippos)
    pyautogui.sleep(0.5)

    newbuttonpos = pyautogui.locateOnScreen("newbutton.png")
    newbuttonpos = pyautogui.center(newbuttonpos)
    pyautogui.leftClick(newbuttonpos)


    pyautogui.moveTo(163,121)
    pyautogui.dragTo(1749,1000)


    pyautogui.sleep(0.7) 
    extractbuttonpos = pyautogui.locateOnScreen("extractbutton.png")
    extractbuttonpos = pyautogui.center(extractbuttonpos)
    pyautogui.leftClick(extractbuttonpos)
    pyautogui.sleep(2) 



    copybutton = pyautogui.locateOnScreen("copyallbutton.png")
    copybutton = pyautogui.center(copybutton)
    pyautogui.leftClick(copybutton)
    pyautogui.sleep(0.7)


    firefox2pos = pyautogui.locateOnScreen("firefox2.png")
    firefox2pos = pyautogui.center(firefox2pos)
    pyautogui.leftClick(firefox2pos)
    pyautogui.press('right')


    notepad = pyautogui.locateOnScreen("notepad.png")
    notepad = pyautogui.center(notepad)
    pyautogui.leftClick(notepad)

    pyautogui.hotkey('ctrl','v')
    for x in range(3):
        pyautogui.press('enter')
