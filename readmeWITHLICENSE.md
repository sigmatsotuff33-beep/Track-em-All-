Ruby–Python Vision & Shodan Toolkit

A hybrid toolkit combining Ruby (for orchestration and CLI interaction)
and Python (for Shodan lookups, image/video processing, and object
detection). This project is built to be modular, extendable, and easy to
understand.

Ruby serves as the controller.
Python handles the heavy computation.
Both communicate using clean JSON messages.

------------------------------------------------------------------------

FEATURES

-   Ruby-driven interactive CLI
-   Shodan IP lookup via Python backend
-   Image and MP4 video processing
-   YOLO-based detection pipeline ready for integration
-   JSON-based communication between Ruby and Python
-   Fully modular folder layout for easy expansion

------------------------------------------------------------------------

PROJECT STRUCTURE

project/ ruby/ app.rb python_bridge.rb shodan_menu.rb python/
pythonapp.py pythonapp_cli.py services/ shodan_client.py
video_processor.py image_processor.py vision/ detect.py models/
yolov8n.pt README.md

------------------------------------------------------------------------

INSTALLATION

1. Python Setup

pip install -r requirements.txt

Requirements: - requests - opencv-python - ultralytics

2. Ruby Setup

Uses standard libraries: - open3 - json

------------------------------------------------------------------------

RUNNING

ruby/ruby app.rb

Menu options: 1) Run Python CLI 2) Shodan lookup 3) Image analysis 4)
Video analysis 0) Exit

------------------------------------------------------------------------

PYTHON TASK INTERFACE

python3 pythonapp.py

Tasks: - shodan: “IP|API_KEY” - image: /path/to/image.jpg - video:
/path/to/video.mp4

------------------------------------------------------------------------

YOLO INTEGRATION

Place YOLO weights in python/vision/models/.

detect.py handles detection and returns JSON.

------------------------------------------------------------------------

ROADMAP

-   Integrated YOLO detection
-   Frame-by-frame video detection
-   Long-running Python worker
-   Web UI option
-   Real-time streaming

------------------------------------------------------------------------

LICENSE

This project is free to use for personal, educational, or non-commercial
purposes.

You MUST include clear credit: “Based on the Ruby–Python Vision & Shodan
Toolkit by ”

Companies or commercial organizations: You must contact the creator via
GitHub BEFORE using this project.

Redistribution without credit is not permitted. Selling this project
directly is prohibited.

------------------------------------------------------------------------

CONTACT

https://github.com/roundpotato924

(round potato924 = DocIotaAegis)
