import time
import pytesseract
import cv2
import pyautogui
from grab_screen import grab_screen
import keyboard
import openpyxl
import os
import difflib

# Tesseract OCR path - Set your Path to your tesseract.exe here like in the example
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Path to the Excel file with the ban list - Set your Path to your Excel Banlist here
banlist_path = r'C:\Users\Alpha-Omega\Desktop\Cloudspeicher\Privat\Zocken\Banlist\banlist.xlsx'

# Load Banlist from Excel file
def load_banlist():
    if not os.path.exists(banlist_path):
        print("Ban list file not found.")
        return {}

    wb = openpyxl.load_workbook(banlist_path)
    ws = wb.active
    banlist = {}

    for row in ws.iter_rows(min_row=2, values_only=True):
        name = str(row[0]).strip().lower()
        reason = str(row[1]).strip()
        if name:
            banlist[name] = reason

    return banlist

def preprocess_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_resized = cv2.resize(gray, None, fx=1.0, fy=1.0)
    _, processed_img = cv2.threshold(img_resized, 150, 255, cv2.THRESH_BINARY)
    return processed_img

def get_text_data(img):
    preprocessed_img = preprocess_image(img)
    data = pytesseract.image_to_data(preprocessed_img, output_type=pytesseract.Output.DICT)
    return data

def check_banned(players, banlist):
    banned_players = []
    for player in players:
        player_lower = player['text'].lower()
        for banned_player in banlist:
            if player_lower == banned_player or difflib.SequenceMatcher(None, player_lower, banned_player).ratio() > 0.8:
                banned_players.append((player, banlist[banned_player]))
                break
    return banned_players

def extract_players_with_positions():
    players = []
    for coords in [(400, 520, 850, 900), (1700, 520, 2150, 900)]:
        frame = grab_screen(coords)
        text_data = get_text_data(frame)
        for i in range(len(text_data['text'])):
            if text_data['text'][i].strip():
                players.append({
                    'text': text_data['text'][i],
                    'x': text_data['left'][i] + coords[0],
                    'y': text_data['top'][i] + coords[1]
                })
    return players

def click_banned_players(banned_players):
    for player, reason in banned_players:
        x, y = player['x'], player['y']
        x_right = x + 40
        y_below = y + 15
        pyautogui.moveTo(x_right, y_below)
        pyautogui.click()
        time.sleep(1)
        y_below_second_click = y + 260
        pyautogui.moveTo(x_right, y_below_second_click)
        pyautogui.click()
        time.sleep(0.5)

def handle_exit():
    print("Exit program.")
    global running
    running = False

# Run banlist
def handle_f3():
    players_with_positions = extract_players_with_positions()

    # Output players
    print("Extracted Players:")
    for player in players_with_positions:
        print(player['text'])

    keyboard.write("Download Wc3Banlist at: https://github.com/RealFutureAI/WC3Banlist")
    time.sleep(.1)
    keyboard.send('enter')
    time.sleep(.1)
    keyboard.write("Players banned:")
    time.sleep(.1)
    keyboard.send('enter')
    time.sleep(.1)

    banned_from_list = check_banned(players_with_positions, load_banlist())
    for player, reason in banned_from_list:
        keyboard.write(f"{player['text']} - Reason: {reason}")
        time.sleep(.1)
        keyboard.send('enter')
        print(f"{player['text']} - Reason: {reason}")

    # Click on banned players
    click_banned_players(banned_from_list)


# Add Hotkeys
keyboard.add_hotkey("F3", handle_f3)
keyboard.add_hotkey("F6", handle_exit)

# Variable to check if the program is running
running = True

print("The Program runs in background. Press F3 to check banned or F6 stop the program.")

# check if hotkeys are pressed
while running:
    time.sleep(0.1)  # short delay, to reduce CPU lag
