import pyautogui
from pynput.mouse import Controller as mouse_controller, Button, Listener as mouse_listener
from pynput.keyboard import Controller as keyboard_controller, Listener as keyboard_listener
import time
import sys

mouse_c = mouse_controller
keyboard_c = keyboard_controller

delay = 60.0
time_of_inactivity = 60  # If 5 minutes have passed, move mouse
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
    if (cursor_x >= width or cursor_x <= 0):
        pyautogui.moveTo(round(width/2), round(height/2))

    # wiggle
    pyautogui.move(100, 0)
    pyautogui.move(0, 100)

    # print(cursor_x, cursor_y, width, height)
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
        if (diff > time_of_inactivity):
            counter += 1
            spazz_out(counter)
            time.sleep(10)
            # time.sleep(delay - ((time.time() - starttime) % delay))


if __name__ == "__main__":
    run()
