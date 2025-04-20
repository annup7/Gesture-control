import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

last_action = None
cooldown = 15
cooldown_counter = 0

def is_finger_up(lm, tip, pip):
    return lm[tip].y < lm[pip].y

def is_fist(lm):
    return (
        lm[8].y > lm[6].y and
        lm[12].y > lm[10].y and
        lm[16].y > lm[14].y and
        lm[20].y > lm[18].y
    )

def is_slide(lm):
    return (
        is_finger_up(lm, 8, 6) and    # Index up
        is_finger_up(lm, 12, 10) and  # Middle up
        is_finger_up(lm, 16, 14) and  # Ring up
        is_finger_up(lm, 20, 18)      # Pinky up
        # Not checking thumb so that open palm is more flexible
    )

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    h, w, _ = img.shape
    action = "neutral"

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            lm = handLms.landmark
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            thumb_x = lm[4].x
            pinky_x = lm[20].x
            tilt_thresh = 0.04

            index_up = is_finger_up(lm, 8, 6)
            middle_up = is_finger_up(lm, 12, 10)

            # Check slide before jump
            if is_slide(lm):
                action = "slide"
            elif index_up and not middle_up:
                action = "jump"
            elif is_fist(lm):
                if (pinky_x - thumb_x) > tilt_thresh:
                    action = "left"
                elif (thumb_x - pinky_x) > tilt_thresh:
                    action = "right"
                else:
                    action = "neutral"

            # Trigger key press
            if action != last_action and cooldown_counter == 0:
                if action == "jump":
                    pyautogui.press("up")
                    print("Jump")
                elif action == "slide":
                    pyautogui.press("down")
                    print("Slide")
                elif action == "left":
                    pyautogui.press("left")
                    print("Left")
                elif action == "right":
                    pyautogui.press("right")
                    print("Right")
                last_action = action
                cooldown_counter = cooldown

            # Display action label
            cv2.putText(img, f"Action: {action}", (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if cooldown_counter > 0:
        cooldown_counter -= 1

    cv2.imshow("Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()