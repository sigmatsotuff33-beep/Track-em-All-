import sys
import json
from services.shodan_client import query_shodan
from services.video_processor import process_video
from services.image_processor import process_image

def cli(task, arg):
    if task == "shodan":
        ip, api = arg.split("|", 1)
        print(json.dumps(query_shodan(ip, api)))

    elif task == "video":
        print(json.dumps(process_video(arg)))

    elif task == "image":
        print(json.dumps(process_image(arg)))

    else:
        print(json.dumps({"error": "unknown task"}))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()

    else:
        # non-interactive, called from Ruby
        task = sys.argv[1]
        arg  = sys.argv[2] if len(sys.argv) > 2 else ""
        cli(task, arg)
