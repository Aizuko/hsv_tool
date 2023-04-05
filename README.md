# HSV masking tool

Cleaned up version of the code from the [OpenCV inRange
tutorial](https://docs.opencv.org/3.4/da/d97/tutorial_threshold_inRange.html)

### Setup

```bash
python3 -mvenv .
. bin/activate
pip install -r requirements.txt
```

### Usage

Run with a list of paths to all the images you want to edit as arguments

```bash
python3 main.py image1.jpg image2.png
```

Use `<space>` to continue to the next image. Use `<esc>` or `q` to quit. In
either case, the HSV values will be printed to the terminal. The tuple format
for copy/paste is below.

```
==== Final HSVs for crossing1.png ====
lowH = 0
lowS = 38
lowV = 111
highH = 21
highS = 255
highV = 235

(0, 38, 111), (21, 255, 235)
====================
```
