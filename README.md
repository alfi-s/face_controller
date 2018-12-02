# F-Controller
Your face as an input device.

## Overview
This is a simple python script that uses the OpenCV library to detect faces, and then use the position of your face relative to your screen to trigger keyboard inputs.

## Prerequisites
In order to run this, you need OpenCV and pynput.
You can install OpenCV by going [here](https://www.learnopencv.com/install-opencv3-on-ubuntu/).
You can install pynput by:
```bash
pip3 install pynput
```

## Usage
As of now, you can set the thresholds for sensing inputs by hardcoding the `x_threshold` and `y_threshold` values in the script. You can also set the keyboard inputs by setting the `key_x_below_threshold`, `key_x_above_threshold`, `key_y_below_threshold`, and `key_y_above_threshold` values in the script.

Run the script using:
```bash
python3 detection.py
```

A webcam feed will appear. Press the I key on the keyboard to tell the program to start listening for inputs. Press the Q key on the keyboard to exit the program.