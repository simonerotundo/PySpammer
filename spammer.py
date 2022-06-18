import pyautogui, time

time.sleep(5)
f = open("list", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

print("+++ END +++")