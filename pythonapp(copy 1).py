import sys
import json

from services.shodan_client import query_shodan
from services.video_processor import process_video
from services.image_processor import process_image

def main():
  if len(sys.argv) < 3:
    print(json.dumps({"error": "Bad call"}))
    return
task = sys.argv[1]
arg = sys.argv[2]

if task = "shodan"
ip, api = arg.split("|",1)
print(json.dumps(query_shodan(ip, api)))

elif task == "image"
print(json.dumps(process_image(arg)))

elif task == "video"
print(json.dumps(process_video(arg)))

else:
    print(json.dumps({"error": "unknown task"}))

    if __name__ == "__main__":
    main()

#notice if launched without args you need to open your interactive cli menu

if len(sys.argv) == 1:
    from pythonapp_cli import run_cli
    run_cli()
else:
    main()
    