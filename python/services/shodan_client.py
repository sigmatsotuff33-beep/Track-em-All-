import requests

def query_shodan(ip, api_key):
    
url =  f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"

try:
    r = requests.get(url, timeout=10)
    if r.status_code !=200:
        return {"error: r.text"}
    return r.json
except Exception as e:
    return{"error": str(e)}
