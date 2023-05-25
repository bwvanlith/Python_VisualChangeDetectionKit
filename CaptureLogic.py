import os
import pyautogui
import datetime
import time

# Set the interval between each screen capture (in seconds)
interval = 5

# Set the directory where the captured images will be saved
output_directory = "screenshots/"

# Create the directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)


# Function to capture the screen and save it as an image
def capture_screen():
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Capture the screen and save it as an image
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{output_directory}screenshot_{timestamp}.png")


# Main loop to capture the screen at the specified interval
try:
    while True:
        capture_screen()
        time.sleep(interval)
except KeyboardInterrupt:
    print("Screen capturing stopped.")
