import cv2
import numpy as np

image = cv2.imread("traffic_signs.jpeg")
if image is None:
    raise FileNotFoundError("traffic_signs.jpeg was not found.")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
red = cv2.inRange(hsv, (0,80,80), (10,255,255)) | cv2.inRange(hsv, (170,80,80), (180,255,255))
blue = cv2.inRange(hsv, (90,80,70), (130,255,255))
yellow = cv2.inRange(hsv, (18,80,80), (40,255,255))
combined = red | blue | yellow

kernel = np.ones((5,5), np.uint8)
combined = cv2.morphologyEx(combined, cv2.MORPH_OPEN, kernel)
combined = cv2.morphologyEx(combined, cv2.MORPH_CLOSE, kernel)

contours, _ = cv2.findContours(combined, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
detections = 0
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 150:
        continue
    perimeter = cv2.arcLength(cnt, True)
    if perimeter == 0:
        continue
    circularity = 4*np.pi*area/(perimeter*perimeter)
    if circularity > 0.35:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(image, "Traffic Sign", (x,max(20,y-8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)
        detections += 1

cv2.imwrite("traffic_signs_detected.jpeg", image)
print(f"Traffic-sign-like regions detected: {detections}")
print("Saved: traffic_signs_detected.jpeg")
