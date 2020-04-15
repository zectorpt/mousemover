import pyautogui, time
print("\n\nExiting by CTRL+C.\n\n")
i=0
while i <= 10:
	pyautogui.move(2, 2)
	pyautogui.move(-2, -2)
	time.sleep (5)
