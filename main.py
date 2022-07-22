import pyautogui as pyautogui
import cv2 as cv
import numpy as np
import pytesseract
import time


def get_deaths(file_name):
    try:
        f = open(file_name, mode='r')
        deaths = int(f.read().split(": ")[1])
        f.close()
        return deaths
    except FileNotFoundError:
        f = open(file_name, mode='x')
        f.write('deaths: 0')
        return 0


def add_death_to_counter(file_name):
    deaths = str(get_deaths(file_name) + 1)
    f = open(file_name, mode='w')
    f.write("deaths: " + deaths)
    f.close()


def has_died(tesseract_binary_location):
    pytesseract.pytesseract.tesseract_cmd = tesseract_binary_location
    image = pyautogui.screenshot(region=(780, 500, 1000, 500))
    image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)

    img_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # lower mask (0-10)
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    mask0 = cv.inRange(img_hsv, lower_red, upper_red)

    # upper mask (170-180)
    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])
    mask1 = cv.inRange(img_hsv, lower_red, upper_red)

    # join my masks
    mask = mask0 + mask1

    # set my output img to zero everywhere except my mask
    output_img = image.copy()
    output_img[np.where(mask == 0)] = 0

    # or your HSV image, which I *believe* is what you want
    output_hsv = img_hsv.copy()
    output_hsv[np.where(mask == 0)] = 0

    return "YOU DIED" in pytesseract.image_to_string(output_hsv)


fileName = 'deaths.txt'
tesseractBinaryLocation = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
isDead = False

while True:

    if has_died(tesseractBinaryLocation):
        isDead = True
        add_death_to_counter(fileName)
        print(f'Oh no! Deaths: {get_deaths(fileName)}')

        while isDead:
            isDead = has_died(tesseractBinaryLocation)
            time.sleep(1)

    time.sleep(1)
