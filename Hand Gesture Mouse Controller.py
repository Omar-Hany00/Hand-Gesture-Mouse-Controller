import cv2
import mediapipe as mp
import pyautogui
import time
import math

SMOOTHING = 3 #smooth motion settings
prev_x, prev_y = 0, 0 #mouse initial value

screen_width, screen_height = pyautogui.size() #screen dimensions

mp_hands = mp.solutions.hands #call the hand algorithm
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) #assign the parameters of the model(one hand,max 70% visible to work, min same)

dragging = False
last_single_click = 0
last_double_click = 0
click_delay = 0.5  # Seconds between allowed clicks

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

cap = cv2.VideoCapture(0) #to open webcam

while True:
    st, frame = cap.read() #to read each frame in the video

    frame = cv2.flip(frame, 1) #to flip the video horizontally
    h, w, _ = frame.shape #assign the dimensions of the frame in variables
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #convert bgr to rgb
    results = hands.process(rgb_frame) #to run the hands program

    if results.multi_hand_landmarks:
        lm = results.multi_hand_landmarks[0].landmark #we take the first hand on the list as the first object in the list

        index_tip = (int(lm[8].x * w), int(lm[8].y * h)) #8 index, 12 middle, 4 thumb
        middle_tip = (int(lm[12].x * w), int(lm[12].y * h)) #we multiply my w, h to get the position of the tip
        thumb_tip = (int(lm[4].x * w), int(lm[4].y * h))

        screen_x = lm[8].x * screen_width #to track the position of the index on the screen
        screen_y = lm[8].y * screen_height
        curr_x = prev_x + (screen_x - prev_x) / SMOOTHING #smoothing function
        curr_y = prev_y + (screen_y - prev_y) / SMOOTHING
        pyautogui.moveTo(curr_x, curr_y) #mouse moving order
        prev_x, prev_y = curr_x, curr_y

        now = time.time()

        # Drag and drop (pinch index + thumb and hold)
        pinch_dist = distance(index_tip, thumb_tip)
        if pinch_dist < 40:
            if not dragging:
                pyautogui.mouseDown()
                dragging = True
        else:
            if dragging:
                pyautogui.mouseUp()
                dragging = False

        # Single click (tap index + thumb)
        if pinch_dist < 30 and not dragging and now - last_single_click > click_delay:
            pyautogui.click()
            last_single_click = now

        # Double click (tap middle + thumb)
        if distance(middle_tip, thumb_tip) < 30 and now - last_double_click > click_delay:
            pyautogui.doubleClick()
            last_double_click = now

    cv2.imshow('Mouse Control', frame)
    if cv2.waitKey(33) & 0xFF == 27:  #number of frames and closing by esc
        break

cap.release()
cv2.destroyAllWindows()
