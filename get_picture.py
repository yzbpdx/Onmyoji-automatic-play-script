import os.path
import pyautogui
import PyHook3
import pythoncom
import win32api
import numpy as np
from PIL import ImageGrab
import time
import cv2
import os

click_count = 0
scale = np.zeros((2, 2), dtype=float)
img_path = r".\print_screen_mumu"
txt_path = r'.\print_screen_mumu'


def onMouseEvent(event):  # 鼠标动作时读取位置坐标
    # print(event.WindowName)
    # print(event.Wheel)
    global click_count, scale
    pos = event.Position
    print(pos)  # type_tuple
    click_count += 1
    screen_size = get_screen_size()
    if click_count == 1:
        scale[0] = np.array(pos).astype(float)
        scale[0] /= screen_size
        print(scale[0])
    elif click_count == 2:
        scale[1] = np.array(pos).astype(float)
        scale[1] /= screen_size
        print(scale[1])
        if scale[0][0] >= scale[1][0] or scale[0][1] >= scale[1][1]:
            print("error")
            win32api.PostQuitMessage()
            return False
        save_path = os.path.join(txt_path, 'picture.txt')
        np.savetxt(save_path, scale, fmt="%8f")
        print_screen(scale)
        win32api.PostQuitMessage()
    return True


def get_screen_size():  # 读取屏幕分辨率
    return pyautogui.size()  # type_Class_pyautogui


def print_screen(s):  # 截图，保存到上示相对路径
    time.sleep(2)
    save_path = os.path.join(img_path, 'picture.png')
    screen_size = get_screen_size()
    s *= screen_size
    print(s)
    img = ImageGrab.grab(bbox=(s[0][0], s[0][1], s[1][0], s[1][1]))
    img.save(save_path)
    img_cv = cv2.imread(save_path)
    cv2.namedWindow("picture")
    cv2.imshow("picture", img_cv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return True


# def get_mouse_postion():
#     if

def main():
    hm = PyHook3.HookManager()
    hm.MouseLeftDown = onMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()


if __name__ == "__main__":
    main()
