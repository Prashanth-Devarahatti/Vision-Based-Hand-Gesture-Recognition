# Hand Gesture Recognition

This project utilizes computer vision techniques to recognize hand gestures captured via a webcam. It employs the MediaPipe library to detect hand landmarks and analyze their positions to recognize gestures in real-time.

## Dependencies:

- Python 3.x
- OpenCV (`cv2`)
- Mediapipe (`mediapipe`)

You can install the required dependencies via pip:

```
pip install opencv-python mediapipe
```

## Usage:

1. Connect a webcam to your computer.
2. Run the Python script provided in this repository.
3. The webcam feed will open, and the system will start recognizing hand gestures.
4. Perform various hand gestures in front of the webcam.
5. The recognized gesture will be displayed on the screen.

## Code Structure:

- **mp_hands.Hands()**: Initializes the MediaPipe hands module with specific configuration parameters.
- **gesture_dict**: A dictionary mapping gesture IDs to their meanings.
- **main()**: The main function that captures frames from the webcam, processes them, recognizes gestures, and displays the results.
- **recognize_gesture(landmarks)**: This function implements gesture recognition logic based on the positions of hand landmarks detected by MediaPipe.
- **cv2.VideoCapture(0)**: Opens the default camera (webcam).
- **cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)**: Converts the captured frame to RGB format for processing with MediaPipe.
- **cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)**: Displays the recognized gesture on the screen.
- **cv2.imshow('Hand Gesture Recognition', frame)**: Displays the webcam feed with the recognized gesture.
- **cv2.waitKey(1)**: Waits for a key press to exit the program.

## Notes:

- Ensure that you have a working webcam connected to your system.
- Make sure that your environment is suitable for hand detection (sufficient lighting, clear background, etc.).
- Experiment with different hand gestures and positions to test the accuracy of gesture recognition.
- This example uses a simple distance-based gesture recognition logic. For more complex gesture recognition, you would replace this with your actual gesture recognition model.
- Feel free to modify and extend the code according to your requirements.

---
Feel free to customize the README further with additional sections or details as needed!
