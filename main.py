import pygetwindow as gw
import pytesseract
import pyautogui
import time
import threading

# left, top, width, height
region = (300, 475, 550, 550)
common = "Common" # pb(432, 889)
uncommon = "Uncommon" # gb(488, 881)
rare = "Rare" # ub(548, 886)
super_rare = "Super Rare" # (548, 886)
legendary = "Legendary" # mb (695, 876)
event_shiny = "Shiny (Event"
shiny = "Shiny (Full-odds" # prb (645, 899)

def main():
    while True:
        if is_discord_active():
            print("discord active")
            spawn()
            time.sleep(5)
        else:
            print("discord not active")

def is_discord_active():
    active_window = gw.getActiveWindow()
    time.sleep(0.25)
    return active_window and "Discord" in active_window.title

def spawn():
    pyautogui.write(';p')
    pyautogui.press('enter')
    time.sleep(1)
    threading.Thread(target=ss).start() # instantly take a ss after sending this command

def ss():
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("test.png") # temp for debugging
    extracted_text = pytesseract.image_to_string(screenshot)
    print(extracted_text)
    if uncommon in extracted_text:
        print('gb')

# TODO: def catch():   




if __name__ == "__main__":
    main()
    