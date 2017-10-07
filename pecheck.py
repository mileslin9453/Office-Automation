# Create Date:8/24/2017
# Author:Miles Lin
# Project Name:Automate PE Check
# Description:routine work
# Revision:1.0
# Additional Comments: reference http://blog.topspeedsnail.com/archives/5373


import pyautogui
import time

def timer(n):
    pyautogui.click(30,100,button='left')       # open WIP application
    time.sleep(1)                               # wait 1 sec
    pyautogui.click(765,540,button='left')      # execute update revision
    time.sleep(1)                               # wait 1 sec
    pyautogui.click(388,200,button='left')      # confirm execute
    time.sleep(90)                              # wait 90 sec for updating from server

    pyautogui.click(30,100,button='left')       # open WIP application
    time.sleep(1)                               # wait 1 sec
    pyautogui.click(772,237,button='left')      # open check in/out of production function
    time.sleep(1)                               # wait 1 sec

    pyautogui.typewrite('123456',0.1)           # keyin employee number and password
    pyautogui.press('tab')
    pyautogui.typewrite('123456',0.1)
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')                    # entry check in/out of production function
    time.sleep(1)

    pyautogui.click(150,330,button='left')      # click PE Check button
    time.sleep(1)
    pyautogui.click(606,535,button='left')      # click confirm buttons
    time.sleep(1)
    pyautogui.click(220,600,button='left')      # click PE Check All button

    for i in range(50,0,-1):                    # repeat 50 times click on pop-up windtow
        pyautogui.press('space')
        time.sleep(0.5)
        pyautogui.click(420,600,button='left')
    time.sleep(1)

    pyautogui.click(820,600,button='left')      # click exit option
    time.sleep(1)

    pyautogui.click(1430,4,button='left')       # close check in /out of production function
    pyautogui.click(1430,4,button='left')       # close WIP application
    time.sleep(n)

timer(1800)                                     # execute once every 30 min
