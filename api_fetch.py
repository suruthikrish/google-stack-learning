import json
import urllib.request

def fetch_open_data():
    """
    A straightforward script to verify my local Python environment
    can successfully make API requests and parse JSON data.
    """
    url = "https://github.com"
    
    print("Testing local environment connectivity...")
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                quote = response.read().decode('utf-8')
                print(f"\n[Success] Connection established!")
                print(f"Parsed Quote from GitHub: \"{quote}\"\n")
                print("Environment status: Ready for DevFest Build Forge.")
            else:
                print(f"Unexpected status code: {response.status}")
    except Exception as e:
        print(f"Error connecting to API: {e}")
        print("Please check your internet connection or proxy settings.")

if __name__ == "__main__":
    fetch_open_data()
