import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load road image
image = cv2.imread("road.jpg")

if image is None:
    raise FileNotFoundError("road.jpg not found.")

output = image.copy()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges
edges = cv2.Canny(blur, 50, 150)

h, w = edges.shape

# Region of Interest
mask = np.zeros_like(edges)

polygon = np.array([[
    (0, h),
    (w, h),
    (int(0.58 * w), int(0.58 * h)),
    (int(0.42 * w), int(0.58 * h))
]], dtype=np.int32)

cv2.fillPoly(mask, polygon, 255)
roi_edges = cv2.bitwise_and(edges, mask)

# Hough Transform
lines = cv2.HoughLinesP(
    roi_edges,
    rho=1,
    theta=np.pi / 180,
    threshold=30,
    minLineLength=30,
    maxLineGap=100
)

if lines is not None:
    for line in lines:
        line = np.asarray(line).reshape(-1)

        x1, y1, x2, y2 = map(int, line[:4])

        cv2.line(
            output,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            3
        )

# Convert for Matplotlib
output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

# Display
plt.figure(figsize=(14, 8))
plt.imshow(output_rgb)
plt.title("Road Lane Detection - Hough Transform")
plt.axis("off")
plt.tight_layout()
plt.show()

# Save result
cv2.imwrite("lane_detection_result.jpg", output)

print("Lane detection completed.")
print("Detected line segments:", 0 if lines is None else len(lines))
print("Result saved as lane_detection_result.jpg")
