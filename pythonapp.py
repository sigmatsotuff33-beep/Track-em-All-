import sys
import json 


from services.shodan_client import query_shodan
from services.video_processor import process_video
from services.image_processor import process_image

def main():
    print("Track'em All")
    print("Doc-Iota-Aegis-Made-This")
    print("[1] Shodan IP lookup")
    print("[2] Analyze MP4 video")
    print("[3] Analyze image")
    print("0 exit booooo")

    choice = input("Select an option: ")

    if choice == "1":
        ip = input("Enter IP: ")
        api_key = input("Enter Shodan API key: ")
        result = query_shodan(ip, api_key)
        print(result)

    elif choice == "2":
        path = input("Enter video file path: ")
        result = process_video(path)
        print(result)

    elif choice == "3":
        path = input("Enter image file path: ")
        result = process_image(path)
        print(result)

    elif choice == "0":
        print("Byeeeeeeeeee")
        sys.exit(0)

    else:
        print("bro choose a correct answer cmon its easy")

if __name__ == "__main__":
    main()
