import math
import operator
import pyautogui
import time
import numpy as np
from PIL import ImageGrab
from PIL import Image
from functools import reduce
import os

import get_picture

scale = np.zeros((2, 2), dtype=float)
cyc_num = 300  # 刷几次
time_internal = 0.6  # 截图间隔和点击等待时间
threshold = 13
digui_flag = 0


def screen_shot(pic_name):  # 截取对应坐标图片
    global scale
    f = open(get_picture.txt_path + "\\" + pic_name)
    line = f.readline()
    data_list = []
    while line:
        num = list(map(float, line.split()))
        data_list.append(num)
        line = f.readline()
    f.close()
    scale = np.array(data_list)
    screen_size = get_picture.get_screen_size()
    scale *= screen_size
    # print(scale)
    img = ImageGrab.grab(bbox=(scale[0][0], scale[0][1], scale[1][0], scale[1][1]))
    # print(img)
    return img


def compare_png(img_local, img_grab):  # 比较图像是否一致
    h1 = img_local.histogram()
    h2 = img_grab.histogram()
    # print((h2))
    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))))
    return result


def click_operation(img_local, txt_name):  # 点击截图位置
    start = time.time()
    if digui_flag:
        time.sleep(5)
    while 1:
        end = time.time()
        img_grab = screen_shot(txt_name)
        result = compare_png(img_local, img_grab)
        # print(result)
        if result < threshold:
            time.sleep(time_internal)
            pyautogui.leftClick(np.random.randint(scale[0][0], scale[1][0]),
                                np.random.randint(scale[0][1], scale[1][1]))
            return True
        if end - start > 50:
            return True
        time.sleep(time_internal)


def click_operation_2(s, txt_name, img_local):  # 点击非截图位置
    screen_size = get_picture.get_screen_size()
    s *= screen_size
    while 1:
        img_grab = screen_shot(txt_name)
        result = compare_png(img_local, img_grab)
        # print(result)
        if result < threshold:
            time.sleep(0.8)
            pyautogui.leftClick(np.random.randint(s[0][0], s[1][0]),
                                np.random.randint(s[0][1], s[1][1]))
            return True
        time.sleep(time_internal)


def yeyingguitan():  # 夜刀神活动
    pic_name = '夜影诡谈_战斗.png'
    txt_name = '夜影诡谈_战斗.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    click_operation(img_local, txt_name)


def zhandoujiesuan_1_huodong():  # 战斗胜利结算界面1
    s = np.zeros((2, 2), dtype=float)
    pic_name = '战斗结算_1_活动.png'
    txt_name = '战斗结算_1_活动.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    s[0][0] = 0.4890625
    s[0][1] = 0.45648148
    s[1][0] = 0.92760417
    s[1][1] = 0.84259259
    click_operation_2(s, txt_name, img_local)


def zhandoujiesuan_1_juexing():  # 觉醒胜利1
    s = np.zeros((2, 2), dtype=float)
    pic_name = '战斗结算_1_觉醒.png'
    txt_name = '战斗结算_1_觉醒.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    s[0][0] = 0.6990625
    s[0][1] = 0.53648148
    s[1][0] = 0.92760417
    s[1][1] = 0.77259259
    click_operation_2(s, txt_name, img_local)


def zhandoujiesuan_1_yuhun():  # 御魂胜利1
    s = np.zeros((2, 2), dtype=float)
    pic_name = '战斗结算_1_御魂.png'
    txt_name = '战斗结算_1_御魂.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    s[0][0] = 0.6990625
    s[0][1] = 0.53648148
    s[1][0] = 0.92760417
    s[1][1] = 0.77259259
    click_operation_2(s, txt_name, img_local)


def zhandoujiesuan_2():  # 战斗胜利结算界面2
    s = np.zeros((2, 2), dtype=float)
    pic_name = '战斗结算_2.png'
    txt_name = '战斗结算_2.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    s[0][0] = 0.60364583
    s[0][1] = 0.74722222
    s[1][0] = 0.92552083
    s[1][1] = 0.91018519
    click_operation_2(s, txt_name, img_local)


def zhandoujiesuan_2_5():
    s = np.zeros((2, 2), dtype=float)
    pic_name = '战斗结算_2.png'
    txt_name = '战斗结算_2.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    s[0][0] = 0.60364583
    s[0][1] = 0.74722222
    s[1][0] = 0.92552083
    s[1][1] = 0.91018519
    img_grab = screen_shot(txt_name)
    result = compare_png(img_local, img_grab)
    if result < threshold:
        time.sleep(0.5)
        pyautogui.leftClick(np.random.randint(s[0][0], s[1][0]),
                            np.random.randint(s[0][1], s[1][1]))
        return True


def zhandoujiesuan_1_5():
    s = np.zeros((2, 2), dtype=float)
    s[0][0] = 0.72708333
    s[0][1] = 0.57407407
    s[1][0] = 0.93854167
    s[1][1] = 0.79259259
    screen_size = get_picture.get_screen_size()
    s *= screen_size
    pyautogui.leftClick(np.random.randint(s[0][0], s[1][0]),
                        np.random.randint(s[0][1], s[1][1]))


def zhandoujiesuan_yongshengzhihai():  # 永生之海胜利2
    s = np.zeros((2, 2), dtype=float)
    pic_name = '永生之海结算.png'
    txt_name = '永生之海结算.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    s[0][0] = 0.60364583
    s[0][1] = 0.74722222
    s[1][0] = 0.92552083
    s[1][1] = 0.91018519
    click_operation_2(s, txt_name, img_local)


def zhandoushibai():  # 战斗失败
    s = np.zeros((2, 2), dtype=float)
    pic_name = '战斗失败.png'
    txt_name = '战斗失败.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    s[0][0] = 0.78125
    s[0][1] = 0.7167
    s[1][0] = 0.92552083
    s[1][1] = 0.91018519
    img_grab = screen_shot(txt_name)
    result = compare_png(img_local, img_grab)
    if result < threshold:
        click_operation_2(s, txt_name, img_local)


def fubentiaozhan():  # 御魂、觉醒等类似准备界面副本点击挑战
    pic_name = '副本挑战.png'
    txt_name = '副本挑战.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    click_operation(img_local, txt_name)


def yongshengzhihaitiaozhan():  # 永生之海点击挑战
    pic_name = '永生之海挑战.png'
    txt_name = '永生之海挑战.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    click_operation(img_local, txt_name)


def yuhun_duizhang():  # 多人队长
    fubentiaozhan()
    zhandoujiesuan_1_yuhun()
    time.sleep(0.5)
    zhandoujiesuan_1_5()
    zhandoujiesuan_2()
    return True


def yuhun_duiyuan():  # 多人队员
    zhandoujiesuan_1_yuhun()
    time.sleep(0.5)
    zhandoujiesuan_1_5()
    zhandoujiesuan_2()
    time.sleep(0.5)
    zhandoujiesuan_2_5()
    return True


def juexing_duiyuan():
    zhandoujiesuan_1_juexing()
    time.sleep(0.5)
    zhandoujiesuan_1_5()
    zhandoujiesuan_2()
    return True


def yongshengzhihai_duizhang():  # 永生之海队长
    yongshengzhihaitiaozhan()
    zhandoujiesuan_1_yuhun()
    time.sleep(0.5)
    zhandoujiesuan_1_5()
    time.sleep(3)
    zhandoujiesuan_2()
    return True


def yongshengzhihai_duiyuan():  # 永生之海队员
    zhandoujiesuan_1_yuhun()
    time.sleep(0.5)
    zhandoujiesuan_1_5()
    time.sleep(3)
    zhandoujiesuan_2()
    return True


def yuhun_shuangren():  # 控制双人御魂
    yuhun_duizhang()
    pyautogui.hotkey('alt', 'tab')
    yuhun_duiyuan()
    pyautogui.hotkey('alt', 'tab')


def yongshengzhihai_shuangren():  # 双人永生之海
    yongshengzhihai_duizhang()
    pyautogui.hotkey('alt', 'tab')
    yongshengzhihai_duiyuan()
    pyautogui.hotkey('alt', 'tab')


def tansuo():  # 庭院界面点击探索
    screen_size = get_picture.get_screen_size()
    pic_name = '勾玉.png'
    txt_name = '勾玉.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    img_grab = screen_shot(txt_name)
    result = compare_png(img_local, img_grab)
    # print(result)
    if result < threshold:
        pyautogui.mouseDown(0.6385 * screen_size[0], 0.7194 * screen_size[1], button='left')
        pyautogui.moveTo(0.4 * screen_size[0], 0.7194 * screen_size[1], 0.5)
        pyautogui.mouseUp(button='left')
        time.sleep(0.5)
        pyautogui.leftClick(0.3953 * screen_size[0], 0.225 * screen_size[1])
    return True


def jiejietupo():  # 探索界面开始结界突破
    # time.sleep(5)
    win_num = 0
    screen_size = get_picture.get_screen_size()
    # print((0.3953 * screen_size[0], 0.225 * screen_size[1]))
    pyautogui.leftClick(0.2432 * screen_size[0], 0.9259 * screen_size[1])
    pic_name = '结界刷新.png'
    txt_name = '结界刷新.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    click_operation(img_local, txt_name)
    pic_name = '刷新确认.png'
    txt_name = '刷新确认.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    click_operation(img_local, txt_name)
    enemies_pos = np.zeros((9, 2), dtype=float)
    enemies_pos[0][0] = 0.309375
    enemies_pos[0][1] = 0.32592593
    attack_pos = np.zeros((9, 2), dtype=float)
    attack_pos[0][0] = 0.30104167
    attack_pos[0][1] = 0.54166667
    for i in range(1, 9):
        enemies_pos[i][0] = enemies_pos[0][0] + i % 3 * 0.2604
        enemies_pos[i][1] = enemies_pos[0][1] + i // 3 * 0.1889
        attack_pos[i][0] = attack_pos[0][0] + i % 3 * 0.2604
        attack_pos[i][1] = attack_pos[0][1] + i // 3 * 0.1889
    enemies_pos *= screen_size
    attack_pos *= screen_size
    # print(enemies_pos, attack_pos)
    for i in range(0, 9):
        time.sleep(1)
        pic_name = '结界挑战券0.png'
        txt_name = '结界挑战券0.txt'
        img_local = Image.open(get_picture.img_path + '\\' + pic_name)
        img_grab = screen_shot(txt_name)
        result = compare_png(img_local, img_grab)
        # print(result)
        if result < threshold:
            print("挑战券不足")
            os.system("pause")
        while 1:
            pic_name = '结界界面.png'
            txt_name = '结界界面.txt'
            img_local = Image.open(get_picture.img_path + '\\' + pic_name)
            img_grab = screen_shot(txt_name)
            result = compare_png(img_local, img_grab)
            if result < threshold:
                break
            time.sleep(0.5)
        time.sleep(time_internal)
        pyautogui.leftClick(enemies_pos[i][0], enemies_pos[i][1])
        time.sleep(1 + np.random.random(1))
        pyautogui.leftClick(attack_pos[i][0], attack_pos[i][1])
        time.sleep(2)
        biaojishishen(3)
        while 1:
            pic_name = '战斗结算_1_觉醒.png'
            txt_name = '战斗结算_1_觉醒.txt'
            img_local = Image.open(get_picture.img_path + '\\' + pic_name)
            img_grab = screen_shot(txt_name)
            result = compare_png(img_local, img_grab)
            # print(result)
            if result < threshold:
                zhandoujiesuan_1_juexing()
                time.sleep(time_internal)
                zhandoujiesuan_1_5()
                zhandoujiesuan_2()
                win_num += 1
                break
            else:
                pic_name = '战斗失败.png'
                txt_name = '战斗失败.txt'
                img_local = Image.open(get_picture.img_path + '\\' + pic_name)
                img_grab = screen_shot(txt_name)
                result = compare_png(img_local, img_grab)
                # print(result)
                if result < threshold:
                    zhandoushibai()
                    break
            time.sleep(time_internal)
        if win_num == 3:
            win_num = 0
            time.sleep(4)
            pic_name = '战斗结算_2.png'
            txt_name = '战斗结算_2.txt'
            img_local = Image.open(get_picture.img_path + '\\' + pic_name)
            img_grab = screen_shot(txt_name)
            result = compare_png(img_local, img_grab)
            if result < threshold:
                # zhandoujiesuan_1_5()
                zhandoujiesuan_2()


def diyuguiwang():
    s = np.zeros((2, 2), dtype=float)
    global digui_flag
    digui_flag = 1
    screen_size = get_picture.get_screen_size()
    pyautogui.leftClick(0.6484 * screen_size[0], 0.8870 * screen_size[1])
    pic_name = '地域最强.png'
    txt_name = '地域最强.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    click_operation(img_local, txt_name)
    digui_flag = 0
    time.sleep(2)
    pyautogui.leftClick(0.0927 * screen_size[0], 0.4278 * screen_size[1])
    time.sleep(2)
    pyautogui.leftClick(0.2646 * screen_size[0], 0.7046 * screen_size[1])
    time.sleep(2)
    pyautogui.mouseDown(0.4068 * screen_size[0], 0.4093 * screen_size[1], button='left')
    pyautogui.moveTo(0.1240 * screen_size[0], 0.4074 * screen_size[1], 0.5)
    pyautogui.mouseUp(button='left')
    pic_name = '地鬼挑战.png'
    txt_name = '地鬼挑战.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    click_operation(img_local, txt_name)
    time.sleep(5)
    pic_name = '地鬼挑战_提示.png'
    txt_name = '地鬼挑战_提示.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    s[0][0] = 0.8146
    s[0][1] = 0.7231
    s[1][0] = 0.8781
    s[1][1] = 0.8352
    img_grab = screen_shot(txt_name)
    result = compare_png(img_local, img_grab)
    if result < threshold:
        pyautogui.leftClick(np.random.randint(s[0][0], s[1][0]),
                            np.random.randint(s[0][1], s[1][1]))
    time.sleep(2)
    pyautogui.leftClick(0.8661 * screen_size[0], 0.7472 * screen_size[1])
    zhandoujiesuan_1_yuhun()
    zhandoujiesuan_2()


def biaojishishen(pos):  # 标记1~5号位式神
    screen_size = get_picture.get_screen_size()
    pic_name = '战斗就绪.png'
    txt_name = '战斗就绪.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    while 1:
        time.sleep(time_internal)
        img_grab = screen_shot(txt_name)
        result = compare_png(img_local, img_grab)
        # print("biaojishishen:", result)
        if result < 13:
            if pos == 3:
                time.sleep(1)
                pyautogui.leftClick(0.4839 * screen_size[0], 0.5407 * screen_size[1])
                return True
            elif pos == 5:
                time.sleep(1)
                pyautogui.leftClick(0.4839 * screen_size[0], 0.5407 * screen_size[1])
                return True


def richang():  # 点击日常活动
    screen_size = get_picture.get_screen_size()
    pic_name = '勾玉.png'
    txt_name = '勾玉.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    img_grab = screen_shot(txt_name)
    result = compare_png(img_local, img_grab)
    # print(result)
    if result < threshold:
        pyautogui.leftClick(0.0359 * screen_size[0], 0.4139 * screen_size[1])
    return True


def douji():  # 斗技界面开始斗技
    screen_size = get_picture.get_screen_size()
    # pic_name = '勾玉.png'
    # txt_name = '勾玉.txt'
    # img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    # img_grab = screen_shot(txt_name)
    # result = compare_png(img_local, img_grab)
    # print(result)
    result = 0
    if result < threshold:
        # pyautogui.leftClick(0.5604 * screen_size[0], 0.4009 * screen_size[1])
        # pic_name = '町中武馆.png'
        # txt_name = '町中武馆.txt'
        # img_local = Image.open(get_picture.img_path + '\\' + pic_name)
        # click_operation(img_local, txt_name)
        # pic_name = '斗技.png'
        # txt_name = '斗技.txt'
        # img_local = Image.open(get_picture.img_path + '\\' + pic_name)
        # click_operation(img_local, txt_name)
        for i in range(cyc_num):
            screen_size = get_picture.get_screen_size()
            while 1:
                pic_name = '斗技界面.png'
                txt_name = '斗技界面.txt'
                img_local = Image.open(get_picture.img_path + '\\' + pic_name)
                img_grab = screen_shot(txt_name)
                result = compare_png(img_local, img_grab)
                if result < threshold:
                    break
                time.sleep(0.5)
            time.sleep(1)
            pyautogui.leftClick(0.9328 * screen_size[0], 84815 * screen_size[1])
            while 1:
                pic_name = '战斗就绪.png'
                txt_name = '战斗就绪.txt'
                img_local = Image.open(get_picture.img_path + '\\' + pic_name)
                time.sleep(time_internal)
                img_grab = screen_shot(txt_name)
                result = compare_png(img_local, img_grab)
                # print(result)
                if result < threshold:
                    time.sleep(1)
                    pyautogui.leftClick(0.9187 * screen_size[0], 0.8231 * screen_size[1])
                    break
                else:
                    pic_name = '自动上阵.png'
                    txt_name = '自动上阵.txt'
                    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
                    time.sleep(time_internal)
                    img_grab = screen_shot(txt_name)
                    result = compare_png(img_local, img_grab)
                    if result < threshold:
                        click_operation(img_local, txt_name)
                        break
            pic_name = '斗技战斗就绪.png'
            txt_name = '斗技战斗就绪.txt'
            img_local = Image.open(get_picture.img_path + '\\' + pic_name)
            while 1:
                time.sleep(time_internal)
                img_grab = screen_shot(txt_name)
                result = compare_png(img_local, img_grab)
                # print("doujijiuxu:", result)
                if result < threshold:
                    time.sleep(1)
                    pic_name = '斗技手动.png'
                    txt_name = '斗技手动.txt'
                    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
                    img_grab = screen_shot(txt_name)
                    result = compare_png(img_local, img_grab)
                    # print("doujishoudong:", result)
                    if result < threshold:
                        s = np.zeros((2, 2), dtype=float)
                        s[0][0] = 0.038
                        s[0][1] = 0.90
                        s[1][0] = 0.05
                        s[1][1] = 0.92
                        click_operation_2(s, txt_name, img_local)
                        time.sleep(1)
                        # biaojishishen(3)
                        break
                    else:
                        time.sleep(1)
                        # biaojishishen(3)
                        break
            #
            # while 1:
            #     time.sleep(time_internal)
            #     pic_name = '战斗结算.png'
            #     txt_name = '战斗结算.txt'
            #     img_local = Image.open(get_picture.img_path + '\\' + pic_name)
            #     img_grab = screen_shot(txt_name)
            #     result = compare_png(img_local, img_grab)
            #     print("zhandoujiesuan:", result)
            #     if result < threshold:
            #         break
            while 1:
                pic_name = '斗技胜利.png'
                txt_name = '斗技胜利.txt'
                img_local = Image.open(get_picture.img_path + '\\' + pic_name)
                img_grab = screen_shot(txt_name)
                result = compare_png(img_local, img_grab)
                # print("doujishengli:", result)
                if result < threshold:
                    s = np.zeros((2, 2), dtype=float)
                    s[0][0] = 0.36197917
                    s[0][1] = 0.82777778
                    s[1][0] = 0.94895833
                    s[1][1] = 0.96666667
                    click_operation_2(s, txt_name, img_local)
                    break
                else:
                    pic_name = '斗技失败.png'
                    txt_name = '斗技失败.txt'
                    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
                    img_grab = screen_shot(txt_name)
                    result = compare_png(img_local, img_grab)
                    # print("doujishibai:", result)
                    if result < threshold:
                        s = np.zeros((2, 2), dtype=float)
                        s[0][0] = 0.40364583
                        s[0][1] = 0.87962963
                        s[1][0] = 0.98229167
                        s[1][1] = 0.97962963
                        click_operation_2(s, txt_name, img_local)
                        break
    return True


def zidongjieshouyaoqing():  # 队员自动接受邀请
    pic_name = '町中武馆.png'
    txt_name = '町中武馆.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    click_operation(img_local, txt_name)


def yanmo():
    pic_name = '阎魔战斗.png'
    txt_name = '阎魔战斗.txt'
    img_local = Image.open(get_picture.img_path + '\\' + pic_name)
    click_operation(img_local, txt_name)
    juexing_duiyuan()


def main():
    i = 0
    time.sleep(5)
    # douji()
    # tansuo()
    while i < cyc_num:
        # yongshengzhihai_shuangren()
        # yuhun_shuangren()
        # yongshengzhihai_duizhang()
        # jiejietupo()
        yuhun_duiyuan()
        # yuhun_duizhang()
        # juexing_duiyuan(  )
        # zhandoujiesuan_2()
        # if not i:
        #     zidongjieshouyaoqing()
        i += 1
        if not i % 10:
            print("cyc:", i)


if __name__ == "__main__":
    main()
