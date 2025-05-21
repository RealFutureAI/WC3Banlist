# WC3Banlist - UPLOAD SOON
A working Banlist for Warcraft 3

This python script uses pytesseract OCR and Microsoft Excel to read all the playernames in your lobby and compares it with your Excel Banlist file.
If there are matching entries, the script will automatically ban the players from your lobby. The script will also output an optional reason, why the players have been banned before kicking them from the lobby. Example:
Players banned:
<name> - Reason: leaver
<name2> - Reason: flamer

This output will be written in the lobby and in the terminal.

Hotkeys:
F3: Check for banned players in the lobby and ban them
F6: End the script

More Info:
The terminal will also output all read names. This is useful if you want to add someone to the banlist after the game to check the read names.
Your Banlist Excel file must have 2 rows called "name" and "reason".
The Tesseract OCR will make mistakes in reading some names, especially russian or asian names. To fix this, add the name what the banlist actually read to your list instead of their names.
The Banlist will also automatically ban names which are very close to actual names. 
Example: 
Player "testing" ist banned for being a leaver.
Player "tseting" joins the game.
Since his name is almost the same as "testing" he will also get banned!
This is for more precise checking the banned players as OCR never guarantees correctly reading the names.

Installation:
Do not try to use this without any programming knowledge as the setup is not very easy!

1. Download Python and install it
2. Download Tesseract OCR and install it
3. Download Wc3Banlist.py
4. Install all dependencies with pip
5. Run the script in your favorite environment
6. F3 to check bans, F6 to end script

