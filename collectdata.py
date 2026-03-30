import os
import cv2

# Initialize video capture from the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Directory where captured images will be saved
directory = 'Image/'

# Ensure all subdirectories A-Z exist
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    os.makedirs(os.path.join(directory, letter), exist_ok=True)

while True:
    # Read a frame from the video capture
    _, frame = cap.read()
    
    # Count the number of images in subdirectories A to Z
    count = {letter: len(os.listdir(os.path.join(directory, letter))) for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    
    # Draw a rectangle as a background for text overlay
    cv2.rectangle(frame, (0, 40), (300, 400), (255, 255, 255), 2)
    
    # Display count for each character
    y_offset = 100
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        cv2.putText(frame, f"{letter} : {count[letter]}", (10, y_offset), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
        y_offset += 10
    
    # Show the frame in a window named "data"
    cv2.imshow("data", frame)
    
    # Show the region of interest (ROI) in a separate window named "ROI"
    cv2.imshow("ROI", frame[40:400, 0:300])
    
    # Crop the frame to the region of interest (ROI)
    frame = frame[40:400, 0:300]
    
    # Wait for a key press event and store the key code in 'interrupt'
    interrupt = cv2.waitKey(10) & 0xFF
    
    # Save image to the respective folder based on key press
    if chr(interrupt).upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letter = chr(interrupt).upper()
        cv2.imwrite(os.path.join(directory, letter, f"{count[letter]}.png"), frame)

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
