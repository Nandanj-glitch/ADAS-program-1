import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Load pedestrian image
image = cv2.imread("ped.webp")

if image is None:
    raise FileNotFoundError(
        "ped.webp not found. Make sure ped.webp is in the same folder as main.py."
    )

# Run object detection
results = model(image)

# Copy image for drawing
output = image.copy()

for result in results:
    boxes = result.boxes

    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        confidence = float(box.conf[0])
        class_id = int(box.cls[0])
        label = model.names[class_id]

        # Calculate bounding-box area
        width = x2 - x1
        height = y2 - y1
        area = width * height

        # Warning based on detected object's size
        if area > 120000:
            warning = "STOP!"
            color = (0, 0, 255)
        elif area > 60000:
            warning = "BRAKE NOW"
            color = (0, 140, 255)
        elif area > 25000:
            warning = "SLOW DOWN"
            color = (0, 255, 255)
        else:
            warning = "SAFE"
            color = (0, 255, 0)

        # Draw bounding box
        cv2.rectangle(output, (x1, y1), (x2, y2), color, 2)

        # Object label and confidence
        cv2.putText(
            output,
            f"{label} {confidence:.2f}",
            (x1, max(y1 - 35, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2,
        )

        # Warning
        cv2.putText(
            output,
            warning,
            (x1, max(y1 - 10, 45)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2,
        )

# Show result
cv2.imshow("Pedestrian Detection - YOLOv8", output)

# Save result
cv2.imwrite("pedestrian_detection_result.jpg", output)

print("Pedestrian detection completed.")
print("Result saved as: pedestrian_detection_result.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()
