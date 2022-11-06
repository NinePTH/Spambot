from distutils.command.bdist import show_formats
import pyautogui
import time
"""time.sleep(4)
count = 0
while count <= 20:
    pyautogui.typewrite("test")
    pyautogui.press("enter")
    count += 1
""" #for spam 1 str

time.sleep(5)
f = open("cowboy", encoding="utf8")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    #for spam entire text file
