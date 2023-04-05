# Right off
# https://docs.opencv.org/3.4/da/d97/tutorial_threshold_inRange.html
from __future__ import print_function
import cv2 as cv
import argparse
from pathlib import Path

max_value = 255
max_value_H = 360 // 2
low_H = 0
low_S = 0
low_V = 0
high_H = max_value_H
high_S = max_value
high_V = max_value
window_capture_name = "Video Capture"
window_detection_name = "Object Detection"
low_H_name = "Low H"
low_S_name = "Low S"
low_V_name = "Low V"
high_H_name = "High H"
high_S_name = "High S"
high_V_name = "High V"


def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H - 1, low_H)
    cv.setTrackbarPos(low_H_name, window_detection_name, low_H)


def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H + 1)
    cv.setTrackbarPos(high_H_name, window_detection_name, high_H)


def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S - 1, low_S)
    cv.setTrackbarPos(low_S_name, window_detection_name, low_S)


def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S + 1)
    cv.setTrackbarPos(high_S_name, window_detection_name, high_S)


def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V - 1, low_V)
    cv.setTrackbarPos(low_V_name, window_detection_name, low_V)


def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V + 1)
    cv.setTrackbarPos(high_V_name, window_detection_name, high_V)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Code for Thresholding Operations using inRange tutorial."
    )
    parser.add_argument(
        "image_path",
        help="Path[s] to images",
        nargs="+",
        type=Path,
    )
    args = parser.parse_args()

    cv.namedWindow(window_capture_name)
    cv.namedWindow(window_detection_name)
    cv.createTrackbar(
        low_H_name,
        window_detection_name,
        low_H,
        max_value_H,
        on_low_H_thresh_trackbar,
    )
    cv.createTrackbar(
        high_H_name,
        window_detection_name,
        high_H,
        max_value_H,
        on_high_H_thresh_trackbar,
    )
    cv.createTrackbar(
        low_S_name,
        window_detection_name,
        low_S,
        max_value,
        on_low_S_thresh_trackbar,
    )
    cv.createTrackbar(
        high_S_name,
        window_detection_name,
        high_S,
        max_value,
        on_high_S_thresh_trackbar,
    )
    cv.createTrackbar(
        low_V_name,
        window_detection_name,
        low_V,
        max_value,
        on_low_V_thresh_trackbar,
    )
    cv.createTrackbar(
        high_V_name,
        window_detection_name,
        high_V,
        max_value,
        on_high_V_thresh_trackbar,
    )

    for image_path in args.image_path:
        while True:
            image = cv.imread(str(image_path))

            image_HSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)
            image_threshold = cv.inRange(
                image_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V)
            )

            cv.imshow(window_capture_name, image)
            cv.imshow(window_detection_name, image_threshold)

            (22, 79, 147), (41, 161, 215)  # Image 16
            (21, 15, 134), (66, 255, 255)  # Image 35

            key = cv.waitKey(30)
            is_quit = key == ord("q") or key == 27  # 27 is escape
            is_next = key == ord(" ")

            if is_quit or is_next:
                print(f"==== Final HSVs for {image_path.stem} ====")
                print(f"lowH = {low_H}")
                print(f"lowS = {low_S}")
                print(f"lowV = {low_V}")
                print(f"highH = {high_H}")
                print(f"highS = {high_S}")
                print(f"highV = {high_V}")
                print()
                print(
                    f"({low_H}, {low_S}, {low_V}), ({high_H}, {high_S}, {high_V})"
                )
                print("====================")

                if is_quit:
                    print("Quitting")
                    exit(0)
                elif is_next:
                    print("Continuing to next image")
                    break
