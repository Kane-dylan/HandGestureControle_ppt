# Gesture-Controlled PowerPoint Presenter

## Overview

The **Gesture-Controlled PowerPoint Presenter** is a Python project that enables users to upload and present PowerPoint (PPT) files using hand gestures. By leveraging computer vision techniques, it tracks the user's hand movements and translates them into commands for navigating through slides during a presentation.

## Features

1. **Upload PPT Files:**
   - Users can upload their PPT files directly to the application.
   - Supported formats include `.ppt` and `.pptx`.

2. **Hand Gesture Recognition:**
   - The project uses the camera module to capture real-time video frames.
   - Computer vision algorithms detect the user's hand gestures (e.g., swiping left, right, or up) to control the presentation.

3. **Slide Navigation:**
   - Gestures allow users to navigate between slides:
     - Swipe left: Move to the previous slide.
     - Swipe right: Move to the next slide.
     - Swipe up: Jump to a specific slide (e.g., show slide 5).

4. **User-Friendly Interface:**
   - The application provides clear instructions for gesture-based controls.
   - Visual feedback (e.g., highlighting the current slide) enhances the user experience.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/gesture-controlled-presenter.git
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python main.py
   ```
## Demo 



https://github.com/Kane-dylan/HandGestureControle_ppt/assets/139806450/cced6014-b9cd-4ca7-a08b-1bf2d3e30a0b



## Usage

1. Launch the application.
2. Upload your PPT file.
3. Position your hand in front of the camera.
4. Perform gestures to control the presentation.

## Dependencies

- Python 3.x
- OpenCV (for hand tracking)
- Flask (for web interface)
- Other necessary libraries (specified in `requirements.txt`)

## Acknowledgments

This project was inspired by the need for more interactive and engaging presentations. Feel free to contribute or customize it further!

---

Feel free to modify the content above to match your project specifics. Remember to update the installation instructions, dependencies, and any other relevant details. Good luck with your Gesture-Controlled PowerPoint Presenter! 🎉👏
