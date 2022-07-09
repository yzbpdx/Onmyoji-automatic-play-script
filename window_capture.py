import win32gui
import win32con
import win32api

name = u'000000000010082A'
# handle = win32gui.FindWindow("LDPlayerMainFrame", None)
# handle1 = win32gui.FindWindowEx(handle, None, "RenderWindow", None)
# handle2 = win32gui.FindWindowEx(handle1, None, "subWin", None)
handle = win32gui.FindWindow("OrpheusBrowserHost", None)
handle1 = win32gui.FindWindowEx(handle, None, "CefBrowserWindow", None)
handle2 = win32gui.FindWindowEx(handle1, None, "Chrome_WidgetWin_0", None)
print(hex(handle))
print(hex(handle1))
print(hex(handle2))
# left, top, right, bottom = win32gui.GetWindowRect(handle)
# print(left, top, right, bottom)
windowRec = win32gui.GetWindowRect(handle2)
print(windowRec)
# x = -windowRec[0] + 688
# y = -windowRec[1] + 94
x = -windowRec[0] + 52
y = -windowRec[1] + 41
print(x, y)
# title = win32gui.GetWindowText(handle)
# clsname = win32gui.GetClassName(handle)
# for i in range(200, 500):
#     for j in range(100, 300):
#         x = -windowRec[0] + i
#         y = -windowRec[1] + j
#         l = win32api.MAKELONG(x, y)
#         win32api.SendMessage(handle2, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, l)
#         win32api.SendMessage(handle2, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, l)
#         print(i, j)
l = win32api.MAKELONG(x, y)
# win32gui.SetForegroundWindow(handle2)
win32api.SendMessage(handle2, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, l)
win32api.SendMessage(handle2, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, l)
#     print(i, j)