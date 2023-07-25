import pyautogui
from pynput.mouse import Controller as mouse_controller, Button, Listener as mouse_listener
from pynput.keyboard import Controller as keyboard_controller, Listener as keyboard_listener
import time
import sys

TIME_OF_INACTIVITY = 120  # If X seconds have passed, move mouse
DELAY = 30.0        # Move mouse every X seconds
pyautogui.FAILSAFE = False # disable builtin "failsafe" which is not a failsafe but a "crash the program" feature

mouse_c = mouse_controller
keyboard_c = keyboard_controller
starttime = time.time()
last = starttime  # last time user did anything

def on_anything(*args):
    global last
    last = time.time()
    return 0


def spazz_out(n):
    width, height = pyautogui.size()
    cursor_x, cursor_y = pyautogui.position()
    # center if out of bounds
    if (cursor_x >= width or cursor_x <= 110):
        pyautogui.moveTo(round(width/2), round(height/2))
    if (cursor_y >= height or cursor_y <= 110):
        pyautogui.moveTo(round(width/2), round(height/2))

    # square wiggle
    pyautogui.move(10, 0)
    pyautogui.move(0, 10)
    pyautogui.move(-10, 0)
    pyautogui.move(0, -10)

    sticky_message(f'unslept {n} time[s]')


def sticky_message(message):
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    print(message)


def run():
    listener_mouse = mouse_listener(
        on_move=on_anything,
        on_click=on_anything,
        on_scroll=on_anything
    )

    listener_keyboard = keyboard_listener(
        on_press=on_anything,
        on_release=on_anything,
    )

    listener_mouse.start()
    listener_keyboard.start()
    print(f'started at {time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())}')
    counter = 0

    while True:
        diff = time.time() - last
        if (diff > TIME_OF_INACTIVITY):
            counter += 1
            spazz_out(counter)
            time.sleep(DELAY)


if __name__ == "__main__":
    run()
