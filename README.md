# Hand Gesture Mouse Controller

A real-time touchless mouse control system built using Python, OpenCV, and MediaPipe.  
The system tracks hand landmarks from a webcam feed and maps specific gestures to cursor movement and mouse actions.

## Features

- Real-time hand tracking
- Cursor movement using hand gestures
- Click gesture recognition
- Touchless human-computer interaction
- Webcam-based control system

## Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

## How It Works

1. Webcam captures live video frames
2. MediaPipe detects and tracks hand landmarks
3. Landmark positions are processed in Python
4. Gestures are interpreted into mouse actions
5. Cursor commands are sent to the operating system

## Installation

Clone the repository:

```bash
git clone https://github.com/Omar-Hany00/Hand-Gesture-Mouse-Controller.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

## Future Improvements

- Scroll gesture support
- Multi-hand tracking
- Gesture customization
- Improved smoothing and stability
- GUI calibration settings

## Author

Omar Hany Mohammed
