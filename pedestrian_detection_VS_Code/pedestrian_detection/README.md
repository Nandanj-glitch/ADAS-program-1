# Pedestrian Detection - YOLOv8

A complete VS Code-ready pedestrian/object detection project using
**YOLOv8** and **OpenCV**.

The supplied pedestrian image is already included as `ped.webp`.

## Project Structure

```text
pedestrian_detection/
├── main.py
├── ped.webp
├── requirements.txt
└── README.md
```

## Run in VS Code

### 1. Extract the ZIP

Extract the ZIP and open the `pedestrian_detection` folder in VS Code.

### 2. Install dependencies

Open the VS Code terminal:

```bash
pip install -r requirements.txt
```

If `pip` does not work:

```bash
python -m pip install -r requirements.txt
```

### 3. Run the program

```bash
python main.py
```

On the first run, Ultralytics will automatically download the
`yolov8n.pt` model.

## What the Program Does

1. Loads the YOLOv8 Nano model.
2. Loads `ped.webp`.
3. Runs YOLO object detection.
4. Gets each detected object's:
   - Bounding box
   - Confidence
   - Class label
5. Calculates the bounding-box area.
6. Displays a warning based on object size:
   - `STOP!` — area > 120,000
   - `BRAKE NOW` — area > 60,000
   - `SLOW DOWN` — area > 25,000
   - `SAFE` — otherwise
7. Draws the result on the image.
8. Opens the result in an OpenCV window.
9. Saves the result as:

```text
pedestrian_detection_result.jpg
```

## Important Note

The warning is based on the **pixel area of the detected bounding box**.
It is not a calibrated measurement of real-world distance or collision risk.

The YOLOv8 model detects multiple COCO object classes, not only pedestrians.
If you want the project to process **only people**, the code can be modified
to filter for the `person` class.

## Troubleshooting

### `ped.webp not found`

Make sure `ped.webp` is in the same folder as `main.py`.

### `pip` is not recognized

Use:

```bash
python -m pip install -r requirements.txt
```

### OpenCV window does not appear

Make sure you installed:

```bash
pip install opencv-python
```

Do not replace it with `opencv-python-headless`, because this project uses
`cv2.imshow()`.

### YOLO model download fails

Make sure your computer has an internet connection the first time you run
the program. The model is downloaded automatically.
