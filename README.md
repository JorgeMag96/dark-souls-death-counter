# Death recognizer and counter for soulslike games
This small Python script updates a text file every time you die in a soulslike game. This works by 
taking a screenshot every set amount of time (1 second), then processing the image by applying a red channel filter 
and finally using Tesseract to recognize letters in the image, in this case we want to recognize the red text **YOU DIED** which appears 
after dying in the game.<br><br>
**But why do this ?**<br>
Well, I use [Streamlabs](https://streamlabs.com/) to stream video games and just by adding a text source with a reference 
to the text file that this script updates I can show/update my deaths while streaming.

## Compatible games:

- Demon's Souls
- Dark Souls
- Dark Souls: Remastered
- Dark Souls 2
- Dark Souls 3
- Bloodborne
- Elden Ring

**Note:** You'll need to [adjust the pyautogui.screenshot region parameter](https://github.com/JorgeMag96/dark-souls-death-counter/blob/3b7c24c49c60ab40fec533045e7e38b7e0be4afb/main.py#L59) depending on the game and resolution of your monitor.
<br> I will add game/resolution profiles in the future to make this step easier.

## You'll need:

- [Python](https://www.python.org/downloads/) (obviously)
### Python libraries:
- [numpy](https://pypi.org/project/numpy/)
- [opencv-contrib-python](https://pypi.org/project/opencv-contrib-python/)
- [pytesseract](https://pypi.org/project/pytesseract/) (python wrapper for Tesseract binary)
### Binaries:
- [tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

## Steps:

1) Install Python.
2) Clone repo.
4) Install Python libraries.
5) Install Tesseract binary.
6) Configure fileName and tesseractBinaryLocation variables in main.py
7) Run script
8) Play your favorite soulslike game !!!
