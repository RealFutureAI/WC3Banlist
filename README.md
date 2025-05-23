# WC3Banlist - UPLOAD SOON
A working Banlist for Warcraft 3

This python script uses pytesseract OCR and Microsoft Excel to read all the playernames in your lobby and compares it with your Excel Banlist file.
If there are matching entries, the script will automatically ban the players from your lobby. The script will also output an optional reason, why the players have been banned before kicking them from the lobby. Example:
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
5. Run the script in your favorite environment
6. F3 to check bans, F6 to end script

Long Version:
✅ Prerequisites
Make sure the following are installed on your system:

[Python 3.6](https://www.python.org/downloads/)
[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

(Install it and note the path in the python script to the tesseract.exe if you're on Windows)

## Required Python Libraries
Install the required Python packages via pip:

pip install pytesseract opencv-python pyautogui keyboard openpyxl
These standard libraries are also used (no need to install):
time, os, difflib

Make sure the file grab_screen.py is present in the same folder as your Wc3Banlist.py

Create a file named banlist.xlsx with the following structure and set the path to it in the Wc3Banlist.py (example path is already given):

name	reason
PlayerOne	Leaver
PlayerTwo	Toxicity
PlayerThree	Cheating

Column headers must be lowercase: name, reason.

## Running the Script
Launch Warcraft III and host a custom game lobby.

Run the script:

python Wc3Banlist.py

Use the hotkeys:

Hotkey	Action
F3	Scan and auto-ban players
F6	Terminate the script

## How It Works
The script uses OCR (via Tesseract) to read player names from the lobby.

It compares those names to your Excel banlist.

Matching players are automatically banned using simulated keystrokes.

## Support

If you want to support me, you can do it here:

- [Buy Me a Coffee](https://buymeacoffee.com/RealFutureAi)
- [PayPal](https://paypal.me/FutureAI)

