from pynput import keyboard


def on_release(key):
    try:
        if key.char == 'e':
            print('Hello worldr')
    except:
        print(f'{key} r eleased')


    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()