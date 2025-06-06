# WC3Banlist
A working Banlist for Warcraft 3 (example banlist.xlsx also available if you don't want to start from zero)

This python script uses pytesseract OCR and Microsoft Excel to read all the playernames in your lobby and compares it with your Excel Banlist file.
If there are matching entries, the script will automatically ban the players from your lobby. The script will also output an optional reason, why the players have been banned before kicking them from the lobby. 
Example:
Players banned:
<name> - Reason: leaver
<name2> - Reason: flamer

This output will be written in the lobby and in the terminal.

## Hotkeys:
F3: Check for banned players in the lobby and ban them

F6: End the script

## More Info:
The terminal will also output all read names. This is useful if you want to add someone to the banlist after the game to check the read names.
Your Banlist Excel file must have 2 rows called "name" and "reason".
The Tesseract OCR will make mistakes in reading some names, especially russian or asian names. To fix this, add the name what the banlist actually read to your list instead of their names.
The Banlist will also automatically ban names which are very close to actual names. 
Example: 
Player "testing" ist banned for being a leaver.
Player "tseting" joins the game.
Since his name is almost the same as "testing" he will also get banned!
This is for more precise checking the banned players as OCR never guarantees correctly reading the names.

## Installation:
Do not try to use this without any programming knowledge as the setup is not very easy!

Short Version:
1. Download Python and install it
2. Download Tesseract OCR and install it
3. Download Wc3Banlist.py
4. Install all dependencies with pip
5. Configure the Coordinates in the script
6. Run the script in your favorite environment
7. F3 to check bans, F6 to end script

Long Version:
## Prerequisites
Make sure the following are installed on your system:

[Python 3.6](https://www.python.org/downloads/)

[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

(Install it and note the path in the python script to the tesseract.exe if you're on Windows)

## Required Python Libraries
Install the required Python packages via pip (open your command line and copy paste the following command):

<pre>pip install pytesseract opencv-python pyautogui keyboard openpyxl</pre>

These standard libraries are also used (no need to install):
time, os, difflib

**Make sure the file grab_screen.py is present in the same folder as your Wc3Banlist.py**

Create a file named banlist.xlsx with the following structure and set the path to it in the Wc3Banlist.py (example path is already given):

| name |	reason |
|------|------|
|PlayerOne |	Leaver|
|PlayerTwo |	Toxicity|
|PlayerThree |	Cheating|

## Customizing Screen Coordinates for Your Resolution
The script uses fixed screen regions to extract player names from the Warcraft III lobby using OCR. These regions are defined as tuples of screen coordinates:

(x1, y1, x2, y2)

Example from the code (for 4K resolution):

<pre>for coords in [(400, 520, 850, 900), (1700, 520, 2150, 900)]</pre>

See this image on how to find your coordinates<img width="1920" alt="Coordinates" src="https://github.com/user-attachments/assets/3de28dfc-0743-4dd6-8ac9-886fb5a97609" />

These represent two rectangular areas to scan for the left and right halves of the player list in the lobby.


## How to Adjust Coordinates for Your Resolution
If you are not using a 4K monitor or your UI scale differs, you'll likely need to update the coordinates.

### Take a Screenshot
Open a game lobby in Warcraft III and take a full-screen screenshot with the player list visible.

### Open the Screenshot in an Image Editor
Use any tool (e.g., Paint, GIMP, Photoshop) that shows pixel coordinates.

### Measure Rectangles Around Player Names
For each column of names (left/right), find the top-left (x1, y1) and bottom-right (x2, y2) corners that encompass all the names.

Replace the coordinates in the extract_players_with_positions() function:

<pre>for coords in [(your_x1, your_y1, your_x2, your_y2), ...]</pre>

Run the script, press F3, and see if names are being recognized. Adjust as needed.

## Tips
Leave extra padding around names to help OCR recognition.

Avoid scanning unnecessary UI elements like borders or icons.

## Running the Script
Launch Warcraft III and host a custom game lobby.

Run the script:

<pre>python Wc3Banlist.py</pre>

Use the hotkeys:

| Hotkey | Action |
|------|------|
| F3   |  Scan and auto-ban players  |
| F6   |  Terminate the script       |

## How It Works
The script uses OCR (via Tesseract) to read player names from the lobby.

It compares those names to your Excel banlist.

Matching players are automatically banned using simulated keystrokes.

## Support

If you want to support me, you can do it here:

- [Buy Me a Coffee](https://buymeacoffee.com/RealFutureAi)
- [PayPal](https://paypal.me/FutureAI)

