import pygetwindow as gw
import pyautogui
import time

# left, top, width, height
region = (300, 475, 550, 550)

def pkmon():
    pyautogui.write(';p')
    pyautogui.press('enter')
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("test.png") # temp for debugging
        

def is_discord_active():
    active_window = gw.getActiveWindow()
    time.sleep(1)
    return active_window and "Discord" in active_window.title
    
def main():
    while True:
        if is_discord_active():
            print("discord active")
            pkmon()
            time.sleep(5)
        else:
            print("discord not active")


if __name__ == "__main__":
    main()