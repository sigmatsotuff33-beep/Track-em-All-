import sys
import json
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Image path from Ruby
image_path = sys.argv[1]

# Run inference
result = model(image_path)[0]

detections = []

for box in result.boxes:
    cls = int(box.cls[0])
    name = model.names[cls]
    conf = float(box.conf[0])

    x1, y1, x2, y2 = map(float, box.xyxy[0])

    detections.append({
        "label": name,
        "confidence": conf,
        "bbox": [x1, y1, x2, y2]
    })

# Print JSON to Ruby
print(json.dumps(detections))
