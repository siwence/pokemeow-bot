from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y})")

# Start listening for mouse events
with mouse.Listener(on_click=on_click) as listener:
    print("Click anywhere to see the cursor coordinates. Press Ctrl+C to stop.")
    listener.join()