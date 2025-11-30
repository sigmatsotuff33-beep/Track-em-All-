require "open3"
require "json"

def run_detection(image_path)
  # command must be split: ["python3", "vision/detect.py", image_path]
  cmd = ["python3", "vision/detect.py", image_path]

  stdout, stderr, status = Open3.capture3(*cmd)

  raise stderr unless status.success?

  JSON.parse(stdout)
end
