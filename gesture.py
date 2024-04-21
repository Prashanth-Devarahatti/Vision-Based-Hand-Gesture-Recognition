import cv2
import mediapipe as mp

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

# Gesture dictionary mapping gesture IDs to their meanings
gesture_dict = {
    0: "Fist",
    1: "L",
    2: "Peace",
    # Add more gestures as needed
}


def main():
    cap = cv2.VideoCapture(0)  # Open default camera
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the image with MediaPipe hands
        results = hands.process(image)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get hand landmarks
                landmarks = [[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]

                # Perform gesture recognition
                gesture_id = recognize_gesture(landmarks)
                gesture = gesture_dict.get(gesture_id, "Unknown")

                # Display the gesture on the screen
                cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('Hand Gesture Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def recognize_gesture(landmarks):
    # Implement your gesture recognition logic here
    # For simplicity, this example calculates the Euclidean distance between certain landmarks
    # You would replace this with your actual gesture recognition model
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    distance = ((thumb_tip[0] - index_tip[0]) ** 2 + (thumb_tip[1] - index_tip[1]) ** 2 + (
                thumb_tip[2] - index_tip[2]) ** 2) ** 0.5

    # Determine gesture based on distance threshold
    if distance < 0.05:  # Adjust threshold as needed
        return 0  # Fist gesture
    elif distance < 0.1:  # Adjust threshold as needed
        return 1  # L gesture
    else:
        return 2  # Peace gesture


if __name__ == "__main__":
    main()
