import pyautogui, time, sys
from datetime import datetime
pyautogui.FAILSAFE = False
print("Exiting by CTRL+C.\n")
print("\n\n\nhttps://github.com/zectorpt/mousemover \nV 0.3\n")
i=0
while i <= 10:
	pyautogui.move(5, 5)
	pyautogui.move(-5, -5)
	pyautogui.press("shift")
	print("Movement made at {}".format(datetime.now().time()))
	time.sleep (5)
