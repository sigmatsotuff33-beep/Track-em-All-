hey welcome to my new project "track em all"
DocIotaAegis production

A hybrid toolkit where **Ruby acts as the controller** and **Python performs
the heavy lifting**: object detection, video inspection, image analysis, and
Shodan lookups.

The architecture is simple:

- Ruby handles user interaction, menus, orchestration.
- Python handles Shodan API queries, image/video work, and YOLO-based detection.
- All communication flows through JSON between subprocess calls.

---

## 📁 Project Structure

project/
│
├── ruby/
│ ├── app.rb # Main Ruby CLI
│ ├── python_bridge.rb # Ruby ↔ Python communication layer
│ └── shodan_menu.rb # Shodan input menu (Ruby side)
│
├── python/
│ ├── pythonapp.py # Python dispatcher / CLI
│ ├── pythonapp_cli.py # (optional) standalone Python CLI mode
│ ├── services/
│ │ ├── shodan_client.py
│ │ ├── video_processor.py
│ │ └── image_processor.py
│ │
│ └── vision/
│ ├── detect.py
│ └── models/
│ └── yolov8n.pt # YOLO model weights
│
└── README.md

