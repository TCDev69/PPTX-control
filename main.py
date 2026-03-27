import keyboard
import win32gui
import win32con
import win32api
import time
WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x0202
WM_APPCOMMAND = 0x0319
APPCOMMAND_BROWSER_BACKWARD = 1
def trova_slideshow():
    hwnd = win32gui.FindWindow("screenClass", None)
    return hwnd
def esegui_avanti():
    hwnd = trova_slideshow()
    if hwnd:
        rect = win32gui.GetWindowRect(hwnd)
        width, height = rect[2] - rect[0], rect[3] - rect[1]
        lparam = win32api.MAKELONG(width // 2, height // 2)
        win32gui.PostMessage(hwnd, WM_LBUTTONDOWN, win32con.MK_LBUTTON, lparam)
        win32gui.PostMessage(hwnd, WM_LBUTTONUP, 0, lparam)
        win32gui.PostMessage(hwnd, win32con.WM_NULL, 0, 0)
        print("Avanti")
    else:
        print("PPT non in F5")
def esegui_indietro():
    hwnd = trova_slideshow()
    if hwnd:
        win32gui.PostMessage(hwnd, WM_APPCOMMAND, 0, (APPCOMMAND_BROWSER_BACKWARD << 16))
        win32gui.PostMessage(hwnd, win32con.WM_NULL, 0, 0)
        print("Indietro")
    else:
        print("PPT non in F5")
print("Controller PPTX")
keyboard.add_hotkey('page down', esegui_avanti, suppress=True, trigger_on_release=True)
keyboard.add_hotkey('page up', esegui_indietro, suppress=True, trigger_on_release=True)
print("In ascolto, premi ESC per uscire.")
keyboard.wait('esc')
