# Onmyoji-automatic-play-script
****
## -*- coding: utf-8 -*-
"""  
@author yzbpdx  
@date 2022年7月22日 13:42:33  
@version 1.0.0  
"""
****
## 说明
仅供参考讨论交流，自用脚本不传播，程序中的截图未提供。  
使用pyhook3和pyautogui实现物理点击。
****
### 环境
不建议直接使用yys.yaml，文件中提供了pyhook3本地包。
### 程序
excute.py执行自动战斗功能，包括御魂、觉醒、结界、斗技等。  
get_picture.py点击截图区域左上和右下可进行截图，保存图片(png)和点击的位置信息(txt)。  
window_capture.py挂载程序窗口，不过模拟器阻止了向窗口内发送信息，并未使用这种方法。
