import cv2

def process_video(path):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        return {"error": "Could not open video"}

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()

    return {"frames": frame_count}
