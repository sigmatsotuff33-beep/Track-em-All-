#stable version

import sys
import json
from ultralytics import YOLO

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "no image provided"}))
        return

    image_path = sys.argv[1]

    try:
        model = YOLO("yolov8n.pt")
        results = model(image_path)

        # results is usually a list
        result = results[0]

        detections = []

        for box in result.boxes:
            cls_id = int(box.cls[0])
            label = model.names.get(cls_id, str(cls_id))
            conf = float(box.conf[0])

            x1, y1, x2, y2 = map(float, box.xyxy[0])

            detections.append({
                "label": label,
                "confidence": conf,
                "bbox": [x1, y1, x2, y2]
            })

        print(json.dumps(detections))

    except Exception as e:
        # Send a meaningful JSON error back to Ruby
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()
