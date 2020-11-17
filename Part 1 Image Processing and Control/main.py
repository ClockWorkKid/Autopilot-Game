import cv2 as cv
import os
from time import time
from windowcapture import WindowCapture
from pynput.keyboard import Key, Listener
import threading


def streamKeys():

    def on_press(key):
        print('{0} pressed'.format(
            key))

    def on_release(key):
        print('{0} release'.format(
            key))
        if key == Key.esc:
            # Stop listener
            return False
a
    print("Starting key detection")

    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def streamScreen(window_name):

    print("Starting streaming game window")

    # initialize the WindowCapture class
    wincap = WindowCapture(window_name)

    loop_time = time()
    frames = 0
    while (True):

        # get an updated image of the game
        screenshot = wincap.get_screenshot()

        cv.imshow('Computer Vision', screenshot)
        frames = frames + 1

        # debug the loop rate
        if frames == 200:

            print('FPS {}'.format(int(200 / (time() - loop_time))))
            loop_time = time()
            frames = 0

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

    print('Done.')


if __name__ == "__main__":

    # Change the working directory to the folder this script is in.
    # Doing this because I'll be putting the files from each video in their own folder on GitHub
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # list all windows
    # WindowCapture.list_window_names()

    # streamScreen('Need for Speed™ Most Wanted')

    thread_game = threading.Thread(target=streamScreen, args=('Need for Speed™ Most Wanted',))
    thread_keys = threading.Thread(target=streamKeys, args=())

    thread_game.start()
    thread_keys.start()
