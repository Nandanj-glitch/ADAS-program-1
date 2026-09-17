import cv2
import numpy as np
from pathlib import Path

# ------------------------------------------------------------
# ADAS Headlight Detection - simple OpenCV version
# Works without TensorFlow.
# ------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent
IMAGE_PATH = PROJECT_DIR / "sample" / "day.jpg"
RESULT_PATH = PROJECT_DIR / "sample" / "headlight_result.jpg"

image = cv2.imread(str(IMAGE_PATH))

if image is None:
    print("ERROR: Could not read:", IMAGE_PATH)
    print("Make sure sample/day.jpg exists.")
    raise SystemExit(1)

print("Image loaded:", IMAGE_PATH)

# Convert to grayscale and calculate average brightness.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
brightness = float(np.mean(gray))

print(f"Ambient brightness: {brightness:.2f}")

# Find very bright regions.
_, bright = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Remove tiny noise.
kernel = np.ones((3, 3), np.uint8)
bright = cv2.morphologyEx(bright, cv2.MORPH_OPEN, kernel)

contours, _ = cv2.findContours(
    bright, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

count = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area < 20:
        continue

    x, y, w, h = cv2.boundingRect(contour)

    # Ignore very large regions such as a large portion of the sky.
    if w * h > image.shape[0] * image.shape[1] * 0.15:
        continue

    count += 1
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(
        image, "Bright region", (x, max(20, y - 8)),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1
    )

# Basic environment classification.
if brightness < 50:
    environment = "DARK"
else:
    environment = "BRIGHT"

# This is a basic bright-region demo, not a trained headlight detector.
if environment == "DARK" and count >= 2:
    decision = "POSSIBLE HEADLIGHTS"
elif environment == "DARK":
    decision = "NO CLEAR HEADLIGHT PAIR"
else:
    decision = "DAY / BRIGHT ENVIRONMENT"

print("Environment:", environment)
print("Bright regions detected:", count)
print("Decision:", decision)

cv2.putText(
    image, f"Environment: {environment}", (15, 30),
    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
)
cv2.putText(
    image, f"Decision: {decision}", (15, 60),
    cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2
)

cv2.imwrite(str(RESULT_PATH), image)
print("Result saved to:", RESULT_PATH)

# Show the result if the system supports an OpenCV window.
try:
    cv2.imshow("ADAS Headlight Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except cv2.error:
    print("OpenCV display window is unavailable.")
    print("Open the saved result image instead:", RESULT_PATH)
