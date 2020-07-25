import cv2 as cv
import os
from time import time
from windowcapture import WindowCapture


def streamScreen(window_name):
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
        if frames == 50:

            print('FPS {}'.format(int(50 / (time() - loop_time))))
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

    # stream the window
    streamScreen('Need for Speed™ Most Wanted')

