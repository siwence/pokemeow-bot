import pygetwindow as gw
import pytesseract
import pyautogui
import time
import threading

# left, top, width, height
region = (300, 475, 550, 550)

# rarity
common = "Common" 
uncommon = "Uncommon" 
rare = "Rare" 
super_rare = "Super Rare" 
legendary = "Legendary" 
event_shiny = "Shiny (Event"
shiny = "Shiny (Full-odds" 

# balls
pb = (432, 910)
gb = (488, 912)
ub = (548, 914)
prb = (645, 916)
mb = (695, 918)


def main():
    while True:
        if is_discord_active():
            print("discord active")
            spawn_and_catch()
        else:
            print("discord not active")

def is_discord_active():
    active_window = gw.getActiveWindow()
    time.sleep(0.25)
    return active_window and "Discord" in active_window.title

def spawn_and_catch():
    pyautogui.write(';p')
    pyautogui.press('enter')
    time.sleep(1)
    threading.Thread(target=ss).start() # instantly take a ss after sending this command
    extracted_text = ss()
    catch(extracted_text)
    time.sleep(8.25)

def ss():
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("test.png") # temp for debugging
    extracted_text = pytesseract.image_to_string(screenshot)
    print(extracted_text)
    return extracted_text
    

def catch(extracted_text):   
    actions = {
        common: ("pb", pb),
        uncommon: ("gb", gb),
        rare: ("ub", ub),
        super_rare: ("ub", ub),
        legendary: ("mb", mb),
        event_shiny: ("mb", mb),
        shiny: ("prb", prb),
    }

    for rarity, (message, position) in actions.items():
        if rarity in extracted_text:
            print(message)
            pyautogui.click(position)

if __name__ == "__main__":
    main()
    