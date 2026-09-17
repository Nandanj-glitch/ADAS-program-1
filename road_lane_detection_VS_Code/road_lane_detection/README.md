# Road Lane Detection - VS Code Project

This project runs the road-lane detection program directly in VS Code using:

- Python
- OpenCV
- NumPy
- Matplotlib
- Canny Edge Detection
- Region of Interest (ROI)
- Probabilistic Hough Line Transform

## Project Structure

```text
road_lane_detection/
├── main.py
├── road.jpg
├── requirements.txt
└── README.md
```

The supplied `road.jpg` is already included in this ZIP.

## Run in VS Code

### Step 1 — Extract the ZIP

Extract the ZIP and open the `road_lane_detection` folder in VS Code.

### Step 2 — Install libraries

Open the VS Code terminal:

```bash
pip install -r requirements.txt
```

Or:

```bash
python -m pip install -r requirements.txt
```

### Step 3 — Run

```bash
python main.py
```

## Output

The program will:

1. Load `road.jpg`.
2. Convert it to grayscale.
3. Apply Gaussian blur.
4. Detect edges with Canny.
5. Create a Region of Interest.
6. Detect line segments using Hough Transform.
7. Draw detected lines in green.
8. Display the result.
9. Save the result as:

```text
lane_detection_result.jpg
```

## Important

The included image is an aerial/top-down road image. The basic Hough Transform method may detect road boundaries, lane markings, and other strong edges rather than only the true driving lanes.

For a cleaner result on this particular image, the ROI and Hough parameters can be customized further.

## Common Problems

### `road.jpg not found`

Make sure `road.jpg` is in the same folder as `main.py`.

### `pip` command not recognized

Use:

```bash
python -m pip install -r requirements.txt
```

### Matplotlib/OpenCV error

Reinstall:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```
