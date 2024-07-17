#!/usr/bin/python3
# -*- coding: utf-8 -*-


#################################################################################

# Title: Scale OCR
# Explain: Computer Automated Measurement using Intel-OpenCV ( Open Source Computer Vision Library ) and HP-Google-Tesseract ( Optical Character Recognition ) , Graphical User Interface using Python tkinter.
# Author: 趙健
# E-mail: 283640621@qq.com
# Telephont number: +86 18604537694
# E-mail: chinaorcaz@gmail.com
# Date: 歲在丙申
# Operating system: Windows10 x86_64 Inter(R)-Core(TM)-m3-6Y30
# Interpreter: python-3.12.4-amd64.exe
# Interpreter: Python-3.12.4-tar.xz, Python-3.12.4-amd64.deb
# Operating system: google-pixel-6 android-11 termux-0.118 ubuntu-22.04-LTS-rootfs arm64-aarch64 MSM8998-Snapdragon835-Qualcomm®-Kryo™-280
# Interpreter: Python-3.10.6-tar.xz, python3-3.10.6-aarch64.deb

#################################################################################


import os  # 加載 Python 原生的操作系統接口模組「os」;
import sys  # 加載 Python 原生的使用或維護的變量的接口模組「sys」;
import signal, stat  # 加載Python原生的「」;
# import math  # 導入 Python 原生包「math」，用於數學計算;
# import random  # 導入 Python 原生包「random」，用於生成隨機數;
# import json  # 導入 Python 原生模組「json」，用於解析 JSON 文檔;
# import platform  # 加載Python原生的與平臺屬性有關的模組;
import inspect  # from inspect import isfunction 加載Python原生的模組、用於判斷對象是否為函數類型;
# import ctypes  # 用於强制終止綫程;
# import multiprocessing  # 加載Python原生的支持多進程模組;
# # from multiprocessing import Process, Pool;
# import subprocess  # 加載Python原生的創建子進程模組;
import threading  # 加載Python原生的支持多綫程（執行緒）模組;
# from queue import Queue
import queue
# from socketserver import ThreadingMixIn  #, ForkingMixIn
# import string  # 加載Python原生的字符串處理模組;
import datetime, time  # 加載Python原生的日期數據處理模組;
# import re  # 加載Python原生的正則表達式對象
# from tempfile import TemporaryFile, TemporaryDirectory, NamedTemporaryFile  # 用於創建臨時目錄和臨時文檔;
import pathlib  # from pathlib import Path 用於檢查判斷指定的路徑對象是目錄還是文檔;
# import struct  # 用於讀、寫、操作二進制本地硬盤文檔;
# import shutil  # 用於刪除完整硬盤目錄樹，清空文件夾;
# import urllib  # 加載Python原生的創建客戶端訪問請求連接模組，urllib 用於對 URL 進行編解碼;
# from urllib import request as urllib_request
# import http.client  # 加載Python原生的創建客戶端訪問請求連接模組;
# from http.server import HTTPServer, BaseHTTPRequestHandler  # 加載Python原生的創建簡單http服務器模組;
# https: // docs.python.org/3/library/http.server.html
# from http import cookiejar  # 用於處理請求Cookie;
# import ssl  # 用於處理請求證書驗證;
# import base64  # 加載加、解密模組;
# 使用base64編碼類似位元組的物件（字節對象）「s」，並返回一個位元組物件（字節對象），可選 altchars 應該是長度為2的位元組串，它為'+'和'/'字元指定另一個字母表，這允許應用程式，比如，生成url或檔案系統安全base64字串;
# base64.b64encode(s, altchars=None)
# 解碼 base64 編碼的位元組類物件（字節對象）或 ASCII 字串「s」，可選的 altchars 必須是一個位元組類物件或長度為2的ascii字串，它指定使用的替代字母表，替代'+'和'/'字元，返回位元組物件，如果「s」被錯誤地填充，則會引發 binascii.Error，如果 validate 為 false（默認），則在填充檢查之前，既不在正常的base-64字母表中也不在替代字母表中的字元將被丟棄，如果 validate 為 True，則輸入中的這些非字母表字元將導致 binascii.Error;
# base64.b64decode(s, altchars=None, validate=False)

# import warnings
# # 棄用控制臺打印警告信息;
# def fxn():
#     warnings.warn("deprecated", DeprecationWarning)  # 棄用控制臺打印警告信息;
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore")
#     fxn()
# with warnings.catch_warnings(record=True) as w:
#     # Cause all warnings to always be triggered.
#     warnings.simplefilter("always")
#     # Trigger a warning.
#     fxn()
#     # Verify some things
#     assert len(w) == 1
#     assert issubclass(w[-1].category, DeprecationWarning)
#     assert "deprecated" in str(w[-1].message)

from tkinter import messagebox as tk_messagebox  # 窗體 tkinter 模組的消息提示框組件;
from tkinter import filedialog as tk_filedialog  # 窗體 tkinter 模組的文檔選擇框組件;
# from tkinter import scrolledtext as tk_scrolledtext  # 窗體 tkinter 模組的滾動條組件;
import tkinter as tk  # 導入 Python 原生模組「tkinter」，用於創建窗口面板，注意如果是 Ubuntu 系統，需要事先安裝配置成功： apt install python3-tk;


# 導入第三方擴展包，需要事先已經在操作系統控制臺命令行安裝配置成功;
# 先升級 pip 擴展包管理工具：root@localhost:~# python -m pip install --upgrade pip
# 再安裝第三方擴展包：root@localhost:~# pip install numpy -i https://mirrors.aliyun.com/pypi/simple/
import numpy as np
import pandas as pd
from pandas import Series as pandas_Series  # 從第三方擴展包「pandas」中導入一維向量「Series」模組，用於構建擴展包「pandas」的一維向量「Series」類型變量;
from pandas import DataFrame as pandas_DataFrame  # 從第三方擴展包「pandas」中導入二維矩陣「DataFrame」模組，用於構建擴展包「pandas」的二維矩陣「DataFrame」類型變量;
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import matplotlib.font_manager as matplotlib_font_manager  # 導入第三方擴展包「matplotlib」中的字體管理器，用於設置生成圖片中文字的字體;
# large = 22; med = 16; small = 12
# params = {
#     'axes.titlesize': large,
#     'legend.fontsize': med,
#     'figure.figsize': (16, 10),
#     'axes.labelsize': med,
#     'axes.titlesize': med,
#     'xtick.labelsize': med,
#     'ytick.labelsize': med,
#     'figure.titlesize': large,
#     'font.sans-serif': 'SimHei',
#     'axes.unicode_minus': False
# }
# plt.rcParams.update(params)
# https://docs.sympy.org/latest/tutorial/preliminaries.html#installation
# import sympy  # 導入第三方擴展包「sympy」，用於符號計算;
# https://www.scipy.org/docs.html
# import scipy
# from scipy import stats as scipy_stats  # 導入第三方擴展包「scipy」，用於實現 beta 分佈概率密度函數;
# import scipy.stats as scipy_stats
# from scipy import ndimage as scipy_ndimage  # 導入第三方擴展包「scipy」中的圖片處理模組「ndimage」，用於實現圖形旋轉矯正操作;
# from scipy import optimize as scipy_optimize  # 導入第三方擴展包「scipy」中的最優化模組「optimize」，用於方程擬合;
# from scipy.interpolate import make_interp_spline as scipy_interpolate_make_interp_spline  # 導入第三方擴展包「scipy」中的插值模組「interpolate」中的「make_interp_spline()」函數，用於擬合插值函數;
# from scipy import special as scipy_special  # 導入第三方擴展包「scipy」中的最優化模組「special」，用於使用「special」模組中的「comb()」函數計算組合數;
from PIL import Image, ImageTk  # 導入第三方擴展包「PIL」，用於從硬盤讀取圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;
# # 需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 OpenCV 應用成功：root@localhost:~# apt install libavcodec-dev libavformat-dev libswscale-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libgtk2.0-dev libgtk-3-dev libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev libjasper-dev libopencv-dev python3-opencv ;
# # 注意，因爲函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，而且因爲庫「opencv-python」與「opencv-contrib-python」之間互相衝突，二者不能同時存在，只能選其一安裝，所以，只能安裝「opencv-contrib-python」庫：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
# import cv2  # 導入第三方擴展包「opencv-contrib-python」，用於驅動 OpenCV 光學圖形處理庫，需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 OpenCV 應用成功：root@localhost:~# apt install libavcodec-dev libavformat-dev libswscale-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libgtk2.0-dev libgtk-3-dev libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev libjasper-dev libopencv-dev python3-opencv ;
# # 需要事先在控制臺安裝配置成功：root@localhost:~# pip install pytesseract -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 Tesseract-OCR 應用成功：root@localhost:~# apt install tesseract-ocr libtesseract-dev tesseract-ocr-chi-tra tesseract-ocr-chi_tra_vert tesseract-ocr-chi-sim tesseract-ocr-chi_sim_vert ;
# import pytesseract  # 導入第三方擴展包「pytesseract」，用於驅動 Tesseract-OCR 文字識別庫，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pytesseract -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 Tesseract-OCR 應用成功：root@localhost:~# apt install tesseract-ocr libtesseract-dev tesseract-ocr-chi-tra tesseract-ocr-chi_tra_vert tesseract-ocr-chi-sim tesseract-ocr-chi_sim_vert ;
import openpyxl  # 導入第三方擴展包「openpyxl」，用於 Python 的 pandas 工具與 MicroSoft Office Excel 軟體通信互傳數據時的解析引擎; 需要事先安裝配置成功： pip3 install openpyxl -i https://mirrors.aliyun.com/pypi/simple/
# import xlwt  # 導入第三方擴展包「xlwt」，用於 Python 的 pandas 工具寫入 MicroSoft Office Excel 軟體通信時的解析引擎; 需要事先安裝配置成功： pip3 install xlwt -i https://mirrors.aliyun.com/pypi/simple/
# import xlrd  # 導入第三方擴展包「xlrd」，用於 Python 的 pandas 工具讀取 MicroSoft Office Excel 軟體通信時的解析引擎; 需要事先安裝配置成功： pip3 install xlrd -i https://mirrors.aliyun.com/pypi/simple/


# # 匯入自定義路由模組脚本文檔「./Router.py」;
# # os.getcwd() # 獲取當前工作目錄路徑;
# # os.path.abspath("..")  # 當前運行脚本所在目錄上一層的絕對路徑;
# # os.path.join(os.path.abspath("."), 'Router.py')  # 拼接路徑字符串;
# # pathlib.Path(os.path.join(os.path.abspath("."), Router.py)  # 返回路徑對象;
# # sys.path.append(os.path.abspath(".."))  # 將上一層目錄加入系統的搜索清單，當導入脚本時會增加搜索這個自定義添加的路徑;
# # 注意導入本地 Python 脚本，只寫文檔名不要加文檔的擴展名「.py」，如果不使用 sys.path.append() 函數添加自定義其它的搜索路徑，則只能放在當前的工作目錄「"."」
# sys.path.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "src", "py"))).replace('\\', '/'))  # 將當前目錄中的子目錄「"./py/"」加入系統的搜索清單，當導入脚本時會增加搜索這個自定義添加的路徑;
# sys.path.append("C:/Criss/OCR-Measuring-Scale/src/py/")
import Input_and_Output as Input_and_Output  # 導入當前運行代碼所在目錄的，自定義脚本文檔「./Input_and_Output.py」;
Input_and_Output_Function = Input_and_Output.Input_and_Output
Run_Input_and_Output = Input_and_Output.Run_Input_and_Output
Path_Conversion = Input_and_Output.Path_Conversion
Queue_update = Input_and_Output.Queue_update
# check_json_format = Input_and_Output.check_json_format
# win_file_is_Used = Input_and_Output.win_file_is_Used
# clear_Directory = Input_and_Output.clear_Directory
# formatByte = Input_and_Output.formatByte
import optical_character_recognition as optical_character_recognition  # 導入當前運行代碼所在目錄的，自定義脚本文檔「./optical_character_recognition.py」;
do_data = optical_character_recognition.do_data

# # 匯入自定義統計描述模組脚本文檔「./Statis_Descript.py」;
# # # sys.path.append(os.path.abspath(".."))  # 將上一層目錄加入系統的搜索清單，當導入脚本時會增加搜索這個自定義添加的路徑;
# # 注意導入本地 Python 脚本，只寫文檔名不要加文檔的擴展名「.py」，如果不使用 sys.path.append() 函數添加自定義其它的搜索路徑，則只能放在當前的工作目錄「"."」;
# from Statis_Descript import Transformation as Transformation  # 導入自定義 Python 脚本文檔「./Statis_Descript.py」中的數據歸一化、數據變換函數「Transformation()」，用於將原始數據歸一化處理;
# from Statis_Descript import outliers_clean as outliers_clean  # 導入自定義 Python 脚本文檔「./Statis_Descript.py」中的離群值檢查（含有粗大誤差的數據）函數「outliers_clean()」，用於檢查原始數據歸中的離群值;



# 控制臺傳參;
# sys_argv = sys.argv[0] # 通過 sys.argv 數組獲取從控制臺傳入的參數
# for i in range(len(sys.argv)):
#     print('arg '+str(i), sys.argv[i])  # 通過 sys.argv 數組獲取從控制臺傳入的參數

# # sub_Process
# Python_say = ""
# # 内置函數 vars() 的作用是获取已定义變量对象的字典，vars().has_key('testVar') 是測試變量'testVar'是否在變量字典中，即變量'testVar'是否已被定義;
# if len(sys.argv) > 1:
#     # print(type(sys.argv[1]))
#     # print(sys.argv[1])
#     # 使用自定義函數check_json_format(raw_msg)判斷傳入參數sys.argv[1]是否為JSON格式的字符串
#     if check_json_format(sys.argv[1]):
#         request_argv_2_JSON = json.loads(sys.argv[1], encoding='utf-8')  # 將讀取到的傳入參數字符串轉換爲JSON對象;
#     else:
#         request_argv_2_JSON = {
#             "Node_say": sys.argv[1]
#         }

#     # 首先判斷傳入的參數是否為一個字符串，如果不是，則强制轉換為字符串:
#     if isinstance(request_argv_2_JSON["Node_say"], str):
#         # 判斷字符串中是否包含指定字符，也可以是用 "char" in String 語句判斷;
#         if request_argv_2_JSON["Node_say"].find("_", 0, int(len(request_argv_2_JSON["Node_say"])-1)):
#             Node_say = request_argv_2_JSON["Node_say"].replace("_", " ") # 將傳入參數字符串中的"_"字符替換為空" "字符
#         else:
#             Node_say = request_argv_2_JSON["Node_say"]
#     else:
#         Node_say = str(request_argv_2_JSON["Node_say"]) # str() 函數可以將任意對象轉換為字符串;

#     # print("Node.js say: ", Node_say)
#     if Node_say == "How are you" or Node_say == "How are you." or Node_say == "How are you!" or Node_say == "How are you !":
#         Python_say = "Fine, thank you, and you ?"
#     else:
#         Python_say = "我現在只會説：「 Fine, thank you, and you ? 」，您就不能按規矩說一個：「 How are you ! 」"
# else:
#     Python_say = "聽不見你説啥 !"

# # print("Python say: ", Python_say)
# response_JSON = {"Python_say": Python_say, "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
# response_String = json.dumps(response_JSON)  # .encode('utf-8')
# sys.stderr.write(response_String)  # 將運算結果寫到操作系統控制臺;
# # print(response_String)  # 將運算結果打印到操作系統控制臺;
# # sys.stdout.write(response_String)  # 將運算結果寫到操作系統控制臺;
# # input_String = sys.stdin.readline()  # 從鍵盤輸入一行字符串，注意只能是字符串類型;
# # print(input_String)

# # Python 使用 shell 語句調用其它語言
# # node 環境;
# # test.js  待執行的JS的檔;
# # %s %s  傳遞給JS檔的參數;
# # shell_to = os.popen('node test.js %s %s' % (1, 2))  執行shell命令，拿到輸出結果;
# shell_to = os.popen('node %s %s %s %s %s' % (to_script, outputTest_path, input_dir, do_Function, inputTest_path))  # 執行shell命令，拿到輸出結果;
# # print(shell_to.readlines());
# result = shell_to.read()  # 取出執行結果
# print(result)
# # // JavaScript 脚本代碼使用 process.argv 傳遞給Node.JS的參數 [nodePath, jsPath, arg1, arg2, ...];
# # let arg1 = process.argv[2];  // 解析出JS參數;
# # let arg2 = process.argv[3];

# # eval(expression[, globals[, locals]]) 函數用來執行一個字符串表達式，並返字符串表達式的值;
# # 參數 expression ：表示待運算的字符串運算式;
# # 參數 globals ：表示變量作用域，全域命名空間，如果被提供，則必須是一個字典對象;
# # 參數 locals ：變量作用域，局部命名空間，如果被提供，可以是任何映射物件;



# 自定義封裝的函數check_json_format(raw_msg)用於判斷是否為JSON格式的字符串;
def check_json_format(raw_msg):
    """
    用於判斷一個字符串是否符合 JSON 格式
    :param self:
    :return:
    """
    if isinstance(raw_msg, str):  # 首先判斷傳入的參數是否為一個字符串，如果不是直接返回false值
        try:
            json.loads(raw_msg)  # , encoding='utf-8'
            return True
        except ValueError:
            return False
    else:
        return False

# 遞歸清空指定目錄（文件夾）下的所有内容（不包括這個文件夾），使用 Python 原生的標準 os 模組;
def clear_Directory(dir_path):
    # os.chdir(dir_path)  # 改變當前工作目錄到指定的路徑;
    list_dir = os.listdir(dir_path)
    if len(list_dir) > 0:
        for f in list_dir:
            if os.path.isfile(dir_path + "\\%s" % f):
                os.remove(dir_path + "\\%s" % f)
            else:
                list_dir_2 = os.listdir(dir_path + "\\%s" % f)
                if len(list_dir_2) > 0:
                    clear_Directory(dir_path + "\\%s" % f)

    list_dir = os.listdir(dir_path)
    if len(list_dir) > 0:
        for f in list_dir:
            if os.path.isfile(dir_path + "\\%s" % f):
                os.remove(dir_path + "\\%s" % f)
            else:
                list_dir_2 = os.listdir(dir_path + "\\%s" % f)
                if len(list_dir_2) == 0:
                    os.rmdir(dir_path + "\\%s" % f)

    return list_dir

# 格式化文檔大小輸出形式;
def formatByte(number):
    for(scale.label) in [(1024*1024*1024, "GB"), (1024*1024, "MB"), (1024, "KB")]:
        if number >= scale:
            return "%.2f %s" % (number*1.0/scale, lable)
        elif number == 1:
            return "1 字節"
        else:
            # 小於 1 字節;
            byte = "%.2f" % (number or 0)
    return str(byte[:-3] if byte.endswith(".00") else byte) + " 字節"

# # 自定義函數，只能在 Windows 系統使用，判斷某個文檔是否被其它進程占用;
# def win_file_is_Used(file_name):
#     try:
#         vHandle = win32file.CreateFile(file_name, win32file.GENERIC_READ, 0, None, win32file.OPEN_EXISTING, win32file.FILE_ATTRIBUTE_NORMAL, None)
#         return int(vHandle) == win32file.INVALID_HANDLE_VALUE
#     except:
#         return True
#     finally:
#         try:
#             win32file.CloseHandle(vHandle)
#         except:
#             pass




# def do_data(require_data):

#     # print(require_data)
#     # print(typeof(require_data))
#     # require_data_bytes = require_data.encode("utf-8")
#     # require_data = require_data_bytes.decode("utf-8")
#     # require_data = str(require_data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
#     # require_data_len = len(bytes(require_data, "utf-8"))
#     # print(typeof(require_data_bytes))

#     # # 使用自定義函數check_json_format(raw_msg)判斷讀取到的請求體表單"form"數據 request_form_value 是否為JSON格式的字符串;
#     # if check_json_format(require_data_String):
#     #     # 將讀取到的請求體表單"form"數據字符串轉換爲JSON對象;
#     #     require_data_JSON = json.loads(require_data_String)  # , encoding='utf-8'
#     # else:
#     #     now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
#     #     require_data_JSON = {
#     #         "Client_say": require_data_String,
#     #         "time": str(now_date)
#     #     }
#     # # print(require_data_JSON)
#     # # print(typeof(require_data_JSON))

#     # Client_say = ""
#     # # 使用函數 isinstance(require_data_JSON, dict) 判斷傳入的參數 require_data_JSON 是否為 dict 字典（JSON）格式對象;
#     # if isinstance(require_data_JSON, dict):
#     #     # 使用 JSON.__contains__("key") 或 "key" in JSON 判断某个"key"是否在JSON中;
#     #     if (require_data_JSON.__contains__("Client_say")):
#     #         Client_say = require_data_JSON["Client_say"]
#     #     else:
#     #         Client_say = ""
#     #         # print('客戶端發送的請求 JSON 對象中無法找到目標鍵(key)信息 ["Client_say"].')
#     #         # print(require_data_JSON)
#     # else:
#     #     Client_say = require_data_JSON

#     # Server_say = Client_say  # "require no problem."
#     # # if Client_say == "How are you" or Client_say == "How are you." or Client_say == "How are you!" or Client_say == "How are you !":
#     # #     Server_say = "Fine, thank you, and you ?"
#     # # else:
#     # #     Server_say = "我現在只會説：「 Fine, thank you, and you ? 」，您就不能按規矩說一個：「 How are you ! 」"

#     # now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
#     # # print(now_date)
#     # response_data_JSON = {
#     #     "Server_say": Server_say,
#     #     "require_Authorization": "",
#     #     "time": str(now_date)
#     # }
#     # # check_json_format(request_data_JSON);
#     # # String = json.dumps(JSON); JSON = json.loads(String);

#     # response_data_String = Server_say
#     # if isinstance(response_data_JSON, dict):
#     #     response_data_String = json.dumps(response_data_JSON)  # 將JOSN對象轉換為JSON字符串;

#     # # response_data_String = str(rresponse_data_String, encoding="utf-8")  # str("", encoding="utf-8") 强制轉換為 "utf-8" 編碼的字符串類型數據;
#     # # .encode("utf-8")將字符串（str）對象轉換為 "utf-8" 編碼的二進制字節流（<bytes>）類型數據;
#     # response_data_bytes = response_data_String.encode("utf-8")
#     # response_data_String_len = len(bytes(response_data_String, "utf-8"))

#     response = require_data

#     return response


# def Input_and_Output(is_window, screenwidth, screenheight, is_Concurrent, is_storage_position, is_storage_type, input_Train_Path, input_Train_File_Array, input_Test_Path, input_Test_File_Array, do_Function, output_Test_Path, output_Test_File_Array, output_Test_URL, time_sleep, outqueue_from_task_to_host, outqueue_from_host_to_task, is_Runing, file_Data, result_Data, complete_Number, Error_Log, Label_State, Text_display_result, image_sample, Canvas_display_sample, Label_display_sample):

#     # if is_Concurrent == "0" or is_Concurrent == 0:
#     #     global is_Runing
#     #     if is_window:
#     #         # global screenwidth
#     #         # global screenheight
#     #         global image_sample
#     #     global input_dir
#     #     global output_dir
#     #     global file_Data
#     #     global result_Data
#     #     global complete_Number
#     #     global Error_Log
#     #     # global file_Data_bytes
#     #     # global file_Data_len

#     # global is_Runing
#     if is_Concurrent == "Multi-Threading":
#         is_Runing = True
#         if outqueue_from_host_to_task:
#             # def Queue_update(outqueue_from_host_to_task):
#             #     # outqueue_from_task_to_host = outqueue[0]
#             #     # outqueue_from_host_to_task = outqueue[1]
#             #     try:
#             #         if outqueue_from_host_to_task.empty():
#             #             window_root.after(250, Queue_update, outqueue_from_host_to_task)
#             #             pass
#             #         if not outqueue_from_host_to_task.empty():
#             #             msg = outqueue_from_host_to_task.get(
#             #                 block=False,
#             #                 timeout=None
#             #             )
#             #             if msg[0] == "is_Runing_True":
#             #                 is_Runing = True
#             #                 window_root.after(250, Queue_update, outqueue_from_host_to_task)
#             #                 # pass
#             #                 # return return_value
#             #             elif msg[0] == "is_Runing_False":
#             #                 is_Runing = False
#             #                 window_root.after(250, Queue_update, outqueue_from_host_to_task)
#             #                 # pass
#             #                 # return return_value
#             #         # else:
#             #         #     # By not calling window_root.after here, we allow update to
#             #         #     # truly end
#             #         #     window_root.after(250, Queue_update, outqueue_from_host_to_task)
#             #         #     pass
#             #     except queue.Empty:
#             #         window_root.after(250, Queue_update, outqueue_from_host_to_task)
#             # window_root.after(250, Queue_update, outqueue_from_host_to_task)
#             if not outqueue_from_host_to_task.empty():
#                 msg = outqueue_from_host_to_task.get(
#                     block=False,
#                     timeout=None
#                 )
#                 if msg[0] == "is_Runing_True":
#                     is_Runing = True
#                     # window_root.after(250, Queue_update, outqueue_from_host_to_task)
#                     # pass
#                     # return return_value
#                 elif msg[0] == "is_Runing_False":
#                     is_Runing = False
#                     # window_root.after(250, Queue_update, outqueue_from_host_to_task)
#                     # pass
#                     # return return_value

#     # global file_Data
#     # global file_Data_bytes
#     # global file_Data_len
#     file_Data = ""
#     # file_Data_bytes = file_Data.encode("utf-8")
#     # file_Data = file_Data_bytes.decode("utf-8")
#     # file_Data = str(file_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
#     # file_Data_len = len(bytes(file_Data, "utf-8"))

#     # global result_Data
#     result_Data = ""
#     # result_Data_bytes = result_Data.encode("utf-8")
#     # result_Data = result_Data_bytes.decode("utf-8")
#     # result_Data = str(result_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
#     # result_Data_len = len(bytes(result_Data, "utf-8"))

#     # global image_sample
#     image_sample = []

#     # global complete_Number
#     complete_Number = int(0)

#     # global Error_Log
#     Error_Log = []

#     if len(input_Test_File_Array) == 0:
#         log_Error = [
#             "Error",
#             str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#             str(os.path.normpath(str(input_Test_Path))).replace('\\', '/')
#         ]

#         if is_Concurrent == "0" or is_Concurrent == 0:
#             # sys.stdout.write("\n")  # 輸出換行;
#             # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_Path))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
#             # sys.stdout.write("\n")  # 輸出換行;
#             print("運行錯誤." + "\n" + "路徑: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_Path))).replace('\\', '/') + " ]" + "\n" + "找不到可處理檔.")
#             if is_window:
#                 Label_State['text'] = "運行錯誤." + "\n" + "路徑: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_Path))).replace('\\', '/') + " ]" + "\n" + "找不到可處理檔."

#         if is_Concurrent == "Multi-Threading":
#             if outqueue_from_task_to_host:
#                 outqueue_from_task_to_host.put(
#                     log_Wrong,
#                     block=False,
#                     timeout=None
#                 )

#         Error_Log.append(str(os.path.normpath(str(input_Test_Path))).replace('\\', '/'))
#         return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_Path))).replace('\\', '/')

#     if is_window:
#         if is_Concurrent == "0" or is_Concurrent == 0:
#             # global image_sample
#             image_sample = []
#             Canvas_display_sample.delete("all")
#             # Canvas_display_sample.create_image(
#             #     0,
#             #     0,
#             #     anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#             #     image=image_sample,
#             #     # fill="red",
#             #     tag="one"
#             # )
#             # Canvas_display_sample.delete(tag="one")
#             Label_display_sample['text'] = "Input file"

#         if is_Concurrent == "Multi-Threading":
#             log_Message = [
#                 "image_sample_delete",
#                 ""
#             ]
#             if outqueue_from_task_to_host:
#                 outqueue_from_task_to_host.put(
#                     log_Message,
#                     block=False,
#                     timeout=None
#                 )

#     # input_Test_Path = Entry_inputTest_path.get()  # 讀取文本框輸入的内容;
#     # input_Test_Path = str(input_Test_Path).replace('\\', '/')
#     # output_Test_Path = Entry_outputTest_path.get()  # 讀取文本框輸入的内容;
#     # output_Test_Path = str(output_Test_Path).replace('\\', '/')

#     # 檢查並創建運算結果輸出目錄;
#     if is_storage_position == "Database_and_Disk" or is_storage_position == "Disk":

#         if len(output_Test_Path) > 0:

#             output_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')

#             # 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
#             if os.path.exists(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')).is_dir():
#                 # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
#                 if not (os.access(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), os.W_OK)):
#                     try:
#                         # 修改文檔權限 mode:777 任何人可讀寫;
#                         os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
#                         # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
#                         # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
#                         # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
#                         # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
#                         # stat.S_IXOTH:  其他用戶有執行權0o001
#                         # stat.S_IWOTH:  其他用戶有寫許可權0o002
#                         # stat.S_IROTH:  其他用戶有讀許可權0o004
#                         # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
#                         # stat.S_IXGRP:  組用戶有執行許可權0o010
#                         # stat.S_IWGRP:  組用戶有寫許可權0o020
#                         # stat.S_IRGRP:  組用戶有讀許可權0o040
#                         # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
#                         # stat.S_IXUSR:  擁有者具有執行許可權0o100
#                         # stat.S_IWUSR:  擁有者具有寫許可權0o200
#                         # stat.S_IRUSR:  擁有者具有讀許可權0o400

#                         # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
#                         # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
#                         # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
#                         # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
#                         # stat.S_IREAD:  windows下設為唯讀
#                         # stat.S_IWRITE: windows下取消唯讀
#                     except OSError as error:
#                         if is_Concurrent == "0" or is_Concurrent == 0:
#                             sys.stdout.write("\n")  # 輸出換行;
#                             sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                             sys.stdout.write("\n")  # 輸出換行;
#                             # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')} : {error}')
#                             # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
#                             if is_window:
#                                 Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
#                         if is_Concurrent == "Multi-Threading":
#                             if outqueue_from_task_to_host:
#                                 outqueue_from_task_to_host.put(
#                                     [
#                                         "Error",
#                                         str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                         str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'),
#                                         str(error)
#                                     ],
#                                     block=False,
#                                     timeout=None
#                                 )
#                         Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'))
#                         return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')
#             else:
#                 try:
#                     # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
#                     # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
#                     os.makedirs(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), mode=0o777, exist_ok=True)
#                 except FileExistsError as error:
#                     # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
#                     if is_Concurrent == "0" or is_Concurrent == 0:
#                         sys.stdout.write("\n")  # 輸出換行;
#                         sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                         sys.stdout.write("\n")  # 輸出換行;
#                         # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')} : {error}')
#                         # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
#                         if is_window:
#                             Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
#                     if is_Concurrent == "Multi-Threading":
#                         if outqueue_from_task_to_host:
#                             outqueue_from_task_to_host.put(
#                                 [
#                                     "Error",
#                                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                     str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'),
#                                     str(error)
#                                 ],
#                                 block=False,
#                                 timeout=None
#                             )
#                     Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'))
#                     return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')

#             if not (os.path.exists(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')).is_dir()):
#                 if is_Concurrent == "0" or is_Concurrent == 0:
#                     sys.stdout.write("\n")  # 輸出換行;
#                     sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
#                     sys.stdout.write("\n")  # 輸出換行;
#                     # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')} : {error}')
#                     # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
#                     if is_window:
#                         Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
#                 if is_Concurrent == "Multi-Threading":
#                     if outqueue_from_task_to_host:
#                         outqueue_from_task_to_host.put(
#                             [
#                                 "Error",
#                                 str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                 str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')
#                             ],
#                             block=False,
#                             timeout=None
#                         )
#                 Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'))
#                 return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')

#     # input_Test_Path = input_Test_Path.replace('/', r'\\')
#     # print(input_Test_File_Array)
#     # for item in input_Test_File_Array:
#     #     print(item)
#     #     tk_messagebox.showinfo(
#     #         title="溫馨提示 input_Test_Path",
#     #         message=str(item)
#     #     )

#     for i in range(0, len(input_Test_File_Array)):

#         if is_Concurrent == "Multi-Threading":
#             if outqueue_from_host_to_task:
#                 # def Queue_update(outqueue_from_host_to_task):
#                 #     # outqueue_from_task_to_host = outqueue[0]
#                 #     # outqueue_from_host_to_task = outqueue[1]
#                 #     try:
#                 #         if outqueue_from_host_to_task.empty():
#                 #             window_root.after(250, Queue_update, outqueue_from_host_to_task)
#                 #             pass
#                 #         if not outqueue_from_host_to_task.empty():
#                 #             msg = outqueue_from_host_to_task.get(
#                 #                 block=False,
#                 #                 timeout=None
#                 #             )
#                 #             if msg[0] == "is_Runing_True":
#                 #                 is_Runing = True
#                 #                 window_root.after(250, Queue_update, outqueue_from_host_to_task)
#                 #                 # pass
#                 #                 # return return_value
#                 #             elif msg[0] == "is_Runing_False":
#                 #                 is_Runing = False
#                 #                 window_root.after(250, Queue_update, outqueue_from_host_to_task)
#                 #                 # pass
#                 #                 # return return_value
#                 #         # else:
#                 #         #     # By not calling window_root.after here, we allow update to
#                 #         #     # truly end
#                 #         #     window_root.after(250, Queue_update, outqueue_from_host_to_task)
#                 #         #     pass
#                 #     except queue.Empty:
#                 #         window_root.after(250, Queue_update, outqueue_from_host_to_task)
#                 # window_root.after(250, Queue_update, outqueue_from_host_to_task)
#                 if not outqueue_from_host_to_task.empty():
#                     msg = outqueue_from_host_to_task.get(
#                         block=False,
#                         timeout=None
#                     )
#                     if msg[0] == "is_Runing_True":
#                         is_Runing = True
#                         # window_root.after(250, Queue_update, outqueue_from_host_to_task)
#                         # pass
#                         # return return_value
#                     elif msg[0] == "is_Runing_False":
#                         is_Runing = False
#                         # window_root.after(250, Queue_update, outqueue_from_host_to_task)
#                         # pass
#                         # return return_value

#         if not is_Runing:

#             if is_Concurrent == "Multi-Threading":
#                 if outqueue_from_task_to_host:
#                     if len(Error_Log) > 0:
#                         outqueue_from_task_to_host.put(
#                             [
#                                 "Discontinue",
#                                 "Error",
#                                 "[" + str(len(Error_Log)) + "]",
#                                 str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                 str(','.join(Error_Log))
#                             ],
#                             block=False,
#                             timeout=None
#                         )
#                     else:
#                         outqueue_from_task_to_host.put(
#                             [
#                                 "Discontinue",
#                                 "Complete",
#                                 "[" + str(complete_Number) + "]",
#                                 str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                 input_Test_Path,
#                                 output_Test_Path
#                             ],
#                             block=False,
#                             timeout=None
#                         )

#             # continue
#             # break
#             if len(Error_Log) > 0:
#                 return "Error," + str(len(Error_Log)) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(','.join(Error_Log))
#             else:
#                 return "Complete," + str(complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_Test_Path + "," + output_Test_Path  # None

#         # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
#         # print(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))

#         if is_Concurrent == "0" or is_Concurrent == 0:
#             if is_window:
#                 Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
#         if is_Concurrent == "Multi-Threading":
#             if outqueue_from_task_to_host:
#                 outqueue_from_task_to_host.put(
#                     [
#                         "Runing",
#                         str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                         str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
#                     ],
#                     block=False,
#                     timeout=None
#                 )

#         file_Data = ""
#         result_Data = ""

#         if is_window:
#             if is_Concurrent == "0" or is_Concurrent == 0:
#                 image_sample = []
#                 # 清除自定義畫布組件中已經繪製的指定圖片;
#                 Canvas_display_sample.delete("all")
#                 # Canvas_display_sample.delete(tag="one")
#                 # Canvas_display_sample.create_image(
#                 #     0,
#                 #     0,
#                 #     anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#                 #     image=image_sample,
#                 #     # fill="red",
#                 #     tag="one"
#                 # )
#                 Label_display_sample['text'] = "Input file"
#             if is_Concurrent == "Multi-Threading":
#                 log_Message = [
#                     "image_sample_delete",
#                     ""
#                 ]
#                 if outqueue_from_task_to_host:
#                     outqueue_from_task_to_host.put(
#                         log_Message,
#                         block=False,
#                         timeout=None
#                     )

#         if os.path.exists(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')) and os.path.isfile(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')):

#             # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
#             if not (os.access(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), os.W_OK)):
#                 try:
#                     # 修改文檔權限 mode:777 任何人可讀寫;
#                     os.chmod(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
#                     # os.chmod(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
#                     # os.chmod(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
#                     # os.chmod(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
#                     # os.chmod(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
#                     # stat.S_IXOTH:  其他用戶有執行權0o001
#                     # stat.S_IWOTH:  其他用戶有寫許可權0o002
#                     # stat.S_IROTH:  其他用戶有讀許可權0o004
#                     # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
#                     # stat.S_IXGRP:  組用戶有執行許可權0o010
#                     # stat.S_IWGRP:  組用戶有寫許可權0o020
#                     # stat.S_IRGRP:  組用戶有讀許可權0o040
#                     # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
#                     # stat.S_IXUSR:  擁有者具有執行許可權0o100
#                     # stat.S_IWUSR:  擁有者具有寫許可權0o200
#                     # stat.S_IRUSR:  擁有者具有讀許可權0o400
#                     # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
#                     # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
#                     # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
#                     # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
#                     # stat.S_IREAD:  windows下設為唯讀
#                     # stat.S_IWRITE: windows下取消唯讀
#                 except OSError as error:
#                     if is_Concurrent == "0" or is_Concurrent == 0:
#                         sys.stdout.write("\n")
#                         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                         sys.stdout.write("\n")
#                         # print(error)
#                         # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
#                         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
#                         if is_window:
#                             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
#                     if is_Concurrent == "Multi-Threading":
#                         if outqueue_from_task_to_host:
#                             outqueue_from_task_to_host.put(
#                                 [
#                                     "Wrong",
#                                     str(int(i) + 1),
#                                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                     str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                                     str(error)
#                                 ],
#                                 block=False,
#                                 timeout=None
#                             )
#                     Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#                     # break
#                     continue

#             fd = open(
#                 str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                 mode="rb+",  # 讀取文本字符：mode="r"，讀取二進制字節<class 'bytes'>：mode="rb+"
#                 buffering=-1,
#                 # encoding="utf-8",
#                 errors=None,
#                 newline=None,
#                 closefd=True,
#                 opener=None
#             )
#             try:
#                 file_Data = fd.read()
#                 # file_Data = fd.read().decode("utf-8")
#                 # data_Bytes = file_Data.encode("utf-8")
#                 # file_Data = str(data_Bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
#                 # fd.write(data_Bytes)
#             except FileNotFoundError:
#                 if is_Concurrent == "0" or is_Concurrent == 0:
#                     sys.stdout.write("\n")
#                     sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                     sys.stdout.write("\n")
#                     # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在.")
#                     if is_window:
#                         Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在."
#                 if is_Concurrent == "Multi-Threading":
#                     if outqueue_from_task_to_host:
#                         outqueue_from_task_to_host.put(
#                             [
#                                 "Wrong",
#                                 str(int(i) + 1),
#                                 str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                 str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                                 str(error)
#                             ],
#                             block=False,
#                             timeout=None
#                         )
#                 Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#                 # break
#                 continue
#             # except PersmissionError:
#             #     if is_Concurrent == "0" or is_Concurrent == 0:
#             #         sys.stdout.write("\n")
#             #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#             #         sys.stdout.write("\n")
#             #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無操作權限.")
#             #         if is_window:
#             #             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無操作權限."
#             #     if is_Concurrent == "Multi-Threading":
#             #         if outqueue_from_task_to_host:
#             #             outqueue_from_task_to_host.put(
#             #                 [
#             #                     "Wrong",
#             #                     str(int(i) + 1),
#             #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#             #                     str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#             #                     str(error)
#             #                 ],
#             #                 block=False,
#             #                 timeout=None
#             #             )
#             #     Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#             #     # break
#             #     continue
#             except Exception as error:
#                 if("[WinError 32]" in str(error)):
#                     if is_Concurrent == "0" or is_Concurrent == 0:
#                         sys.stdout.write("\n")
#                         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                         sys.stdout.write("\n")
#                         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據.")
#                         # print(error)
#                         # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
#                         if is_window:
#                             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據."
#                         print("延時等待 " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ].")
#                         if is_window:
#                             # Label_State['text'] = "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
#                             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據." + "\n" + "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
#                     if is_Concurrent == "Multi-Threading":
#                         if outqueue_from_task_to_host:
#                             outqueue_from_task_to_host.put(
#                                 [
#                                     "Wrong",
#                                     str(int(i) + 1),
#                                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                     str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                                     str(error)
#                                 ],
#                                 block=False,
#                                 timeout=None
#                             )
#                     time.sleep(time_sleep)  # 用於讀取文檔時延遲參數，以防文檔被占用錯誤，單位（秒）;
#                     try:
#                         file_Data = fd.read()
#                         # file_Data = fd.read().decode("utf-8")
#                         # data_Bytes = file_Data.encode("utf-8")
#                         # fd.write(data_Bytes)
#                     except OSError as error:
#                         if is_Concurrent == "0" or is_Concurrent == 0:
#                             sys.stdout.write("\n")
#                             sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                             sys.stdout.write("\n")
#                             # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據.")
#                             # print(error)
#                             # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
#                             if is_window:
#                                 Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據."
#                         if is_Concurrent == "Multi-Threading":
#                             if outqueue_from_task_to_host:
#                                 outqueue_from_task_to_host.put(
#                                     [
#                                         "Wrong",
#                                         str(int(i) + 1),
#                                         str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                         str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                                         str(error)
#                                     ],
#                                     block=False,
#                                     timeout=None
#                                 )
#                         Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#                         # break
#                         continue
#                 else:
#                     if is_Concurrent == "0" or is_Concurrent == 0:
#                         sys.stdout.write("\n")
#                         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                         sys.stdout.write("\n")
#                         # print(error)
#                         # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
#                         if is_window:
#                             Label_State['text'] = "讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "發生錯誤." + "\n" + str(error)
#                     if is_Concurrent == "Multi-Threading":
#                         if outqueue_from_task_to_host:
#                             outqueue_from_task_to_host.put(
#                                 [
#                                     "Wrong",
#                                     str(int(i) + 1),
#                                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                     str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                                     str(error)
#                                 ],
#                                 block=False,
#                                 timeout=None
#                             )
#                     Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#                     # break
#                     continue
#             finally:
#                 fd.close()
#             # 注：可以用try/finally語句來確保最後能關閉檔，不能把open語句放在try塊裡，因為當打開檔出現異常時，檔物件file_object無法執行close()方法;


#             if is_window:
#                 # 讀取用於在畫布 canvas 組件中展示的樣本圖片;
#                 try:
#                     # image_sample = tk.PhotoImage(file=str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))  # 使用 Python 原生的 tkinter 包中的 tkinter.PhotoImage() 函數讀取圖片檔;
#                     imgFile = Image.open(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')).resize((int(int(screenwidth)*0.42), int(int(screenheight)*0.55)))  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.Image.open() 函數打開圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;
#                     image_sample = ImageTk.PhotoImage(imgFile)  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.ImageTk.PhotoImage() 函數讀取圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;

#                     if is_Concurrent == "0" or is_Concurrent == 0:
#                         Label_display_sample['text'] = str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
#                         # 在自定義畫布組件中展示讀入的圖片樣本;
#                         # Canvas_display_sample.delete("all")
#                         # Canvas_display_sample.delete(tag="one")
#                         Canvas_display_sample.create_image(
#                             0,
#                             0,
#                             anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#                             image=image_sample,
#                             # fill="red",
#                             tag="one"
#                         )

#                     if is_Concurrent == "Multi-Threading":
#                         if outqueue_from_task_to_host:
#                             outqueue_from_task_to_host.put(
#                                 [
#                                     "image_sample",
#                                     str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                                     image_sample
#                                 ],
#                                 block=False,
#                                 timeout=None
#                             )

#                 except FileNotFoundError:
#                     if is_Concurrent == "0" or is_Concurrent == 0:
#                         sys.stdout.write("\n")
#                         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                         sys.stdout.write("\n")
#                         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在.")
#                         Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在."
#                     if is_Concurrent == "Multi-Threading":
#                         if outqueue_from_task_to_host:
#                             outqueue_from_task_to_host.put(
#                                 [
#                                     "Wrong",
#                                     str(int(i) + 1),
#                                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                     str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                                     str(error)
#                                 ],
#                                 block=False,
#                                 timeout=None
#                             )
#                     # Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#                     # break
#                     # continue
#                 # except PersmissionError:
#                 #     if is_Concurrent == "0" or is_Concurrent == 0:
#                 #         sys.stdout.write("\n")
#                 #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                 #         sys.stdout.write("\n")
#                 #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無操作權限.")
#                 #         Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無操作權限."
#                 #     if is_Concurrent == "Multi-Threading":
#                 #         if outqueue_from_task_to_host:
#                 #             outqueue_from_task_to_host.put(
#                 #                 [
#                 #                     "Wrong",
#                 #                     str(int(i) + 1),
#                 #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                 #                     str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                 #                     str(error)
#                 #                 ],
#                 #                 block=False,
#                 #                 timeout=None
#                 #             )
#                 #     # Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#                 #     # break
#                 #     # continue
#                 except Exception as error:
#                     if("[WinError 32]" in str(error)):
#                         if is_Concurrent == "0" or is_Concurrent == 0:
#                             sys.stdout.write("\n")
#                             sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                             sys.stdout.write("\n")
#                             # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據.")
#                             # print(error)
#                             # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
#                             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據."
#                             print("延時等待 " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ].")
#                             # Label_State['text'] = "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
#                             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據." + "\n" + "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
#                         if is_Concurrent == "Multi-Threading":
#                             if outqueue_from_task_to_host:
#                                 outqueue_from_task_to_host.put(
#                                     [
#                                         "Wrong",
#                                         str(int(i) + 1),
#                                         str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                         str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                                         str(error)
#                                     ],
#                                     block=False,
#                                     timeout=None
#                                 )
#                         time.sleep(time_sleep)  # 用於讀取文檔時延遲參數，以防文檔被占用錯誤，單位（秒）;
#                         try:
#                             imgFile = Image.open(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')).resize((int(int(screenwidth)*0.42), int(int(screenheight)*0.55)))  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.Image.open() 函數打開圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;
#                             image_sample = ImageTk.PhotoImage(imgFile)  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.ImageTk.PhotoImage() 函數讀取圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;

#                             if is_Concurrent == "0" or is_Concurrent == 0:
#                                 Label_display_sample['text'] = str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
#                                 # 在自定義畫布組件中展示讀入的圖片樣本;
#                                 Canvas_display_sample.delete("all")
#                                 # Canvas_display_sample.delete(tag="one")
#                                 Canvas_display_sample.create_image(
#                                     0,
#                                     0,
#                                     anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#                                     image=image_sample,
#                                     # fill="red",
#                                     tag="one"
#                                 )

#                             if is_Concurrent == "Multi-Threading":
#                                 if outqueue_from_task_to_host:
#                                     outqueue_from_task_to_host.put(
#                                         [
#                                             "image_sample",
#                                             str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                                             image_sample
#                                         ],
#                                         block=False,
#                                         timeout=None
#                                     )

#                         except OSError as error:
#                             if is_Concurrent == "0" or is_Concurrent == 0:
#                                 sys.stdout.write("\n")
#                                 sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                                 sys.stdout.write("\n")
#                                 # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據.")
#                                 # print(error)
#                                 # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
#                                 Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據."
#                             if is_Concurrent == "Multi-Threading":
#                                 if outqueue_from_task_to_host:
#                                     outqueue_from_task_to_host.put(
#                                         [
#                                             "Wrong",
#                                             str(int(i) + 1),
#                                             str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                             str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                                             str(error)
#                                         ],
#                                         block=False,
#                                         timeout=None
#                                     )
#                             # Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#                             # break
#                             # continue
#                     else:
#                         if is_Concurrent == "0" or is_Concurrent == 0:
#                             sys.stdout.write("\n")
#                             sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                             sys.stdout.write("\n")
#                             # print(error)
#                             # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
#                             Label_State['text'] = "讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "發生錯誤." + "\n" + str(error)
#                         if is_Concurrent == "Multi-Threading":
#                             if outqueue_from_task_to_host:
#                                 outqueue_from_task_to_host.put(
#                                     [
#                                         "Wrong",
#                                         str(int(i) + 1),
#                                         str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                         str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                                         str(error)
#                                     ],
#                                     block=False,
#                                     timeout=None
#                                 )
#                         # Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#                         # break
#                         # continue
#                 finally:
#                     imgFile.close()
#                 # 注：可以用try/finally語句來確保最後能關閉檔，不能把open語句放在try塊裡，因為當打開檔出現異常時，檔物件file_object無法執行close()方法;


#             # # 使用 str("").encode("utf-8") 方法，將字符串（str）對象轉換為 "utf-8" 編碼的二進制字節流（<bytes>）類型數據;
#             # file_Data_bytes = file_Data.encode("utf-8")
#             # file_Data = file_Data_bytes.decode("utf-8")
#             # file_Data_len = len(bytes(file_Data, "utf-8"))


#             # # 讀取到輸入數據之後，刪除文檔;
#             # try:
#             #     os.remove(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))  # os.unlink(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')) 刪除文檔;
#             #     # os.listdir(input_dir)  # 刷新目錄内容列表
#             #     # print(os.listdir(input_dir))
#             # except Exception as error:
#             #     if is_Concurrent == "0" or is_Concurrent == 0:
#             #         print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除.")
#             #         print(f'Wrong: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
#             #         if is_window:
#             #             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除."
#             #     if is_Concurrent == "Multi-Threading":
#             #         if outqueue_from_task_to_host:
#             #             outqueue_from_task_to_host.put(
#             #                 [
#             #                     "Wrong",
#             #                     str(int(i) + 1),
#             #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#             #                     str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#             #                     str(error)
#             #                 ],
#             #                 block=False,
#             #                 timeout=None
#             #             )
#             #     if("[WinError 32]" in str(error)):
#             #         if is_Concurrent == "0" or is_Concurrent == 0:
#             #             print("延時等待 " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試刪除檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ].")
#             #             if is_window:
#             #                 # Label_State['text'] = "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試刪除檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
#             #                 Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除." + "\n" + "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試刪除檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
#             #         if is_Concurrent == "Multi-Threading":
#             #             if outqueue_from_task_to_host:
#             #                 outqueue_from_task_to_host.put(
#             #                     [
#             #                         "Wrong",
#             #                         str(int(i) + 1),
#             #                         str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#             #                         str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#             #                         str(error)
#             #                     ],
#             #                     block=False,
#             #                     timeout=None
#             #                 )
#             #         time.sleep(time_sleep)  # 用於刪除文檔時延遲參數，以防文檔被占用錯誤，單位（秒）;
#             #         try:
#             #             # os.unlink(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))  # 刪除文檔;
#             #             os.remove(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#             #             # os.listdir(input_dir)  # 刷新目錄内容列表
#             #             # print(os.listdir(input_dir))
#             #         except OSError as error:
#             #             if is_Concurrent == "0" or is_Concurrent == 0:
#             #                 print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除.")
#             #                 print(error)
#             #                 # print(f'Wrong: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
#             #                 if is_window:
#             #                     Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除."
#             #             if is_Concurrent == "Multi-Threading":
#             #                 if outqueue_from_task_to_host:
#             #                     outqueue_from_task_to_host.put(
#             #                         [
#             #                             "Wrong",
#             #                             str(int(i) + 1),
#             #                             str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#             #                             str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#             #                             str(error)
#             #                         ],
#             #                         block=False,
#             #                         timeout=None
#             #                     )
#             #             Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#             #             # break
#             #             continue
#             #     # else:
#             #     #     if is_Concurrent == "0" or is_Concurrent == 0:
#             #     #         print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除.")
#             #     #         print(error)
#             #     #         # print(f'Wrong: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
#             #     #         if is_window:
#             #     #             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除."
#             #     #     if is_Concurrent == "Multi-Threading":
#             #     #         if outqueue_from_task_to_host:
#             #     #             outqueue_from_task_to_host.put(
#             #     #                 [
#             #     #                     "Wrong",
#             #     #                     str(int(i) + 1),
#             #     #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#             #     #                     str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#             #     #                     str(error)
#             #     #                 ],
#             #     #                 block=False,
#             #     #                 timeout=None
#             #     #             )
#             #     #     Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#             #     #     # break
#             #     #     continue


#             # 在這裏插入具體的數據處理算法;
#             result_Data_JSON = do_Function(file_Data)
#             result_Data = result_Data_JSON

#             # print(type(file_Data))  # <class 'bytes'>
#             # result_Data = str(file_Data)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
#             # print(type(result_Data))  # <class 'str'>

#             # # String = json.dumps(JSON); JSON = json.loads(String);
#             # # 使用自定義函數check_json_format(raw_msg)判斷讀取到的請求體表單"form"數據 request_form_value 是否為JSON格式的字符串;
#             # if check_json_format(require_data_String):
#             #     # 將讀取到的請求體表單"form"數據字符串轉換爲JSON對象;
#             #     require_data_JSON = json.loads(require_data_String)  # , encoding='utf-8'
#             # # print(require_data_JSON)
#             # # print(typeof(require_data_JSON))

#             # Client_say = ""
#             # # 使用函數 isinstance(require_data_JSON, dict) 判斷傳入的參數 require_data_JSON 是否為 dict 字典（JSON）格式對象;
#             # if isinstance(require_data_JSON, dict):
#             #     # 使用 JSON.__contains__("key") 或 "key" in JSON 判断某个"key"是否在JSON中;
#             #     if (require_data_JSON.__contains__("Client_say")):
#             #         Client_say = require_data_JSON["Client_say"]

#             # 將運算結果寫入用於展示結果的多行文本輸入框;
#             if is_window:

#                 if is_Concurrent == "0" or is_Concurrent == 0:

#                     # Label_State['text'] = "Succeed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(input_Test_File_Array[i])
#                     Label_State['text'] = "Succeed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')

#                     # # 讀取多行文本輸入框中的内容;
#                     # Text_display_result_value = Text_display_result.get(
#                     #     "0.0",  # 表示讀取多行文本輸入框 .Text 控件中的全部值，如果設定參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始讀取;
#                     #     "end"  # 表示讀取至多行文本輸入框 .Text 控件中全部值的最後一個字符爲止;
#                     # )
#                     # Text_display_result_value = str(Text_display_result_value)
#                     # print(Text_display_result_value)

#                     # # 刪除多行文本輸入框中的内容;
#                     # Text_display_result.delete(
#                     #     "1.0",  # 參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始刪除;
#                     #     "end"  # 參數爲 "end" 表示刪除直至最後一個字符，即清空輸入框;
#                     # )

#                     # new_Text_display_result_value = Text_display_result_value + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Test_File_Array[i]) + "," + str(result_Data)

#                     # new_Text_display_result_value = str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Test_File_Array[i]) + "," + str(result_Data) + "\n"
#                     new_Text_display_result_value = str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n"
#                     # print(new_Text_display_result_value)

#                     # 將字符串寫入多行文本輸入框;
#                     Text_display_result.insert(
#                         "end",  # 參數 "1.0" 表示從第一行第一列開始插入，參數 "insert" 表示在當前光標位置處插入一個字符串，參數 "end" 表示在末尾位置處追加寫入一個字符串;
#                         str(new_Text_display_result_value)
#                     )

#                     Text_display_result.see("end"),  # 表示將 .Text 組件中聚焦在文本末行，即顯示末尾;

#             # 將運算結果寫入磁碟文檔;
#             if is_storage_position == "Database_and_Disk" or is_storage_position == "Disk":

#                 for j in range(0, len(output_Test_File_Array)):

#                     if len(str(output_Test_File_Array[j])) > 0:

#                         # output_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')

#                         # # 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
#                         # if os.path.exists(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')).is_dir():
#                         #     # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
#                         #     if not (os.access(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), os.W_OK)):
#                         #         try:
#                         #             # 修改文檔權限 mode:777 任何人可讀寫;
#                         #             os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
#                         #             # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
#                         #             # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
#                         #             # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
#                         #             # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
#                         #             # stat.S_IXOTH:  其他用戶有執行權0o001
#                         #             # stat.S_IWOTH:  其他用戶有寫許可權0o002
#                         #             # stat.S_IROTH:  其他用戶有讀許可權0o004
#                         #             # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
#                         #             # stat.S_IXGRP:  組用戶有執行許可權0o010
#                         #             # stat.S_IWGRP:  組用戶有寫許可權0o020
#                         #             # stat.S_IRGRP:  組用戶有讀許可權0o040
#                         #             # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
#                         #             # stat.S_IXUSR:  擁有者具有執行許可權0o100
#                         #             # stat.S_IWUSR:  擁有者具有寫許可權0o200
#                         #             # stat.S_IRUSR:  擁有者具有讀許可權0o400

#                         #             # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
#                         #             # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
#                         #             # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
#                         #             # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
#                         #             # stat.S_IREAD:  windows下設為唯讀
#                         #             # stat.S_IWRITE: windows下取消唯讀
#                         #         except OSError as error:
#                         #             if is_Concurrent == "0" or is_Concurrent == 0:
#                         #                 sys.stdout.write("\n")  # 輸出換行;
#                         #                 sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')) + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                         #                 sys.stdout.write("\n")  # 輸出換行;
#                         #                 # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')} : {error}')
#                         #                 # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
#                         #                 if is_window:
#                         #                     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
#                         #             if is_Concurrent == "Multi-Threading":
#                         #                 if outqueue_from_task_to_host:
#                         #                     outqueue_from_task_to_host.put(
#                         #                         [
#                         #                             "Wrong",
#                         #                             str(int(i) + 1),
#                         #                             str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                         #                             str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'),
#                         #                             str(error)
#                         #                         ],
#                         #                         block=False,
#                         #                         timeout=None
#                         #                     )
#                         #             Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'))
#                         #             # break
#                         #             continue
#                         # else:
#                         #     try:
#                         #         # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
#                         #         # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
#                         #         os.makedirs(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), mode=0o777, exist_ok=True)
#                         #     except FileExistsError as error:
#                         #         # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
#                         #         if is_Concurrent == "0" or is_Concurrent == 0:
#                         #             sys.stdout.write("\n")  # 輸出換行;
#                         #             sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')) + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                         #             sys.stdout.write("\n")  # 輸出換行;
#                         #             # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')} : {error}')
#                         #             # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
#                         #             if is_window:
#                         #                 Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
#                         #         if is_Concurrent == "Multi-Threading":
#                         #             if outqueue_from_task_to_host:
#                         #                 outqueue_from_task_to_host.put(
#                         #                     [
#                         #                         "Wrong",
#                         #                         str(int(i) + 1),
#                         #                         str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                         #                         str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'),
#                         #                         str(error)
#                         #                     ],
#                         #                     block=False,
#                         #                     timeout=None
#                         #                 )
#                         #         Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'))
#                         #         # break
#                         #         continue

#                         # if not (os.path.exists(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')).is_dir()):
#                         #     if is_Concurrent == "0" or is_Concurrent == 0:
#                         #         sys.stdout.write("\n")  # 輸出換行;
#                         #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')))  # 將字符串輸出寫到操作系統控制臺;
#                         #         sys.stdout.write("\n")  # 輸出換行;
#                         #         # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')} : {error}')
#                         #         # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
#                         #         if is_window:
#                         #             Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
#                         #     if is_Concurrent == "Multi-Threading":
#                         #         if outqueue_from_task_to_host:
#                         #             outqueue_from_task_to_host.put(
#                         #                 [
#                         #                     "Wrong",
#                         #                     str(int(i) + 1),
#                         #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                         #                     str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')
#                         #                 ],
#                         #                 block=False,
#                         #                 timeout=None
#                         #             )
#                         #     Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'))
#                         #     # break
#                         #     continue


#                         # 判斷文檔，是否已經存在且是否為文檔;
#                         if os.path.exists(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')) and os.path.isfile(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')):
#                             # print(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), "is a file 是一個文檔.")
#                             # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
#                             if not (os.access(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), os.W_OK)):
#                                 try:
#                                     # 修改文檔權限 mode:777 任何人可讀寫;
#                                     os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
#                                     # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
#                                     # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
#                                     # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
#                                     # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
#                                     # stat.S_IXOTH:  其他用戶有執行權0o001
#                                     # stat.S_IWOTH:  其他用戶有寫許可權0o002
#                                     # stat.S_IROTH:  其他用戶有讀許可權0o004
#                                     # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
#                                     # stat.S_IXGRP:  組用戶有執行許可權0o010
#                                     # stat.S_IWGRP:  組用戶有寫許可權0o020
#                                     # stat.S_IRGRP:  組用戶有讀許可權0o040
#                                     # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
#                                     # stat.S_IXUSR:  擁有者具有執行許可權0o100
#                                     # stat.S_IWUSR:  擁有者具有寫許可權0o200
#                                     # stat.S_IRUSR:  擁有者具有讀許可權0o400
#                                     # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
#                                     # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
#                                     # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
#                                     # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
#                                     # stat.S_IREAD:  windows下設為唯讀
#                                     # stat.S_IWRITE: windows下取消唯讀
#                                 except OSError as error:
#                                     if is_Concurrent == "0" or is_Concurrent == 0:
#                                         sys.stdout.write("\n")
#                                         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                                         sys.stdout.write("\n")
#                                         # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
#                                         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在但無法修改為可讀可寫權限.")
#                                         if is_window:
#                                             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在但無法修改為可讀可寫權限."
#                                     if is_Concurrent == "Multi-Threading":
#                                         if outqueue_from_task_to_host:
#                                             outqueue_from_task_to_host.put(
#                                                 [
#                                                     "Wrong",
#                                                     str(int(i) + 1),
#                                                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                                     str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
#                                                     str(error)
#                                                 ],
#                                                 block=False,
#                                                 timeout=None
#                                             )
#                                     Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
#                                     # break
#                                     continue


#                             # # 如果文檔已存在則從硬盤刪除，然後重新創建並寫入新值;
#                             # try:
#                             #     os.remove(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))  # 刪除文檔
#                             # except OSError as error:
#                             #     if is_Concurrent == "0" or is_Concurrent == 0:
#                             #         sys.stdout.write("\n")
#                             #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                             #         sys.stdout.write("\n")
#                             #         # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
#                             #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在且無法刪除，以重新創建更新數據.")
#                             #         if is_window:
#                             #             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在且無法刪除，以重新創建更新數據."
#                             #     if is_Concurrent == "Multi-Threading":
#                             #         if outqueue_from_task_to_host:
#                             #             outqueue_from_task_to_host.put(
#                             #                 [
#                             #                     "Wrong",
#                             #                     str(int(i) + 1),
#                             #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                             #                     str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
#                             #                     str(error)
#                             #                 ],
#                             #                 block=False,
#                             #                 timeout=None
#                             #             )
#                             #     Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
#                             #     # break
#                             #     continue

#                             # # 判斷用於接收傳值的媒介文檔，是否已經從硬盤刪除;
#                             # if os.path.exists(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')) and os.path.isfile(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')):
#                             #     if is_Concurrent == "0" or is_Concurrent == 0:
#                             #         sys.stdout.write("\n")
#                             #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
#                             #         sys.stdout.write("\n")
#                             #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在且無法刪除，以重新創建更新數據.")
#                             #         if is_window:
#                             #             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在且無法刪除，以重新創建更新數據."
#                             #     if is_Concurrent == "Multi-Threading":
#                             #         if outqueue_from_task_to_host:
#                             #             outqueue_from_task_to_host.put(
#                             #                 [
#                             #                     "Wrong",
#                             #                     str(int(i) + 1),
#                             #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                             #                     str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')
#                             #                 ],
#                             #                 block=False,
#                             #                 timeout=None
#                             #             )
#                             #     Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
#                             #     # break
#                             #     continue


#                         # # 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
#                         # if os.path.exists(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')).is_dir():
#                         #     # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
#                         #     if not (os.access(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), os.W_OK)):
#                         #         try:
#                         #             # 修改文檔權限 mode:777 任何人可讀寫;
#                         #             os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
#                         #             # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
#                         #             # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
#                         #             # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
#                         #             # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
#                         #             # stat.S_IXOTH:  其他用戶有執行權0o001
#                         #             # stat.S_IWOTH:  其他用戶有寫許可權0o002
#                         #             # stat.S_IROTH:  其他用戶有讀許可權0o004
#                         #             # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
#                         #             # stat.S_IXGRP:  組用戶有執行許可權0o010
#                         #             # stat.S_IWGRP:  組用戶有寫許可權0o020
#                         #             # stat.S_IRGRP:  組用戶有讀許可權0o040
#                         #             # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
#                         #             # stat.S_IXUSR:  擁有者具有執行許可權0o100
#                         #             # stat.S_IWUSR:  擁有者具有寫許可權0o200
#                         #             # stat.S_IRUSR:  擁有者具有讀許可權0o400
#                         #             # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
#                         #             # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
#                         #             # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
#                         #             # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
#                         #             # stat.S_IREAD:  windows下設為唯讀
#                         #             # stat.S_IWRITE: windows下取消唯讀
#                         #         except OSError as error:
#                         #             if is_Concurrent == "0" or is_Concurrent == 0:
#                         #                 sys.stdout.write("\n")
#                         #                 sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                         #                 sys.stdout.write("\n")
#                         #                 # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
#                         #                 # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
#                         #                 if is_window:
#                         #                     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
#                         #             if is_Concurrent == "Multi-Threading":
#                         #                 if outqueue_from_task_to_host:
#                         #                     outqueue_from_task_to_host.put(
#                         #                         [
#                         #                             "Wrong",
#                         #                             str(int(i) + 1),
#                         #                             str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                         #                             str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
#                         #                             str(error)
#                         #                         ],
#                         #                         block=False,
#                         #                         timeout=None
#                         #                     )
#                         #             Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
#                         #             # break
#                         #             continue
#                         # else:
#                         #     try:
#                         #         # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
#                         #         # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
#                         #         os.makedirs(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), mode=0o777, exist_ok=True)
#                         #     except FileExistsError as error:
#                         #         # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
#                         #         if is_Concurrent == "0" or is_Concurrent == 0:
#                         #             sys.stdout.write("\n")
#                         #             sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                         #             sys.stdout.write("\n")
#                         #             # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
#                         #             # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
#                         #             if is_window:
#                         #                 Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
#                         #         if is_Concurrent == "Multi-Threading":
#                         #             if outqueue_from_task_to_host:
#                         #                 outqueue_from_task_to_host.put(
#                         #                     [
#                         #                         "Wrong",
#                         #                         str(int(i) + 1),
#                         #                         str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                         #                         str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
#                         #                         str(error)
#                         #                     ],
#                         #                     block=False,
#                         #                     timeout=None
#                         #                 )
#                         #         Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
#                         #         # break
#                         #         continue

#                         # if not (os.path.exists(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')).is_dir()):
#                         #     if is_Concurrent == "0" or is_Concurrent == 0:
#                         #         sys.stdout.write("\n")
#                         #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
#                         #         sys.stdout.write("\n")
#                         #         # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
#                         #         # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
#                         #         if is_window:
#                         #             Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
#                         #     if is_Concurrent == "Multi-Threading":
#                         #         if outqueue_from_task_to_host:
#                         #             outqueue_from_task_to_host.put(
#                         #                 [
#                         #                     "Wrong",
#                         #                     str(int(i) + 1),
#                         #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                         #                     str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')
#                         #                 ],
#                         #                 block=False,
#                         #                 timeout=None
#                         #             )
#                         #     Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
#                         #     # break
#                         #     continue


#                         # 以可寫方式打開硬盤文檔，如果文檔不存在，則會自動創建一個文檔;
#                         fd = open(
#                             str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
#                             mode="wb+",  # 寫入文本字符：mode="w"，寫入二進制字節<class 'bytes'>：mode="wb+"
#                             buffering=-1,
#                             # encoding="utf-8",
#                             errors=None,
#                             newline=None,
#                             closefd=True,
#                             opener=None
#                         )
#                         try:
#                             fd.write(result_Data)
#                             # result_Data_bytes = result_Data.encode("utf-8")
#                             # result_Data_len = len(bytes(result_Data, "utf-8"))
#                             # fd.write(result_Data_bytes)
#                         except FileNotFoundError:
#                             if is_Concurrent == "0" or is_Concurrent == 0:
#                                 sys.stdout.write("\n")
#                                 sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                                 sys.stdout.write("\n")
#                                 # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
#                                 # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "寫入失敗.")
#                                 if is_window:
#                                     Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "寫入失敗."
#                             if is_Concurrent == "Multi-Threading":
#                                 if outqueue_from_task_to_host:
#                                     outqueue_from_task_to_host.put(
#                                         [
#                                             "Wrong",
#                                             str(int(i) + 1),
#                                             str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                                             str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
#                                             str(error)
#                                         ],
#                                         block=False,
#                                         timeout=None
#                                     )
#                             Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
#                             # break
#                             continue
#                         # except PersmissionError:
#                         #     if is_Concurrent == "0" or is_Concurrent == 0:
#                         #         sys.stdout.write("\n")
#                         #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                         #         sys.stdout.write("\n")
#                         #         # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
#                         #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無操作權限.")
#                         #         if is_window:
#                         #             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無操作權限."
#                         #     if is_Concurrent == "Multi-Threading":
#                         #         if outqueue_from_task_to_host:
#                         #             outqueue_from_task_to_host.put(
#                         #                 [
#                         #                     "Wrong",
#                         #                     str(int(i) + 1),
#                         #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                         #                     str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
#                         #                     str(error)
#                         #                 ],
#                         #                 block=False,
#                         #                 timeout=None
#                         #             )
#                         #     Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
#                         #     # break
#                         #     continue
#                         finally:
#                             fd.close()
#                         # 注：可以用try/finally語句來確保最後能關閉檔，不能把open語句放在try塊裡，因為當打開檔出現異常時，檔物件file_object無法執行close()方法;

#             # if is_storage_position == "Database" or is_storage_position == "Database_and_Disk":

#             complete_Number = complete_Number + int(1)  # 記錄處理成功的文檔個數;

#             if is_Concurrent == "0" or is_Concurrent == 0:
#                 # sys.stdout.write("\n")  # 輸出換行;
#                 # sys.stdout.write("Succeed," + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "," + str(result_Data))  # 將字符串輸出寫到操作系統控制臺;
#                 # print("Succeed," + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "," + str(result_Data))  # 將字符串輸出寫到操作系統控制臺;
#                 print("Succeed," + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))

#             if is_Concurrent == "Multi-Threading":
#                 if outqueue_from_task_to_host:
#                     outqueue_from_task_to_host.put(
#                         [
#                             "Succeed",
#                             str(int(i)+1),
#                             str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                             str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
#                             str(str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n"),
#                             str("Succeed" + "\n" + str(int(i)+1) + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#                         ],
#                         block=False,
#                         timeout=None
#                     )

#         else:

#             if is_Concurrent == "0" or is_Concurrent == 0:
#                 # sys.stdout.write("\n")  # 輸出換行;
#                 # sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
#                 # sys.stdout.write("\n")  # 輸出換行;
#                 # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在或不是檔.")
#                 if is_window:
#                     Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在或不是檔."
#             if is_Concurrent == "Multi-Threading":
#                 if outqueue_from_task_to_host:
#                     outqueue_from_task_to_host.put(
#                         [
#                             "Wrong",
#                             str(int(i) + 1),
#                             str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                             str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
#                         ],
#                         block=False,
#                         timeout=None
#                     )
#             Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
#             # break
#             continue


#     # file_Data = ""
#     # result_Data = ""
#     # image_sample = []
#     # 清除自定義畫布組件中已經繪製的指定圖片;
#     # Canvas_display_sample.delete("all")
#     # Canvas_display_sample.delete(tag="one")
#     # Canvas_display_sample.create_image(
#     #     0,
#     #     0,
#     #     anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     #     image=image_sample,
#     #     # fill="red",
#     #     tag="one"
#     # )
#     # Label_display_sample['text'] = "input file"


#     # if is_Concurrent == "0" or is_Concurrent == 0:
#     #     # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
#     #     if is_window:
#     #         Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + input_Test_Path + " ]." + "\n" + "Output: [ " + output_Test_Path + " ]." + "\n" + "complete [ " + str(complete_Number) + " ]."
#     #         # Label_State['text'] = "Stand by"

#     if is_Concurrent == "Multi-Threading":
#         if outqueue_from_task_to_host:
#             if len(Error_Log) > 0:
#                 outqueue_from_task_to_host.put(
#                     [
#                         "Error",
#                         "[" + str(len(Error_Log)) + "]",
#                         str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                         str(','.join(Error_Log))
#                     ],
#                     block=False,
#                     timeout=None
#                 )
#             else:
#                 outqueue_from_task_to_host.put(
#                     [
#                         "Complete",
#                         "[" + str(complete_Number) + "]",
#                         str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
#                         input_Test_Path,
#                         output_Test_Path
#                     ],
#                     block=False,
#                     timeout=None
#                 )

#     # # 使用消息提示框控件給出溫馨提示;
#     # tk_messagebox.showinfo(
#     #     title = "溫馨提示",
#     #     message = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + input_Test_Path + " ]." + "\n" + "Output: [ " + output_Test_Path + " ]." + "\n" + "complete [ " + str(complete_Number) + " ]."
#     # )

#     if len(Error_Log) > 0:
#         return "Error,[" + str(len(Error_Log)) + "]," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(','.join(Error_Log))
#     else:
#         return "Complete,[" + str(complete_Number) + "]," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_Test_Path + "," + output_Test_Path  # None


# def Path_Conversion(input_Path_String, time_sleep):

#     if is_Concurrent == "0" or is_Concurrent == 0:
#         global Error_Log

#     # global Error_Log
#     Error_Log = []

#     file_Array = []

#     # input_Path_String = input_Path_String.replace('/', r'\\')
#     if os.path.exists(input_Path_String):

#         if pathlib.Path(input_Path_String).is_dir():

#             items_1 = os.listdir(input_Path_String)
#             # print(items_1)
#             # for item in items_1:
#             #     print(item)
#             #     tk_messagebox.showinfo(
#             #         title="溫馨提示 input_Path_String",
#             #         message=str(item)
#             #     )

#             for i in range(0, len(items_1)):

#                 if os.path.exists(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/')) and os.path.isfile(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/')):

#                     # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
#                     if not (os.access(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), os.W_OK)):
#                         try:
#                             # 修改文檔權限 mode:777 任何人可讀寫;
#                             os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
#                             # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
#                             # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
#                             # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
#                             # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
#                             # stat.S_IXOTH:  其他用戶有執行權0o001
#                             # stat.S_IWOTH:  其他用戶有寫許可權0o002
#                             # stat.S_IROTH:  其他用戶有讀許可權0o004
#                             # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
#                             # stat.S_IXGRP:  組用戶有執行許可權0o010
#                             # stat.S_IWGRP:  組用戶有寫許可權0o020
#                             # stat.S_IRGRP:  組用戶有讀許可權0o040
#                             # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
#                             # stat.S_IXUSR:  擁有者具有執行許可權0o100
#                             # stat.S_IWUSR:  擁有者具有寫許可權0o200
#                             # stat.S_IRUSR:  擁有者具有讀許可權0o400
#                             # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
#                             # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
#                             # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
#                             # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
#                             # stat.S_IREAD:  windows下設為唯讀
#                             # stat.S_IWRITE: windows下取消唯讀
#                         except OSError as error:
#                             if is_Concurrent == "0" or is_Concurrent == 0:
#                                 sys.stdout.write("\n")  # 輸出換行;
#                                 sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                                 sys.stdout.write("\n")  # 輸出換行;
#                                 # print(error)
#                                 # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/')} : {error}')
#                                 # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
#                                 if is_window:
#                                     Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
#                             Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))
#                             # break
#                             continue

#                     file_Array.append(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))
                
#                 else:
#                     if is_Concurrent == "0" or is_Concurrent == 0:
#                         sys.stdout.write("\n")  # 輸出換行;
#                         sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
#                         sys.stdout.write("\n")  # 輸出換行;
#                         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + " ]" + "\n" + "不存在或者不是檔.")
#                         if is_window:
#                             Label_State['text'] = "運行錯誤." + "\n" + "檔:" + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + " ]" + "\n" + "不存在或者不是檔."
#                     Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))
#                     # break
#                     continue

#                 if is_Concurrent == "0" or is_Concurrent == 0:
#                     if is_window:
#                         Label_State['text'] = "Parsed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/')

#                 # sys.stdout.write("\n")  # 輸出換行;
#                 # sys.stdout.write("Parsed," + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
#                 # print("Parsed," + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))

#         elif os.path.isfile(input_Path_String):

#             # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
#             # print(input_Path_String)

#             # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
#             if not (os.access(input_Path_String, os.R_OK) and os.access(input_Path_String, os.W_OK)):
#                 try:
#                     # 修改文檔權限 mode:777 任何人可讀寫;
#                     os.chmod(input_Path_String, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
#                     # os.chmod(input_Path_String, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
#                     # os.chmod(input_Path_String, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
#                     # os.chmod(input_Path_String, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
#                     # os.chmod(input_Path_String, stat.S_IWOTH)  # 可被其它用戶寫入;
#                     # stat.S_IXOTH:  其他用戶有執行權0o001
#                     # stat.S_IWOTH:  其他用戶有寫許可權0o002
#                     # stat.S_IROTH:  其他用戶有讀許可權0o004
#                     # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
#                     # stat.S_IXGRP:  組用戶有執行許可權0o010
#                     # stat.S_IWGRP:  組用戶有寫許可權0o020
#                     # stat.S_IRGRP:  組用戶有讀許可權0o040
#                     # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
#                     # stat.S_IXUSR:  擁有者具有執行許可權0o100
#                     # stat.S_IWUSR:  擁有者具有寫許可權0o200
#                     # stat.S_IRUSR:  擁有者具有讀許可權0o400
#                     # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
#                     # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
#                     # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
#                     # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
#                     # stat.S_IREAD:  windows下設為唯讀
#                     # stat.S_IWRITE: windows下取消唯讀
#                 except OSError as error:
#                     if is_Concurrent == "0" or is_Concurrent == 0:
#                         sys.stdout.write("\n")  # 輸出換行;
#                         sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String) + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
#                         sys.stdout.write("\n")  # 輸出換行;
#                         # print(f'Error: {input_Path_String} : {error}')
#                         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + input_Path_String + " ]" + "\n" + "無法修改為可讀可寫權限.")
#                         if is_window:
#                             Label_State['text'] = "運行錯誤." + "\n" + "檔:" + "\n" + "[ " + input_Path_String + " ]" + "\n" + "無法修改為可讀可寫權限."
#                     Error_Log.append(input_Path_String)
#                     return [file_Array, Error_Log, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))]  # None

#             file_Array.append(input_Path_String)

#             if is_Concurrent == "0" or is_Concurrent == 0:
#                 if is_window:
#                     Label_State['text'] = "Parsed [ 1 ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(input_Path_String)

#             # sys.stdout.write("\n")  # 輸出換行;
#             # sys.stdout.write("Parsed,1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String))  # 將字符串輸出寫到操作系統控制臺;
#             # print("Parsed,1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String))

#         else:
#             if is_Concurrent == "0" or is_Concurrent == 0:
#                 sys.stdout.write("\n")  # 輸出換行;
#                 sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String))  # 將字符串輸出寫到操作系統控制臺;
#                 sys.stdout.write("\n")  # 輸出換行;
#                 # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + input_Path_String + " ]" + "\n" + "類型無法識別.")
#                 if is_window:
#                     Label_State['text'] = "運行錯誤." + "\n" + "檔:" + "\n" + "[ " + input_Path_String + " ]" + "\n" + "類型無法識別."
#             Error_Log.append(input_Path_String)
#             # return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_Path_String

#     else:
#         if is_Concurrent == "0" or is_Concurrent == 0:
#             sys.stdout.write("\n")  # 輸出換行;
#             sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String))  # 將字符串輸出寫到操作系統控制臺;
#             sys.stdout.write("\n")  # 輸出換行;
#             # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + input_Path_String + " ]" + "\n" + "不存在.")
#             if is_window:
#                 Label_State['text'] = "運行錯誤." + "\n" + "檔:" + "\n" + "[ " + input_Path_String + " ]" + "\n" + "不存在."
#         Error_Log.append(input_Path_String)
#         # return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_Path_String

#     # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
#     if is_Concurrent == "0" or is_Concurrent == 0:
#         if is_window:
#             Label_State['text'] = "Path parse complete [ " + str(len(file_Array)) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + input_Path_String + " ]."
#             # Label_State['text'] = "Stand by"

#     # # 使用消息提示框控件給出溫馨提示;
#     # tk_messagebox.showinfo(
#     #     title = "溫馨提示",
#     #     message = str("Path parse complete [ " + str(len(file_Array)) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + input_Path_String + " ].")
#     # )

#     return [file_Array, Error_Log, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))]  # None


# def Queue_update(outqueue_from_task_to_host):

#     # global inputTrain_File_Array
#     # global inputValidation_File_Array
#     global inputTest_File_Array
#     global outputTest_File_Array
#     global image_sample
#     global is_Runing
#     global is_window

#     # outqueue_from_task_to_host = outqueue[0]
#     # outqueue_from_host_to_task = outqueue[1]

#     try:

#         if outqueue_from_task_to_host.empty():
#             window_root.after(5, Queue_update, outqueue_from_task_to_host)
#             pass

#         if not outqueue_from_task_to_host.empty():

#             msg = outqueue_from_task_to_host.get(
#                 block=False,
#                 timeout=None
#             )

#             if msg[0] == "Complete":

#                 # inputTrain_File_Array = []
#                 # inputValidation_File_Array = []
#                 inputTest_File_Array = []
#                 outputTest_File_Array = []

#                 if is_Runing:
#                     is_Runing = not is_Runing
#                 if is_Runing:
#                     Button_start_and_stop_Test['text'] = "Stop Test"
#                     Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                 else:
#                     Button_start_and_stop_Test['text'] = "Start Test"
#                     Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

#                 return_value = str(','.join(msg))
#                 # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
#                 # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
#                 print(return_value)
#                 # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
#                 if is_window:
#                     Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
#                     # Label_State['text'] = "Stand by"

#                     Label_display_sample['text'] = "Input file"  # "悟空，您好.",
#                     Canvas_display_sample.delete("all")

#                 # 使用消息提示框控件給出溫馨提示;
#                 tk_messagebox.showinfo(
#                     title = "溫馨提示",
#                     message = str('\n'.join(return_value.split(',')))
#                 )

#                 return return_value  # None

#             elif msg[0] == "Error":

#                 # inputTrain_File_Array = []
#                 # inputValidation_File_Array = []
#                 inputTest_File_Array = []
#                 outputTest_File_Array = []

#                 if is_Runing:
#                     is_Runing = not is_Runing
#                 if is_Runing:
#                     Button_start_and_stop_Test['text'] = "Stop Test"
#                     Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                 else:
#                     Button_start_and_stop_Test['text'] = "Start Test"
#                     Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

#                 return_value = str(','.join(msg))
#                 # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
#                 # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
#                 print(return_value)
#                 # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
#                 if is_window:
#                     Label_State['text'] = str('\n'.join(str(','.join(msg)).split(',')))
#                     # Label_State['text'] = "Stand by"

#                     Label_display_sample['text'] = "Input file"  # "悟空，您好.",
#                     Canvas_display_sample.delete("all")

#                 # 使用消息提示框控件給出溫馨提示;
#                 tk_messagebox.showinfo(
#                     title = "溫馨提示",
#                     message = str('\n'.join(return_value.split(',')))
#                 )

#                 return return_value  # None

#             elif msg[0] == "Discontinue":

#                 # inputTrain_File_Array = []
#                 # inputValidation_File_Array = []
#                 inputTest_File_Array = []
#                 outputTest_File_Array = []

#                 if is_Runing:
#                     is_Runing = not is_Runing
#                 if is_Runing:
#                     Button_start_and_stop_Test['text'] = "Stop Test"
#                     Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                 else:
#                     Button_start_and_stop_Test['text'] = "Start Test"
#                     Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
#                     # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
#                     Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

#                 return_value = str(','.join(msg))
#                 # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
#                 # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
#                 print(return_value)
#                 # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
#                 if is_window:
#                     Label_State['text'] = str('\n'.join(str(','.join(msg)).split(',')))
#                     # Label_State['text'] = "Stand by"

#                     Label_display_sample['text'] = "Input file"  # "悟空，您好.",
#                     Canvas_display_sample.delete("all")

#                 # 使用消息提示框控件給出溫馨提示;
#                 tk_messagebox.showinfo(
#                     title = "溫馨提示",
#                     message = str('\n'.join(return_value.split(',')))
#                 )

#                 return return_value  # None

#             elif msg[0] == "Runing":

#                 return_value = str(','.join(msg))
#                 # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
#                 # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
#                 # print(return_value)
#                 # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
#                 if is_window:
#                     Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
#                     # Label_State['text'] = "Stand by"

#                     # Label_display_sample['text'] = "Input file"  # "悟空，您好.",
#                     # Canvas_display_sample.delete("all")

#                 window_root.after(5, Queue_update, outqueue_from_task_to_host)

#             elif msg[0] == "image_sample_delete":

#                 # return_value = str(','.join(msg))
#                 # # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
#                 # # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
#                 # print(return_value)
#                 # # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
#                 if is_window:
#                     # Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
#                     # Label_State['text'] = "Stand by"

#                     Label_display_sample['text'] = "Input file"  # "悟空，您好.",
#                     Canvas_display_sample.delete("all")
#                     image_sample = []

#                 window_root.after(5, Queue_update, outqueue_from_task_to_host)

#             elif msg[0] == "image_sample":

#                 # return_value = str(','.join(msg))
#                 # # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
#                 # # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
#                 # print(return_value)
#                 # # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
#                 if is_window:
#                     # Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
#                     # Label_State['text'] = "Stand by"

#                     Label_display_sample['text'] = str(msg[1])  # "悟空，您好.",
#                     image_sample = msg[2]
#                     Canvas_display_sample.delete("all")
#                     # Canvas_display_sample.delete(tag="one")
#                     Canvas_display_sample.create_image(
#                         0,
#                         0,
#                         anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#                         image=image_sample,
#                         # fill="red",
#                         tag="one"
#                     )

#                 window_root.after(5, Queue_update, outqueue_from_task_to_host)

#             elif msg[0] == "Succeed":

#                 return_value = str(','.join(str(msg[5]).split('\n')))
#                 print(return_value)

#                 # 將運算結果寫入用於展示結果的多行文本輸入框;
#                 if is_window:

#                     # Label_State['text'] = "Succeed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(input_Test_File_Array[i])
#                     # Label_State['text'] = "Succeed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
#                     Label_State['text'] = msg[5]

#                     # # 讀取多行文本輸入框中的内容;
#                     # Text_display_result_value = Text_display_result.get(
#                     #     "0.0",  # 表示讀取多行文本輸入框 .Text 控件中的全部值，如果設定參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始讀取;
#                     #     "end"  # 表示讀取至多行文本輸入框 .Text 控件中全部值的最後一個字符爲止;
#                     # )
#                     # Text_display_result_value = str(Text_display_result_value)
#                     # print(Text_display_result_value)

#                     # # 刪除多行文本輸入框中的内容;
#                     # Text_display_result.delete(
#                     #     "1.0",  # 參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始刪除;
#                     #     "end"  # 參數爲 "end" 表示刪除直至最後一個字符，即清空輸入框;
#                     # )

#                     # new_Text_display_result_value = Text_display_result_value + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Test_File_Array[i]) + "," + str(result_Data)

#                     # new_Text_display_result_value = str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Test_File_Array[i]) + "," + str(result_Data) + "\n"
#                     # new_Text_display_result_value = str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n"
#                     # print(new_Text_display_result_value)

#                     # 將字符串寫入多行文本輸入框;
#                     Text_display_result.insert(
#                         "end",  # 參數 "1.0" 表示從第一行第一列開始插入，參數 "insert" 表示在當前光標位置處插入一個字符串，參數 "end" 表示在末尾位置處追加寫入一個字符串;
#                         str(msg[4])  # str(new_Text_display_result_value)
#                     )

#                     Text_display_result.see("end"),  # 表示將 .Text 組件中聚焦在文本末行，即顯示末尾;

#                 # return_value = str(','.join(msg))
#                 # # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
#                 # # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
#                 # print(return_value)
#                 # # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
#                 # Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
#                 # # Label_State['text'] = "Stand by"

#                 # Label_display_sample['text'] = "Input file"  # "悟空，您好.",
#                 # Canvas_display_sample.delete("all")

#                 window_root.after(5, Queue_update, outqueue_from_task_to_host)

#             elif msg[0] == "Wrong":

#                 return_value = str(','.join(msg))
#                 # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
#                 # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
#                 print(return_value)
#                 # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
#                 if is_window:
#                     Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
#                     # Label_State['text'] = "Stand by"

#                     # Label_display_sample['text'] = "Input file"  # "悟空，您好.",
#                     # Canvas_display_sample.delete("all")

#                 window_root.after(5, Queue_update, outqueue_from_task_to_host)

#         # else:
#         #     # By not calling window_root.after here, we allow update to
#         #     # truly end
#         #     window_root.after(50, Queue_update, (outqueue_from_task_to_host, outqueue_from_host_to_task))
#         #     pass
#     except queue.Empty:
#         window_root.after(5, Queue_update, outqueue_from_task_to_host)


default_input_tabel_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
default_input_measuringRuler_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;

file_Data = ""
# file_Data_bytes = file_Data.encode("utf-8")
# file_Data = file_Data_bytes.decode("utf-8")
# file_Data = str(file_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
# file_Data_len = len(bytes(file_Data, "utf-8"))

result_Data = ""
# result_Data_bytes = result_Data.encode("utf-8")
# result_Data = result_Data_bytes.decode("utf-8")
# result_Data = str(result_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
# result_Data_len = len(bytes(result_Data, "utf-8"))

complete_Number = int(0)  # 記錄處理的文件個數

image_sample = []

is_Runing = False  # bool("True"), bool("False") 判斷程式是否正在運行中;

Error_Log = []  # 記錄出錯的樣本;

is_storage_position = "Disk"  # "Database", "Database_and_Disk", "Disk" 判斷存儲位置;

is_storage_type = "csv"  # "json", "csv", "txt", "xlsx", 判斷存儲類型;


iconbitmap_path = ""
# 判斷是否爲打包（.exe）後的環境;
if getattr(sys, 'frozen', False):
    iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "Icon", "iconbitmap.png"))).replace('\\', '/')
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "Icon", "iconbitmap.png"))).replace('\\', '/')
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "Icon", "iconbitmap.png"))).replace('\\', '/')
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "Icon", "iconbitmap.png"))).replace('\\', '/')
else:
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "Icon", "iconbitmap.png"))).replace('\\', '/')
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "Icon", "iconbitmap.png"))).replace('\\', '/')
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "Icon", "iconbitmap.png"))).replace('\\', '/')
    iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "Icon", "iconbitmap.png"))).replace('\\', '/')
# print(iconbitmap_path)  # "C:/Criss/OCR/src/Icon/iconbitmap.png"


default_inputTrain_path = ""
default_inputValidation_path = ""
default_inputTest_path = ""
default_outputTest_path = ""
# 判斷是否爲打包（.exe）後的環境;
if getattr(sys, 'frozen', False):
    default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTrain"))).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTrain"))).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTrain"))).replace('\\', '/')
    default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputValidation"))).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputValidation"))).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputValidation"))).replace('\\', '/')
    default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTest"))).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTest"))).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTest"))).replace('\\', '/')
    default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
else:
    default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTrain"))).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTrain"))).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTrain"))).replace('\\', '/')
    default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputValidation"))).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputValidation"))).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputValidation"))).replace('\\', '/')
    default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTest"))).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTest"))).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTest"))).replace('\\', '/')
    default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')


input_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
output_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')


# 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
if os.path.exists(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')).is_dir():
    # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
    if not (os.access(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/'), os.W_OK)):
        try:
            # 修改文檔權限 mode:777 任何人可讀寫;
            os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
            # stat.S_IXOTH:  其他用戶有執行權0o001
            # stat.S_IWOTH:  其他用戶有寫許可權0o002
            # stat.S_IROTH:  其他用戶有讀許可權0o004
            # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
            # stat.S_IXGRP:  組用戶有執行許可權0o010
            # stat.S_IWGRP:  組用戶有寫許可權0o020
            # stat.S_IRGRP:  組用戶有讀許可權0o040
            # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
            # stat.S_IXUSR:  擁有者具有執行許可權0o100
            # stat.S_IWUSR:  擁有者具有寫許可權0o200
            # stat.S_IRUSR:  擁有者具有讀許可權0o400

            # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
            # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
            # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
            # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
            # stat.S_IREAD:  windows下設為唯讀
            # stat.S_IWRITE: windows下取消唯讀
        except OSError as error:
            sys.stdout.write("\n")  # 輸出換行;
            sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
            sys.stdout.write("\n")  # 輸出換行;
            # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')} : {error}')
            # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
            # if is_window:
            #     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
            Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/'))
            sys.exit(1)  # 中止當前進程，退出當前程序;
else:
    try:
        # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
        # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
        os.makedirs(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/'), mode=0o777, exist_ok=True)
    except FileExistsError as error:
        # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
        sys.stdout.write("\n")  # 輸出換行;
        sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
        sys.stdout.write("\n")  # 輸出換行;
        # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')} : {error}')
        # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
        # if is_window:
        #     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
        Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/'))
        sys.exit(1)  # 中止當前進程，退出當前程序;

if not (os.path.exists(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')).is_dir()):
    sys.stdout.write("\n")  # 輸出換行;
    sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
    sys.stdout.write("\n")  # 輸出換行;
    # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')} : {error}')
    # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
    # if is_window:
    #     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
    Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/'))
    sys.exit(1)  # 中止當前進程，退出當前程序;


# 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
if os.path.exists(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')).is_dir():
    # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
    if not (os.access(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/'), os.W_OK)):
        try:
            # 修改文檔權限 mode:777 任何人可讀寫;
            os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
            # stat.S_IXOTH:  其他用戶有執行權0o001
            # stat.S_IWOTH:  其他用戶有寫許可權0o002
            # stat.S_IROTH:  其他用戶有讀許可權0o004
            # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
            # stat.S_IXGRP:  組用戶有執行許可權0o010
            # stat.S_IWGRP:  組用戶有寫許可權0o020
            # stat.S_IRGRP:  組用戶有讀許可權0o040
            # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
            # stat.S_IXUSR:  擁有者具有執行許可權0o100
            # stat.S_IWUSR:  擁有者具有寫許可權0o200
            # stat.S_IRUSR:  擁有者具有讀許可權0o400

            # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
            # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
            # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
            # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
            # stat.S_IREAD:  windows下設為唯讀
            # stat.S_IWRITE: windows下取消唯讀
        except OSError as error:
            sys.stdout.write("\n")  # 輸出換行;
            sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
            sys.stdout.write("\n")  # 輸出換行;
            # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')} : {error}')
            # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
            # if is_window:
            #     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
            Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/'))
            sys.exit(1)  # 中止當前進程，退出當前程序;
else:
    try:
        # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
        # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
        os.makedirs(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/'), mode=0o777, exist_ok=True)
    except FileExistsError as error:
        # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
        sys.stdout.write("\n")  # 輸出換行;
        sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
        sys.stdout.write("\n")  # 輸出換行;
        # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')} : {error}')
        # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
        # if is_window:
        #     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
        Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/'))
        sys.exit(1)  # 中止當前進程，退出當前程序;

if not (os.path.exists(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')).is_dir()):
    sys.stdout.write("\n")  # 輸出換行;
    sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
    sys.stdout.write("\n")  # 輸出換行;
    # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')} : {error}')
    # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
    # if is_window:
    #     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
    Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/'))
    sys.exit(1)  # 中止當前進程，退出當前程序;


# 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
if os.path.exists(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')).is_dir():
    # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
    if not (os.access(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/'), os.W_OK)):
        try:
            # 修改文檔權限 mode:777 任何人可讀寫;
            os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
            # stat.S_IXOTH:  其他用戶有執行權0o001
            # stat.S_IWOTH:  其他用戶有寫許可權0o002
            # stat.S_IROTH:  其他用戶有讀許可權0o004
            # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
            # stat.S_IXGRP:  組用戶有執行許可權0o010
            # stat.S_IWGRP:  組用戶有寫許可權0o020
            # stat.S_IRGRP:  組用戶有讀許可權0o040
            # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
            # stat.S_IXUSR:  擁有者具有執行許可權0o100
            # stat.S_IWUSR:  擁有者具有寫許可權0o200
            # stat.S_IRUSR:  擁有者具有讀許可權0o400

            # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
            # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
            # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
            # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
            # stat.S_IREAD:  windows下設為唯讀
            # stat.S_IWRITE: windows下取消唯讀
        except OSError as error:
            sys.stdout.write("\n")  # 輸出換行;
            sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
            sys.stdout.write("\n")  # 輸出換行;
            # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')} : {error}')
            # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
            # if is_window:
            #     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
            Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/'))
            sys.exit(1)  # 中止當前進程，退出當前程序;
else:
    try:
        # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
        # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
        os.makedirs(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/'), mode=0o777, exist_ok=True)
    except FileExistsError as error:
        # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
        sys.stdout.write("\n")  # 輸出換行;
        sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
        sys.stdout.write("\n")  # 輸出換行;
        # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')} : {error}')
        # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
        # if is_window:
        #     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
        Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/'))
        sys.exit(1)  # 中止當前進程，退出當前程序;

if not (os.path.exists(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')).is_dir()):
    sys.stdout.write("\n")  # 輸出換行;
    sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
    sys.stdout.write("\n")  # 輸出換行;
    # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')} : {error}')
    # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
    # if is_window:
    #     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
    Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/'))
    sys.exit(1)  # 中止當前進程，退出當前程序;


# 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
if os.path.exists(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')).is_dir():
    # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
    if not (os.access(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/'), os.W_OK)):
        try:
            # 修改文檔權限 mode:777 任何人可讀寫;
            os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
            # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
            # stat.S_IXOTH:  其他用戶有執行權0o001
            # stat.S_IWOTH:  其他用戶有寫許可權0o002
            # stat.S_IROTH:  其他用戶有讀許可權0o004
            # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
            # stat.S_IXGRP:  組用戶有執行許可權0o010
            # stat.S_IWGRP:  組用戶有寫許可權0o020
            # stat.S_IRGRP:  組用戶有讀許可權0o040
            # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
            # stat.S_IXUSR:  擁有者具有執行許可權0o100
            # stat.S_IWUSR:  擁有者具有寫許可權0o200
            # stat.S_IRUSR:  擁有者具有讀許可權0o400

            # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
            # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
            # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
            # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
            # stat.S_IREAD:  windows下設為唯讀
            # stat.S_IWRITE: windows下取消唯讀
        except OSError as error:
            sys.stdout.write("\n")  # 輸出換行;
            sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
            sys.stdout.write("\n")  # 輸出換行;
            # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')} : {error}')
            # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
            # if is_window:
            #     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
            Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/'))
            sys.exit(1)  # 中止當前進程，退出當前程序;
else:
    try:
        # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
        # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
        os.makedirs(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/'), mode=0o777, exist_ok=True)
    except FileExistsError as error:
        # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
        sys.stdout.write("\n")  # 輸出換行;
        sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
        sys.stdout.write("\n")  # 輸出換行;
        # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')} : {error}')
        # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
        # if is_window:
        #     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
        Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/'))
        sys.exit(1)  # 中止當前進程，退出當前程序;

if not (os.path.exists(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')).is_dir()):
    sys.stdout.write("\n")  # 輸出換行;
    sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
    sys.stdout.write("\n")  # 輸出換行;
    # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')} : {error}')
    # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
    # if is_window:
    #     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
    Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/'))
    sys.exit(1)  # 中止當前進程，退出當前程序;


default_outputTest_URL = "mongodb://username:password@127.0.0.1:27017/testDB"

inputTrain_File_Array = []
inputValidation_File_Array = []
inputTest_File_Array = []
outputTest_File_Array = []

outqueue_from_task_to_host = queue.Queue(maxsize=0)
outqueue_from_host_to_task = queue.Queue(maxsize=0)

# 使用 while True: 的方法設置死循環創建看守進程，監聽指定的硬盤目錄或文檔，響應創建事件，從而達到不同語言之間利用硬盤文檔傳輸數據交互的效果;
# 控制臺傳參，通過 sys.argv 數組獲取從控制臺傳入的參數
is_window = True  # bool(True), bool(False) 判斷只需要執行一次還是啓動監聽服務器功能;
is_Concurrent = "Multi-Threading"  # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程），可取值：0、"0"、"Multi-Threading"、"Multi-Processes";
# is_storage_position = "Disk"  # 判斷存儲位置，可取值："Database", "Database_and_Disk", "Disk" ;
# is_storage_type = "csv"  # 判斷存儲類型，可取值："json", "csv", "txt", "xlsx";
# input_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')

input_tabel_tesseract_config = default_input_tabel_tesseract_config
input_measuringRuler_tesseract_config = default_input_measuringRuler_tesseract_config

inputTrain_path = default_inputTrain_path  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
inputValidation_path = default_inputValidation_path  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
inputTest_path = default_inputTest_path  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
Input_and_Output_Function = Input_and_Output_Function  # 操作硬盤文檔的函數讀取或寫入;
do_Function = do_data  # 用於接收執行功能的函數 "do_data";
# output_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')
outputTest_path = default_outputTest_path  # 用於輸出傳值的媒介文檔 "../temp/intermediary_write_Python.txt";
outputTest_URL = default_outputTest_URL
# temp_cache_IO_data_dir = ""  # 用於暫存輸入輸出傳值文檔的媒介目錄 temp_cache_IO_data_dir = "../temp/";
# number_Worker_process = int(0)  # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
time_sleep = float(0.01)  # float(0.05) 用於監聽程序的輪詢延遲參數，單位（秒）;
screenwidth = int(0)  # int(tk.Tk().winfo_screenwidth())  # 獲取顯示器屏幕寬度;
screenheight = int(0)  # int(tk.Tk().winfo_screenheight())  # 獲取顯示器屏幕高度;
# # 控制臺傳參，通過 sys.argv 數組獲取從控制臺傳入的參數
# # print(type(sys.argv))
# # print(sys.argv)
# if len(sys.argv) > 1:
#     for i in range(len(sys.argv)):
#         # print('arg '+ str(i), sys.argv[i])  # 通過 sys.argv 數組獲取從控制臺傳入的參數
#         if i > 0:
#             # 使用函數 isinstance(sys.argv[i], str) 判斷傳入的參數是否為 str 字符串類型 type(sys.argv[i]);
#             if isinstance(sys.argv[i], str) and sys.argv[i] != "" and sys.argv[i].find("=", 0, int(len(sys.argv[i])-1)) != -1:
#                 # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
#                 if sys.argv[i].split("=", -1)[0] == "is_window":
#                     # is_window = bool(sys.argv[i].split("=", -1)[1])  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
#                     if sys.argv[i].split("=", -1)[1] == "True":
#                         is_window = True  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
#                     elif sys.argv[i].split("=", -1)[1] == "False":
#                         is_window = False  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
#                     elif int(sys.argv[i].split("=", -1)[1]) >= int(1):
#                         is_window = True  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
#                     elif int(sys.argv[i].split("=", -1)[1]) == int(0):
#                         is_window = False  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
#                     # else:
#                     # print("Is window:", is_window)
#                 # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程）可取值：is_Concurrent = 0 or "0" or "Multi-Threading" or "Multi-Processes";
#                 elif sys.argv[i].split("=", -1)[0] == "is_Concurrent":
#                     is_Concurrent = str(sys.argv[i].split("=", -1)[1])  # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程），可取值：is_Concurrent = 0 or "0" or "Multi-Threading" or "Multi-Processes";
#                     # print("Is Monitor Concurrent:", is_Concurrent)
#                 # 用於判斷存儲位置：is_storage_position = "Database", "Database_and_Disk", "Disk" ;
#                 elif sys.argv[i].split("=", -1)[0] == "is_storage_position":
#                     is_storage_position = sys.argv[i].split("=", -1)[1]  # 用於判斷存儲位置：is_storage_position = "Database", "Database_and_Disk", "Disk" ;
#                     # print("storage position:", is_storage_position)
#                 # 用於判斷存儲類型：is_storage_type = "json", "csv", "txt", "xlsx" ;
#                 elif sys.argv[i].split("=", -1)[0] == "is_storage_type":

#                     is_storage_type = sys.argv[i].split("=", -1)[1]  # 用於判斷存儲類型：is_storage_type = "json", "csv", "txt", "xlsx" ;
#                     # print("storage type:", is_storage_type)

#                     if not (is_storage_type == "json" or is_storage_type == "csv" or is_storage_type == "txt" or is_storage_type == "xlsx"):
#                         # sys.stdout.write("\n")  # 輸出換行;
#                         # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(is_storage_type))  # 將字符串輸出寫到操作系統控制臺;
#                         # sys.stdout.write("\n")  # 輸出換行;
#                         print("參數錯誤." + "\n" + "傳入的運算結果的輸出檔類型:" + "\n" + "[ " + is_storage_type + " ]" + "\n" + "不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
#                         # Error_Log.append(is_storage_type)
#                         sys.exit(1)  # 中止當前進程，退出當前程序;

#                     if len(is_storage_type) > 0:

#                         if len(default_outputTest_path) > 0:
#                             if default_outputTest_path.find(".", 0, int(len(default_outputTest_path)-1)) != -1:
#                                 # del default_outputTest_path.split('.')[len(default_outputTest_path.split('.'))-1]
#                                 default_outputTest_path = str(''.join(default_outputTest_path.split('.')[0:len(default_outputTest_path.split('.'))-1])) + "." + is_storage_type
#                             else:
#                                 default_outputTest_path = default_outputTest_path + "." + is_storage_type
#                         # print("default output test path:", default_outputTest_path)

#                         if len(outputTest_path) > 0:
#                             if outputTest_path.find(".", 0, int(len(outputTest_path)-1)) != -1:
#                                 # del outputTest_path.split('.')[len(outputTest_path.split('.'))-1]
#                                 outputTest_path = str(''.join(outputTest_path.split('.')[0:len(outputTest_path.split('.'))-1])) + "." + is_storage_type
#                             else:
#                                 outputTest_path = outputTest_path + "." + is_storage_type
#                         # print("output test path:", outputTest_path)

#                         # if is_storage_type == "json":
#                         #     Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
#                         #     Radiobutton_storage_type_txt.deselect()
#                         #     Radiobutton_storage_type_Excel.deselect()
#                         #     Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
#                         # elif is_storage_type == "csv":
#                         #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
#                         #     Radiobutton_storage_type_txt.deselect()
#                         #     Radiobutton_storage_type_Excel.deselect()
#                         #     Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
#                         # elif is_storage_type == "txt":
#                         #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
#                         #     Radiobutton_storage_type_csv.deselect()
#                         #     Radiobutton_storage_type_Excel.deselect()
#                         #     Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
#                         # elif is_storage_type == "xlsx":
#                         #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
#                         #     Radiobutton_storage_type_csv.deselect()
#                         #     Radiobutton_storage_type_txt.deselect()
#                         #     Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
#                         # elif len(is_storage_type) == 0:
#                         #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
#                         #     Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
#                         #     Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
#                         #     Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
#                         # else:
#                         #     # sys.stdout.write("\n")  # 輸出換行;
#                         #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(is_storage_type))  # 將字符串輸出寫到操作系統控制臺;
#                         #     # sys.stdout.write("\n")  # 輸出換行;
#                         #     print("參數錯誤." + "\n" + "傳入的運算結果的輸出檔類型:" + "\n" + "[ " + is_storage_type + " ]" + "\n" + "不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
#                         #     # Error_Log.append(is_storage_type)
#                         #     sys.exit(1)  # 中止當前進程，退出當前程序;
#                     else:
#                         # sys.stdout.write("\n")  # 輸出換行;
#                         # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(is_storage_type))  # 將字符串輸出寫到操作系統控制臺;
#                         # sys.stdout.write("\n")  # 輸出換行;
#                         print("參數錯誤." + "\n" + "傳入的運算結果的輸出檔類型:" + "\n" + "[ " + is_storage_type + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
#                         # Error_Log.append(is_storage_type)
#                         sys.exit(1)  # 中止當前進程，退出當前程序;

#                 # 用於輸入傳值的媒介目錄 input_dir = "../temp/";
#                 elif sys.argv[i].split("=", -1)[0] == "input_dir":
#                     input_dir = sys.argv[i].split("=", -1)[1]  # 用於輸入傳值的媒介目錄 "../temp/";
#                     # print("input dir:", input_dir)
#                 # 用於配置 Google Tesseract 的參數（tesseract_config）：input_tabel_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";
#                 # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
#                 elif sys.argv[i].split("=", -1)[0] == "input_tabel_tesseract_config":
#                     input_tabel_tesseract_config = sys.argv[i].split("=", -1)[1]  # 用於配置 Google Tesseract 的參數（tesseract_config）：input_tabel_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";;
#                     # print("input tabel tesseract config:", input_tabel_tesseract_config)
#                     default_input_tabel_tesseract_config = sys.argv[i].split("=", -1)[1]
#                     # print("default input tabel tesseract config:", default_input_tabel_tesseract_config)

#                 # 用於配置 Google Tesseract 的參數（tesseract_config）：input_measuringRuler_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";
#                 # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
#                 elif sys.argv[i].split("=", -1)[0] == "input_measuringRuler_tesseract_config":
#                     input_measuringRuler_tesseract_config = sys.argv[i].split("=", -1)[1]  # 用於配置 Google Tesseract 的參數（tesseract_config）：input_measuringRuler_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";;
#                     # print("input measuring ruler tesseract config:", input_measuringRuler_tesseract_config)
#                     default_input_measuringRuler_tesseract_config = sys.argv[i].split("=", -1)[1]
#                     # print("default input measuring ruler tesseract config:", default_input_measuringRuler_tesseract_config)
#                 # 用於接收傳值的媒介文檔 inputTrain_path = "../temp/intermediary_write_Node.txt";
#                 elif sys.argv[i].split("=", -1)[0] == "inputTrain_path":
#                     inputTrain_path = sys.argv[i].split("=", -1)[1]  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
#                     # print("input train path:", inputTrain_path)
#                     default_inputTrain_path = sys.argv[i].split("=", -1)[1]
#                     # print("default input train path:", default_inputTrain_path)
#                 # 用於接收傳值的媒介文檔 inputValidation_path = "../temp/intermediary_write_Node.txt";
#                 elif sys.argv[i].split("=", -1)[0] == "inputValidation_path":
#                     inputValidation_path = sys.argv[i].split("=", -1)[1]  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
#                     # print("input validation path:", inputValidation_path)
#                     default_inputValidation_path = sys.argv[i].split("=", -1)[1]
#                     # print("default input validation path:", default_inputValidation_path)
#                 # 用於接收傳值的媒介文檔 inputTest_path = "../temp/intermediary_write_Node.txt";
#                 elif sys.argv[i].split("=", -1)[0] == "inputTest_path":
#                     inputTest_path = sys.argv[i].split("=", -1)[1]  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
#                     # print("input test path:", inputTest_path)
#                     default_inputTest_path = sys.argv[i].split("=", -1)[1]
#                     # print("default input test path:", default_inputTest_path)
#                 # 用於暫存輸入輸出傳值文檔的媒介目錄 temp_cache_IO_data_dir = "../temp/";
#                 # elif sys.argv[i].split("=", -1)[0] == "temp_cache_IO_data_dir":
#                 #     temp_cache_IO_data_dir = sys.argv[i].split("=", -1)[1]  # 用於輸入傳值的媒介目錄 "../temp/";
#                 #     # print("temp cache IO data file dir:", temp_cache_IO_data_dir)
#                 # 用於操作硬盤文檔讀取或寫入的函數 Input_and_Output_Function = "Input_and_Output";
#                 elif sys.argv[i].split("=", -1)[0] == "Input_and_Output_Function":
#                     Input_and_Output_Function = sys.argv[i].split("=", -1)[1]  # 用於操作硬盤文檔讀取或寫入的函數 "Input_and_Output";
#                     # print("Input and Output Function:", Input_and_Output_Function)
#                 # 用於接收執行功能的函數 do_Function = "do_data";
#                 elif sys.argv[i].split("=", -1)[0] == "do_Function":
#                     do_Function = sys.argv[i].split("=", -1)[1]  # 用於接收執行功能的函數 "do_data";
#                     # print("do Function:", do_Function)
#                 # 用於輸出傳值的媒介目錄 input_dir = "../temp/";
#                 elif sys.argv[i].split("=", -1)[0] == "output_dir":
#                     output_dir = sys.argv[i].split("=", -1)[1]  # 用於輸出傳值的媒介目錄 "../temp/";
#                     # print("output dir:", output_dir)
#                 # 用於輸出傳值的媒介文檔 outputTest_path = "../temp/intermediary_write_Python.txt";
#                 elif sys.argv[i].split("=", -1)[0] == "outputTest_path":

#                     outputTest_path = sys.argv[i].split("=", -1)[1]  # 用於輸出傳值的媒介文檔 "../temp/intermediary_write_Python.txt";
#                     # print("output test path:", outputTest_path)
#                     default_outputTest_path = sys.argv[i].split("=", -1)[1]
#                     # print("default output test path:", default_outputTest_path)

#                     if len(outputTest_path) > 0:
#                         if outputTest_path.find(".", 0, int(len(outputTest_path)-1)) != -1:

#                             is_storage_type = str(outputTest_path.split('.')[len(outputTest_path.split('.'))-1])
#                             # print("storage type:", is_storage_type)

#                             if not (is_storage_type == "json" or is_storage_type == "csv" or is_storage_type == "txt" or is_storage_type == "xlsx"):
#                                 # sys.stdout.write("\n")  # 輸出換行;
#                                 # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
#                                 # sys.stdout.write("\n")  # 輸出換行;
#                                 print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
#                                 # Error_Log.append(outputTest_path)
#                                 sys.exit(1)  # 中止當前進程，退出當前程序;

#                             # if is_storage_type == "json":
#                             #     Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
#                             #     Radiobutton_storage_type_txt.deselect()
#                             #     Radiobutton_storage_type_Excel.deselect()
#                             #     Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
#                             # elif is_storage_type == "csv":
#                             #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
#                             #     Radiobutton_storage_type_txt.deselect()
#                             #     Radiobutton_storage_type_Excel.deselect()
#                             #     Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
#                             # elif is_storage_type == "txt":
#                             #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
#                             #     Radiobutton_storage_type_csv.deselect()
#                             #     Radiobutton_storage_type_Excel.deselect()
#                             #     Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
#                             # elif is_storage_type == "xlsx":
#                             #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
#                             #     Radiobutton_storage_type_csv.deselect()
#                             #     Radiobutton_storage_type_txt.deselect()
#                             #     Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
#                             # elif len(is_storage_type) == 0:
#                             #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
#                             #     Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
#                             #     Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
#                             #     Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
#                             # else:
#                             #     # sys.stdout.write("\n")  # 輸出換行;
#                             #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
#                             #     # sys.stdout.write("\n")  # 輸出換行;
#                             #     print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
#                             #     # Error_Log.append(outputTest_path)
#                             #     sys.exit(1)  # 中止當前進程，退出當前程序;
#                         else:
#                             # sys.stdout.write("\n")  # 輸出換行;
#                             # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
#                             # sys.stdout.write("\n")  # 輸出換行;
#                             print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + outputTest_path + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
#                             # Error_Log.append(outputTest_path)
#                             sys.exit(1)  # 中止當前進程，退出當前程序;

#                 # 用於用於保存運算結果的數據庫服務器網址 outputTest_URL = "mongodb://username:password@127.0.0.1:27017/test-movie?authSource=admin&retryWrites=true&w=majority";
#                 elif sys.argv[i].split("=", -1)[0] == "outputTest_URL":
#                     outputTest_URL = sys.argv[i].split("=", -1)[1]  # 用於用於保存運算結果的數據庫服務器網址 outputTest_URL = "mongodb://username:password@127.0.0.1:27017/test-movie?authSource=admin&retryWrites=true&w=majority";
#                     # print("output test url:", outputTest_URL)
#                     default_outputTest_URL = sys.argv[i].split("=", -1)[1]
#                     # print("default output test url:", default_outputTest_URL)
#                 # # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
#                 # elif sys.argv[i].split("=", -1)[0] == "number_Worker_process":
#                 #     number_Worker_process = int(sys.argv[i].split("=", -1)[1])  # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
#                 #     # print("number Worker processes:", number_Worker_process)
#                 # 用於監聽程序的輪詢延遲參數，單位（秒） time_sleep = float(0.02);
#                 elif sys.argv[i].split("=", -1)[0] == "time_sleep":
#                     time_sleep = float(sys.argv[i].split("=", -1)[1])  # 用於監聽程序的輪詢延遲參數，單位（秒） time_sleep = float(0.02);
#                     # print("Operation document time sleep:", time_sleep)
#                 # elif sys.argv[i].split("=", -1)[0] == "screenwidth":
#                 #     screenwidth = int(sys.argv[i].split("=", -1)[1])  # 顯示屏寬度，單位：像素;
#                 #     # print("Screen width:", screenwidth)
#                 # elif sys.argv[i].split("=", -1)[0] == "screenheight":
#                 #     screenheight = int(sys.argv[i].split("=", -1)[1])  # 顯示屏高度，單位：像素;
#                 #     # print("Screen height:", screenheight)
#                 else:
#                     print(sys.argv[i], "unrecognized.")
#                     # sys.exit(1)  # 中止當前進程，退出當前程序;

optical_character_recognition.tabel_tesseract_config = input_tabel_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
optical_character_recognition.measuringRuler_tesseract_config = input_measuringRuler_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;

# Python 自定義類時，類名第一個字母需要大寫，并且不能有參數;
# class Window_Graphical_User_Interface:
class Window_Optical_Character_Recognition:
    # 可變參數
    # def Function(*args, **kwargs)  Function(a, b, c, a=1, b=2, c=3)
    # a --int
    # *args --tuple  args == (a, b, c)
    # **kwargs -- dict  kwargs == {'a': 1, 'b': 2, 'c': 3}

    # 在 Python 類 class 中的 def __init__(self) 函數，可以用於配置需要從類外部傳入的參數，預設會將實例化類時傳入的參數複製到這個函數中，並，在類啓動時先運行一下這個函數;
    def __init__(self, **kwargs):

        # 檢查函數需要用到的 Python 原生模組是否已經載入(import)，如果還沒載入，則執行載入操作;
        imported_package_list = dir(list)
        if not("os" in imported_package_list):
            import os  # 加載Python原生的操作系統接口模組os、使用或維護的變量的接口模組sys;
        if not("sys" in imported_package_list):
            import sys  # 加載Python原生的操作系統接口模組os、使用或維護的變量的接口模組sys;
        if not("signal" in imported_package_list):
            import signal  # 加載Python原生的操作系統接口模組os、使用或維護的變量的接口模組sys;
        if not("stat" in imported_package_list):
            import stat  # 加載Python原生的操作系統接口模組os、使用或維護的變量的接口模組sys;
        # if not("platform" in imported_package_list):
        #     import platform  # 加載Python原生的與平臺屬性有關的模組;
        # if not("subprocess" in imported_package_list):
        #     import subprocess  # 加載Python原生的創建子進程模組;
        # if not("string" in imported_package_list):
        #     import string  # 加載Python原生的字符串處理模組;
        if not("datetime" in imported_package_list):
            import datetime  # 加載Python原生的日期數據處理模組;
        if not("time" in imported_package_list):
            import time  # 加載Python原生的日期數據處理模組;
        if not("json" in imported_package_list):
            import json  # import the module of json. 加載Python原生的Json處理模組;
        # if not("re" in imported_package_list):
        #     import re  # 加載Python原生的正則表達式對象
        # if not("tempfile" in imported_package_list):
        #     import tempfile  # from tempfile import TemporaryFile, TemporaryDirectory, NamedTemporaryFile  # 用於創建臨時目錄和臨時文檔;
        if not("pathlib" in imported_package_list):
            import pathlib  # from pathlib import Path 用於檢查判斷指定的路徑對象是目錄還是文檔;
        # if not("shutil" in imported_package_list):
        #     import shutil  # 用於刪除完整硬盤目錄樹，清空文件夾;
        # if not("multiprocessing" in imported_package_list):
        #     import multiprocessing  # 加載Python原生的支持多進程模組 from multiprocessing import Process, Pool;
        if not("threading" in imported_package_list):
            import threading  # 加載Python原生的支持多綫程（執行緒）模組;
        if not("queue" in imported_package_list):
            import queue  # 加載Python原生的用於多綫程（執行緒）數據通信的模組 from queue import Queue;
        if not("inspect" in imported_package_list):
            import inspect  # from inspect import isfunction 加載Python原生的模組、用於判斷對象是否為函數類型，以及用於强制終止綫程;
        if not("ctypes" in imported_package_list):
            import ctypes  # 用於强制終止綫程;
        # if not("socketserver" in imported_package_list):
        #     import socketserver  # from socketserver import ThreadingMixIn  #, ForkingMixIn
        # if not("urllib" in imported_package_list):
        #     import urllib  # 加載Python原生的創建客戶端訪問請求連接模組，urllib 用於對 URL 進行編解碼;
        # if not("http.client" in imported_package_list):
        #     import http.client  # 加載Python原生的創建客戶端訪問請求連接模組;
        # if not("http.server" in imported_package_list):
        #     import http.server  # from http.server import HTTPServer, BaseHTTPRequestHandler  # 加載Python原生的創建簡單http服務器模組;
        #     # https: // docs.python.org/3/library/http.server.html
        # if not("cookiejar" in imported_package_list):
        #     from http import cookiejar  # 用於處理請求Cookie;
        # if not("ssl" in imported_package_list):
        #     import ssl  # 用於處理請求證書驗證;
        # if not("base64" in imported_package_list):
        #     import base64  # 加載加、解密模組;
        # if not("venv" in imported_package_list):
        #     import venv  # 加載Python的原生庫，用於建立環境隔離的模組，需要事先在控制臺安裝配置成功：root@localhost:~# pip install venv -i https://mirrors.aliyun.com/pypi/simple/，注意如果是 Ubuntu 系統，需要事先安裝配置成功： apt install python3-venv;
        # if not("pyinstaller" in imported_package_list):
        #     import pyinstaller as pd  # 加載Python第三方庫，用於將Python源代碼工程編譯打包爲二進制可執行檔的模組，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pyinstaller -i https://mirrors.aliyun.com/pypi/simple/;
        # # if not("jupyter" in imported_package_list):
        # #     import jupyter  # 加載Python第三方庫，用於將Python源代碼工程編譯打包爲二進制可執行檔的模組，需要事先在控制臺安裝配置成功：root@localhost:~# pip install jupyter -i https://mirrors.aliyun.com/pypi/simple/，注意如果是 Ubuntu 系統，需要事先安裝配置成功： apt install ;
        # if not("numpy" in imported_package_list):
        #     import numpy as np  # 加載Python第三方庫，用於矩陣運算的模組，需要事先在控制臺安裝配置成功：root@localhost:~# pip install numpy -i https://mirrors.aliyun.com/pypi/simple/，注意如果是 Ubuntu 系統，需要事先安裝配置成功： apt install python3-numpy;
        # if not("pandas" in imported_package_list):
        #     import pandas as pd  # 加載Python第三方庫，用於分析數據的數據框模組，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pandas -i https://mirrors.aliyun.com/pypi/simple/，注意如果是 Ubuntu 系統，需要事先安裝配置成功： apt install python3-pandas;
        # if not("matplotlib" in imported_package_list):
        #     import matplotlib.pyplot as plt
        #     import matplotlib.font_manager as matplotlib_font_manager  # 導入第三方擴展包「matplotlib」中的字體管理器，用於設置生成圖片中文字的字體;
        #     # import matplotlib as mpl  # 加載Python第三方庫，用於繪圖的模組，需要事先在控制臺安裝配置成功：root@localhost:~# pip install matplotlib -i https://mirrors.aliyun.com/pypi/simple/，注意如果是 Ubuntu 系統，需要事先安裝配置成功： apt install python3-matplotlib;
        if not("tkinter" in imported_package_list):
            from tkinter import messagebox as tk_messagebox  # 窗體 tkinter 模組的消息提示框
            from tkinter import filedialog as tk_filedialog  # 窗體 tkinter 模組的文檔選擇框
            import tkinter as tk  # 導入 Python 原生的圖形介面窗體模組「tkinter」，用於創建窗口面板，注意如果是 Ubuntu 系統，需要事先安裝配置成功： apt install python3-tk;
        if not("PIL" in imported_package_list):
            from PIL import Image, ImageTk  # 導入第三方擴展包「PIL」，用於從硬盤讀取圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/，注意如果是 Ubuntu 系統，需要事先安裝配置成功： apt install python3-pillow;
        # if not("cv2" in imported_package_list):
        #     import cv2  # 導入第三方擴展包「PIL」，用於驅動 OpenCV 光學圖形處理庫，需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-python -i https://mirrors.aliyun.com/pypi/simple/，如果是 Ubuntu 系統需要事先安裝 OpenCV 應用成功：root@localhost:~# apt install libavcodec-dev libavformat-dev libswscale-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libgtk2.0-dev libgtk-3-dev libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev libjasper-dev libopencv-dev python3-opencv;
        # if not("pytesseract" in imported_package_list):
        #     import pytesseract  # 導入第三方擴展包「PIL」，用於驅動 Tesseract-OCR 文字識別庫，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pytesseract -i https://mirrors.aliyun.com/pypi/simple/，如果是 Ubuntu 系統需要事先安裝 Tesseract-OCR 應用成功：root@localhost:~# apt install tesseract-ocr libtesseract-dev tesseract-ocr-chi-tra tesseract-ocr-chi_tra_vert tesseract-ocr-chi-sim tesseract-ocr-chi_sim_vert;

        # # 檢查函數需要用到的 Python 第三方模組是否已經安裝成功(pip install)，如果還沒安裝，則執行安裝操作;
        # if "os" in dir(list):
        #     installed_package_list = os.popen("pip list").read()
        # if isinstance(installed_package_list, list) and not("Flask" in installed_package_list):
        #     os_popen_read = os.popen("pip install Flask --trusted-host -i https://pypi.tuna.tsinghua.edu.cn/simple").read()
        #     print(os_popen_read)


        # 配置預設值;
        self.is_Runing = False  # bool("True"), bool("False") 判斷程式是否正在運行中;
        self.is_Concurrent = "Multi-Threading"  # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程），可取值：0、"0"、"Multi-Threading"、"Multi-Processes";
        self.is_window = True  # bool(True), bool(False) 判斷只需要執行一次還是啓動監聽服務器功能;
        self.is_storage_position = "Disk"  # "Database", "Database_and_Disk", "Disk" 判斷存儲位置;
        self.is_storage_type = "csv"  # "json", "csv", "txt", "xlsx", 判斷存儲類型;
        self.default_input_tabel_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        self.input_tabel_tesseract_config = self.default_input_tabel_tesseract_config
        self.inputTabelTesseractConfig = tk.StringVar(value=self.default_input_tabel_tesseract_config)
        self.default_input_measuringRuler_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        self.input_measuringRuler_tesseract_config = self.default_input_measuringRuler_tesseract_config
        self.inputMeasuringRulerTesseractConfig = tk.StringVar(value=self.default_input_measuringRuler_tesseract_config)
        self.default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')
        self.inputTrain_path = self.default_inputTrain_path
        self.inputTrain_File_Array = []
        self.inputTrainpath = tk.StringVar(value=self.default_inputTrain_path)
        self.default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')
        self.inputValidation_path = self.default_inputValidation_path
        self.inputValidation_File_Array = []
        self.inputValidationpath = tk.StringVar(value=self.default_inputValidation_path)
        self.default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
        self.inputTest_path = self.default_inputTest_path
        self.inputTest_File_Array = []
        self.inputTestpath = tk.StringVar(value=self.default_inputTest_path)
        self.default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest", "test" + "." + self.is_storage_type))).replace('\\', '/')
        # self.default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "outputTest", "test" + "." + self.is_storage_type))).replace('\\', '/')
        # self.default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "outputTest", "test" + "." + self.is_storage_type))).replace('\\', '/')
        # self.default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "outputTest", "test" + "." + self.is_storage_type))).replace('\\', '/')
        # os.path.abspath(".")  # 獲取當前文檔所在的絕對路徑;
        # os.path.abspath("..")  # 獲取當前文檔所在目錄的上一層路徑;
        self.outputTest_path = self.default_outputTest_path
        self.outputTest_File_Array = []
        self.outputTestpath = tk.StringVar(value=self.default_outputTest_path)
        self.input_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
        self.output_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')
        self.default_outputTest_URL = "mongodb://username:password@127.0.0.1:27017/testDB"
        self.outputTest_URL = self.default_outputTest_URL
        self.outputTestURL = tk.StringVar(value=self.default_outputTest_URL)
        self.Input_and_Output_Function = self.Input_and_Output
        self.do_Function = self.temp_default_doFunction  # None 或匿名函數 lambda arguments:arguments，其中 lambda 表示聲明匿名函數， do_data 用於接收執行功能的函數;
        self.temp_cache_IO_data_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "temp"))).replace('\\', '/')  # os.path.join(os.path.abspath(".."), "temp")  # "D:\\temp\\"，"../temp/" 需要注意目錄操作權限，用於暫存輸入輸出傳值的媒介目錄;
        self.number_Worker_process = int(0)  # 子進程數目默認 0 個;
        self.time_sleep = float(0.01)  # 用於監聽程序的輪詢延遲參數，單位（秒），預設延遲等待時長為 10 毫秒;
        self.outqueue_from_task_to_host = queue.Queue(maxsize=0)
        self.outqueue_from_host_to_task = queue.Queue(maxsize=0)
        self.file_Data = ""  # 讀入的待處理的樣本數據;
        # self.file_Data_bytes = self.file_Data.encode("utf-8")
        # self.file_Data = self.file_Data_bytes.decode("utf-8")
        # self.file_Data_len = len(bytes(self.file_Data, "utf-8"))
        self.result_Data = ""  # 寫出的處理完畢的樣本數據;
        # self.result_Data_bytes = self.result_Data.encode("utf-8")
        # self.result_Data = self.result_Data_bytes.decode("utf-8")
        # self.result_Data_len = len(bytes(self.result_Data, "utf-8"))
        self.complete_Number = int(0)  # 記錄處理成功的樣本個數
        self.image_sample = []  # 保存用於展示觀察的樣本圖片;
        self.Error_Log = []  # 記錄出錯的樣本路徑;

        self.initializer_Window = None  # 預設延遲等待時長為 20 毫秒;
        self.iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "Icon", "iconbitmap.png"))).replace('\\', '/')
        self.screenwidth = int(0)  # int(tk.Tk().winfo_screenwidth())  # 獲取顯示器屏幕寬度;
        self.screenheight = int(0)  # int(tk.Tk().winfo_screenheight())  # 獲取顯示器屏幕高度;
        self.size_XY = '{}x{}+{}+{}'.format(str(int(int(self.screenwidth)*0.6)), str(int(int(self.screenheight)*0.6)), str(int(int(self.screenwidth)*0.2)), str(int(int(self.screenheight)*0.2)))
        self.LabelFrame_storage_position = None
        self.Checkbutton_storage_position_Database = None
        self.Checkbutton_storage_position_Database_Var = tk.BooleanVar(value=False)  # tk.IntVar(value=0)
        self.Checkbutton_storage_position_Disk = None
        self.Checkbutton_storage_position_Disk_Var = tk.BooleanVar(value=False)  # tk.IntVar(value=0)
        self.Label_outputTest_URL = None
        self.Entry_outputTest_URL = None
        self.Button_outputTest_URL = None
        self.Label_outputTest_path = None
        self.Entry_outputTest_path = None
        self.Button_outputTest_path = None
        self.LabelFrame_storage_type = None
        self.Radiobutton_storage_type_Var = tk.StringVar(value="csv")  # tk.IntVar(value=0)
        self.Radiobutton_storage_type_json = None
        self.Radiobutton_storage_type_csv = None
        self.Radiobutton_storage_type_txt = None
        self.Radiobutton_storage_type_Excel = None
        self.Label_tabel_tesseract_config = None
        self.Entry_tabel_tesseract_config = None
        self.Label_measuringRuler_tesseract_config = None
        self.Entry_measuringRuler_tesseract_config = None
        self.Label_inputTrain_path = None
        self.Entry_inputTrain_path = None
        self.Button_inputTrain_path = None
        self.Label_inputValidation_path = None
        self.Entry_inputValidation_path = None
        self.Button_inputValidation_path = None
        self.Label_inputTest_path = None
        self.Entry_inputTest_path = None
        self.Button_inputTest_path = None
        self.Button_start_and_stop_Train = None
        self.Button_start_and_stop_Test = None
        self.Button_shut_down = None
        self.Label_State = None
        self.Text_display_result = None
        # self.Y_Scrollbar_Text_display_result = None
        # self.X_Scrollbar_Text_display_result = None
        self.LabelFrame_display_sample = None
        self.Label_display_sample = None
        self.Canvas_display_sample = None
        self.Label_Isolation = None


        # 讀取自定義傳入的參數值;
        if "initializer_Window" in kwargs:
            self.initializer_Window = kwargs["initializer_Window"]

        if "outqueue_from_task_to_host" in kwargs:
            self.outqueue_from_task_to_host = kwargs["outqueue_from_task_to_host"]

        if "outqueue_from_task_to_host_maxsize" in kwargs:
            self.outqueue_from_task_to_host = queue.Queue(maxsize=int(kwargs["outqueue_from_task_to_host_maxsize"]))

        if "outqueue_from_host_to_task" in kwargs:
            self.outqueue_from_host_to_task = kwargs["outqueue_from_host_to_task"]

        if "outqueue_from_host_to_task_maxsize" in kwargs:
            self.outqueue_from_host_to_task = queue.Queue(maxsize=int(kwargs["outqueue_from_host_to_task_maxsize"]))

        if "is_Concurrent" in kwargs:
            self.is_Concurrent = str(kwargs["is_Concurrent"])
            # print(self.is_Concurrent)

        # if "is_window" in kwargs:
        #     self.is_window = bool(kwargs["is_window"])

        if "is_storage_position" in kwargs:
            self.is_storage_position = str(kwargs["is_storage_position"])

        if "is_storage_type" in kwargs:
            self.is_storage_type = str(kwargs["is_storage_type"])

        if "default_input_tabel_tesseract_config" in kwargs:
            self.default_input_tabel_tesseract_config = str(kwargs["default_input_tabel_tesseract_config"])

        if "input_tabel_tesseract_config" in kwargs:
            self.input_tabel_tesseract_config = str(kwargs["input_tabel_tesseract_config"])

        if "inputTabelTesseractConfig" in kwargs:
            self.inputTabelTesseractConfig = tk.StringVar(value=str(kwargs["inputTabelTesseractConfig"]))

        if "default_input_measuringRuler_tesseract_config" in kwargs:
            self.default_input_measuringRuler_tesseract_config = str(kwargs["default_input_measuringRuler_tesseract_config"])

        if "input_measuringRuler_tesseract_config" in kwargs:
            self.input_measuringRuler_tesseract_config = str(kwargs["input_measuringRuler_tesseract_config"])

        if "inputMeasuringRulerTesseractConfig" in kwargs:
            self.inputMeasuringRulerTesseractConfig = tk.StringVar(value=str(kwargs["inputMeasuringRulerTesseractConfig"]))

        if "default_inputTrain_path" in kwargs:
            self.default_inputTrain_path = str(kwargs["default_inputTrain_path"])

        if "inputTrain_path" in kwargs:
            self.inputTrain_path = str(kwargs["inputTrain_path"])

        if "inputTrain_File_Array" in kwargs:
            self.inputTrain_File_Array = kwargs["inputTrain_File_Array"]

        if "inputTrainpath" in kwargs:
            self.inputTrainpath = tk.StringVar(value=str(kwargs["inputTrainpath"]))

        if "default_inputValidation_path" in kwargs:
            self.default_inputValidation_path = str(kwargs["default_inputValidation_path"])

        if "inputValidation_path" in kwargs:
            self.inputValidation_path = str(kwargs["inputValidation_path"])

        if "inputValidation_File_Array" in kwargs:
            self.inputValidation_File_Array = kwargs["inputValidation_File_Array"]

        if "inputValidationpath" in kwargs:
            self.inputValidationpath = tk.StringVar(value=str(kwargs["inputValidationpath"]))

        if "default_inputTest_path" in kwargs:
            self.default_inputTest_path = str(kwargs["default_inputTest_path"])

        if "inputTest_path" in kwargs:
            self.inputTest_path = str(kwargs["inputTest_path"])

        if "inputTest_File_Array" in kwargs:
            self.inputTest_File_Array = kwargs["inputTest_File_Array"]

        if "inputTestpath" in kwargs:
            self.inputTestpath = tk.StringVar(value=str(kwargs["inputTestpath"]))

        if "default_outputTest_path" in kwargs:
            self.default_outputTest_path = str(kwargs["default_outputTest_path"])

        if "outputTest_path" in kwargs:
            self.outputTest_path = str(kwargs["outputTest_path"])

        if "outputTest_File_Array" in kwargs:
            self.outputTest_File_Array = kwargs["outputTest_File_Array"]

        if "outputTestpath" in kwargs:
            self.outputTestpath = tk.StringVar(value=str(kwargs["outputTestpath"]))

        if "input_dir" in kwargs:
            self.input_dir = str(kwargs["input_dir"])

        if "output_dir" in kwargs:
            self.output_dir = str(kwargs["output_dir"])

        if "default_outputTest_URL" in kwargs:
            self.default_outputTest_URL = str(kwargs["default_outputTest_URL"])

        if "outputTest_URL" in kwargs:
            self.outputTest_URL = str(kwargs["outputTest_URL"])

        if "outputTestURL" in kwargs:
            self.outputTestURL = tk.StringVar(value=str(kwargs["outputTestURL"]))

        # if "temp_cache_IO_data_dir" in kwargs:
        #     self.temp_cache_IO_data_dir = str(kwargs["temp_cache_IO_data_dir"])

        if "Input_and_Output_Function" in kwargs and inspect.isfunction(kwargs["Input_and_Output_Function"]):
            self.Input_and_Output_Function = kwargs["Input_and_Output_Function"]

        if "do_Function" in kwargs and inspect.isfunction(kwargs["do_Function"]):
            self.do_Function = kwargs["do_Function"]

        # 用於監聽程序的輪詢延遲參數，單位（秒） and isinstance(time_sleep, str);
        if "time_sleep" in kwargs:
            self.time_sleep = float(kwargs["time_sleep"])  # 延遲時長;

        # # 用於判斷監聽創建子進程池數目的參數  and isinstance(number_Worker_process, str);
        # if "number_Worker_process" in kwargs:
        #     self.number_Worker_process = int(kwargs["number_Worker_process"])  # 子進程數目默認 0 個;

        # 具體處理數據的函數;
        # self.do_Function = None
        if "do_Function_obj" in kwargs and isinstance(kwargs["do_Function_obj"], dict) and any(kwargs["do_Function_obj"]):
            # isinstance(do_Function_obj, dict) type(do_Function_obj) == dict do_Function_obj != {} any(do_Function_obj)
            for key in kwargs["do_Function_obj"]:
                # isinstance(do_Function_obj[key], FunctionType)  # 使用原生模組 inspect 中的 isfunction() 方法判斷對象是否是一個函數，或者使用 hasattr(var, '__call__') 判斷變量 var 是否為函數或類的方法，如果是函數返回 True 否則返回 False;
                if key == "do_Function" and inspect.isfunction(kwargs["do_Function_obj"][key]):
                    self.do_Function = kwargs["do_Function_obj"][key]

        if "iconbitmap_path" in kwargs:
            self.iconbitmap_path = str(kwargs["iconbitmap_path"])

        if "screenwidth" in kwargs:
            self.screenwidth = int(kwargs["screenwidth"])

        if "screenheight" in kwargs:
            self.screenheight = int(kwargs["screenheight"])

        if "size_XY" in kwargs:
            self.size_XY = str(kwargs["size_XY"])

        if self.input_tabel_tesseract_config != self.default_input_tabel_tesseract_config:
            self.default_input_tabel_tesseract_config = self.input_tabel_tesseract_config

        if self.input_measuringRuler_tesseract_config != self.default_input_measuringRuler_tesseract_config:
            self.default_input_measuringRuler_tesseract_config = self.input_measuringRuler_tesseract_config

        # # 判斷是否爲打包（.exe）後的環境;
        # if getattr(sys, 'frozen', False):
        #     self.default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')
        #     # self.default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTrain"))).replace('\\', '/')
        #     # self.default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTrain"))).replace('\\', '/')
        #     # self.default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTrain"))).replace('\\', '/')
        #     self.default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')
        #     # self.default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputValidation"))).replace('\\', '/')
        #     # self.default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputValidation"))).replace('\\', '/')
        #     # self.default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputValidation"))).replace('\\', '/')
        #     self.default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
        #     # self.default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTest"))).replace('\\', '/')
        #     # self.default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTest"))).replace('\\', '/')
        #     # self.default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTest"))).replace('\\', '/')
        #     self.default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest", "test" + "." + self.is_storage_type))).replace('\\', '/')
        #     # self.default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "outputTest", "test" + "." + self.is_storage_type))).replace('\\', '/')
        #     # self.default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "outputTest", "test" + "." + self.is_storage_type))).replace('\\', '/')
        #     # self.default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "outputTest", "test" + "." + self.is_storage_type))).replace('\\', '/')
        # else:
        #     self.default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')
        #     # self.default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTrain"))).replace('\\', '/')
        #     # self.default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTrain"))).replace('\\', '/')
        #     # self.default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTrain"))).replace('\\', '/')
        #     self.default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')
        #     # self.default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputValidation"))).replace('\\', '/')
        #     # self.default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputValidation"))).replace('\\', '/')
        #     # self.default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputValidation"))).replace('\\', '/')
        #     self.default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
        #     # self.default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTest"))).replace('\\', '/')
        #     # self.default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTest"))).replace('\\', '/')
        #     # self.default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTest"))).replace('\\', '/')
        #     self.default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest", "test" + "." + self.is_storage_type))).replace('\\', '/')
        #     # self.default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "outputTest", "test" + "." + self.is_storage_type))).replace('\\', '/')
        #     # self.default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "outputTest", "test" + "." + self.is_storage_type))).replace('\\', '/')
        #     # self.default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "outputTest", "test" + "." + self.is_storage_type))).replace('\\', '/')

        # # 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
        # if os.path.exists(self.default_inputTrain_path) and pathlib.Path(self.default_inputTrain_path).is_dir():
        #     # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
        #     if not (os.access(self.default_inputTrain_path, os.R_OK) and os.access(self.default_inputTrain_path, os.W_OK)):
        #         try:
        #             # 修改文檔權限 mode:777 任何人可讀寫;
        #             os.chmod(self.default_inputTrain_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        #             # os.chmod(self.default_inputTrain_path, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
        #             # os.chmod(self.default_inputTrain_path, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
        #             # os.chmod(self.default_inputTrain_path, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
        #             # os.chmod(self.default_inputTrain_path, stat.S_IWOTH)  # 可被其它用戶寫入;
        #             # stat.S_IXOTH:  其他用戶有執行權0o001
        #             # stat.S_IWOTH:  其他用戶有寫許可權0o002
        #             # stat.S_IROTH:  其他用戶有讀許可權0o004
        #             # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
        #             # stat.S_IXGRP:  組用戶有執行許可權0o010
        #             # stat.S_IWGRP:  組用戶有寫許可權0o020
        #             # stat.S_IRGRP:  組用戶有讀許可權0o040
        #             # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
        #             # stat.S_IXUSR:  擁有者具有執行許可權0o100
        #             # stat.S_IWUSR:  擁有者具有寫許可權0o200
        #             # stat.S_IRUSR:  擁有者具有讀許可權0o400

        #             # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
        #             # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
        #             # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
        #             # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
        #             # stat.S_IREAD:  windows下設為唯讀
        #             # stat.S_IWRITE: windows下取消唯讀
        #         except OSError as error:
        #             sys.stdout.write("\n")  # 輸出換行;
        #             sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.default_inputTrain_path + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
        #             sys.stdout.write("\n")  # 輸出換行;
        #             # print(f'Error: {self.default_inputTrain_path} : {error}')
        #             # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputTrain_path + " ]" + "\n" + "無法修改為可讀可寫權限.")
        #             # if self.is_window:
        #             #     self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputTrain_path + " ]" + "\n" + "無法修改為可讀可寫權限."
        #             self.Error_Log.append(self.default_inputTrain_path)
        #             sys.exit(1)  # 中止當前進程，退出當前程序;
        # else:
        #     try:
        #         # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
        #         # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
        #         os.makedirs(self.default_inputTrain_path, mode=0o777, exist_ok=True)
        #     except FileExistsError as error:
        #         # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
        #         sys.stdout.write("\n")  # 輸出換行;
        #         sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.default_inputTrain_path + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
        #         sys.stdout.write("\n")  # 輸出換行;
        #         # print(f'Error: {self.default_inputTrain_path} : {error}')
        #         # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputTrain_path + " ]" + "\n" + "無法修改為可讀可寫權限.")
        #         # if self.is_window:
        #         #     self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputTrain_path + " ]" + "\n" + "無法修改為可讀可寫權限."
        #         self.Error_Log.append(self.default_inputTrain_path)
        #         sys.exit(1)  # 中止當前進程，退出當前程序;

        # if not (os.path.exists(self.default_inputTrain_path) and pathlib.Path(self.default_inputTrain_path).is_dir()):
        #     sys.stdout.write("\n")  # 輸出換行;
        #     sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.default_inputTrain_path)  # 將字符串輸出寫到操作系統控制臺;
        #     sys.stdout.write("\n")  # 輸出換行;
        #     # print(f'Error: {self.default_inputTrain_path} : {error}')
        #     # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputTrain_path + " ]" + "\n" + "無法修改為可讀可寫權限.")
        #     # if self.is_window:
        #     #     self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputTrain_path + " ]" + "\n" + "無法修改為可讀可寫權限."
        #     self.Error_Log.append(self.default_inputTrain_path)
        #     sys.exit(1)  # 中止當前進程，退出當前程序;

        if self.inputTrain_path != self.default_inputTrain_path:
            self.default_inputTrain_path = self.inputTrain_path

        # # print(self.inputTrain_path)
        # # print(self.inputTrain_File_Array)
        # if len(self.inputTrain_File_Array) == 0:
        #     if len(self.inputTrain_path) > 0:
        #         # self.inputTrain_File_Array = []
        #         self.inputTrain_File_Array = self.Path_Conversion(self.inputTrain_path, self.time_sleep)[0]

        # # 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
        # if os.path.exists(self.default_inputValidation_path) and pathlib.Path(self.default_inputValidation_path).is_dir():
        #     # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
        #     if not (os.access(self.default_inputValidation_path, os.R_OK) and os.access(self.default_inputValidation_path, os.W_OK)):
        #         try:
        #             # 修改文檔權限 mode:777 任何人可讀寫;
        #             os.chmod(self.default_inputValidation_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        #             # os.chmod(self.default_inputValidation_path, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
        #             # os.chmod(self.default_inputValidation_path, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
        #             # os.chmod(self.default_inputValidation_path, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
        #             # os.chmod(self.default_inputValidation_path, stat.S_IWOTH)  # 可被其它用戶寫入;
        #             # stat.S_IXOTH:  其他用戶有執行權0o001
        #             # stat.S_IWOTH:  其他用戶有寫許可權0o002
        #             # stat.S_IROTH:  其他用戶有讀許可權0o004
        #             # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
        #             # stat.S_IXGRP:  組用戶有執行許可權0o010
        #             # stat.S_IWGRP:  組用戶有寫許可權0o020
        #             # stat.S_IRGRP:  組用戶有讀許可權0o040
        #             # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
        #             # stat.S_IXUSR:  擁有者具有執行許可權0o100
        #             # stat.S_IWUSR:  擁有者具有寫許可權0o200
        #             # stat.S_IRUSR:  擁有者具有讀許可權0o400

        #             # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
        #             # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
        #             # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
        #             # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
        #             # stat.S_IREAD:  windows下設為唯讀
        #             # stat.S_IWRITE: windows下取消唯讀
        #         except OSError as error:
        #             sys.stdout.write("\n")  # 輸出換行;
        #             sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.default_inputValidation_path + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
        #             sys.stdout.write("\n")  # 輸出換行;
        #             # print(f'Error: {self.default_inputValidation_path} : {error}')
        #             # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputValidation_path + " ]" + "\n" + "無法修改為可讀可寫權限.")
        #             # if self.is_window:
        #             #     self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputValidation_path + " ]" + "\n" + "無法修改為可讀可寫權限."
        #             self.Error_Log.append(self.default_inputValidation_path)
        #             sys.exit(1)  # 中止當前進程，退出當前程序;
        # else:
        #     try:
        #         # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
        #         # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
        #         os.makedirs(self.default_inputValidation_path, mode=0o777, exist_ok=True)
        #     except FileExistsError as error:
        #         # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
        #         sys.stdout.write("\n")  # 輸出換行;
        #         sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.default_inputValidation_path + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
        #         sys.stdout.write("\n")  # 輸出換行;
        #         # print(f'Error: {self.default_inputValidation_path} : {error}')
        #         # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputValidation_path + " ]" + "\n" + "無法修改為可讀可寫權限.")
        #         # if self.is_window:
        #         #     self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputValidation_path + " ]" + "\n" + "無法修改為可讀可寫權限."
        #         self.Error_Log.append(self.default_inputValidation_path)
        #         sys.exit(1)  # 中止當前進程，退出當前程序;

        # if not (os.path.exists(self.default_inputValidation_path) and pathlib.Path(self.default_inputValidation_path).is_dir()):
        #     sys.stdout.write("\n")  # 輸出換行;
        #     sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.default_inputValidation_path)  # 將字符串輸出寫到操作系統控制臺;
        #     sys.stdout.write("\n")  # 輸出換行;
        #     # print(f'Error: {self.default_inputValidation_path} : {error}')
        #     # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputValidation_path + " ]" + "\n" + "無法修改為可讀可寫權限.")
        #     # if self.is_window:
        #     #     self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputValidation_path + " ]" + "\n" + "無法修改為可讀可寫權限."
        #     self.Error_Log.append(self.default_inputValidation_path)
        #     sys.exit(1)  # 中止當前進程，退出當前程序;

        if self.inputValidation_path != self.default_inputValidation_path:
            self.default_inputValidation_path = self.inputValidation_path

        # # print(self.inputValidation_path)
        # if len(self.inputValidation_File_Array) == 0:
        #     if len(self.inputValidation_path) > 0:
        #         # self.inputValidation_File_Array = []
        #         self.inputValidation_File_Array = self.Path_Conversion(self.inputValidation_path, self.time_sleep)[0]

        # # 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
        # if os.path.exists(self.default_inputTest_path) and pathlib.Path(self.default_inputTest_path).is_dir():
        #     # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
        #     if not (os.access(self.default_inputTest_path, os.R_OK) and os.access(self.default_inputTest_path, os.W_OK)):
        #         try:
        #             # 修改文檔權限 mode:777 任何人可讀寫;
        #             os.chmod(self.default_inputTest_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        #             # os.chmod(self.default_inputTest_path, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
        #             # os.chmod(self.default_inputTest_path, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
        #             # os.chmod(self.default_inputTest_path, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
        #             # os.chmod(self.default_inputTest_path, stat.S_IWOTH)  # 可被其它用戶寫入;
        #             # stat.S_IXOTH:  其他用戶有執行權0o001
        #             # stat.S_IWOTH:  其他用戶有寫許可權0o002
        #             # stat.S_IROTH:  其他用戶有讀許可權0o004
        #             # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
        #             # stat.S_IXGRP:  組用戶有執行許可權0o010
        #             # stat.S_IWGRP:  組用戶有寫許可權0o020
        #             # stat.S_IRGRP:  組用戶有讀許可權0o040
        #             # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
        #             # stat.S_IXUSR:  擁有者具有執行許可權0o100
        #             # stat.S_IWUSR:  擁有者具有寫許可權0o200
        #             # stat.S_IRUSR:  擁有者具有讀許可權0o400

        #             # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
        #             # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
        #             # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
        #             # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
        #             # stat.S_IREAD:  windows下設為唯讀
        #             # stat.S_IWRITE: windows下取消唯讀
        #         except OSError as error:
        #             sys.stdout.write("\n")  # 輸出換行;
        #             sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.default_inputTest_path + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
        #             sys.stdout.write("\n")  # 輸出換行;
        #             # print(f'Error: {self.default_inputTest_path} : {error}')
        #             # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputTest_path + " ]" + "\n" + "無法修改為可讀可寫權限.")
        #             # if self.is_window:
        #             #     self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputTest_path + " ]" + "\n" + "無法修改為可讀可寫權限."
        #             self.Error_Log.append(self.default_inputTest_path)
        #             sys.exit(1)  # 中止當前進程，退出當前程序;
        # else:
        #     try:
        #         # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
        #         # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
        #         os.makedirs(self.default_inputTest_path, mode=0o777, exist_ok=True)
        #     except FileExistsError as error:
        #         # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
        #         sys.stdout.write("\n")  # 輸出換行;
        #         sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.default_inputTest_path + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
        #         sys.stdout.write("\n")  # 輸出換行;
        #         # print(f'Error: {self.default_inputTest_path} : {error}')
        #         # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputTest_path + " ]" + "\n" + "無法修改為可讀可寫權限.")
        #         # if self.is_window:
        #         #     self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputTest_path + " ]" + "\n" + "無法修改為可讀可寫權限."
        #         self.Error_Log.append(self.default_inputTest_path)
        #         sys.exit(1)  # 中止當前進程，退出當前程序;

        # if not (os.path.exists(self.default_inputTest_path) and pathlib.Path(self.default_inputTest_path).is_dir()):
        #     sys.stdout.write("\n")  # 輸出換行;
        #     sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.default_inputTest_path)  # 將字符串輸出寫到操作系統控制臺;
        #     sys.stdout.write("\n")  # 輸出換行;
        #     # print(f'Error: {self.default_inputTest_path} : {error}')
        #     # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputTest_path + " ]" + "\n" + "無法修改為可讀可寫權限.")
        #     # if self.is_window:
        #     #     self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_inputTest_path + " ]" + "\n" + "無法修改為可讀可寫權限."
        #     self.Error_Log.append(self.default_inputTest_path)
        #     sys.exit(1)  # 中止當前進程，退出當前程序;

        if self.inputTest_path != self.default_inputTest_path:
            self.default_inputTest_path = self.inputTest_path

        # # print(self.inputTest_path)
        # if len(self.inputTest_File_Array) == 0:
        #     if len(self.inputTest_path) > 0:
        #         # self.inputTest_File_Array = []
        #         self.inputTest_File_Array = self.Path_Conversion(self.inputTest_path, self.time_sleep)[0]

        # # 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
        # if os.path.exists(self.default_outputTest_path) and pathlib.Path(self.default_outputTest_path).is_dir():
        #     # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
        #     if not (os.access(self.default_outputTest_path, os.R_OK) and os.access(self.default_outputTest_path, os.W_OK)):
        #         try:
        #             # 修改文檔權限 mode:777 任何人可讀寫;
        #             os.chmod(self.default_outputTest_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        #             # os.chmod(self.default_outputTest_path, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
        #             # os.chmod(self.default_outputTest_path, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
        #             # os.chmod(self.default_outputTest_path, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
        #             # os.chmod(self.default_outputTest_path, stat.S_IWOTH)  # 可被其它用戶寫入;
        #             # stat.S_IXOTH:  其他用戶有執行權0o001
        #             # stat.S_IWOTH:  其他用戶有寫許可權0o002
        #             # stat.S_IROTH:  其他用戶有讀許可權0o004
        #             # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
        #             # stat.S_IXGRP:  組用戶有執行許可權0o010
        #             # stat.S_IWGRP:  組用戶有寫許可權0o020
        #             # stat.S_IRGRP:  組用戶有讀許可權0o040
        #             # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
        #             # stat.S_IXUSR:  擁有者具有執行許可權0o100
        #             # stat.S_IWUSR:  擁有者具有寫許可權0o200
        #             # stat.S_IRUSR:  擁有者具有讀許可權0o400

        #             # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
        #             # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
        #             # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
        #             # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
        #             # stat.S_IREAD:  windows下設為唯讀
        #             # stat.S_IWRITE: windows下取消唯讀
        #         except OSError as error:
        #             sys.stdout.write("\n")  # 輸出換行;
        #             sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.default_outputTest_path + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
        #             sys.stdout.write("\n")  # 輸出換行;
        #             # print(f'Error: {self.default_outputTest_path} : {error}')
        #             # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_outputTest_path + " ]" + "\n" + "無法修改為可讀可寫權限.")
        #             # if self.is_window:
        #             #     self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_outputTest_path + " ]" + "\n" + "無法修改為可讀可寫權限."
        #             self.Error_Log.append(self.default_outputTest_path)
        #             sys.exit(1)  # 中止當前進程，退出當前程序;
        # else:
        #     try:
        #         # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
        #         # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
        #         os.makedirs(self.default_outputTest_path, mode=0o777, exist_ok=True)
        #     except FileExistsError as error:
        #         # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
        #         sys.stdout.write("\n")  # 輸出換行;
        #         sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.default_outputTest_path + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
        #         sys.stdout.write("\n")  # 輸出換行;
        #         # print(f'Error: {self.default_outputTest_path} : {error}')
        #         # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_outputTest_path + " ]" + "\n" + "無法修改為可讀可寫權限.")
        #         # if self.is_window:
        #         #     self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_outputTest_path + " ]" + "\n" + "無法修改為可讀可寫權限."
        #         self.Error_Log.append(self.default_outputTest_path)
        #         sys.exit(1)  # 中止當前進程，退出當前程序;

        # if not (os.path.exists(self.default_outputTest_path) and pathlib.Path(self.default_outputTest_path).is_dir()):
        #     sys.stdout.write("\n")  # 輸出換行;
        #     sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.default_outputTest_path)  # 將字符串輸出寫到操作系統控制臺;
        #     sys.stdout.write("\n")  # 輸出換行;
        #     # print(f'Error: {self.default_outputTest_path} : {error}')
        #     # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_outputTest_path + " ]" + "\n" + "無法修改為可讀可寫權限.")
        #     # if self.is_window:
        #     #     self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + self.default_outputTest_path + " ]" + "\n" + "無法修改為可讀可寫權限."
        #     self.Error_Log.append(self.default_outputTest_path)
        #     sys.exit(1)  # 中止當前進程，退出當前程序;

        if self.outputTest_path != self.default_outputTest_path:
            self.default_outputTest_path = self.outputTest_path

        # # print(self.outputTest_path)
        # if len(self.outputTest_File_Array) == 0:
        #     if len(self.outputTest_path) > 0:
        #         # # self.outputTest_File_Array = []
        #         # self.outputTest_File_Array = self.Path_Conversion(self.outputTest_path, self.time_sleep)[0]
        #         self.outputTest_File_Array = [self.outputTest_path]

        if len(self.outputTest_path) > 0:
            if self.outputTest_path.find(".", 0, int(len(self.outputTest_path)-1)) != -1:

                self.is_storage_type = str(self.outputTest_path.split('.')[len(self.outputTest_path.split('.'))-1])
                # print("storage type:", self.is_storage_type)

                if not (self.is_storage_type == "json" or self.is_storage_type == "csv" or self.is_storage_type == "txt" or self.is_storage_type == "xlsx"):
                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                    # self.Error_Log.append(self.outputTest_path)
                    sys.exit(1)  # 中止當前進程，退出當前程序;

                # if self.is_storage_type == "json":
                #     self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                #     self.Radiobutton_storage_type_txt.deselect()
                #     self.Radiobutton_storage_type_Excel.deselect()
                #     self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                # elif self.is_storage_type == "csv":
                #     self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                #     self.Radiobutton_storage_type_txt.deselect()
                #     self.Radiobutton_storage_type_Excel.deselect()
                #     self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                # elif self.is_storage_type == "txt":
                #     self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                #     self.Radiobutton_storage_type_csv.deselect()
                #     self.Radiobutton_storage_type_Excel.deselect()
                #     self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                # elif self.is_storage_type == "xlsx":
                #     self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                #     self.Radiobutton_storage_type_csv.deselect()
                #     self.Radiobutton_storage_type_txt.deselect()
                #     self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                # elif len(self.is_storage_type) == 0:
                #     self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                #     self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                #     self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                #     self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                # else:
                #     # sys.stdout.write("\n")  # 輸出換行;
                #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                #     # sys.stdout.write("\n")  # 輸出換行;
                #     print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                #     # self.Error_Log.append(self.outputTest_path)
                #     sys.exit(1)  # 中止當前進程，退出當前程序;
            else:
                # sys.stdout.write("\n")  # 輸出換行;
                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                # sys.stdout.write("\n")  # 輸出換行;
                print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                # self.Error_Log.append(self.outputTest_path)
                sys.exit(1)  # 中止當前進程，退出當前程序;

        if os.path.exists(self.inputTest_path) and os.path.isfile(self.inputTest_path):
            self.input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(self.inputTest_path)))).replace('\\', '/')
        elif os.path.exists(self.inputTest_path) and pathlib.Path(self.inputTest_path).is_dir():
            self.input_dir = str(self.inputTest_path)

        if os.path.exists(self.outputTest_path) and os.path.isfile(self.outputTest_path):
            self.output_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(self.outputTest_path)))).replace('\\', '/')

        # if not outqueue_from_task_to_host:
        #     outqueue_from_task_to_host = queue.Queue(maxsize=0)
        # if not outqueue_from_host_to_task:
        #     outqueue_from_host_to_task = queue.Queue(maxsize=0)

        if self.initializer_Window:

            # 設置窗體標題;
            self.initializer_Window.title('悟空')  # 設置窗體標題;

            # 設置窗口北京色爲：全黑色;
            # self.initializer_Window.configure(bg="#ffffff")  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色;

            if getattr(sys, 'frozen', False):
                self.iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "Icon", "iconbitmap.png"))).replace('\\', '/')
                # self.iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "Icon", "iconbitmap.png"))).replace('\\', '/')
                # self.iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "Icon", "iconbitmap.png"))).replace('\\', '/')
                # self.iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "Icon", "iconbitmap.png"))).replace('\\', '/')
            else:
                # self.iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "Icon", "iconbitmap.png"))).replace('\\', '/')
                # self.iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "Icon", "iconbitmap.png"))).replace('\\', '/')
                # self.iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "Icon", "iconbitmap.png"))).replace('\\', '/')
                self.iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "Icon", "iconbitmap.png"))).replace('\\', '/')
            # print(self.iconbitmap_path)  # "C:/Criss/OCR/src/Icon/iconbitmap.png"

            if os.path.exists(self.iconbitmap_path) and os.path.isfile(self.iconbitmap_path):
                self.initializer_Window.iconbitmap(self.iconbitmap_path)  # 設置窗體徽標;
            # else:
            #     print("Error iconbitmap path: " + "\n" + self.iconbitmap_path)

            # 獲取顯示器屏幕寬度;
            self.screenwidth = int(self.initializer_Window.winfo_screenwidth())  # 獲取顯示器屏幕寬度;
            # print(self.screenwidth)
            # 獲取顯示器屏幕高度;
            self.screenheight = int(self.initializer_Window.winfo_screenheight())  # 獲取顯示器屏幕高度;
            # print(self.screenheight)

            self.size_XY = '{}x{}+{}+{}'.format(str(int(int(self.screenwidth)*0.6)), str(int(int(self.screenheight)*0.6)), str(int(int(self.screenwidth)*0.2)), str(int(int(self.screenheight)*0.2)))
            # print(self.size_XY)

            self.initializer_Window.geometry(self.size_XY)  # 設定窗口的大小（寬 × 長），單位爲：像素（px），注意，這裏的乘號使用小寫字母「x」符號表示;

            # 設置隱藏窗口上部的工具欄，注意因爲將不會顯示關閉按鈕，所以無法點擊關閉窗口;
            # self.initializer_Window.overrideredirect(True)  # 設置隱藏窗口上部的工具欄;

            # 設置使窗口置頂（顯示爲當前活動窗口）;
            # self.initializer_Window.wm_attributes('-topmost', True)  # 第二個參數取：1 或 True 值，表示設置使窗口保持頂層（顯示爲當前活動窗口，覆蓋其它窗口），第二個參數若取：0 或 False 值，則表示爲正常窗口，允許其它窗口覆蓋;

            # self.initializer_Window.attributes("-toolwindow", True)  #第二個參數取：1 或 True 值，表示設置工具欄樣式窗口;

            # 設置窗口的透明性;
            self.initializer_Window.attributes("-alpha", 1.0)
            # 設置使窗口默認顔色透明;
            # self.initializer_Window.wm_attributes('-transparentcolor', self.initializer_Window['bg'])  # 設置使窗口默認顔色透明;

            # self.initializer_Window.withdraw()  # 設置隱藏窗體，不需要事先執行：self.initializer_Window.update()，因爲直接就不繪製窗體，但會裝在内存裏;
            # self.initializer_Window.state("zoomed")  # 使窗體最大化;
            # self.initializer_Window.state("iconic")  # 使窗體最小化，相當於隱藏窗口;
            # self.initializer_Window.state("normal")  # 使窗體爲：普通窗口;
            # self.initializer_Window.update()  # 刷新窗體介面;

            # 設置橫向 x 軸（寬度，左右）方向、縱向 y 軸（高度，上下）方向，是否可以拖曳調整窗體大小，第一個參數表示橫向 x 軸（寬度，左右）方向的可調性，第二個參數表示縱向 y 軸（高度，上下）方向的可調性;
            self.initializer_Window.resizable(False, False)  # 設置橫向 x 軸（寬度，左右）方向、縱向 y 軸（高度，上下）方向，是否可以拖曳調整窗體大小，第一個參數表示橫向 x 軸（寬度，左右）方向的可調性，第二個參數表示縱向 y 軸（高度，上下）方向的可調性;

            # 創建用於判斷結果存儲位置的標簽框架（tkinter.LabelFrame）組件;
            self.LabelFrame_storage_position = tk.LabelFrame(
                master=self.initializer_Window,
                text="Result storage position",
                # bg="#ffffff",  # 參數：bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色;
                borderwidth=1.0
            )
            # 將標簽框架（tkinter.LabelFrame）組件插入窗體介面中;
            self.LabelFrame_storage_position.grid(
                row=1,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=2,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建判斷結果存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            self.Checkbutton_storage_position_Database_Var = tk.BooleanVar(value=False)  # tk.IntVar(value=0)
            self.Checkbutton_storage_position_Database = tk.Checkbutton(
                master=self.LabelFrame_storage_position,  # 將複選框組件放置在自定義的標簽框架組件内;
                text="Database",
                variable=self.Checkbutton_storage_position_Database_Var,
                onvalue=True,
                offvalue=False,
                # height=5,
                # width=20,
                state="disabled",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.select_Checkbutton_storage_position
            )
            # 將複選框（tkinter.Checkbutton）組件插入到標簽框架（tkinter.LabelFrame）組件中;
            self.Checkbutton_storage_position_Database.grid(
                row=1,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建判斷結果存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
            self.Checkbutton_storage_position_Disk_Var = tk.BooleanVar(value=True)  # tk.IntVar(value=1)
            self.Checkbutton_storage_position_Disk = tk.Checkbutton(
                master=self.LabelFrame_storage_position,  # 將複選框組件放置在自定義的標簽框架組件内;
                text="Disk",
                variable=self.Checkbutton_storage_position_Disk_Var,
                onvalue=True,
                offvalue=False,
                # height=5,
                # width=20,
                state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.select_Checkbutton_storage_position
            )
            # 將複選框（tkinter.Checkbutton）組件插入到標簽框架（tkinter.LabelFrame）組件中;
            self.Checkbutton_storage_position_Disk.grid(
                row=1,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=2,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            if self.is_storage_position == "Database":
                # self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                # self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            elif self.is_storage_position == "Database_and_Disk":
                self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                # self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                # self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            elif self.is_storage_position == "Disk":
                self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                # self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                # self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            elif len(self.is_storage_position) == 0:
                # self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                # self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            else:
                # sys.stdout.write("\n")  # 輸出換行;
                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + ",." + str(self.is_storage_position))  # 將字符串輸出寫到操作系統控制臺;
                # sys.stdout.write("\n")  # 輸出換行;
                print("參數錯誤." + "\n" + "用於輸出保存運算結果的位置:" + "\n" + "[ ." + str(self.is_storage_position) + " ]" + "\n" + "不合規，目前只支持:" + "\n" + "Database, Disk" + "\n" + "兩種方法.")
                # Label_State['text'] = "參數錯誤." + "\n" + "用於輸出保存運算結果的位置:" + "\n" + "[ ." + str(self.is_storage_position) + " ]" + "\n" + "不合規，目前只支持:" + "\n" + "Database, Disk" + "\n" + "兩種方法."
                # Error_Log.append(str(self.is_storage_position))
                sys.exit(1)  # 中止當前進程，退出當前程序;

            # 創建輸出運算結果路徑輸入框提示標簽（tkinter.Label）組件;
            self.Label_outputTest_URL = tk.Label(
                master=self.initializer_Window,
                text='Output url: ',
                # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
                # font=('Arial', 12),
                # width=30,  # 注意，標簽 width 的單位為「字符」個數;
                # height=2  # 注意，標簽 height 的單位為「字符」個數;
            )
            self.Label_outputTest_URL.grid(
                row=2,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            self.outputTestURL = tk.StringVar(value=self.default_outputTest_URL)
            # self.outputTestURL.set(self.default_outputTest_URL)
            # 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
            # 創建輸出運算結果位置的單行文本輸入框（tkinter.Entry）組件;
            self.Entry_outputTest_URL = tk.Entry(
                master=self.initializer_Window,
                # font=("Arial", 14),
                textvariable=self.outputTestURL,
                state="disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
            )
            self.Entry_outputTest_URL.grid(
                row=2,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=2,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建訓練集樣本加載按鈕（tkinter.Button）組件;
            self.Button_outputTest_URL = tk.Button(
                master=self.initializer_Window,
                text="Output url",
                # image=img_1,
                compound="center",
                cursor="hand2",
                state="disabled",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.click_Button_outputTest_URL  # 指定按鈕控件被單擊後執行的函數;
            )
            self.Button_outputTest_URL.grid(
                row=2,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=3,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建輸出運算結果路徑輸入框提示標簽（tkinter.Label）組件;
            self.Label_outputTest_path = tk.Label(
                master=self.initializer_Window,
                text='Output path: ',
                # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
                # font=('Arial', 12),
                # width=30,  # 注意，標簽 width 的單位為「字符」個數;
                # height=2  # 注意，標簽 height 的單位為「字符」個數;
            )
            self.Label_outputTest_path.grid(
                row=3,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            self.outputTestpath = tk.StringVar(value=self.default_outputTest_path)
            # self.outputTestpath.set(self.default_outputTest_path)
            # 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
            # 創建輸出運算結果位置的單行文本輸入框（tkinter.Entry）組件;
            self.Entry_outputTest_path = tk.Entry(
                master=self.initializer_Window,
                # font=("Arial", 14),
                textvariable=self.outputTestpath,
                state="normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
            )
            self.Entry_outputTest_path.grid(
                row=3,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=2,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # self.outputTest_path = self.Entry_outputTest_path.get()  # 讀取文本框輸入的内容;
            # self.outputTest_path = str(self.outputTest_path).replace('\\', '/')
            # # self.outputTest_path = self.outputTest_path.replace('/', r'\\')
            # print(self.outputTest_path)
            # tk_messagebox.showinfo(
            #     title="溫馨提示 tkinter.Entry 2",
            #     message=self.outputTest_path
            # )

            # 創建訓練集樣本加載按鈕（tkinter.Button）組件;
            self.Button_outputTest_path = tk.Button(
                master=self.initializer_Window,
                text="Output Test",
                # image=img_1,
                compound="center",
                cursor="hand2",
                state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.click_Button_outputTest_path  # 指定按鈕控件被單擊後執行的函數;
            )
            self.Button_outputTest_path.grid(
                row=3,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=3,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建用於判斷結果存儲類型的標簽框架（tkinter.LabelFrame）組件;
            self.LabelFrame_storage_type = tk.LabelFrame(
                master=self.initializer_Window,
                text="Result storage type",
                # bg="#ffffff",  # 參數：bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色;
                borderwidth=1.0
            )
            # 將標簽框架（tkinter.LabelFrame）組件插入到窗體介面中;
            self.LabelFrame_storage_type.grid(
                row=4,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=4,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            self.Radiobutton_storage_type_Var = tk.StringVar(value="csv")  # tk.IntVar(value=0)

            # 創建判斷結果存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
            self.Radiobutton_storage_type_json = tk.Radiobutton(
                master=self.LabelFrame_storage_type,  # 將單選框組件放置在自定義的標簽框架組件内;
                text=".json",
                variable=self.Radiobutton_storage_type_Var,
                value="json",
                state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.select_Radiobutton_storage_type
            )
            # 將單選框（tkinter.Radiobutton）組件插入到標簽框架（tkinter.LabelFrame）組件中;
            self.Radiobutton_storage_type_json.grid(
                row=1,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建判斷結果存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
            self.Radiobutton_storage_type_csv = tk.Radiobutton(
                master=self.LabelFrame_storage_type,  # 將單選框組件放置在自定義的標簽框架組件内;
                text=".csv",
                variable=self.Radiobutton_storage_type_Var,
                value="csv",
                state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.select_Radiobutton_storage_type
            )
            # 將單選框（tkinter.Radiobutton）組件插入到標簽框架（tkinter.LabelFrame）組件中;
            self.Radiobutton_storage_type_csv.grid(
                row=1,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=2,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建判斷結果存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
            self.Radiobutton_storage_type_txt = tk.Radiobutton(
                master=self.LabelFrame_storage_type,  # 將單選框組件放置在自定義的標簽框架組件内;
                text=".txt",
                variable=self.Radiobutton_storage_type_Var,
                value="txt",
                state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.select_Radiobutton_storage_type
            )
            # 將單選框（tkinter.Radiobutton）組件插入到標簽框架（tkinter.LabelFrame）組件中;
            self.Radiobutton_storage_type_txt.grid(
                row=1,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=3,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建判斷結果存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
            self.Radiobutton_storage_type_Excel = tk.Radiobutton(
                master=self.LabelFrame_storage_type,  # 將單選框組件放置在自定義的標簽框架組件内;
                text="Excel",
                variable=self.Radiobutton_storage_type_Var,
                value="xlsx",
                state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.select_Radiobutton_storage_type
            )
            # 將單選框（tkinter.Radiobutton）組件插入到標簽框架（tkinter.LabelFrame）組件中;
            self.Radiobutton_storage_type_Excel.grid(
                row=1,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=4,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            if self.is_storage_type == "json":
                self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
            elif self.is_storage_type == "csv":
                # self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
            elif self.is_storage_type == "txt":
                # self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
            elif self.is_storage_type == "xlsx":
                # self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
            elif len(self.is_storage_type) == 0:
                # self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                # self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
            else:
                # sys.stdout.write("\n")  # 輸出換行;
                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + ",." + str(self.is_storage_type))  # 將字符串輸出寫到操作系統控制臺;
                # sys.stdout.write("\n")  # 輸出換行;
                print("參數錯誤." + "\n" + "用於輸出保存運算結果的檔的類型:" + "\n" + "[ ." + str(self.is_storage_type) + " ]" + "\n" + "不合規，目前只支持:" + "\n" + ".csv .txt .json .xlsx" + "\n" + "四種類型.")
                # self.Label_State['text'] = "參數錯誤." + "\n" + "用於輸出保存運算結果的檔的類型:" + "\n" + "[ ." + str(self.is_storage_type) + " ]" + "\n" + "不合規，目前只支持:" + "\n" + ".csv .txt .json .xlsx" + "\n" + "四種類型."
                # self.Error_Log.append(str(self.is_storage_type))
                sys.exit(1)  # 中止當前進程，退出當前程序;

            # 創建訓練集樣本輸入框提示標簽（tkinter.Label）組件;
            self.Label_inputTrain_path = tk.Label(
                master=self.initializer_Window,
                text='Input train: ',
                # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
                # font=('Arial', 12),
                # width=30,  # 注意，標簽 width 的單位為「字符」個數;
                # height=2  # 注意，標簽 height 的單位為「字符」個數;
            )
            # self.Label_inputTrain_path.grid(
            #     row=5,  # 橫向行號;
            #     rowspan=1,  # 縱向跨行合并縱向行數目;
            #     column=1,  # 縱向列號;
            #     columnspan=1,  # 橫向跨列合并橫向列數目;
            #     ipadx=0,  # 組件内部左右間距;
            #     ipady=0,  # 組件内部上下間距;
            #     padx=0,  # 組件外部左右間距;
            #     pady=0,  # 組件外部上下間距;
            #     sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            # )

            # 定義變量 inputTrainpath 爲 tk.StringVar() 類型，在定義的時候，設置其參數 value 爲某一個值，這個值就是預設的默認值，或者使用 .set 屬性也可以設置其值。
            self.inputTrainpath = tk.StringVar(value=self.default_inputTrain_path)
            # self.inputTrainpath.set(self.default_inputTrain_path)
            # 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
            # 在插入單行文本輸入框 Entry 控件的時候，使用參數 textvariable 指向變量 inputTrainpath，即可指定單行文本輸入框 Entry 控件的預設值。
            # 創建訓練集樣本輸入單行文本框（tkinter.Entry）組件;
            self.Entry_inputTrain_path = tk.Entry(
                master=self.initializer_Window,
                # font=("Arial", 14),
                textvariable=self.inputTrainpath,
                state="disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
            )
            # 將單行文本框（tkinter.Entry）組件插入到窗體介面;
            # self.Entry_inputTrain_path.grid(
            #     row=5,  # 橫向行號;
            #     rowspan=1,  # 縱向跨行合并縱向行數目;
            #     column=2,  # 縱向列號;
            #     columnspan=1,  # 橫向跨列合并橫向列數目;
            #     ipadx=0,  # 組件内部左右間距;
            #     ipady=0,  # 組件内部上下間距;
            #     padx=0,  # 組件外部左右間距;
            #     pady=0,  # 組件外部上下間距;
            #     sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            # )

            # 創建訓練集樣本加載按鈕（tkinter.Button）組件;
            self.Button_inputTrain_path = tk.Button(
                master=self.initializer_Window,
                text="Input Train",
                # image=img_1,
                compound="center",
                cursor="hand2",
                state="disabled",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.click_Button_inputTrain_path  # 指定按鈕控件被單擊後執行的函數;
            )
            # self.Button_inputTrain_path.grid(
            #     row=5,  # 橫向行號;
            #     rowspan=1,  # 縱向跨行合并縱向行數目;
            #     column=3,  # 縱向列號;
            #     columnspan=1,  # 橫向跨列合并橫向列數目;
            #     ipadx=0,  # 組件内部左右間距;
            #     ipady=0,  # 組件内部上下間距;
            #     padx=0,  # 組件外部左右間距;
            #     pady=0,  # 組件外部上下間距;
            #     sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            # )

            # 創建驗證集樣本輸入框提示標簽（tkinter.Label）組件;
            self.Label_inputValidation_path = tk.Label(
                master=self.initializer_Window,
                text='Input validation: ',
                # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
                # font=('Arial', 12),
                # width=30,  # 注意，標簽 width 的單位為「字符」個數;
                # height=2  # 注意，標簽 height 的單位為「字符」個數;
            )
            # self.Label_inputValidation_path.grid(
            #     row=6,  # 橫向行號;
            #     rowspan=1,  # 縱向跨行合并縱向行數目;
            #     column=1,  # 縱向列號;
            #     columnspan=1,  # 橫向跨列合并橫向列數目;
            #     ipadx=0,  # 組件内部左右間距;
            #     ipady=0,  # 組件内部上下間距;
            #     padx=0,  # 組件外部左右間距;
            #     pady=0,  # 組件外部上下間距;
            #     sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            # )

            # 定義變量 inputValidationpath 爲 tk.StringVar() 類型，在定義的時候，設置其參數 value 爲某一個值，這個值就是預設的默認值，或者使用 .set 屬性也可以設置其值。
            self.inputValidationpath = tk.StringVar(value=self.default_inputValidation_path)
            # self.inputValidationpath.set(self.default_inputValidation_path)
            # 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
            # 在插入單行文本輸入框 Entry 控件的時候，使用參數 textvariable 指向變量 inputValidationpath，即可指定單行文本輸入框 Entry 控件的預設值。
            # 創建驗證集樣本輸入單行文本框（tkinter.Entry）組件;
            self.Entry_inputValidation_path = tk.Entry(
                master=self.initializer_Window,
                # font=("Arial", 14),
                textvariable=self.inputValidationpath,
                state="disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
            )
            # self.Entry_inputValidation_path.grid(
            #     row=6,  # 橫向行號;
            #     rowspan=1,  # 縱向跨行合并縱向行數目;
            #     column=2,  # 縱向列號;
            #     columnspan=1,  # 橫向跨列合并橫向列數目;
            #     ipadx=0,  # 組件内部左右間距;
            #     ipady=0,  # 組件内部上下間距;
            #     padx=0,  # 組件外部左右間距;
            #     pady=0,  # 組件外部上下間距;
            #     sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            # )

            # 創建訓練集樣本加載按鈕（tkinter.Button）組件;
            self.Button_inputValidation_path = tk.Button(
                master=self.initializer_Window,
                text="Input Validation",
                # image=img_1,
                compound="center",
                cursor="hand2",
                state="disabled",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.click_Button_inputValidation_path  # 指定按鈕控件被單擊後執行的函數;
            )
            # self.Button_inputValidation_path.grid(
            #     row=6,  # 橫向行號;
            #     rowspan=1,  # 縱向跨行合并縱向行數目;
            #     column=3,  # 縱向列號;
            #     columnspan=1,  # 橫向跨列合并橫向列數目;
            #     ipadx=0,  # 組件内部左右間距;
            #     ipady=0,  # 組件内部上下間距;
            #     padx=0,  # 組件外部左右間距;
            #     pady=0,  # 組件外部上下間距;
            #     sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            # )

            # 創建用於表格（tabel）中文本識別的 Google tesseract 參數（tesseract config）輸入框提示標簽（tkinter.Label）組件;
            self.Label_tabel_tesseract_config = tk.Label(
                master=self.initializer_Window,
                text='Tabel Config: ',
                # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
                # font=('Arial', 12),
                # width=30,  # 注意，標簽 width 的單位為「字符」個數;
                # height=2  # 注意，標簽 height 的單位為「字符」個數;
            )
            self.Label_tabel_tesseract_config.grid(
                row=5,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 定義變量 inputTabelTesseractConfig 爲 tk.StringVar() 類型，在定義的時候，設置其參數 value 爲某一個值，這個值就是預設的默認值，或者使用 .set 屬性也可以設置其值。
            self.inputTabelTesseractConfig = tk.StringVar(value=self.default_input_tabel_tesseract_config)
            # self.inputTabelTesseractConfig.set(self.default_input_tabel_tesseract_config)
            # 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
            # 在插入單行文本輸入框 Entry 控件的時候，使用參數 textvariable 指向變量 inputTabelTesseractConfig，即可指定單行文本輸入框 Entry 控件的預設值。
            # 創建訓練集樣本輸入單行文本框（tkinter.Entry）組件;
            self.Entry_tabel_tesseract_config = tk.Entry(
                master=self.initializer_Window,
                # font=("Arial", 14),
                textvariable=self.inputTabelTesseractConfig,
                state="normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
            )
            # 將單行文本框（tkinter.Entry）組件插入到窗體介面;
            self.Entry_tabel_tesseract_config.grid(
                row=5,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=2,  # 縱向列號;
                columnspan=2,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建用於測量尺（Measuring Ruler）中文本識別的 Google tesseract 參數（tesseract config）輸入框提示標簽（tkinter.Label）組件;
            self.Label_measuringRuler_tesseract_config = tk.Label(
                master=self.initializer_Window,
                text='Measuring Config: ',
                # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
                # font=('Arial', 12),
                # width=30,  # 注意，標簽 width 的單位為「字符」個數;
                # height=2  # 注意，標簽 height 的單位為「字符」個數;
            )
            self.Label_measuringRuler_tesseract_config.grid(
                row=6,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 定義變量 inputMeasuringRulerTesseractConfig 爲 tk.StringVar() 類型，在定義的時候，設置其參數 value 爲某一個值，這個值就是預設的默認值，或者使用 .set 屬性也可以設置其值。
            self.inputMeasuringRulerTesseractConfig = tk.StringVar(value=self.default_input_measuringRuler_tesseract_config)
            # self.inputMeasuringRulerTesseractConfig.set(self.default_input_measuringRuler_tesseract_config)
            # 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
            # 在插入單行文本輸入框 Entry 控件的時候，使用參數 textvariable 指向變量 inputMeasuringRulerTesseractConfig，即可指定單行文本輸入框 Entry 控件的預設值。
            # 創建驗證集樣本輸入單行文本框（tkinter.Entry）組件;
            self.Entry_measuringRuler_tesseract_config = tk.Entry(
                master=self.initializer_Window,
                # font=("Arial", 14),
                textvariable=self.inputMeasuringRulerTesseractConfig,
                state="normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
            )
            self.Entry_measuringRuler_tesseract_config.grid(
                row=6,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=2,  # 縱向列號;
                columnspan=2,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建測試集樣本輸入框提示標簽（tkinter.Label）組件;
            self.Label_inputTest_path = tk.Label(
                master=self.initializer_Window,
                text='Input test: ',
                # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
                # font=('Arial', 12),
                # width=30,  # 注意，標簽 width 的單位為「字符」個數;
                # height=2  # 注意，標簽 height 的單位為「字符」個數;
            )
            self.Label_inputTest_path.grid(
                row=7,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 定義變量 inputTestpath 爲 tk.StringVar() 類型，在定義的時候，設置其參數 value 爲某一個值，這個值就是預設的默認值，或者使用 .set 屬性也可以設置其值。
            self.inputTestpath = tk.StringVar(value=self.default_inputTest_path)
            # self.inputTestpath.set(self.default_inputTest_path)
            # 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
            # 在插入單行文本輸入框 Entry 控件的時候，使用參數 textvariable 指向變量 inputTestpath，即可指定單行文本輸入框 Entry 控件的預設值。
            # 創建測試集樣本輸入單行文本框（tkinter.Entry）組件;
            self.Entry_inputTest_path = tk.Entry(
                master=self.initializer_Window,
                # font=("Arial", 14),
                textvariable=self.inputTestpath,
                state="normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
            )
            self.Entry_inputTest_path.grid(
                row=7,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=2,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建訓練集樣本加載按鈕（tkinter.Button）組件;
            self.Button_inputTest_path = tk.Button(
                master=self.initializer_Window,
                text="Input Test",
                # image=img_1,
                compound="center",
                cursor="hand2",
                state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.click_Button_inputTest_path  # 指定按鈕控件被單擊後執行的函數;
            )
            self.Button_inputTest_path.grid(
                row=7,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=3,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建啓動訓練程式按鈕（tkinter.Button）組件;
            self.Button_start_and_stop_Train = tk.Button(
                master=self.initializer_Window,
                text="Start Train",
                # image=img_1,
                compound="center",
                cursor="hand2",
                state="disabled",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.click_Button_start_and_stop_Train  # 指定按鈕控件被單擊後執行的函數;
            )
            self.Button_start_and_stop_Train.grid(
                row=8,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建啓動或中止運行按鈕（tkinter.Button）組件;
            self.Button_start_and_stop_Test = tk.Button(
                master=self.initializer_Window,
                text="Start test",
                # image=img_1,
                compound="center",
                cursor="hand2",
                state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.click_Button_start_and_stop_Test  # 指定按鈕控件被單擊後執行的函數;
            )
            self.Button_start_and_stop_Test.grid(
                row=8,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=2,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建啓動或中止運行按鈕（tkinter.Button）組件;
            self.Button_shut_down = tk.Button(
                master=self.initializer_Window,
                text="Shut down",
                # image=img_1,
                compound="center",
                cursor="hand2",
                state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                command=self.click_Button_shut_down  # 指定按鈕控件被單擊後執行的函數;
            )
            self.Button_shut_down.grid(
                row=8,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=3,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建運行狀態提示標簽（tkinter.Label）組件;
            self.Label_State = tk.Label(
                master=self.initializer_Window,
                text='Stand by',  # 'Label: running state.', '悟空，您好.',
                # anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
                # justify='center'  # 定義對齊方式，可取值：'left', 'right', 'center'，預設值爲：'center' ;
                # bg='#ffffff',  # 背景色，bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
                # fg="#ffffff",  # 前景色;
                # font=('Arial', 12),
                # relief='flat',  # 邊框樣式，可取值：'flat', 'sunken', 'raised', 'groove', 'ridge'，預設值爲：'flat' ;
                # bd=1.0,  # 邊框寬度值;
                # wraplength=0,  # 設置標簽文本爲多少行顯示，預設值爲：0 ;
                # width=30,  # 注意，標簽 width 的單位為「字符」個數;
                # height=2  # 注意，標簽 height 的單位為「字符」個數;
            )
            self.Label_State.grid(
                row=9,  # 橫向行號;
                rowspan=5,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=4,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky="ew",  # 設置控件位於單元格的方位 None，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建展示運算結果的多行文本輸入框（tkinter.Text）組件;
            self.Text_display_result = tk.Text(
                master=self.initializer_Window,
                exportselection=True,  # 表示被選中的文本是否可以被複製到剪切板，預設值爲：True，若取：False 值，則表示不允許複製;
                undo=False,  # 表示 .Text 組件是否允許「撤銷」功能，預設值爲：False，若取：True 值，則表示允許「撤銷」功能;
                # autoseparators=True,  # 表示執行撤銷操作時是否自動插入一個「分隔符」（其作用是用於分隔操作記錄），預設值爲：True ;
                width=20,  # 標簽 width 的單位爲「字符」個數;，例如：width=13 表示設置爲 13 個字符的寬度，int(int(self.screenwidth)*0.4),
                height=4,  # 標簽 height 的單位爲「字符」個數;，例如：height=3 表示設置爲 3 個字符的高度，int(int(self.screenheight)*0.4),
                # anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
                # justify='center'  # 定義對齊方式，可取值：'left', 'right', 'center'，預設值爲：'center' ;
                # bg='#ffffff',  # 背景色，bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
                # fg="#000000",  # 前景色;
                font=('Arial', 12),
                # relief='flat',  # 邊框樣式，可取值：'flat', 'sunken', 'raised', 'groove', 'ridge'，預設值爲：'flat' ;
                # bd=1.0,  # 邊框寬度值;
                # highlightcolor='green',  # 設置文本框點擊後的邊框顔色;
                # highlightthickness=1.0,  # 設置文本框點擊後的邊框寬度值;
                # insertbackground='black',  # 設置插入光標的顔色，預設值爲： BLACK ;
                # insertborderwidth=0,  # 設置插入光標的邊框寬度，預設值爲：0 ;
                # insertofftime,  # 控制光標的閃爍頻率（滅的狀態）;
                # insertontime,  # 控制光標的閃爍頻率（亮的狀態）;
                # selectbackground,  # 指定被選中文本的背景顔色，預設由系統自動判斷;
                # selectborderwidth=0,  # 指定被選中文本的邊框寬度，預設值爲：0 ;
                # selectforeground,  # 指定被選中文本的字體顔色，預設由系統自動判斷;
                # setgrid=False,  # 用於確定是否啓用網格控制，預設值爲： False ;
                # spacing1=0,  # 指定 .Text 組件文本塊中，每一行與上方的空白間隔（忽略自動換行），預設值爲：0 ;
                # spacing2=0,  # 指定 .Text 組件文本塊中，自動換行的各行間的空白間隔（忽略自動換行），預設值爲：0 ;
                # spacing3=0,  # 指定 .Text 組件文本塊中，每一行與下方的空白間隔（忽略自動換行），預設值爲：0 ;
                # tabs='8c',  # 定制參數：Tag 所描述的文本塊中 Tab 鍵的功能，預設值爲：'8c' 表示 8 個字符寬度，比如 tabs=('1c', '2c', '8c') 表示前 3 個 Tab 寬度分別爲：1厘米，2厘米，8厘米;
                wrap=None,  # 該參數用來設置，當一行文本的長度超過 width 選項設定的寬度時，是否自動換行，取：None 值表示不自動換行，取：'char' 值表示按字符自動換行，取：'word' 值表示按單詞自動換行;
                # xscrollcommand,  # 該參數與滾動條（Scrollbar）組件相關聯，表示沿水平方向左右滑動;
                # yscrollcommand,  # 該參數與滾動條（Scrollbar）組件相關聯，表示沿垂直方向上下滑動;
                state='normal'  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作;
            )
            # 將多行文本輸入框（tkinter.Text）組件插入窗體介面中;
            self.Text_display_result.grid(
                row=14,  # 橫向行號;
                rowspan=5,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=4,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky="ewsn",  # 設置控件位於單元格的方位 None，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )
            # # 將任何按鍵都綁定到 break 功能，以使多行輸入文本框（tkinter.Text）組件中的内容設置爲只讀，除了「Ctrl」+「c」和「Shift」+「↑」+「↓」+「←」+「→」鍵，從而不鎖定文本複製的功能;
            # def ctrlEvent(event):
            #     if (12==event.state and event.keysym=='c') or (event.keysym=='Up') or (event.keysym=='Down') or (event.keysym=='Left') or (event.keysym=='Right'):
            #         return
            #     else:
            #         return "break"
            self.Text_display_result.bind("<Key>", lambda e: self.ctrlEvent(e))
            # 刪除多行文本輸入框中的内容;
            # self.Text_display_result.delete(
            #     "1.0",  # 參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始刪除;
            #     "end"  # 參數爲 "end" 表示刪除直至最後一個字符，即清空輸入框;
            # )
            # 設置多行文本輸入框 Text 控件的預設值;
            # self.Text_display_result.insert(
            #     "1.0",  # 參數 "1.0" 表示從第一行第一列開始插入，參數 "insert" 表示在當前光標位置處插入一個字符串，參數 "end" 表示在末尾位置處追加寫入一個字符串;
            #     str("a1a2a3a4a5a6a7a8a9a10a11a12a13a14a15a16a17a18a19a20a21" + "\n" + "b1b2b3b4b5b6b7b8b9b10b11b12b13b14b15b16b17b18b19b20b21" + "\n" + "c1c2c3c4c5c6c7c8c9c10c11c12c13c14c15c16c17c18c19c20c21" + "\n" + "d1d2d3d4d5d6d7d8d9d10d11d12d13d14d15d16d17d18d19d20d21" + "\n" + "e1e2e3e4e5e6e7e8e9e10e11e12e13e14e15e16e17e18e19e20e21" + "\n" + "f1f2f3f4f5f6f7f8f9f10f11f12f13f14f15f16f17f18f19f20f21")
            # )
            # self.Text_display_result.see("end"),  # 表示將 .Text 組件中聚焦在文本末行，即顯示末尾;
            # 讀取文本框輸入的内容;
            # Text_display_result_value = self.Text_display_result.get(
            #     "0.0",  # 表示讀取多行文本輸入框 .Text 控件中的全部值，如果設定參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始讀取;
            #     "end"  # 表示讀取至多行文本輸入框 .Text 控件中全部值的最後一個字符爲止;
            # )
            # Text_display_result_value = str(Text_display_result_value)
            # # Text_display_result_value = str(Text_display_result_value).replace('\\', '/').replace('\n', '')
            # print(Text_display_result_value)

            # # 創建滾動條（tkinter.Scrollbar）組件;
            # self.Y_Scrollbar_Text_display_result = tk.Scrollbar(
            #     master=self.Text_display_result,  # self.initializer_Window,
            #     orient='vertical'  # 'vertical' 表示設置滾動條垂直滾動，'horizontal' 表示設置滾動條橫向水平滾動;
            # )
            # # self.Y_Scrollbar_Text_display_result.grid(
            # #     row=1,  # 橫向行號;
            # #     rowspan=1,  # 縱向跨行合并縱向行數目;
            # #     column=1,  # 縱向列號;
            # #     columnspan=1,  # 橫向跨列合并橫向列數目;
            # #     ipadx=0,  # 組件内部左右間距;
            # #     ipady=0,  # 組件内部上下間距;
            # #     padx=0,  # 組件外部左右間距;
            # #     pady=0,  # 組件外部上下間距;
            # #     sticky="e",  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            # # )
            # # 將滾動條（tkinter.Scrollbar）組件插入窗體介面中;
            # self.Y_Scrollbar_Text_display_result.pack(
            #     anchor="e",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
            #     side="right",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
            #     fill="y",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
            #     expand=1  # 設置允許控件在橫向、縱向拉伸;
            # )
            # # 創建滾動條（tkinter.Scrollbar）組件;
            # self.X_Scrollbar_Text_display_result = tk.Scrollbar(
            #     master=self.Text_display_result,  # self.initializer_Window,
            #     orient='horizontal'  # 'vertical' 表示設置滾動條垂直滾動，'horizontal' 表示設置滾動條橫向水平滾動;
            # )
            # # self.X_Scrollbar_Text_display_result.grid(
            # #     row=1,  # 橫向行號;
            # #     rowspan=1,  # 縱向跨行合并縱向行數目;
            # #     column=1,  # 縱向列號;
            # #     columnspan=1,  # 橫向跨列合并橫向列數目;
            # #     ipadx=0,  # 組件内部左右間距;
            # #     ipady=0,  # 組件内部上下間距;
            # #     padx=0,  # 組件外部左右間距;
            # #     pady=0,  # 組件外部上下間距;
            # #     sticky="s",  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            # # )
            # # 將滾動條（tkinter.Scrollbar）組件插入窗體介面中;
            # self.X_Scrollbar_Text_display_result.pack(
            #     anchor="s",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
            #     side="bottom",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
            #     fill="x",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
            #     expand=1  # 設置允許控件在橫向、縱向拉伸;
            # )
            # # 關聯多行文本輸入框（tkinter.Text）組件和滾動條（tkinter.Scrollbar）組件;
            # self.Y_Scrollbar_Text_display_result.config(command=self.Text_display_result.yview)
            # self.Text_display_result.config(yscrollcommand=self.Y_Scrollbar_Text_display_result.set)
            # self.X_Scrollbar_Text_display_result.config(command=self.Text_display_result.xview)
            # self.Text_display_result.config(xscrollcommand=self.X_Scrollbar_Text_display_result.set)

            # 創建用於展示處理樣本的標簽框架（tkinter.LabelFrame）組件;
            self.LabelFrame_display_sample = tk.LabelFrame(
                master=self.initializer_Window,
                text="Sample display",
                # bg="#ffffff",  # 參數：bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色;
                borderwidth=1.0
            )
            # 將標簽框架（tkinter.LabelFrame）組件插入窗體介面中;
            self.LabelFrame_display_sample.grid(
                row=1,  # 橫向行號;
                rowspan=18,  # 縱向跨行合并縱向行數目;
                column=6,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # 創建運行狀態提示標簽（tkinter.Label）組件;
            self.Label_display_sample = tk.Label(
                master=self.LabelFrame_display_sample,  # master=self.initializer_Window,
                text='Input file',  # '悟空，您好.',
                # bg='#ffffff',  # 背景色，bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
                # fg="#ffffff",  # 前景色;
                # font=('Arial', 12),
                # relief='flat',  # 邊框樣式，可取值：'flat', 'sunken', 'raised', 'groove', 'ridge'，預設值爲：'flat' ;
                # bd=1.0,  # 邊框寬度值;
                # justify='center'  # 定義對齊方式，可取值：'left', 'right', 'center'，預設值爲：'center' ;
                # anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
                # wraplength=0,  # 設置標簽文本爲多少行顯示，預設值爲：0 ;
                # width=30,  # 注意，標簽 width 的單位為「字符」個數;
                # height=2  # 注意，標簽 height 的單位為「字符」個數;
            )
            # 將標簽（tkinter.Label）組件插入到標簽框架（tkinter.LabelFrame）組件中;
            self.Label_display_sample.grid(
                row=1,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )
            # self.Label_display_sample['text'] = "./test.png"

            # 創建處理樣本展示畫布（tkinter.Canvas）控件，並在畫布中插入自定義圖片;
            self.Canvas_display_sample = tk.Canvas(
                master=self.LabelFrame_display_sample,  # master=self.initializer_Window,
                width=int(int(self.screenwidth)*0.41),
                height=int(int(self.screenheight)*0.55),
                # anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
                # bg='#ffffff',  # 背景色，bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
                # fg="#000000",  # 前景色;
                # font=('Arial', 12),
                # relief='flat',  # 邊框樣式，可取值：'flat', 'sunken', 'raised', 'groove', 'ridge'，預設值爲：'flat' ;
                # bd=1.0,  # 邊框寬度值;
                # highlightcolor='green',  # 設置文本框點擊後的邊框顔色;
                # highlightthickness=1.0,  # 設置文本框點擊後的邊框寬度值;
            )
            # 將畫布（tkinter.Canvas）控件插入到標簽框架（tkinter.LabelFrame）組件中;
            self.Canvas_display_sample.grid(
                row=2,  # 橫向行號;
                rowspan=1,  # 縱向跨行合并縱向行數目;
                column=1,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky=None,  # 設置控件位於單元格的方位，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )
            # self.image_sample = []
            # self.image_sample = tk.PhotoImage(file="./test.png")
            # imgFile = Image.open("./test.png").resize((int(int(self.screenwidth)*0.42), int(int(self.screenheight)*0.55)))  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.Image.open() 函數打開圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;
            # self.image_sample = ImageTk.PhotoImage(imgFile)  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.ImageTk.PhotoImage() 函數讀取圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;
            # imgFile.close()
            # 清除自定義畫布組件中已經繪製的指定圖片;
            # self.Canvas_display_sample.delete("all")
            # self.Canvas_display_sample.delete(tag="one")
            # self.Canvas_display_sample.create_image(
            #     0,
            #     0,
            #     anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
            #     image=self.image_sample,
            #     # fill="red",
            #     tag="one"
            # )

            # 創建窗體佈局隔離缐條標簽（tkinter.Label）組件;
            self.Label_Isolation = tk.Label(
                master=self.initializer_Window,
                text='|',
                # bg='#000000',  # 背景色，bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
                # fg="#ffffff",  # 前景色;
                # font=('Arial', 12),
                # relief='flat',  # 邊框樣式，可取值：'flat', 'sunken', 'raised', 'groove', 'ridge'，預設值爲：'flat' ;
                # bd=1.0,  # 邊框寬度值;
                # justify='center'  # 定義對齊方式，可取值：'left', 'right', 'center'，預設值爲：'center' ;
                # anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
                # wraplength=0,  # 設置標簽文本爲多少行顯示，預設值爲：0 ;
                # width=1,  # int(int(self.screenwidth)*0.4),  # 注意，標簽 width 的單位為「字符」個數;
                # height=1  # int(int(self.screenheight)*0.4)  # 注意，標簽 height 的單位為「字符」個數;
            )
            # 將標簽（tkinter.Label）組件插入窗體介面中;
            self.Label_Isolation.grid(
                row=2,  # 橫向行號;
                rowspan=16,  # 縱向跨行合并縱向行數目;
                column=5,  # 縱向列號;
                columnspan=1,  # 橫向跨列合并橫向列數目;
                ipadx=0,  # 組件内部左右間距;
                ipady=0,  # 組件内部上下間距;
                padx=0,  # 組件外部左右間距;
                pady=0,  # 組件外部上下間距;
                sticky="sn",  # 設置控件位於單元格的方位 None，參數：sticky 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」表示東西南北;
            )

            # def on_closing():
            #     # 使用消息提示框控件給出溫馨提示;
            #     # tk_messagebox.showinfo(
            #     #     title="溫馨提示",
            #     #     message="窗口關閉事件被觸發：WM_DELETE_WINDOW"
            #     # )
            #     # # 使用消息問詢框控件做確認動作;
            #     # if tk_messagebox.askokcancel("Quit", "Do you want to quit?"):
            #     #     self.initializer_Window.quit()  # 關閉窗口，可以從窗口小部件取值;
            #     #     # self.initializer_Window.destroy()  # 關閉窗口，不能再從窗口小部件取值;
            #     self.initializer_Window.quit()  # 關閉窗口，可以從窗口小部件取值;
            #     # self.initializer_Window.destroy()  # 關閉窗口，不能再從窗口小部件取值;
            #     # self.initializer_Window.iconify()  # 窗口最小化;
            #     # self.initializer_Window.maxsize()  # 窗口最大化;
            #     return None

            self.initializer_Window.protocol("WM_DELETE_WINDOW", self.on_closing)  # 監聽捕捉窗口關閉事件，並綁定觸發執行的回調函數;

            # # 主窗口循環顯示;
            # self.initializer_Window.mainloop()
            # # 注意，loop 是循環的意思，該行代碼會讓窗口（window）不斷地刷新，如果沒有 .mainloop() ，就會是一個靜態的窗口（window），所有的窗口對象 tk.TK() 都必須有 .mainloop() 函數;
        else:
            print("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + ",initializerWindow=None")
            # sys.stdout.write("\n")  # 輸出換行;
            # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + ",initializerWindow=None")  # 將字符串輸出寫到操作系統控制臺;
            # sys.stdout.write("\n")  # 輸出換行;
            # print("參數錯誤" + "\n" + "傳入的窗體變量無法識別 ( initializerWindow = None ).")
            # self.Label_State['text'] = "參數錯誤." + "\n" + "傳入的窗體變量無法識別 ( initializerWindow = None )."
            sys.exit(1)  # 中止當前進程，退出當前程序;

    # 預設的可能被推入子進程執行功能的函數，可以在類實例化的時候輸入參數修改;
    def temp_default_doFunction(self, arguments):
        return arguments

    # 自定義封裝的函數check_json_format(raw_msg)用於判斷是否為JSON格式的字符串;
    def check_json_format(self, raw_msg):
        """
        用於判斷一個字符串是否符合 JSON 格式
        :param self:
        :return:
        """
        if isinstance(raw_msg, str):  # 首先判斷傳入的參數是否為一個字符串，如果不是直接返回false值
            try:
                json.loads(raw_msg)  # , encoding='utf-8'
                return True
            except ValueError:
                return False
        else:
            return False

    # 遞歸清空指定目錄（文件夾）下的所有内容（不包括這個文件夾），使用 Python 原生的標準 os 模組;
    def clear_Directory(self, dir_path):
        # os.chdir(dir_path)  # 改變當前工作目錄到指定的路徑;
        list_dir = os.listdir(dir_path)
        if len(list_dir) > 0:
            for f in list_dir:
                if os.path.isfile(dir_path + "\\%s" % f):
                    os.remove(dir_path + "\\%s" % f)
                else:
                    list_dir_2 = os.listdir(dir_path + "\\%s" % f)
                    if len(list_dir_2) > 0:
                        clear_Directory(dir_path + "\\%s" % f)

        list_dir = os.listdir(dir_path)
        if len(list_dir) > 0:
            for f in list_dir:
                if os.path.isfile(dir_path + "\\%s" % f):
                    os.remove(dir_path + "\\%s" % f)
                else:
                    list_dir_2 = os.listdir(dir_path + "\\%s" % f)
                    if len(list_dir_2) == 0:
                        os.rmdir(dir_path + "\\%s" % f)

        return list_dir

    # 格式化文檔大小輸出形式;
    def formatByte(self, number):
        for(scale.label) in [(1024*1024*1024, "GB"), (1024*1024, "MB"), (1024, "KB")]:
            if number >= scale:
                return "%.2f %s" % (number*1.0/scale, lable)
            elif number == 1:
                return "1 字節"
            else:
                # 小於 1 字節;
                byte = "%.2f" % (number or 0)
        return str(byte[:-3] if byte.endswith(".00") else byte) + " 字節"

    # # 自定義函數，只能在 Windows 系統使用，判斷某個文檔是否被其它進程占用;
    # def win_file_is_Used(self, file_name):
    #     try:
    #         vHandle = win32file.CreateFile(file_name, win32file.GENERIC_READ, 0, None, win32file.OPEN_EXISTING, win32file.FILE_ATTRIBUTE_NORMAL, None)
    #         return int(vHandle) == win32file.INVALID_HANDLE_VALUE
    #     except:
    #         return True
    #     finally:
    #         try:
    #             win32file.CloseHandle(vHandle)
    #         except:
    #             pass

    def Path_Conversion(self, input_Path_String, time_sleep):

        # if self.is_Concurrent == "0" or self.is_Concurrent == 0:
        #     # global self.Error_Log

        # global self.Error_Log
        self.Error_Log = []

        # global file_Array
        file_Array = []

        # input_Path_String = input_Path_String.replace('/', r'\\')
        if os.path.exists(input_Path_String):

            if pathlib.Path(input_Path_String).is_dir():

                items_1 = os.listdir(input_Path_String)
                # print(items_1)
                # for item in items_1:
                #     print(item)
                #     tk_messagebox.showinfo(
                #         title="溫馨提示 input_Path_String",
                #         message=str(item)
                #     )

                for i in range(0, len(items_1)):

                    if os.path.exists(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/')) and os.path.isfile(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/')):

                        # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
                        if not (os.access(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), os.W_OK)):
                            try:
                                # 修改文檔權限 mode:777 任何人可讀寫;
                                os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                                # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                                # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                                # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                                # os.chmod(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
                                # stat.S_IXOTH:  其他用戶有執行權0o001
                                # stat.S_IWOTH:  其他用戶有寫許可權0o002
                                # stat.S_IROTH:  其他用戶有讀許可權0o004
                                # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
                                # stat.S_IXGRP:  組用戶有執行許可權0o010
                                # stat.S_IWGRP:  組用戶有寫許可權0o020
                                # stat.S_IRGRP:  組用戶有讀許可權0o040
                                # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
                                # stat.S_IXUSR:  擁有者具有執行許可權0o100
                                # stat.S_IWUSR:  擁有者具有寫許可權0o200
                                # stat.S_IRUSR:  擁有者具有讀許可權0o400
                                # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
                                # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
                                # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
                                # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
                                # stat.S_IREAD:  windows下設為唯讀
                                # stat.S_IWRITE: windows下取消唯讀
                            except OSError as error:
                                if self.is_Concurrent == "0" or self.is_Concurrent == 0:
                                    sys.stdout.write("\n")  # 輸出換行;
                                    sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                                    sys.stdout.write("\n")  # 輸出換行;
                                    # print(error)
                                    # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/')} : {error}')
                                    # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                                    self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
                                self.Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))
                                # break
                                continue

                        file_Array.append(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))

                    else:
                        if self.is_Concurrent == "0" or self.is_Concurrent == 0:
                            sys.stdout.write("\n")  # 輸出換行;
                            sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
                            sys.stdout.write("\n")  # 輸出換行;
                            # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + " ]" + "\n" + "不存在或者不是檔.")
                            self.Label_State['text'] = "運行錯誤." + "\n" + "檔:" + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + " ]" + "\n" + "不存在或者不是檔."
                        self.Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))
                        # break
                        continue

                    if self.is_Concurrent == "0" or self.is_Concurrent == 0:
                        self.Label_State['text'] = "Parsed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/')

                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Parsed," + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
                    # print("Parsed," + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))

            elif os.path.isfile(input_Path_String):

                # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                # print(input_Path_String)

                # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
                if not (os.access(input_Path_String, os.R_OK) and os.access(input_Path_String, os.W_OK)):
                    try:
                        # 修改文檔權限 mode:777 任何人可讀寫;
                        os.chmod(input_Path_String, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                        # os.chmod(input_Path_String, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                        # os.chmod(input_Path_String, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                        # os.chmod(input_Path_String, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                        # os.chmod(input_Path_String, stat.S_IWOTH)  # 可被其它用戶寫入;
                        # stat.S_IXOTH:  其他用戶有執行權0o001
                        # stat.S_IWOTH:  其他用戶有寫許可權0o002
                        # stat.S_IROTH:  其他用戶有讀許可權0o004
                        # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
                        # stat.S_IXGRP:  組用戶有執行許可權0o010
                        # stat.S_IWGRP:  組用戶有寫許可權0o020
                        # stat.S_IRGRP:  組用戶有讀許可權0o040
                        # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
                        # stat.S_IXUSR:  擁有者具有執行許可權0o100
                        # stat.S_IWUSR:  擁有者具有寫許可權0o200
                        # stat.S_IRUSR:  擁有者具有讀許可權0o400
                        # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
                        # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
                        # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
                        # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
                        # stat.S_IREAD:  windows下設為唯讀
                        # stat.S_IWRITE: windows下取消唯讀
                    except OSError as error:
                        if self.is_Concurrent == "0" or self.is_Concurrent == 0:
                            sys.stdout.write("\n")  # 輸出換行;
                            sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String) + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            sys.stdout.write("\n")  # 輸出換行;
                            # print(f'Error: {input_Path_String} : {error}')
                            # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + input_Path_String + " ]" + "\n" + "無法修改為可讀可寫權限.")
                            self.Label_State['text'] = "運行錯誤." + "\n" + "檔:" + "\n" + "[ " + input_Path_String + " ]" + "\n" + "無法修改為可讀可寫權限."
                        self.Error_Log.append(input_Path_String)
                        return [file_Array, self.Error_Log, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))]  # None

                file_Array.append(input_Path_String)

                if self.is_Concurrent == "0" or self.is_Concurrent == 0:
                    self.Label_State['text'] = "Parsed [ 1 ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(input_Path_String)

                # sys.stdout.write("\n")  # 輸出換行;
                # sys.stdout.write("Parsed,1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String))  # 將字符串輸出寫到操作系統控制臺;
                # print("Parsed,1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String))

            else:
                if self.is_Concurrent == "0" or self.is_Concurrent == 0:
                    sys.stdout.write("\n")  # 輸出換行;
                    sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String))  # 將字符串輸出寫到操作系統控制臺;
                    sys.stdout.write("\n")  # 輸出換行;
                    # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + input_Path_String + " ]" + "\n" + "類型無法識別.")
                    self.Label_State['text'] = "運行錯誤." + "\n" + "檔:" + "\n" + "[ " + input_Path_String + " ]" + "\n" + "類型無法識別."
                self.Error_Log.append(input_Path_String)
                # return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_Path_String

        else:
            if self.is_Concurrent == "0" or self.is_Concurrent == 0:
                sys.stdout.write("\n")  # 輸出換行;
                sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String))  # 將字符串輸出寫到操作系統控制臺;
                sys.stdout.write("\n")  # 輸出換行;
                # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + input_Path_String + " ]" + "\n" + "不存在.")
                self.Label_State['text'] = "運行錯誤." + "\n" + "檔:" + "\n" + "[ " + input_Path_String + " ]" + "\n" + "不存在."
            self.Error_Log.append(input_Path_String)
            # return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_Path_String

        # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
        if self.is_Concurrent == "0" or self.is_Concurrent == 0:
            # print("Path parse complete [ " + str(len(file_Array)) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + input_Path_String + " ].")
            self.Label_State['text'] = "Path parse complete [ " + str(len(file_Array)) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + input_Path_String + " ]."
            # self.Label_State['text'] = "Stand by"

        # # 使用消息提示框控件給出溫馨提示;
        # tk_messagebox.showinfo(
        #     title = "溫馨提示",
        #     message = str("Path parse complete [ " + str(len(file_Array)) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + input_Path_String + " ].")
        # )

        # print(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")))
        # print(file_Array)
        # print(self.Error_Log)
        return [file_Array, self.Error_Log, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))]  # None

    def Input_and_Output(self, is_window, screenwidth, screenheight, is_Concurrent, is_storage_position, is_storage_type, input_Train_Path, input_Train_File_Array, input_Test_Path, input_Test_File_Array, do_Function, output_Test_Path, output_Test_File_Array, output_Test_URL, time_sleep, outqueue_from_task_to_host, outqueue_from_host_to_task, is_Runing, file_Data, result_Data, complete_Number, Error_Log, Label_State, Text_display_result, image_sample, Canvas_display_sample, Label_display_sample):

        # global self.is_Runing
        if is_Concurrent == "Multi-Threading":
            self.is_Runing = True
            if outqueue_from_host_to_task:
                # def Queue_update(outqueue_from_host_to_task):
                #     # outqueue_from_task_to_host = outqueue[0]
                #     # outqueue_from_host_to_task = outqueue[1]
                #     try:
                #         if outqueue_from_host_to_task.empty():
                #             self.initializer_Window.after(250, Queue_update, outqueue_from_host_to_task)
                #             pass
                #         if not outqueue_from_host_to_task.empty():
                #             msg = outqueue_from_host_to_task.get(
                #                 block=False,
                #                 timeout=None
                #             )
                #             if msg[0] == "is_Runing_True":
                #                 self.is_Runing = True
                #                 self.initializer_Window.after(10, Queue_update, outqueue_from_host_to_task)
                #                 # pass
                #                 # return return_value
                #             elif msg[0] == "is_Runing_False":
                #                 self.is_Runing = False
                #                 self.initializer_Window.after(10, Queue_update, outqueue_from_host_to_task)
                #                 # pass
                #                 # return return_value
                #         # else:
                #         #     # By not calling self.initializer_Window.after here, we allow update to
                #         #     # truly end
                #         #     self.initializer_Window.after(10, Queue_update, outqueue_from_host_to_task)
                #         #     pass
                #     except queue.Empty:
                #         self.initializer_Window.after(10, self.Queue_update, outqueue_from_host_to_task)
                # self.initializer_Window.after(10, Queue_update, outqueue_from_host_to_task)
                if not outqueue_from_host_to_task.empty():
                    msg = outqueue_from_host_to_task.get(
                        block=False,
                        timeout=None
                    )
                    if msg[0] == "is_Runing_True":
                        self.is_Runing = True
                        # self.initializer_Window.after(10, self.Queue_update, outqueue_from_host_to_task)
                        # pass
                        # return return_value
                    elif msg[0] == "is_Runing_False":
                        self.is_Runing = False
                        # self.initializer_Window.after(10, self.Queue_update, outqueue_from_host_to_task)
                        # pass
                        # return return_value

        # global self.file_Data
        # global self.file_Data_bytes
        # global self.file_Data_len
        self.file_Data = ""
        # self.file_Data_bytes = self.file_Data.encode("utf-8")
        # self.file_Data = self.file_Data_bytes.decode("utf-8")
        # self.file_Data = str(self.file_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
        # self.file_Data_len = len(bytes(self.file_Data, "utf-8"))

        # global self.result_Data
        self.result_Data = ""
        # self.result_Data_bytes = self.result_Data.encode("utf-8")
        # self.result_Data = self.result_Data_bytes.decode("utf-8")
        # self.result_Data = str(self.result_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
        # self.result_Data_len = len(bytes(self.result_Data, "utf-8"))

        # global self.image_sample
        self.image_sample = []

        # global self.complete_Number
        self.complete_Number = int(0)

        # global self.Error_Log
        self.Error_Log = []

        if len(input_Test_File_Array) == 0:
            log_Error = [
                "Error",
                str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                str(os.path.normpath(str(input_Test_Path))).replace('\\', '/')
            ]

            if is_Concurrent == "0" or is_Concurrent == 0:
                # sys.stdout.write("\n")  # 輸出換行;
                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_Path))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
                # sys.stdout.write("\n")  # 輸出換行;
                print("運行錯誤." + "\n" + "路徑: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_Path))).replace('\\', '/') + " ]" + "\n" + "找不到可處理檔.")
                self.Label_State['text'] = "運行錯誤." + "\n" + "路徑: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_Path))).replace('\\', '/') + " ]" + "\n" + "找不到可處理檔."

            if is_Concurrent == "Multi-Threading":
                if outqueue_from_task_to_host:
                    outqueue_from_task_to_host.put(
                        log_Wrong,
                        block=False,
                        timeout=None
                    )

            self.Error_Log.append(str(os.path.normpath(str(input_Test_Path))).replace('\\', '/'))
            return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_Path))).replace('\\', '/')

        if is_Concurrent == "0" or is_Concurrent == 0:
            # global self.image_sample
            self.image_sample = []
            self.Canvas_display_sample.delete("all")
            # self.Canvas_display_sample.create_image(
            #     0,
            #     0,
            #     anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
            #     image=self.image_sample,
            #     # fill="red",
            #     tag="one"
            # )
            # self.Canvas_display_sample.delete(tag="one")
            self.Label_display_sample['text'] = "Input file"

        if is_Concurrent == "Multi-Threading":
            log_Message = [
                "image_sample_delete",
                ""
            ]
            if outqueue_from_task_to_host:
                outqueue_from_task_to_host.put(
                    log_Message,
                    block=False,
                    timeout=None
                )

        # input_Test_Path = Entry_inputTest_path.get()  # 讀取文本框輸入的内容;
        # input_Test_Path = str(input_Test_Path).replace('\\', '/')
        # output_Test_Path = Entry_outputTest_path.get()  # 讀取文本框輸入的内容;
        # output_Test_Path = str(output_Test_Path).replace('\\', '/')

        # 檢查並創建運算結果輸出目錄;
        if is_storage_position == "Database_and_Disk" or is_storage_position == "Disk":

            if len(output_Test_Path) > 0:

                self.output_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')

                # 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
                if os.path.exists(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')).is_dir():
                    # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
                    if not (os.access(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), os.W_OK)):
                        try:
                            # 修改文檔權限 mode:777 任何人可讀寫;
                            os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                            # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                            # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                            # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                            # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
                            # stat.S_IXOTH:  其他用戶有執行權0o001
                            # stat.S_IWOTH:  其他用戶有寫許可權0o002
                            # stat.S_IROTH:  其他用戶有讀許可權0o004
                            # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
                            # stat.S_IXGRP:  組用戶有執行許可權0o010
                            # stat.S_IWGRP:  組用戶有寫許可權0o020
                            # stat.S_IRGRP:  組用戶有讀許可權0o040
                            # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
                            # stat.S_IXUSR:  擁有者具有執行許可權0o100
                            # stat.S_IWUSR:  擁有者具有寫許可權0o200
                            # stat.S_IRUSR:  擁有者具有讀許可權0o400

                            # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
                            # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
                            # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
                            # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
                            # stat.S_IREAD:  windows下設為唯讀
                            # stat.S_IWRITE: windows下取消唯讀
                        except OSError as error:
                            if is_Concurrent == "0" or is_Concurrent == 0:
                                sys.stdout.write("\n")  # 輸出換行;
                                sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                                sys.stdout.write("\n")  # 輸出換行;
                                # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')} : {error}')
                                # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                                self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
                            if is_Concurrent == "Multi-Threading":
                                if outqueue_from_task_to_host:
                                    outqueue_from_task_to_host.put(
                                        [
                                            "Error",
                                            str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                            str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'),
                                            str(error)
                                        ],
                                        block=False,
                                        timeout=None
                                    )
                            self.Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'))
                            return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')
                else:
                    try:
                        # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
                        # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
                        os.makedirs(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'), mode=0o777, exist_ok=True)
                    except FileExistsError as error:
                        # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
                        if is_Concurrent == "0" or is_Concurrent == 0:
                            sys.stdout.write("\n")  # 輸出換行;
                            sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            sys.stdout.write("\n")  # 輸出換行;
                            # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')} : {error}')
                            # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                            self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
                        if is_Concurrent == "Multi-Threading":
                            if outqueue_from_task_to_host:
                                outqueue_from_task_to_host.put(
                                    [
                                        "Error",
                                        str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                        str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'),
                                        str(error)
                                    ],
                                    block=False,
                                    timeout=None
                                )
                        self.Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'))
                        return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')

                if not (os.path.exists(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')).is_dir()):
                    if is_Concurrent == "0" or is_Concurrent == 0:
                        sys.stdout.write("\n")  # 輸出換行;
                        sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
                        sys.stdout.write("\n")  # 輸出換行;
                        # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')} : {error}')
                        # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                        self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
                    if is_Concurrent == "Multi-Threading":
                        if outqueue_from_task_to_host:
                            outqueue_from_task_to_host.put(
                                [
                                    "Error",
                                    str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                    str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')
                                ],
                                block=False,
                                timeout=None
                            )
                    self.Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'))
                    return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')

        # input_Test_Path = input_Test_Path.replace('/', r'\\')
        # print(input_Test_File_Array)
        # for item in input_Test_File_Array:
        #     print(item)
        #     tk_messagebox.showinfo(
        #         title="溫馨提示 input_Test_Path",
        #         message=str(item)
        #     )

        for i in range(0, len(input_Test_File_Array)):

            if is_Concurrent == "Multi-Threading":
                if outqueue_from_host_to_task:
                    # def Queue_update(outqueue_from_host_to_task):
                    #     # outqueue_from_task_to_host = outqueue[0]
                    #     # outqueue_from_host_to_task = outqueue[1]
                    #     try:
                    #         if outqueue_from_host_to_task.empty():
                    #             self.initializer_Window.after(10, Queue_update, outqueue_from_host_to_task)
                    #             pass
                    #         if not outqueue_from_host_to_task.empty():
                    #             msg = outqueue_from_host_to_task.get(
                    #                 block=False,
                    #                 timeout=None
                    #             )
                    #             if msg[0] == "is_Runing_True":
                    #                 self.is_Runing = True
                    #                 self.initializer_Window.after(10, Queue_update, outqueue_from_host_to_task)
                    #                 # pass
                    #                 # return return_value
                    #             elif msg[0] == "is_Runing_False":
                    #                 self.is_Runing = False
                    #                 self.initializer_Window.after(10, Queue_update, outqueue_from_host_to_task)
                    #                 # pass
                    #                 # return return_value
                    #         # else:
                    #         #     # By not calling self.initializer_Window.after here, we allow update to
                    #         #     # truly end
                    #         #     self.initializer_Window.after(10, Queue_update, outqueue_from_host_to_task)
                    #         #     pass
                    #     except queue.Empty:
                    #         self.initializer_Window.after(10, Queue_update, outqueue_from_host_to_task)
                    # self.initializer_Window.after(10, Queue_update, outqueue_from_host_to_task)
                    if not outqueue_from_host_to_task.empty():
                        msg = outqueue_from_host_to_task.get(
                            block=False,
                            timeout=None
                        )
                        if msg[0] == "is_Runing_True":
                            self.is_Runing = True
                            # self.initializer_Window.after(250, self.Queue_update, outqueue_from_host_to_task)
                            # pass
                            # return return_value
                        elif msg[0] == "is_Runing_False":
                            self.is_Runing = False
                            # self.initializer_Window.after(250, self.Queue_update, outqueue_from_host_to_task)
                            # pass
                            # return return_value

            if not self.is_Runing:

                if is_Concurrent == "Multi-Threading":
                    if outqueue_from_task_to_host:
                        if len(self.Error_Log) > 0:
                            outqueue_from_task_to_host.put(
                                [
                                    "Discontinue",
                                    "Error",
                                    "[" + str(len(self.Error_Log)) + "]",
                                    str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                    str(','.join(self.Error_Log))
                                ],
                                block=False,
                                timeout=None
                            )
                        else:
                            outqueue_from_task_to_host.put(
                                [
                                    "Discontinue",
                                    "Complete",
                                    "[" + str(self.complete_Number) + "]",
                                    str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                    input_Test_Path,
                                    output_Test_Path
                                ],
                                block=False,
                                timeout=None
                            )

                # continue
                # break
                if len(self.Error_Log) > 0:
                    return "Error," + str(len(self.Error_Log)) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(','.join(self.Error_Log))
                else:
                    return "Complete," + str(self.complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_Test_Path + "," + output_Test_Path  # None

            # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
            # print(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))

            if is_Concurrent == "0" or is_Concurrent == 0:
                self.Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
            if is_Concurrent == "Multi-Threading":
                if outqueue_from_task_to_host:
                    outqueue_from_task_to_host.put(
                        [
                            "Runing",
                            str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
                        ],
                        block=False,
                        timeout=None
                    )

            self.file_Data = ""
            self.result_Data = ""

            if is_Concurrent == "0" or is_Concurrent == 0:
                self.image_sample = []
                # 清除自定義畫布組件中已經繪製的指定圖片;
                self.Canvas_display_sample.delete("all")
                # self.Canvas_display_sample.delete(tag="one")
                # self.Canvas_display_sample.create_image(
                #     0,
                #     0,
                #     anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
                #     image=self.image_sample,
                #     # fill="red",
                #     tag="one"
                # )
                self.Label_display_sample['text'] = "Input file"
            if is_Concurrent == "Multi-Threading":
                log_Message = [
                    "image_sample_delete",
                    ""
                ]
                if outqueue_from_task_to_host:
                    outqueue_from_task_to_host.put(
                        log_Message,
                        block=False,
                        timeout=None
                    )

            if os.path.exists(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')) and os.path.isfile(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')):

                # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
                if not (os.access(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), os.W_OK)):
                    try:
                        # 修改文檔權限 mode:777 任何人可讀寫;
                        os.chmod(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                        # os.chmod(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                        # os.chmod(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                        # os.chmod(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                        # os.chmod(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
                        # stat.S_IXOTH:  其他用戶有執行權0o001
                        # stat.S_IWOTH:  其他用戶有寫許可權0o002
                        # stat.S_IROTH:  其他用戶有讀許可權0o004
                        # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
                        # stat.S_IXGRP:  組用戶有執行許可權0o010
                        # stat.S_IWGRP:  組用戶有寫許可權0o020
                        # stat.S_IRGRP:  組用戶有讀許可權0o040
                        # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
                        # stat.S_IXUSR:  擁有者具有執行許可權0o100
                        # stat.S_IWUSR:  擁有者具有寫許可權0o200
                        # stat.S_IRUSR:  擁有者具有讀許可權0o400
                        # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
                        # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
                        # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
                        # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
                        # stat.S_IREAD:  windows下設為唯讀
                        # stat.S_IWRITE: windows下取消唯讀
                    except OSError as error:
                        if is_Concurrent == "0" or is_Concurrent == 0:
                            sys.stdout.write("\n")
                            sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            sys.stdout.write("\n")
                            # print(error)
                            # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
                            # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                            self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
                        if is_Concurrent == "Multi-Threading":
                            if outqueue_from_task_to_host:
                                outqueue_from_task_to_host.put(
                                    [
                                        "Wrong",
                                        str(int(i) + 1),
                                        str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                        str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                        str(error)
                                    ],
                                    block=False,
                                    timeout=None
                                )
                        self.Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                        # break
                        continue

                fd = open(
                    str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                    mode="rb+",  # 讀取文本字符：mode="r"，讀取二進制字節<class 'bytes'>：mode="rb+"
                    buffering=-1,
                    # encoding="utf-8",
                    errors=None,
                    newline=None,
                    closefd=True,
                    opener=None
                )
                try:
                    self.file_Data = fd.read()
                    # self.file_Data = fd.read().decode("utf-8")
                    # data_Bytes = self.file_Data.encode("utf-8")
                    # self.file_Data = str(data_Bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
                    # fd.write(data_Bytes)
                except FileNotFoundError:
                    if is_Concurrent == "0" or is_Concurrent == 0:
                        sys.stdout.write("\n")
                        sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                        sys.stdout.write("\n")
                        # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在.")
                        self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在."
                    if is_Concurrent == "Multi-Threading":
                        if outqueue_from_task_to_host:
                            outqueue_from_task_to_host.put(
                                [
                                    "Wrong",
                                    str(int(i) + 1),
                                    str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                    str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                    str(error)
                                ],
                                block=False,
                                timeout=None
                            )
                    self.Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                    # break
                    continue
                # except PersmissionError:
                #     if is_Concurrent == "0" or is_Concurrent == 0:
                #         sys.stdout.write("\n")
                #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                #         sys.stdout.write("\n")
                #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無操作權限.")
                #         self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無操作權限."
                #     if is_Concurrent == "Multi-Threading":
                #         if outqueue_from_task_to_host:
                #             outqueue_from_task_to_host.put(
                #                 [
                #                     "Wrong",
                #                     str(int(i) + 1),
                #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                #                     str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                #                     str(error)
                #                 ],
                #                 block=False,
                #                 timeout=None
                #             )
                #     self.Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                #     # break
                #     continue
                except Exception as error:
                    if("[WinError 32]" in str(error)):
                        if is_Concurrent == "0" or is_Concurrent == 0:
                            sys.stdout.write("\n")
                            sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            sys.stdout.write("\n")
                            # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據.")
                            # print(error)
                            # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
                            self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據."
                            print("延時等待 " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ].")
                            # self.Label_State['text'] = "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
                            self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據." + "\n" + "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
                        if is_Concurrent == "Multi-Threading":
                            if outqueue_from_task_to_host:
                                outqueue_from_task_to_host.put(
                                    [
                                        "Wrong",
                                        str(int(i) + 1),
                                        str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                        str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                        str(error)
                                    ],
                                    block=False,
                                    timeout=None
                                )
                        time.sleep(time_sleep)  # 用於讀取文檔時延遲參數，以防文檔被占用錯誤，單位（秒）;
                        try:
                            self.file_Data = fd.read()
                            # self.file_Data = fd.read().decode("utf-8")
                            # data_Bytes = self.file_Data.encode("utf-8")
                            # fd.write(data_Bytes)
                        except OSError as error:
                            if is_Concurrent == "0" or is_Concurrent == 0:
                                sys.stdout.write("\n")
                                sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                                sys.stdout.write("\n")
                                # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據.")
                                # print(error)
                                # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
                                self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據."
                            if is_Concurrent == "Multi-Threading":
                                if outqueue_from_task_to_host:
                                    outqueue_from_task_to_host.put(
                                        [
                                            "Wrong",
                                            str(int(i) + 1),
                                            str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                            str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                            str(error)
                                        ],
                                        block=False,
                                        timeout=None
                                    )
                            self.Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                            # break
                            continue
                    else:
                        if is_Concurrent == "0" or is_Concurrent == 0:
                            sys.stdout.write("\n")
                            sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            sys.stdout.write("\n")
                            # print(error)
                            # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
                            self.Label_State['text'] = "讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "發生錯誤." + "\n" + str(error)
                        if is_Concurrent == "Multi-Threading":
                            if outqueue_from_task_to_host:
                                outqueue_from_task_to_host.put(
                                    [
                                        "Wrong",
                                        str(int(i) + 1),
                                        str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                        str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                        str(error)
                                    ],
                                    block=False,
                                    timeout=None
                                )
                        self.Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                        # break
                        continue
                finally:
                    fd.close()
                # 注：可以用try/finally語句來確保最後能關閉檔，不能把open語句放在try塊裡，因為當打開檔出現異常時，檔物件file_object無法執行close()方法;

                # 讀取用於在畫布 canvas 組件中展示的樣本圖片;
                try:
                    # self.image_sample = tk.PhotoImage(file=str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))  # 使用 Python 原生的 tkinter 包中的 tkinter.PhotoImage() 函數讀取圖片檔;
                    imgFile = Image.open(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')).resize((int(int(screenwidth)*0.42), int(int(screenheight)*0.55)))  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.Image.open() 函數打開圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;
                    self.image_sample = ImageTk.PhotoImage(imgFile)  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.ImageTk.PhotoImage() 函數讀取圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;

                    if is_Concurrent == "0" or is_Concurrent == 0:
                        self.Label_display_sample['text'] = str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
                        # 在自定義畫布組件中展示讀入的圖片樣本;
                        # self.Canvas_display_sample.delete("all")
                        # self.Canvas_display_sample.delete(tag="one")
                        self.Canvas_display_sample.create_image(
                            0,
                            0,
                            anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
                            image=self.image_sample,
                            # fill="red",
                            tag="one"
                        )

                    if is_Concurrent == "Multi-Threading":
                        if outqueue_from_task_to_host:
                            outqueue_from_task_to_host.put(
                                [
                                    "image_sample",
                                    str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                    self.image_sample
                                ],
                                block=False,
                                timeout=None
                            )

                except FileNotFoundError:
                    if is_Concurrent == "0" or is_Concurrent == 0:
                        sys.stdout.write("\n")
                        sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                        sys.stdout.write("\n")
                        # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在.")
                        self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在."
                    if is_Concurrent == "Multi-Threading":
                        if outqueue_from_task_to_host:
                            outqueue_from_task_to_host.put(
                                [
                                    "Wrong",
                                    str(int(i) + 1),
                                    str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                    str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                    str(error)
                                ],
                                block=False,
                                timeout=None
                            )
                    # self.Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                    # break
                    # continue
                # except PersmissionError:
                #     if is_Concurrent == "0" or is_Concurrent == 0:
                #         sys.stdout.write("\n")
                #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                #         sys.stdout.write("\n")
                #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無操作權限.")
                #         self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無操作權限."
                #     if is_Concurrent == "Multi-Threading":
                #         if outqueue_from_task_to_host:
                #             outqueue_from_task_to_host.put(
                #                 [
                #                     "Wrong",
                #                     str(int(i) + 1),
                #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                #                     str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                #                     str(error)
                #                 ],
                #                 block=False,
                #                 timeout=None
                #             )
                #     # self.Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                #     # break
                #     # continue
                except Exception as error:
                    if("[WinError 32]" in str(error)):
                        if is_Concurrent == "0" or is_Concurrent == 0:
                            sys.stdout.write("\n")
                            sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            sys.stdout.write("\n")
                            # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據.")
                            # print(error)
                            # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
                            self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據."
                            print("延時等待 " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ].")
                            # self.Label_State['text'] = "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
                            self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據." + "\n" + "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
                        if is_Concurrent == "Multi-Threading":
                            if outqueue_from_task_to_host:
                                outqueue_from_task_to_host.put(
                                    [
                                        "Wrong",
                                        str(int(i) + 1),
                                        str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                        str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                        str(error)
                                    ],
                                    block=False,
                                    timeout=None
                                )
                        time.sleep(time_sleep)  # 用於讀取文檔時延遲參數，以防文檔被占用錯誤，單位（秒）;
                        try:
                            imgFile = Image.open(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')).resize((int(int(screenwidth)*0.42), int(int(screenheight)*0.55)))  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.Image.open() 函數打開圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;
                            self.image_sample = ImageTk.PhotoImage(imgFile)  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.ImageTk.PhotoImage() 函數讀取圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;

                            if is_Concurrent == "0" or is_Concurrent == 0:
                                self.Label_display_sample['text'] = str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
                                # 在自定義畫布組件中展示讀入的圖片樣本;
                                self.Canvas_display_sample.delete("all")
                                # self.Canvas_display_sample.delete(tag="one")
                                self.Canvas_display_sample.create_image(
                                    0,
                                    0,
                                    anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
                                    image=self.image_sample,
                                    # fill="red",
                                    tag="one"
                                )

                            if is_Concurrent == "Multi-Threading":
                                if outqueue_from_task_to_host:
                                    outqueue_from_task_to_host.put(
                                        [
                                            "image_sample",
                                            str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                            self.image_sample
                                        ],
                                        block=False,
                                        timeout=None
                                    )

                        except OSError as error:
                            if is_Concurrent == "0" or is_Concurrent == 0:
                                sys.stdout.write("\n")
                                sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                                sys.stdout.write("\n")
                                # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據.")
                                # print(error)
                                # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
                                self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據."
                            if is_Concurrent == "Multi-Threading":
                                if outqueue_from_task_to_host:
                                    outqueue_from_task_to_host.put(
                                        [
                                            "Wrong",
                                            str(int(i) + 1),
                                            str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                            str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                            str(error)
                                        ],
                                        block=False,
                                        timeout=None
                                    )
                            # self.Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                            # break
                            # continue
                    else:
                        if is_Concurrent == "0" or is_Concurrent == 0:
                            sys.stdout.write("\n")
                            sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            sys.stdout.write("\n")
                            # print(error)
                            # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
                            self.Label_State['text'] = "讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "發生錯誤." + "\n" + str(error)
                        if is_Concurrent == "Multi-Threading":
                            if outqueue_from_task_to_host:
                                outqueue_from_task_to_host.put(
                                    [
                                        "Wrong",
                                        str(int(i) + 1),
                                        str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                        str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                        str(error)
                                    ],
                                    block=False,
                                    timeout=None
                                )
                        # self.Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                        # break
                        # continue
                finally:
                    imgFile.close()
                # 注：可以用try/finally語句來確保最後能關閉檔，不能把open語句放在try塊裡，因為當打開檔出現異常時，檔物件file_object無法執行close()方法;


                # # 使用 str("").encode("utf-8") 方法，將字符串（str）對象轉換為 "utf-8" 編碼的二進制字節流（<bytes>）類型數據;
                # self.file_Data_bytes = file_Data.encode("utf-8")
                # self.file_Data = self.file_Data_bytes.decode("utf-8")
                # self.file_Data_len = len(bytes(self.file_Data, "utf-8"))


                # # 讀取到輸入數據之後，刪除文檔;
                # try:
                #     os.remove(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))  # os.unlink(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')) 刪除文檔;
                #     # os.listdir(input_dir)  # 刷新目錄内容列表
                #     # print(os.listdir(input_dir))
                # except Exception as error:
                #     if is_Concurrent == "0" or is_Concurrent == 0:
                #         print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除.")
                #         print(f'Wrong: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
                #         self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除."
                #     if is_Concurrent == "Multi-Threading":
                #         if outqueue_from_task_to_host:
                #             outqueue_from_task_to_host.put(
                #                 [
                #                     "Wrong",
                #                     str(int(i) + 1),
                #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                #                     str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                #                     str(error)
                #                 ],
                #                 block=False,
                #                 timeout=None
                #             )
                #     if("[WinError 32]" in str(error)):
                #         if is_Concurrent == "0" or is_Concurrent == 0:
                #             print("延時等待 " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試刪除檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ].")
                #             # self.Label_State['text'] = "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試刪除檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
                #             self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除." + "\n" + "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試刪除檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
                #         if is_Concurrent == "Multi-Threading":
                #             if outqueue_from_task_to_host:
                #                 outqueue_from_task_to_host.put(
                #                     [
                #                         "Wrong",
                #                         str(int(i) + 1),
                #                         str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                #                         str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                #                         str(error)
                #                     ],
                #                     block=False,
                #                     timeout=None
                #                 )
                #         time.sleep(time_sleep)  # 用於刪除文檔時延遲參數，以防文檔被占用錯誤，單位（秒）;
                #         try:
                #             # os.unlink(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))  # 刪除文檔;
                #             os.remove(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                #             # os.listdir(input_dir)  # 刷新目錄内容列表
                #             # print(os.listdir(input_dir))
                #         except OSError as error:
                #             if is_Concurrent == "0" or is_Concurrent == 0:
                #                 print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除.")
                #                 print(error)
                #                 # print(f'Wrong: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
                #                 self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除."
                #             if is_Concurrent == "Multi-Threading":
                #                 if outqueue_from_task_to_host:
                #                     outqueue_from_task_to_host.put(
                #                         [
                #                             "Wrong",
                #                             str(int(i) + 1),
                #                             str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                #                             str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                #                             str(error)
                #                         ],
                #                         block=False,
                #                         timeout=None
                #                     )
                #             self.Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                #             # break
                #             continue
                #     # else:
                #     #     if is_Concurrent == "0" or is_Concurrent == 0:
                #     #         print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除.")
                #     #         print(error)
                #     #         # print(f'Wrong: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
                #     #         self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除."
                #     #     if is_Concurrent == "Multi-Threading":
                #     #         if outqueue_from_task_to_host:
                #     #             outqueue_from_task_to_host.put(
                #     #                 [
                #     #                     "Wrong",
                #     #                     str(int(i) + 1),
                #     #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                #     #                     str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                #     #                     str(error)
                #     #                 ],
                #     #                 block=False,
                #     #                 timeout=None
                #     #             )
                #     #     self.Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                #     #     # break
                #     #     continue


                # 在這裏插入具體的數據處理算法;
                result_Data_JSON = do_Function(self.file_Data)
                self.result_Data = result_Data_JSON

                # print(type(self.file_Data))  # <class 'bytes'>
                # self.result_Data = str(self.file_Data)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
                # print(type(self.result_Data))  # <class 'str'>

                # # String = json.dumps(JSON); JSON = json.loads(String);
                # # 使用自定義函數check_json_format(raw_msg)判斷讀取到的請求體表單"form"數據 request_form_value 是否為JSON格式的字符串;
                # if check_json_format(require_data_String):
                #     # 將讀取到的請求體表單"form"數據字符串轉換爲JSON對象;
                #     require_data_JSON = json.loads(require_data_String)  # , encoding='utf-8'
                # # print(require_data_JSON)
                # # print(typeof(require_data_JSON))

                # Client_say = ""
                # # 使用函數 isinstance(require_data_JSON, dict) 判斷傳入的參數 require_data_JSON 是否為 dict 字典（JSON）格式對象;
                # if isinstance(require_data_JSON, dict):
                #     # 使用 JSON.__contains__("key") 或 "key" in JSON 判断某个"key"是否在JSON中;
                #     if (require_data_JSON.__contains__("Client_say")):
                #         Client_say = require_data_JSON["Client_say"]

                # 將運算結果寫入用於展示結果的多行文本輸入框;
                if is_Concurrent == "0" or is_Concurrent == 0:

                    # self.Label_State['text'] = "Succeed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(input_Test_File_Array[i])
                    self.Label_State['text'] = "Succeed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')

                    # # 讀取多行文本輸入框中的内容;
                    # Text_display_result_value = self.Text_display_result.get(
                    #     "0.0",  # 表示讀取多行文本輸入框 .Text 控件中的全部值，如果設定參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始讀取;
                    #     "end"  # 表示讀取至多行文本輸入框 .Text 控件中全部值的最後一個字符爲止;
                    # )
                    # Text_display_result_value = str(Text_display_result_value)
                    # print(Text_display_result_value)

                    # # 刪除多行文本輸入框中的内容;
                    # self.Text_display_result.delete(
                    #     "1.0",  # 參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始刪除;
                    #     "end"  # 參數爲 "end" 表示刪除直至最後一個字符，即清空輸入框;
                    # )

                    # new_Text_display_result_value = Text_display_result_value + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Test_File_Array[i]) + "," + str(self.result_Data)

                    # new_Text_display_result_value = str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Test_File_Array[i]) + "," + str(self.result_Data) + "\n"
                    new_Text_display_result_value = str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n"
                    # print(new_Text_display_result_value)

                    # 將字符串寫入多行文本輸入框;
                    self.Text_display_result.insert(
                        "end",  # 參數 "1.0" 表示從第一行第一列開始插入，參數 "insert" 表示在當前光標位置處插入一個字符串，參數 "end" 表示在末尾位置處追加寫入一個字符串;
                        str(new_Text_display_result_value)
                    )

                    self.Text_display_result.see("end"),  # 表示將 .Text 組件中聚焦在文本末行，即顯示末尾;

                # 將運算結果寫入磁碟文檔;
                if is_storage_position == "Database_and_Disk" or is_storage_position == "Disk":

                    for j in range(0, len(output_Test_File_Array)):

                        if len(str(output_Test_File_Array[j])) > 0:

                            # self.output_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')

                            # # 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
                            # if os.path.exists(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')).is_dir():
                            #     # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
                            #     if not (os.access(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), os.W_OK)):
                            #         try:
                            #             # 修改文檔權限 mode:777 任何人可讀寫;
                            #             os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                            #             # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                            #             # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                            #             # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                            #             # os.chmod(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
                            #             # stat.S_IXOTH:  其他用戶有執行權0o001
                            #             # stat.S_IWOTH:  其他用戶有寫許可權0o002
                            #             # stat.S_IROTH:  其他用戶有讀許可權0o004
                            #             # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
                            #             # stat.S_IXGRP:  組用戶有執行許可權0o010
                            #             # stat.S_IWGRP:  組用戶有寫許可權0o020
                            #             # stat.S_IRGRP:  組用戶有讀許可權0o040
                            #             # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
                            #             # stat.S_IXUSR:  擁有者具有執行許可權0o100
                            #             # stat.S_IWUSR:  擁有者具有寫許可權0o200
                            #             # stat.S_IRUSR:  擁有者具有讀許可權0o400

                            #             # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
                            #             # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
                            #             # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
                            #             # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
                            #             # stat.S_IREAD:  windows下設為唯讀
                            #             # stat.S_IWRITE: windows下取消唯讀
                            #         except OSError as error:
                            #             if is_Concurrent == "0" or is_Concurrent == 0:
                            #                 sys.stdout.write("\n")  # 輸出換行;
                            #                 sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')) + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            #                 sys.stdout.write("\n")  # 輸出換行;
                            #                 # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')} : {error}')
                            #                 # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                            #                 self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
                            #             if is_Concurrent == "Multi-Threading":
                            #                 if outqueue_from_task_to_host:
                            #                     outqueue_from_task_to_host.put(
                            #                         [
                            #                             "Wrong",
                            #                             str(int(i) + 1),
                            #                             str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            #                             str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'),
                            #                             str(error)
                            #                         ],
                            #                         block=False,
                            #                         timeout=None
                            #                     )
                            #             self.Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'))
                            #             # break
                            #             continue
                            # else:
                            #     try:
                            #         # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
                            #         # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
                            #         os.makedirs(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'), mode=0o777, exist_ok=True)
                            #     except FileExistsError as error:
                            #         # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
                            #         if is_Concurrent == "0" or is_Concurrent == 0:
                            #             sys.stdout.write("\n")  # 輸出換行;
                            #             sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')) + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            #             sys.stdout.write("\n")  # 輸出換行;
                            #             # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')} : {error}')
                            #             # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                            #             self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
                            #         if is_Concurrent == "Multi-Threading":
                            #             if outqueue_from_task_to_host:
                            #                 outqueue_from_task_to_host.put(
                            #                     [
                            #                         "Wrong",
                            #                         str(int(i) + 1),
                            #                         str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            #                         str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'),
                            #                         str(error)
                            #                     ],
                            #                     block=False,
                            #                     timeout=None
                            #                 )
                            #         self.Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'))
                            #         # break
                            #         continue

                            # if not (os.path.exists(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')).is_dir()):
                            #     if is_Concurrent == "0" or is_Concurrent == 0:
                            #         sys.stdout.write("\n")  # 輸出換行;
                            #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')))  # 將字符串輸出寫到操作系統控制臺;
                            #         sys.stdout.write("\n")  # 輸出換行;
                            #         # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')} : {error}')
                            #         # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                            #         self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
                            #     if is_Concurrent == "Multi-Threading":
                            #         if outqueue_from_task_to_host:
                            #             outqueue_from_task_to_host.put(
                            #                 [
                            #                     "Wrong",
                            #                     str(int(i) + 1),
                            #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            #                     str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')
                            #                 ],
                            #                 block=False,
                            #                 timeout=None
                            #             )
                            #     self.Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'))
                            #     # break
                            #     continue


                            # 判斷文檔，是否已經存在且是否為文檔;
                            if os.path.exists(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')) and os.path.isfile(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')):
                                # print(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), "is a file 是一個文檔.")
                                # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
                                if not (os.access(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), os.W_OK)):
                                    try:
                                        # 修改文檔權限 mode:777 任何人可讀寫;
                                        os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                                        # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                                        # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                                        # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                                        # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
                                        # stat.S_IXOTH:  其他用戶有執行權0o001
                                        # stat.S_IWOTH:  其他用戶有寫許可權0o002
                                        # stat.S_IROTH:  其他用戶有讀許可權0o004
                                        # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
                                        # stat.S_IXGRP:  組用戶有執行許可權0o010
                                        # stat.S_IWGRP:  組用戶有寫許可權0o020
                                        # stat.S_IRGRP:  組用戶有讀許可權0o040
                                        # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
                                        # stat.S_IXUSR:  擁有者具有執行許可權0o100
                                        # stat.S_IWUSR:  擁有者具有寫許可權0o200
                                        # stat.S_IRUSR:  擁有者具有讀許可權0o400
                                        # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
                                        # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
                                        # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
                                        # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
                                        # stat.S_IREAD:  windows下設為唯讀
                                        # stat.S_IWRITE: windows下取消唯讀
                                    except OSError as error:
                                        if is_Concurrent == "0" or is_Concurrent == 0:
                                            sys.stdout.write("\n")
                                            sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                                            sys.stdout.write("\n")
                                            # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
                                            # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在但無法修改為可讀可寫權限.")
                                            self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在但無法修改為可讀可寫權限."
                                        if is_Concurrent == "Multi-Threading":
                                            if outqueue_from_task_to_host:
                                                outqueue_from_task_to_host.put(
                                                    [
                                                        "Wrong",
                                                        str(int(i) + 1),
                                                        str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                                        str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
                                                        str(error)
                                                    ],
                                                    block=False,
                                                    timeout=None
                                                )
                                        self.Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
                                        # break
                                        continue


                                # # 如果文檔已存在則從硬盤刪除，然後重新創建並寫入新值;
                                # try:
                                #     os.remove(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))  # 刪除文檔
                                # except OSError as error:
                                #     if is_Concurrent == "0" or is_Concurrent == 0:
                                #         sys.stdout.write("\n")
                                #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                                #         sys.stdout.write("\n")
                                #         # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
                                #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在且無法刪除，以重新創建更新數據.")
                                #         self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在且無法刪除，以重新創建更新數據."
                                #     if is_Concurrent == "Multi-Threading":
                                #         if outqueue_from_task_to_host:
                                #             outqueue_from_task_to_host.put(
                                #                 [
                                #                     "Wrong",
                                #                     str(int(i) + 1),
                                #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                #                     str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
                                #                     str(error)
                                #                 ],
                                #                 block=False,
                                #                 timeout=None
                                #             )
                                #     self.Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
                                #     # break
                                #     continue

                                # # 判斷用於接收傳值的媒介文檔，是否已經從硬盤刪除;
                                # if os.path.exists(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')) and os.path.isfile(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')):
                                #     if is_Concurrent == "0" or is_Concurrent == 0:
                                #         sys.stdout.write("\n")
                                #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
                                #         sys.stdout.write("\n")
                                #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在且無法刪除，以重新創建更新數據.")
                                #         self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在且無法刪除，以重新創建更新數據."
                                #     if is_Concurrent == "Multi-Threading":
                                #         if outqueue_from_task_to_host:
                                #             outqueue_from_task_to_host.put(
                                #                 [
                                #                     "Wrong",
                                #                     str(int(i) + 1),
                                #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                #                     str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')
                                #                 ],
                                #                 block=False,
                                #                 timeout=None
                                #             )
                                #     self.Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
                                #     # break
                                #     continue


                            # # 使用Python原生模組os判斷指定的用於輸出傳值的目錄或文檔是否存在，如果不存在，則創建目錄，並為所有者和組用戶提供讀、寫、執行權限，默認模式為 0o777;
                            # if os.path.exists(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')).is_dir():
                            #     # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
                            #     if not (os.access(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), os.R_OK) and os.access(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), os.W_OK)):
                            #         try:
                            #             # 修改文檔權限 mode:777 任何人可讀寫;
                            #             os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                            #             # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                            #             # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                            #             # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                            #             # os.chmod(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), stat.S_IWOTH)  # 可被其它用戶寫入;
                            #             # stat.S_IXOTH:  其他用戶有執行權0o001
                            #             # stat.S_IWOTH:  其他用戶有寫許可權0o002
                            #             # stat.S_IROTH:  其他用戶有讀許可權0o004
                            #             # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
                            #             # stat.S_IXGRP:  組用戶有執行許可權0o010
                            #             # stat.S_IWGRP:  組用戶有寫許可權0o020
                            #             # stat.S_IRGRP:  組用戶有讀許可權0o040
                            #             # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
                            #             # stat.S_IXUSR:  擁有者具有執行許可權0o100
                            #             # stat.S_IWUSR:  擁有者具有寫許可權0o200
                            #             # stat.S_IRUSR:  擁有者具有讀許可權0o400
                            #             # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
                            #             # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
                            #             # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
                            #             # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
                            #             # stat.S_IREAD:  windows下設為唯讀
                            #             # stat.S_IWRITE: windows下取消唯讀
                            #         except OSError as error:
                            #             if is_Concurrent == "0" or is_Concurrent == 0:
                            #                 sys.stdout.write("\n")
                            #                 sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            #                 sys.stdout.write("\n")
                            #                 # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
                            #                 # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                            #                 self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
                            #             if is_Concurrent == "Multi-Threading":
                            #                 if outqueue_from_task_to_host:
                            #                     outqueue_from_task_to_host.put(
                            #                         [
                            #                             "Wrong",
                            #                             str(int(i) + 1),
                            #                             str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            #                             str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
                            #                             str(error)
                            #                         ],
                            #                         block=False,
                            #                         timeout=None
                            #                     )
                            #             self.Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
                            #             # break
                            #             continue
                            # else:
                            #     try:
                            #         # os.chmod(os.getcwd(), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 修改文檔權限 mode:777 任何人可讀寫;
                            #         # exist_ok：是否在目錄存在時觸發異常。如果exist_ok為False（預設值），則在目標目錄已存在的情況下觸發FileExistsError異常；如果exist_ok為True，則在目標目錄已存在的情況下不會觸發FileExistsError異常;
                            #         os.makedirs(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'), mode=0o777, exist_ok=True)
                            #     except FileExistsError as error:
                            #         # 如果指定創建的目錄已經存在，則捕獲並抛出 FileExistsError 錯誤
                            #         if is_Concurrent == "0" or is_Concurrent == 0:
                            #             sys.stdout.write("\n")
                            #             sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            #             sys.stdout.write("\n")
                            #             # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
                            #             # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                            #             self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
                            #         if is_Concurrent == "Multi-Threading":
                            #             if outqueue_from_task_to_host:
                            #                 outqueue_from_task_to_host.put(
                            #                     [
                            #                         "Wrong",
                            #                         str(int(i) + 1),
                            #                         str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            #                         str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
                            #                         str(error)
                            #                     ],
                            #                     block=False,
                            #                     timeout=None
                            #                 )
                            #         self.Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
                            #         # break
                            #         continue

                            # if not (os.path.exists(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')).is_dir()):
                            #     if is_Concurrent == "0" or is_Concurrent == 0:
                            #         sys.stdout.write("\n")
                            #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
                            #         sys.stdout.write("\n")
                            #         # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
                            #         # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                            #         self.Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
                            #     if is_Concurrent == "Multi-Threading":
                            #         if outqueue_from_task_to_host:
                            #             outqueue_from_task_to_host.put(
                            #                 [
                            #                     "Wrong",
                            #                     str(int(i) + 1),
                            #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            #                     str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')
                            #                 ],
                            #                 block=False,
                            #                 timeout=None
                            #             )
                            #     self.Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
                            #     # break
                            #     continue


                            # 以可寫方式打開硬盤文檔，如果文檔不存在，則會自動創建一個文檔;
                            fd = open(
                                str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
                                mode="wb+",  # 寫入文本字符：mode="w"，寫入二進制字節<class 'bytes'>：mode="wb+"
                                buffering=-1,
                                # encoding="utf-8",
                                errors=None,
                                newline=None,
                                closefd=True,
                                opener=None
                            )
                            try:
                                fd.write(self.result_Data)
                                # self.result_Data_bytes = self.result_Data.encode("utf-8")
                                # self.result_Data_len = len(bytes(self.result_Data, "utf-8"))
                                # fd.write(self.result_Data_bytes)
                            except FileNotFoundError:
                                if is_Concurrent == "0" or is_Concurrent == 0:
                                    sys.stdout.write("\n")
                                    sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                                    sys.stdout.write("\n")
                                    # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
                                    # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "寫入失敗.")
                                    self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "寫入失敗."
                                if is_Concurrent == "Multi-Threading":
                                    if outqueue_from_task_to_host:
                                        outqueue_from_task_to_host.put(
                                            [
                                                "Wrong",
                                                str(int(i) + 1),
                                                str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                                str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
                                                str(error)
                                            ],
                                            block=False,
                                            timeout=None
                                        )
                                self.Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
                                # break
                                continue
                            # except PersmissionError:
                            #     if is_Concurrent == "0" or is_Concurrent == 0:
                            #         sys.stdout.write("\n")
                            #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            #         sys.stdout.write("\n")
                            #         # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
                            #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無操作權限.")
                            #         self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無操作權限."
                            #     if is_Concurrent == "Multi-Threading":
                            #         if outqueue_from_task_to_host:
                            #             outqueue_from_task_to_host.put(
                            #                 [
                            #                     "Wrong",
                            #                     str(int(i) + 1),
                            #                     str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            #                     str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'),
                            #                     str(error)
                            #                 ],
                            #                 block=False,
                            #                 timeout=None
                            #             )
                            #     self.Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
                            #     # break
                            #     continue
                            finally:
                                fd.close()
                            # 注：可以用try/finally語句來確保最後能關閉檔，不能把open語句放在try塊裡，因為當打開檔出現異常時，檔物件file_object無法執行close()方法;

                # if is_storage_position == "Database" or is_storage_position == "Database_and_Disk":

                self.complete_Number = self.complete_Number + int(1)  # 記錄處理成功的文檔個數;

                if is_Concurrent == "0" or is_Concurrent == 0:
                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Succeed," + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "," + str(self.result_Data))  # 將字符串輸出寫到操作系統控制臺;
                    # print("Succeed," + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "," + str(self.result_Data))  # 將字符串輸出寫到操作系統控制臺;
                    print("Succeed," + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))

                if is_Concurrent == "Multi-Threading":
                    if outqueue_from_task_to_host:
                        outqueue_from_task_to_host.put(
                            [
                                "Succeed",
                                str(int(i)+1),
                                str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                str(str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n"),
                                str("Succeed" + "\n" + str(int(i)+1) + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                            ],
                            block=False,
                            timeout=None
                        )

            else:

                if is_Concurrent == "0" or is_Concurrent == 0:
                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在或不是檔.")
                    self.Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在或不是檔."
                if is_Concurrent == "Multi-Threading":
                    if outqueue_from_task_to_host:
                        outqueue_from_task_to_host.put(
                            [
                                "Wrong",
                                str(int(i) + 1),
                                str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
                            ],
                            block=False,
                            timeout=None
                        )
                self.Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                # break
                continue


        # self.file_Data = ""
        # self.result_Data = ""
        # self.image_sample = []
        # 清除自定義畫布組件中已經繪製的指定圖片;
        # self.Canvas_display_sample.delete("all")
        # self.Canvas_display_sample.delete(tag="one")
        # self.Canvas_display_sample.create_image(
        #     0,
        #     0,
        #     anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
        #     image=self.image_sample,
        #     # fill="red",
        #     tag="one"
        # )
        # self.Label_display_sample['text'] = "input file"


        # if is_Concurrent == "0" or is_Concurrent == 0:
        #     # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
        #     self.Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + input_Test_Path + " ]." + "\n" + "Output: [ " + output_Test_Path + " ]." + "\n" + "complete [ " + str(self.complete_Number) + " ]."
        #     # self.Label_State['text'] = "Stand by"

        if is_Concurrent == "Multi-Threading":
            if outqueue_from_task_to_host:
                if len(self.Error_Log) > 0:
                    outqueue_from_task_to_host.put(
                        [
                            "Error",
                            "[" + str(len(self.Error_Log)) + "]",
                            str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            str(','.join(self.Error_Log))
                        ],
                        block=False,
                        timeout=None
                    )
                else:
                    outqueue_from_task_to_host.put(
                        [
                            "Complete",
                            "[" + str(self.complete_Number) + "]",
                            str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            input_Test_Path,
                            output_Test_Path
                        ],
                        block=False,
                        timeout=None
                    )

        # # 使用消息提示框控件給出溫馨提示;
        # tk_messagebox.showinfo(
        #     title = "溫馨提示",
        #     message = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + input_Test_Path + " ]." + "\n" + "Output: [ " + output_Test_Path + " ]." + "\n" + "complete [ " + str(self.complete_Number) + " ]."
        # )

        if len(self.Error_Log) > 0:
            return "Error,[" + str(len(self.Error_Log)) + "]," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(','.join(self.Error_Log))
        else:
            return "Complete,[" + str(self.complete_Number) + "]," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_Test_Path + "," + output_Test_Path  # None

    def Run_Input_and_Output_Function(self, Path_Conversion, Input_and_Output, is_window, screenwidth, screenheight, is_Concurrent, is_storage_position, is_storage_type, inputTrain_path, inputTrain_File_Array, inputTest_path, inputTest_File_Array, do_Function, outputTest_path, outputTest_File_Array, outputTest_URL, time_sleep, outqueue_from_task_to_host, outqueue_from_host_to_task, is_Runing, file_Data, result_Data, complete_Number, Error_Log, Label_State, Text_display_result, image_sample, Canvas_display_sample, Label_display_sample):

        try:
            # if not self.is_Runing:
            #     self.is_Runing = not self.is_Runing

            # self.complete_Number = int(0)
            # self.Error_Log = []
            # self.file_Data = ""
            # self.result_Data = ""
            # self.image_sample = []

            # # print(inputTrain_path)
            # if len(inputTrain_File_Array) == 0:
            #     if len(inputTrain_path) > 0:
            #         # inputTrain_File_Array = []
            #         inputTrain_File_Array = Path_Conversion(inputTrain_path, time_sleep)[0]

            # # print(inputValidation_path)
            # if len(inputValidation_File_Array) == 0:
            #     if len(inputValidation_path) > 0:
            #         # inputValidation_File_Array = []
            #         inputValidation_File_Array = Path_Conversion(inputValidation_path, time_sleep)[0]

            # # print(inputTest_path)
            # if len(inputTest_File_Array) == 0:
            #     if len(inputTest_path) > 0:
            #         # inputTest_File_Array = []
            #         inputTest_File_Array = Path_Conversion(inputTest_path, time_sleep)[0]

            # # print(outputTest_path)
            # if len(outputTest_File_Array) == 0:
            #     if len(outputTest_path) > 0:
            #         # # outputTest_File_Array = []
            #         # outputTest_File_Array = Path_Conversion(outputTest_path, time_sleep)[0]
            #         outputTest_File_Array = [outputTest_path]

            return_value = ""
            return_value = Input_and_Output(
                is_window,
                screenwidth,
                screenheight,
                is_Concurrent,
                is_storage_position,
                is_storage_type,
                inputTrain_path,
                inputTrain_File_Array,
                inputTest_path,
                inputTest_File_Array,
                do_Function,
                outputTest_path,
                outputTest_File_Array,
                outputTest_URL,
                time_sleep,
                outqueue_from_task_to_host,
                outqueue_from_host_to_task,
                is_Runing,
                file_Data,
                result_Data,
                complete_Number,
                Error_Log,
                Label_State,
                Text_display_result,
                image_sample,
                Canvas_display_sample,
                Label_display_sample
            )
            # print(return_value)

            # inputTrain_File_Array = []
            # inputValidation_File_Array = []
            # inputTest_File_Array = []
            # outputTest_File_Array = []

            # if self.is_Runing:
            #     self.is_Runing = not self.is_Runing

        except Exception as error:
            if is_Concurrent == "0" or is_Concurrent == 0:
                print(error)
            if is_Concurrent == "Multi-Threading":
                if outqueue_from_task_to_host:
                    outqueue_from_task_to_host.put(str(error))
        finally:
            # sys.exit(0)  # 中止當前進程，退出當前程序;
            return return_value
        # 注：可以用try/finally語句來確保最後能中止當前進程，退出當前程序;

    # 創建複選框（tkinter.Checkbutton）組件;
    def select_Checkbutton_storage_position(self):

        # global self.is_storage_position
        self.is_storage_position = ""
        if self.Checkbutton_storage_position_Database_Var.get() and self.Checkbutton_storage_position_Disk_Var.get():
            self.is_storage_position = str(self.Checkbutton_storage_position_Database['text']) + "_and_" + str(self.Checkbutton_storage_position_Disk['text'])
        elif self.Checkbutton_storage_position_Database_Var.get() and not self.Checkbutton_storage_position_Disk_Var.get():
            self.is_storage_position = str(self.Checkbutton_storage_position_Database['text'])
        elif not self.Checkbutton_storage_position_Database_Var.get() and self.Checkbutton_storage_position_Disk_Var.get():
            self.is_storage_position = str(self.Checkbutton_storage_position_Disk['text'])
        elif not self.Checkbutton_storage_position_Database_Var.get() and not self.Checkbutton_storage_position_Disk_Var.get():
            self.is_storage_position = ""
        else:
            print("參數錯誤." + "\n" + "判斷運算結果存儲在數據庫的複選框值:" + "\n" + str(self.Checkbutton_storage_position_Database['text']) + "\n" + "無法識別." + "\n" + "判斷運算結果存儲在磁碟文檔的複選框值:" + "\n" + str(self.Checkbutton_storage_position_Disk['text']) + "\n" + "無法識別.")

            # 使用消息提示框控件給出溫馨提示;
            tk_messagebox.showinfo(
                title = "溫馨提示",
                message = str("參數錯誤." + "\n" + "判斷運算結果存儲在數據庫的複選框值:" + "\n" + str(self.Checkbutton_storage_position_Database['text']) + "\n" + "無法識別." + "\n" + "判斷運算結果存儲在磁碟文檔的複選框值:" + "\n" + str(self.Checkbutton_storage_position_Disk['text']) + "\n" + "無法識別.")
            )

        # print("storage position:", self.is_storage_position)

        # global self.default_outputTest_path
        # global self.outputTest_path
        # global self.outputTestpath
        # global self.default_outputTest_URL
        # global self.outputTest_URL
        # global self.outputTestURL

        if len(str(self.Entry_outputTest_path.get())) > 0:
            self.outputTest_path = str(self.Entry_outputTest_path.get())  # 讀取結果輸出位置文本框輸入的内容;

        if len(str(self.Entry_outputTest_URL.get())) > 0:
            self.outputTest_URL = str(self.Entry_outputTest_URL.get())  # 讀取結果輸出位置文本框輸入的内容;

        if  len(self.is_storage_position) == 0:

            self.outputTest_path = ""
            self.outputTestpath.set(self.outputTest_path)
            self.Entry_outputTest_path['textvariable'] = self.outputTestpath

            # self.outputTest_URL = ""
            # self.outputTestURL.set(self.outputTest_URL)
            # self.Entry_outputTest_URL['textvariable'] = self.outputTestURL

            if len(str(self.Entry_outputTest_path.get())) > 0:
                if str(self.Entry_outputTest_path.get()).find(".", 0, int(len(str(self.Entry_outputTest_path.get()))-1)) != -1:

                    self.is_storage_type = str(str(self.Entry_outputTest_path.get()).split('.')[len(str(self.Entry_outputTest_path.get()).split('.'))-1])
                    # print("storage type:", self.is_storage_type)

                    if not (self.is_storage_type == "json" or self.is_storage_type == "csv" or self.is_storage_type == "txt" or self.is_storage_type == "xlsx"):
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get())  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(self.Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                        # Error_Log.append(str(self.Entry_outputTest_path.get()))
                        return self.is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get())

                    if self.is_storage_type == "json":
                        self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()
                        self.Radiobutton_storage_type_Excel.deselect()
                        self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    elif self.is_storage_type == "csv":
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()
                        self.Radiobutton_storage_type_Excel.deselect()
                        self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    elif self.is_storage_type == "txt":
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()
                        self.Radiobutton_storage_type_Excel.deselect()
                        self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    elif self.is_storage_type == "xlsx":
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()
                        self.Radiobutton_storage_type_txt.deselect()
                        self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                    elif len(self.is_storage_type) == 0:
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                    else:
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(self.Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                        # Error_Log.append(str(self.Entry_outputTest_path.get()))
                        return self.is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get())
                else:
                    self.is_storage_type = ""
                    self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(self.Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                    # Error_Log.append(str(self.Entry_outputTest_path.get()))
                    return self.is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get())
            else:
                self.is_storage_type = ""
                self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                # # sys.stdout.write("\n")  # 輸出換行;
                # # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                # # sys.stdout.write("\n")  # 輸出換行;
                # print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(self.Entry_outputTest_path.get()) + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                # # Error_Log.append(str(self.Entry_outputTest_path.get()))
                # return self.is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get())

        elif self.is_storage_position == "Database_and_Disk":

            if  len(self.outputTest_path) == 0:
                self.outputTestpath.set(self.default_outputTest_path)
                self.Entry_outputTest_path['textvariable'] = self.outputTestpath
            else:
                self.outputTestpath.set(self.outputTest_path)
                self.Entry_outputTest_path['textvariable'] = self.outputTestpath

            # if  len(self.outputTest_URL) == 0:
            #     self.outputTestURL.set(self.default_outputTest_URL)
            #     self.Entry_outputTest_URL['textvariable'] = self.outputTestURL
            # else:
            #     self.outputTestURL.set(self.outputTest_URL)
            #     self.Entry_outputTest_URL['textvariable'] = self.outputTestURL

            if len(str(self.Entry_outputTest_path.get())) > 0:
                if str(self.Entry_outputTest_path.get()).find(".", 0, int(len(str(self.Entry_outputTest_path.get()))-1)) != -1:

                    self.is_storage_type = str(str(self.Entry_outputTest_path.get()).split('.')[len(str(self.Entry_outputTest_path.get()).split('.'))-1])
                    # print("storage type:", self.is_storage_type)

                    if not (self.is_storage_type == "json" or self.is_storage_type == "csv" or self.is_storage_type == "txt" or self.is_storage_type == "xlsx"):
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(self.Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                        # Error_Log.append(str(self.Entry_outputTest_path.get()))
                        return self.is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get())

                    if self.is_storage_type == "json":
                        self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()
                        self.Radiobutton_storage_type_Excel.deselect()
                        self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    elif self.is_storage_type == "csv":
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()
                        self.Radiobutton_storage_type_Excel.deselect()
                        self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    elif self.is_storage_type == "txt":
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()
                        self.Radiobutton_storage_type_Excel.deselect()
                        self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    elif self.is_storage_type == "xlsx":
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()
                        self.Radiobutton_storage_type_txt.deselect()
                        self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                    elif len(self.is_storage_type) == 0:
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                    else:
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(self.Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                        # Error_Log.append(str(self.Entry_outputTest_path.get()))
                        return self.is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get())
                else:
                    self.is_storage_type = ""
                    self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(self.Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                    # Error_Log.append(str(self.Entry_outputTest_path.get()))
                    return self.is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get())
            else:
                self.is_storage_type = ""
                self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                # # sys.stdout.write("\n")  # 輸出換行;
                # # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                # # sys.stdout.write("\n")  # 輸出換行;
                # print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(self.Entry_outputTest_path.get()) + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                # # Error_Log.append(str(self.Entry_outputTest_path.get()))
                # return self.is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get())

        elif self.is_storage_position == "Database":

            self.outputTest_path = ""
            self.outputTestpath.set(self.outputTest_path)
            self.Entry_outputTest_path['textvariable'] = self.outputTestpath

            # if  len(self.outputTest_URL) == 0:
            #     self.outputTestURL.set(self.default_outputTest_URL)
            #     self.Entry_outputTest_URL['textvariable'] = self.outputTestURL
            # else:
            #     self.outputTestURL.set(self.outputTest_URL)
            #     self.Entry_outputTest_URL['textvariable'] = self.outputTestURL

        elif self.is_storage_position == "Disk":

            if  len(self.outputTest_path) == 0:
                self.outputTestpath.set(self.default_outputTest_path)
                self.Entry_outputTest_path['textvariable'] = self.outputTestpath
            else:
                self.outputTestpath.set(self.outputTest_path)
                self.Entry_outputTest_path['textvariable'] = self.outputTestpath

            # self.outputTest_URL = ""
            # self.outputTestURL.set(self.outputTest_URL)
            # self.Entry_outputTest_URL['textvariable'] = self.outputTestURL

            if len(str(self.Entry_outputTest_path.get())) > 0:
                if str(self.Entry_outputTest_path.get()).find(".", 0, int(len(str(self.Entry_outputTest_path.get()))-1)) != -1:

                    self.is_storage_type = str(str(self.Entry_outputTest_path.get()).split('.')[len(str(self.Entry_outputTest_path.get()).split('.'))-1])
                    # print("storage type:", self.is_storage_type)

                    if not (self.is_storage_type == "json" or self.is_storage_type == "csv" or self.is_storage_type == "txt" or self.is_storage_type == "xlsx"):
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(self.Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                        # Error_Log.append(str(self.Entry_outputTest_path.get()))
                        return self.is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get())

                    if self.is_storage_type == "json":
                        self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()
                        self.Radiobutton_storage_type_Excel.deselect()
                        self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    elif self.is_storage_type == "csv":
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()
                        self.Radiobutton_storage_type_Excel.deselect()
                        self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    elif self.is_storage_type == "txt":
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()
                        self.Radiobutton_storage_type_Excel.deselect()
                        self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    elif self.is_storage_type == "xlsx":
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()
                        self.Radiobutton_storage_type_txt.deselect()
                        self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                    elif len(self.is_storage_type) == 0:
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                    else:
                        self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                        self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(self.Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                        # Error_Log.append(str(self.Entry_outputTest_path.get()))
                        return self.is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get())
                else:
                    self.is_storage_type = ""
                    self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(self.Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                    # Error_Log.append(str(self.Entry_outputTest_path.get()))
                    return self.is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get())
            else:
                self.is_storage_type = ""
                self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                # # sys.stdout.write("\n")  # 輸出換行;
                # # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                # # sys.stdout.write("\n")  # 輸出換行;
                # print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(self.Entry_outputTest_path.get()) + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                # # Error_Log.append(str(self.Entry_outputTest_path.get()))
                # return self.is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.Entry_outputTest_path.get())

        else:
            print("參數錯誤." + "\n" + "判斷運算結果存儲位置的複選框值:" + "\n" + str(self.is_storage_position) + "\n" + "無法識別.")

            # 使用消息提示框控件給出溫馨提示;
            tk_messagebox.showinfo(
                title = "溫馨提示",
                message = str("參數錯誤." + "\n" + "判斷運算結果存儲位置的複選框值:" + "\n" + str(self.is_storage_position) + "\n" + "無法識別.")
            )

        # print("Output test path: ", self.outputTest_path)
        # print("Output test url: ", self.outputTest_URL)

        return self.is_storage_position  # None

    def click_Button_outputTest_URL(self):

        # global self.outputTest_URL

        self.outputTest_URL = str(self.Entry_outputTest_URL.get())  # 讀取結果輸出位置文本框輸入的内容;
        # self.outputTest_URL = str(self.outputTest_URL).replace('\\', '/')
        print(self.outputTest_URL)

        return self.outputTest_URL  # None

    def click_Button_outputTest_path(self):

        # global self.is_storage_position
        # global self.is_storage_type
        # # global self.initializer_Window
        # global self.output_dir
        # global self.outputTestpath
        # # self.outputTestpath = ""
        # global self.outputTest_path
        # # self.outputTest_path = ""
        # global self.outputTest_File_Array
        # self.outputTest_File_Array = []

        self.outputTest_path = str(self.Entry_outputTest_path.get())  # 讀取結果輸出位置文本框輸入的内容;
        self.outputTest_path = str(self.outputTest_path).replace('\\', '/')
        # self.outputTest_path = self.outputTest_path.replace('/', r'\\')

        # sysencode = sys.getfilesystemencoding()  # 包含有中文字符的文檔名編碼;

        self.output_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(self.outputTest_path))))).replace('\\', '/')
        # self.output_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(self.outputTest_path))))).replace('\\', '/')).encode(sysencode)

        # file_name_String = tk_filedialog.askopenfilename(title = '選定單檔')
        # directory_name_String = tk_filedialog.askdirectory(title = '選定資料夾')
        # files_name_Array = tk_filedialog.askopenfilenames(title = '選定多檔')

        self.outputTest_path = tk_filedialog.askopenfilename(
            title = '單選定運算結果輸出保存文檔',
            initialdir = self.output_dir,  # r'./test.csv', 默認打開路徑;
            defaultextension = ".csv",  # 預設文檔擴展名;
            initialfile = "test.csv",  # 對話框中初始化顯示的文檔名;
            # parent = self.initializer_Window,  # 父對話框（由哪個窗口彈出就在哪個上端）;
            filetypes=[
                ("Result output documents", "*.csv *.txt *.json *.xlsx"),
                ("Comma-Separated Values files", "*.csv"),
                ("JavaScript Object Notation files", "*.json"),
                ("Plain text files", "*.txt"),
                ("Microsoft Office Excel files", "*.xlsx"),  # ("Microsoft Office Excel files", "*.xlsx .xls"),
                ("All files", ".*")
            ]
        )
        # print(self.outputTest_path)

        if len(self.outputTest_path) > 0:

            self.outputTest_path = str(os.path.normpath(os.path.abspath(os.path.normpath(self.outputTest_path)))).replace('\\', '/')
            # self.outputTest_path = str(str(os.path.normpath(os.path.abspath(os.path.normpath(self.outputTest_path)))).replace('\\', '/')).encode(sysencode)

            if self.outputTest_path.find(".", 0, int(len(self.outputTest_path)-1)) != -1:

                self.is_storage_type = str(self.outputTest_path.split('.')[len(self.outputTest_path.split('.'))-1])
                # print("storage type:", self.is_storage_type)

                if self.is_storage_type == "csv":
                    self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_txt.deselect()
                    self.Radiobutton_storage_type_Excel.deselect()
                    self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                elif self.is_storage_type == "json":
                    self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_txt.deselect()
                    self.Radiobutton_storage_type_Excel.deselect()
                    self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                elif self.is_storage_type == "txt":
                    self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_csv.deselect()
                    self.Radiobutton_storage_type_Excel.deselect()
                    self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                elif self.is_storage_type == "xlsx":
                    self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_csv.deselect()
                    self.Radiobutton_storage_type_txt.deselect()
                    self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                elif len(self.is_storage_type) == 0:
                    self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                else:
                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                    self.Label_State['text'] = str("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                    # self.Error_Log.append(self.outputTest_path)
                    return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.outputTest_path  # None

                if self.is_storage_position == "":
                    self.is_storage_position = "Disk"
                elif self.is_storage_position == "Database":
                    self.is_storage_position = self.is_storage_position + "_and_" + "Disk"

                if self.is_storage_position == "Database":
                    # self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                    self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                    self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                    # self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                elif self.is_storage_position == "Database_and_Disk":
                    self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                    # self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                    self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                    # self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                elif self.is_storage_position == "Disk":
                    self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                    # self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                    # self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                    self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                elif len(self.is_storage_position) == 0:
                    # self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                    self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                    # self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                    self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                else:
                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + ",." + str(self.is_storage_position))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    print("參數錯誤." + "\n" + "用於輸出保存運算結果的位置:" + "\n" + "[ ." + str(self.is_storage_position) + " ]" + "\n" + "不合規，目前只支持:" + "\n" + "Database, Disk" + "\n" + "兩種方法.")
                    # Label_State['text'] = "參數錯誤." + "\n" + "用於輸出保存運算結果的位置:" + "\n" + "[ ." + str(self.is_storage_position) + " ]" + "\n" + "不合規，目前只支持:" + "\n" + "Database, Disk" + "\n" + "兩種方法."
                    # Error_Log.append(str(self.is_storage_position))
                    sys.exit(1)  # 中止當前進程，退出當前程序;

            else:
                # sys.stdout.write("\n")  # 輸出換行;
                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                # sys.stdout.write("\n")  # 輸出換行;
                print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                self.Label_State['text'] = str("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                # self.Error_Log.append(self.outputTest_path)
                return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.outputTest_path  # None

            self.outputTestpath.set(self.outputTest_path)
            self.Entry_outputTest_path['textvariable'] = self.outputTestpath

            self.outputTest_File_Array.append(self.outputTest_path)

            self.Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Output: [ " + str(self.outputTest_path) + " ] files."

        return self.outputTest_path  # None

    # 創建單選框（tkinter.Radiobutton）組件;
    def select_Radiobutton_storage_type(self):

        # global self.is_storage_type
        self.is_storage_type = str(self.Radiobutton_storage_type_Var.get())
        # print("storage type:", self.is_storage_type)

        # global self.default_outputTest_path
        # global self.outputTest_path
        # global self.outputTestpath

        if len(str(self.Entry_outputTest_path.get())) > 0:
            self.outputTest_path = str(self.Entry_outputTest_path.get())  # 讀取結果輸出位置文本框輸入的内容;

        if len(self.outputTest_path) > 0:
            self.outputTest_path = str(self.outputTest_path).replace('\\', '/')
            if self.outputTest_path.find(".", 0, int(len(self.outputTest_path)-1)) != -1:
                # del self.default_outputTest_path.split('.')[len(self.default_outputTest_path.split('.'))-1]
                self.outputTest_path = str(''.join(self.outputTest_path.split('.')[0:len(self.outputTest_path.split('.'))-1])) + "." + self.is_storage_type
            else:
                self.outputTest_path = self.outputTest_path + "." + self.is_storage_type
            # print("output test path: ", self.outputTest_path)

            # self.outputTest_path = self.default_outputTest_path
            # print("output test path: ", self.outputTest_path)

        # print("storage position: ", self.is_storage_position)
        if self.is_storage_position == "Database_and_Disk" or self.is_storage_position == "Disk":
            self.outputTestpath.set(self.outputTest_path)
            self.Entry_outputTest_path['textvariable'] = self.outputTestpath

        return self.is_storage_type + "," + self.outputTest_path

    def click_Button_inputTrain_path(self):

        # # global self.initializer_Window
        # global self.input_dir
        # global self.inputTrainpath
        # # self.inputTrainpath = ""
        # global self.inputTrain_path
        # # self.inputTrain_path = ""
        # global self.inputTrain_File_Array
        self.inputTrain_File_Array = []

        self.inputTrain_path = str(self.Entry_inputTrain_path.get())  # 讀取結果輸出位置文本框輸入的内容;
        self.inputTrain_path = str(self.inputTrain_path).replace('\\', '/')
        # self.inputTrain_path = self.inputTrain_path.replace('/', r'\\')

        # sysencode = sys.getfilesystemencoding()  # 包含有中文字符的文檔名編碼;

        if os.path.exists(self.inputTrain_path):
            if pathlib.Path(self.inputTrain_path).is_dir():
                self.input_dir = str(os.path.normpath(os.path.abspath(os.path.normpath(self.inputTrain_path)))).replace('\\', '/')
                # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
                if not (os.access(self.input_dir, os.R_OK) and os.access(self.input_dir, os.W_OK)):
                    try:
                        # 修改文檔權限 mode:777 任何人可讀寫;
                        os.chmod(self.input_dir, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                        # os.chmod(self.input_dir, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                        # os.chmod(self.input_dir, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                        # os.chmod(self.input_dir, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                        # os.chmod(self.input_dir, stat.S_IWOTH)  # 可被其它用戶寫入;
                        # stat.S_IXOTH:  其他用戶有執行權0o001
                        # stat.S_IWOTH:  其他用戶有寫許可權0o002
                        # stat.S_IROTH:  其他用戶有讀許可權0o004
                        # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
                        # stat.S_IXGRP:  組用戶有執行許可權0o010
                        # stat.S_IWGRP:  組用戶有寫許可權0o020
                        # stat.S_IRGRP:  組用戶有讀許可權0o040
                        # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
                        # stat.S_IXUSR:  擁有者具有執行許可權0o100
                        # stat.S_IWUSR:  擁有者具有寫許可權0o200
                        # stat.S_IRUSR:  擁有者具有讀許可權0o400
                        # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
                        # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
                        # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
                        # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
                        # stat.S_IREAD:  windows下設為唯讀
                        # stat.S_IWRITE: windows下取消唯讀
                    except OSError as error:
                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.input_dir + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        # print(error)
                        # print(f'Error: {self.input_dir} : {error}')
                        # print("參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + self.input_dir + " ]" + "\n" + "無法修改為可讀可寫權限.")
                        self.Label_State['text'] = "參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + self.input_dir + " ]" + "\n" + "無法修改為可讀可寫權限."
                        # self.Error_Log.append(self.input_dir)
                        # return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.input_dir  # None
            elif os.path.isfile(self.inputTrain_path):
                self.input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(self.inputTrain_path))))).replace('\\', '/')
                # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
                if not (os.access(self.input_dir, os.R_OK) and os.access(self.input_dir, os.W_OK)):
                    try:
                        # 修改文檔權限 mode:777 任何人可讀寫;
                        os.chmod(self.input_dir, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                        # os.chmod(self.input_dir, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                        # os.chmod(self.input_dir, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                        # os.chmod(self.input_dir, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                        # os.chmod(self.input_dir, stat.S_IWOTH)  # 可被其它用戶寫入;
                        # stat.S_IXOTH:  其他用戶有執行權0o001
                        # stat.S_IWOTH:  其他用戶有寫許可權0o002
                        # stat.S_IROTH:  其他用戶有讀許可權0o004
                        # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
                        # stat.S_IXGRP:  組用戶有執行許可權0o010
                        # stat.S_IWGRP:  組用戶有寫許可權0o020
                        # stat.S_IRGRP:  組用戶有讀許可權0o040
                        # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
                        # stat.S_IXUSR:  擁有者具有執行許可權0o100
                        # stat.S_IWUSR:  擁有者具有寫許可權0o200
                        # stat.S_IRUSR:  擁有者具有讀許可權0o400
                        # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
                        # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
                        # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
                        # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
                        # stat.S_IREAD:  windows下設為唯讀
                        # stat.S_IWRITE: windows下取消唯讀
                    except OSError as error:
                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.input_dir + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        # print(error)
                        # print(f'Error: {self.input_dir} : {error}')
                        # print("參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + self.input_dir + " ]" + "\n" + "無法修改為可讀可寫權限.")
                        self.Label_State['text'] = "參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + self.input_dir + " ]" + "\n" + "無法修改為可讀可寫權限."
                        # self.Error_Log.append(self.input_dir)
                        # return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.input_dir  # None
        #     else:
        #         # sys.stdout.write("\n")  # 輸出換行;
        #         # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.inputTrain_path))  # 將字符串輸出寫到操作系統控制臺;
        #         # sys.stdout.write("\n")  # 輸出換行;
        #         print("參數錯誤." + "\n" + "檔:" + "\n" + "[ " + self.inputTrain_path + " ]" + "\n" + "類型無法識別.")
        #         self.Label_State['text'] = "參數錯誤." + "\n" + "檔:" + "\n" + "[ " + self.inputTrain_path + " ]" + "\n" + "類型無法識別."
        #         # self.Error_Log.append(self.inputTrain_path)
        #         return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTrain_path  # None
        # else:
        #     # sys.stdout.write("\n")  # 輸出換行;
        #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.inputTrain_path))  # 將字符串輸出寫到操作系統控制臺;
        #     # sys.stdout.write("\n")  # 輸出換行;
        #     print("參數錯誤." + "\n" + "檔:" + "\n" + "[ " + self.inputTrain_path + " ]" + "\n" + "不存在.")
        #     self.Label_State['text'] = "參數錯誤." + "\n" + "檔:" + "\n" + "[ " + self.inputTrain_path + " ]" + "\n" + "不存在."
        #     # self.Error_Log.append(self.inputTrain_path)
        #     return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTrain_path  # None

        # file_name_String = tk_filedialog.askopenfilename(title = '選定單檔')
        # directory_name_String = tk_filedialog.askdirectory(title = '選定資料夾')
        # files_name_Array = tk_filedialog.askopenfilenames(title = '選定多檔')

        files_name_Array = tk_filedialog.askopenfilenames(
            title = '多選定待處理的圖片檔',
            initialdir = self.input_dir,  # r'./a/b/c', 默認打開路徑;
            initialfile = "",  # "test.bmp" 對話框中初始化顯示的文檔名;
            defaultextension = ".bmp",  # 預設文檔擴展名;
            # parent = self.initializer_Window,  # 父對話框（由哪個窗口彈出就在哪個上端）;
            filetypes=[
                ("Image files to process", "*.gif *.png *.bmp *.dxf *.fli *.flc *.eps *.psd *.pdd *.jpeg *.jpg *.wmf *.emf *.pcx *.tga *.tif"),
                ("Pixel images files", "*.jpeg *.jpg"),
                (".GIF images files", "*.gif"),
                (".BMP images files", "*.bmp"),
                (".PNG images files", "*.png"),
                ("AutoCAD images files", "*.dxf *.fli *.flc"),
                (".EPS images files", "*.eps"),
                (".WMF images files", "*.wmf *.emf"),
                ("PDF images files", "*.psd *.pdd"),
                ("Images files", "*.pcx *.tga *.tif"),
                ("All files", ".*")
            ]
        )
        # print(files_name_Array)

        for i in range(0, len(files_name_Array)):
            # print(files_name_Array[i])
            if len(files_name_Array[i]) > 0:
                # files_name_Array[i] = str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/')
                self.inputTrain_File_Array.append(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/'))
                # self.inputTrain_File_Array.append(str(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/')).encode(sysencode))

        # print(files_name_Array[0])
        if len(files_name_Array) == 1:
            if len(files_name_Array[0]) > 0:
                self.input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
                # self.input_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
                self.inputTrain_path = str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[0])))).replace('\\', '/')
                # self.inputTrain_path = str(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[0])))).replace('\\', '/')).encode(sysencode)
                self.inputTrainpath.set(self.inputTrain_path)
                self.Entry_inputTrain_path['textvariable'] = self.inputTrainpath
        elif len(files_name_Array) > 1:
            if len(files_name_Array[0]) > 0:
                self.input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
                # self.input_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
                self.inputTrain_path = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
                # self.inputTrain_path = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
                self.inputTrainpath.set(self.inputTrain_path)
                self.Entry_inputTrain_path['textvariable'] = self.inputTrainpath
        # elif len(files_name_Array) == 0:
        #     self.inputTrain_path = self.input_dir
        #     self.inputTrainpath.set(self.inputTrain_path)
        #     self.Entry_inputTrain_path['textvariable'] = self.inputTrainpath
        # else:

        if len(self.inputTrain_File_Array) > 0:
            self.Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "From: " + "[ " + self.inputTrain_path + " ]" + "\n" + "Input: [ " + str(len(self.inputTrain_File_Array)) + " ] files."

        return self.inputTrain_File_Array  # None

    def click_Button_inputValidation_path(self):

        # # global self.initializer_Window
        # global self.input_dir
        # global self.inputValidationpath
        # # self.inputValidationpath = ""
        # global self.inputValidation_path
        # # self.inputValidation_path = ""
        # global self.inputValidation_File_Array
        self.inputValidation_File_Array = []

        self.inputValidation_path = str(self.Entry_inputValidation_path.get())  # 讀取結果輸出位置文本框輸入的内容;
        self.inputValidation_path = str(self.inputValidation_path).replace('\\', '/')
        # self.inputValidation_path = self.inputValidation_path.replace('/', r'\\')

        # sysencode = sys.getfilesystemencoding()  # 包含有中文字符的文檔名編碼;

        if os.path.exists(self.inputValidation_path):
            if pathlib.Path(self.inputValidation_path).is_dir():
                self.input_dir = str(os.path.normpath(os.path.abspath(os.path.normpath(self.inputValidation_path)))).replace('\\', '/')
                # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
                if not (os.access(self.input_dir, os.R_OK) and os.access(self.input_dir, os.W_OK)):
                    try:
                        # 修改文檔權限 mode:777 任何人可讀寫;
                        os.chmod(self.input_dir, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                        # os.chmod(self.input_dir, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                        # os.chmod(self.input_dir, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                        # os.chmod(self.input_dir, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                        # os.chmod(self.input_dir, stat.S_IWOTH)  # 可被其它用戶寫入;
                        # stat.S_IXOTH:  其他用戶有執行權0o001
                        # stat.S_IWOTH:  其他用戶有寫許可權0o002
                        # stat.S_IROTH:  其他用戶有讀許可權0o004
                        # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
                        # stat.S_IXGRP:  組用戶有執行許可權0o010
                        # stat.S_IWGRP:  組用戶有寫許可權0o020
                        # stat.S_IRGRP:  組用戶有讀許可權0o040
                        # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
                        # stat.S_IXUSR:  擁有者具有執行許可權0o100
                        # stat.S_IWUSR:  擁有者具有寫許可權0o200
                        # stat.S_IRUSR:  擁有者具有讀許可權0o400
                        # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
                        # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
                        # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
                        # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
                        # stat.S_IREAD:  windows下設為唯讀
                        # stat.S_IWRITE: windows下取消唯讀
                    except OSError as error:
                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.input_dir + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        # print(error)
                        # print(f'Error: {self.input_dir} : {error}')
                        # print("參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + self.input_dir + " ]" + "\n" + "無法修改為可讀可寫權限.")
                        self.Label_State['text'] = "參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + self.input_dir + " ]" + "\n" + "無法修改為可讀可寫權限."
                        # self.Error_Log.append(self.input_dir)
                        # return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.input_dir  # None
            elif os.path.isfile(self.inputValidation_path):
                self.input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(self.inputValidation_path))))).replace('\\', '/')
                # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
                if not (os.access(self.input_dir, os.R_OK) and os.access(self.input_dir, os.W_OK)):
                    try:
                        # 修改文檔權限 mode:777 任何人可讀寫;
                        os.chmod(self.input_dir, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                        # os.chmod(self.input_dir, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                        # os.chmod(self.input_dir, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                        # os.chmod(self.input_dir, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                        # os.chmod(self.input_dir, stat.S_IWOTH)  # 可被其它用戶寫入;
                        # stat.S_IXOTH:  其他用戶有執行權0o001
                        # stat.S_IWOTH:  其他用戶有寫許可權0o002
                        # stat.S_IROTH:  其他用戶有讀許可權0o004
                        # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
                        # stat.S_IXGRP:  組用戶有執行許可權0o010
                        # stat.S_IWGRP:  組用戶有寫許可權0o020
                        # stat.S_IRGRP:  組用戶有讀許可權0o040
                        # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
                        # stat.S_IXUSR:  擁有者具有執行許可權0o100
                        # stat.S_IWUSR:  擁有者具有寫許可權0o200
                        # stat.S_IRUSR:  擁有者具有讀許可權0o400
                        # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
                        # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
                        # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
                        # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
                        # stat.S_IREAD:  windows下設為唯讀
                        # stat.S_IWRITE: windows下取消唯讀
                    except OSError as error:
                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.input_dir + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        # print(error)
                        # print(f'Error: {self.input_dir} : {error}')
                        # print("參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + self.input_dir + " ]" + "\n" + "無法修改為可讀可寫權限.")
                        self.Label_State['text'] = "參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + self.input_dir + " ]" + "\n" + "無法修改為可讀可寫權限."
                        # self.Error_Log.append(self.input_dir)
                        # return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.input_dir  # None
        #     else:
        #         # sys.stdout.write("\n")  # 輸出換行;
        #         # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.inputValidation_path))  # 將字符串輸出寫到操作系統控制臺;
        #         # sys.stdout.write("\n")  # 輸出換行;
        #         print("參數錯誤." + "\n" + "檔:" + "\n" + "[ " + self.inputValidation_path + " ]" + "\n" + "類型無法識別.")
        #         self.Label_State['text'] = "參數錯誤." + "\n" + "檔:" + "\n" + "[ " + self.inputValidation_path + " ]" + "\n" + "類型無法識別."
        #         # self.Error_Log.append(self.inputValidation_path)
        #         return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputValidation_path  # None
        # else:
        #     # sys.stdout.write("\n")  # 輸出換行;
        #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.inputValidation_path))  # 將字符串輸出寫到操作系統控制臺;
        #     # sys.stdout.write("\n")  # 輸出換行;
        #     print("參數錯誤." + "\n" + "檔:" + "\n" + "[ " + self.inputValidation_path + " ]" + "\n" + "不存在.")
        #     self.Label_State['text'] = "參數錯誤." + "\n" + "檔:" + "\n" + "[ " + self.inputValidation_path + " ]" + "\n" + "不存在."
        #     # self.Error_Log.append(self.inputValidation_path)
        #     return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputValidation_path  # None

        # file_name_String = tk_filedialog.askopenfilename(title = '選定單檔')
        # directory_name_String = tk_filedialog.askdirectory(title = '選定資料夾')
        # files_name_Array = tk_filedialog.askopenfilenames(title = '選定多檔')

        files_name_Array = tk_filedialog.askopenfilenames(
            title = '多選定待處理的圖片檔',
            initialdir = self.input_dir,  # r'./a/b/c', 默認打開路徑;
            initialfile = "",  # "test.bmp" 對話框中初始化顯示的文檔名;
            defaultextension = ".bmp",  # 預設文檔擴展名;
            # parent = self.initializer_Window,  # 父對話框（由哪個窗口彈出就在哪個上端）;
            filetypes=[
                ("Image files to process", "*.gif *.png *.bmp *.dxf *.fli *.flc *.eps *.psd *.pdd *.jpeg *.jpg *.wmf *.emf *.pcx *.tga *.tif"),
                ("Pixel images files", "*.jpeg *.jpg"),
                (".GIF images files", "*.gif"),
                (".BMP images files", "*.bmp"),
                (".PNG images files", "*.png"),
                ("AutoCAD images files", "*.dxf *.fli *.flc"),
                (".EPS images files", "*.eps"),
                (".WMF images files", "*.wmf *.emf"),
                ("PDF images files", "*.psd *.pdd"),
                ("Images files", "*.pcx *.tga *.tif"),
                ("All files", ".*")
            ]
        )
        # print(files_name_Array)

        for i in range(0, len(files_name_Array)):
            # print(files_name_Array[i])
            if len(files_name_Array[i]) > 0:
                # files_name_Array[i] = str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/')
                self.inputValidation_File_Array.append(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/'))
                # self.inputValidation_File_Array.append(str(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/')).encode(sysencode))

        # print(files_name_Array[0])
        if len(files_name_Array) == 1:
            if len(files_name_Array[0]) > 0:
                self.input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
                # self.input_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
                self.inputValidation_path = str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[0])))).replace('\\', '/')
                # self.inputValidation_path = str(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[0])))).replace('\\', '/')).encode(sysencode)
                self.inputValidationpath.set(self.inputValidation_path)
                self.Entry_inputValidation_path['textvariable'] = self.inputValidationpath
        elif len(files_name_Array) > 1:
            if len(files_name_Array[0]) > 0:
                self.input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
                # self.input_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
                self.inputValidation_path = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
                # self.inputValidation_path = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
                self.inputValidationpath.set(self.inputValidation_path)
                self.Entry_inputValidation_path['textvariable'] = self.inputValidationpath
        # elif len(files_name_Array) == 0:
        #     self.inputValidation_path = self.input_dir
        #     self.inputValidationpath.set(self.inputValidation_path)
        #     self.Entry_inputValidation_path['textvariable'] = self.inputValidationpath
        # else:

        if len(self.inputValidation_File_Array) > 0:
            self.Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "From: " + "[ " + self.inputValidation_path + " ]" + "\n" + "Input: [ " + str(len(self.inputValidation_File_Array)) + " ] files."

        return self.inputValidation_File_Array  # None

    def click_Button_inputTest_path(self):

        # # global self.initializer_Window
        # global self.input_dir
        # global self.inputTestpath
        # # self.inputTestpath = ""
        # global self.inputTest_path
        # # self.inputTest_path = ""
        # global self.inputTest_File_Array
        self.inputTest_File_Array = []

        self.inputTest_path = str(self.Entry_inputTest_path.get())  # 讀取結果輸出位置文本框輸入的内容;
        self.inputTest_path = str(self.inputTest_path).replace('\\', '/')
        # self.inputTest_path = self.inputTest_path.replace('/', r'\\')

        # sysencode = sys.getfilesystemencoding()  # 包含有中文字符的文檔名編碼;

        if os.path.exists(self.inputTest_path):
            if pathlib.Path(self.inputTest_path).is_dir():
                self.input_dir = str(os.path.normpath(os.path.abspath(os.path.normpath(self.inputTest_path)))).replace('\\', '/')
                # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
                if not (os.access(self.input_dir, os.R_OK) and os.access(self.input_dir, os.W_OK)):
                    try:
                        # 修改文檔權限 mode:777 任何人可讀寫;
                        os.chmod(self.input_dir, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                        # os.chmod(self.input_dir, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                        # os.chmod(self.input_dir, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                        # os.chmod(self.input_dir, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                        # os.chmod(self.input_dir, stat.S_IWOTH)  # 可被其它用戶寫入;
                        # stat.S_IXOTH:  其他用戶有執行權0o001
                        # stat.S_IWOTH:  其他用戶有寫許可權0o002
                        # stat.S_IROTH:  其他用戶有讀許可權0o004
                        # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
                        # stat.S_IXGRP:  組用戶有執行許可權0o010
                        # stat.S_IWGRP:  組用戶有寫許可權0o020
                        # stat.S_IRGRP:  組用戶有讀許可權0o040
                        # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
                        # stat.S_IXUSR:  擁有者具有執行許可權0o100
                        # stat.S_IWUSR:  擁有者具有寫許可權0o200
                        # stat.S_IRUSR:  擁有者具有讀許可權0o400
                        # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
                        # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
                        # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
                        # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
                        # stat.S_IREAD:  windows下設為唯讀
                        # stat.S_IWRITE: windows下取消唯讀
                    except OSError as error:
                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.input_dir + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        # print(error)
                        # print(f'Error: {self.input_dir} : {error}')
                        # print("參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + self.input_dir + " ]" + "\n" + "無法修改為可讀可寫權限.")
                        self.Label_State['text'] = "參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + self.input_dir + " ]" + "\n" + "無法修改為可讀可寫權限."
                        # self.Error_Log.append(self.input_dir)
                        # return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.input_dir  # None
            elif os.path.isfile(self.inputTest_path):
                self.input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(self.inputTest_path))))).replace('\\', '/')
                # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
                if not (os.access(self.input_dir, os.R_OK) and os.access(self.input_dir, os.W_OK)):
                    try:
                        # 修改文檔權限 mode:777 任何人可讀寫;
                        os.chmod(self.input_dir, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                        # os.chmod(self.input_dir, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                        # os.chmod(self.input_dir, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                        # os.chmod(self.input_dir, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                        # os.chmod(self.input_dir, stat.S_IWOTH)  # 可被其它用戶寫入;
                        # stat.S_IXOTH:  其他用戶有執行權0o001
                        # stat.S_IWOTH:  其他用戶有寫許可權0o002
                        # stat.S_IROTH:  其他用戶有讀許可權0o004
                        # stat.S_IRWXO:  其他使用者有全部許可權(許可權遮罩)0o007
                        # stat.S_IXGRP:  組用戶有執行許可權0o010
                        # stat.S_IWGRP:  組用戶有寫許可權0o020
                        # stat.S_IRGRP:  組用戶有讀許可權0o040
                        # stat.S_IRWXG:  組使用者有全部許可權(許可權遮罩)0o070
                        # stat.S_IXUSR:  擁有者具有執行許可權0o100
                        # stat.S_IWUSR:  擁有者具有寫許可權0o200
                        # stat.S_IRUSR:  擁有者具有讀許可權0o400
                        # stat.S_IRWXU:  擁有者有全部許可權(許可權遮罩)0o700
                        # stat.S_ISVTX:  目錄裡檔目錄只有擁有者才可刪除更改0o1000
                        # stat.S_ISGID:  執行此檔其進程有效組為檔所在組0o2000
                        # stat.S_ISUID:  執行此檔其進程有效使用者為檔所有者0o4000
                        # stat.S_IREAD:  windows下設為唯讀
                        # stat.S_IWRITE: windows下取消唯讀
                    except OSError as error:
                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.input_dir + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        # print(error)
                        # print(f'Error: {self.input_dir} : {error}')
                        # print("參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + self.input_dir + " ]" + "\n" + "無法修改為可讀可寫權限.")
                        self.Label_State['text'] = "參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + self.input_dir + " ]" + "\n" + "無法修改為可讀可寫權限."
                        # self.Error_Log.append(self.input_dir)
                        # return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.input_dir  # None
        #     else:
        #         # sys.stdout.write("\n")  # 輸出換行;
        #         # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.inputTest_path))  # 將字符串輸出寫到操作系統控制臺;
        #         # sys.stdout.write("\n")  # 輸出換行;
        #         print("參數錯誤." + "\n" + "檔:" + "\n" + "[ " + self.inputTest_path + " ]" + "\n" + "類型無法識別.")
        #         self.Label_State['text'] = "參數錯誤." + "\n" + "檔:" + "\n" + "[ " + self.inputTest_path + " ]" + "\n" + "類型無法識別."
        #         # self.Error_Log.append(self.inputTest_path)
        #         return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTest_path  # None
        # else:
        #     # sys.stdout.write("\n")  # 輸出換行;
        #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.inputTest_path))  # 將字符串輸出寫到操作系統控制臺;
        #     # sys.stdout.write("\n")  # 輸出換行;
        #     print("參數錯誤." + "\n" + "檔:" + "\n" + "[ " + self.inputTest_path + " ]" + "\n" + "不存在.")
        #     self.Label_State['text'] = "參數錯誤." + "\n" + "檔:" + "\n" + "[ " + self.inputTest_path + " ]" + "\n" + "不存在."
        #     # self.Error_Log.append(self.inputTest_path)
        #     return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTest_path  # None

        # file_name_String = tk_filedialog.askopenfilename(title = '選定單檔')
        # directory_name_String = tk_filedialog.askdirectory(title = '選定資料夾')
        # files_name_Array = tk_filedialog.askopenfilenames(title = '選定多檔')

        files_name_Array = tk_filedialog.askopenfilenames(
            title = '多選定待處理的圖片檔',
            initialdir = self.input_dir,  # r'./a/b/c', 默認打開路徑;
            initialfile = "",  # "test.bmp" 對話框中初始化顯示的文檔名;
            defaultextension = ".bmp",  # 預設文檔擴展名;
            # parent = self.initializer_Window,  # 父對話框（由哪個窗口彈出就在哪個上端）;
            filetypes=[
                ("Image files to process", "*.gif *.png *.bmp *.dxf *.fli *.flc *.eps *.psd *.pdd *.jpeg *.jpg *.wmf *.emf *.pcx *.tga *.tif"),
                ("Pixel images files", "*.jpeg *.jpg"),
                (".GIF images files", "*.gif"),
                (".BMP images files", "*.bmp"),
                (".PNG images files", "*.png"),
                ("AutoCAD images files", "*.dxf *.fli *.flc"),
                (".EPS images files", "*.eps"),
                (".WMF images files", "*.wmf *.emf"),
                ("PDF images files", "*.psd *.pdd"),
                ("Images files", "*.pcx *.tga *.tif"),
                ("All files", ".*")
            ]
        )
        # print(files_name_Array)

        for i in range(0, len(files_name_Array)):
            # print(files_name_Array[i])
            if len(files_name_Array[i]) > 0:
                # files_name_Array[i] = str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/')
                self.inputTest_File_Array.append(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/'))
                # self.inputTest_File_Array.append(str(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/')).encode(sysencode))

        # print(files_name_Array[0])
        if len(files_name_Array) == 1:
            if len(files_name_Array[0]) > 0:
                self.input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
                # self.input_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
                self.inputTest_path = str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[0])))).replace('\\', '/')
                # self.inputTest_path = str(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[0])))).replace('\\', '/')).encode(sysencode)
                self.inputTestpath.set(self.inputTest_path)
                self.Entry_inputTest_path['textvariable'] = self.inputTestpath
        elif len(files_name_Array) > 1:
            if len(files_name_Array[0]) > 0:
                self.input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
                # self.input_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
                self.inputTest_path = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
                # self.inputTest_path = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
                self.inputTestpath.set(self.inputTest_path)
                self.Entry_inputTest_path['textvariable'] = self.inputTestpath
        # elif len(files_name_Array) == 0:
        #     self.inputTest_path = self.input_dir
        #     self.inputTestpath.set(self.inputTest_path)
        #     self.Entry_inputTest_path['textvariable'] = self.inputTestpath
        # else:

        if len(self.inputTest_File_Array) > 0:
            self.Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "From: " + "[ " + self.inputTest_path + " ]" + "\n" + "Input: [ " + str(len(self.inputTest_File_Array)) + " ] files."

        return self.inputTest_File_Array  # None

    def click_Button_start_and_stop_Train(self):

        # global self.screenwidth
        # global self.screenheight
        # global self.is_storage_position
        # global self.is_storage_type
        # global default_input_tabel_tesseract_config  # = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        # global input_tabel_tesseract_config  # = self.default_input_tabel_tesseract_config
        # global inputTabelTesseractConfig  # = tk.StringVar(value=self.default_input_tabel_tesseract_config)
        # global default_input_measuringRuler_tesseract_config  # = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        # global input_measuringRuler_tesseract_config  # = self.default_input_measuringRuler_tesseract_config
        # global inputMeasuringRulerTesseractConfig  # = tk.StringVar(value=self.default_input_measuringRuler_tesseract_config)
        # global self.default_input_tabel_tesseract_config  # = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        # global self.input_tabel_tesseract_config  # = self.default_input_tabel_tesseract_config
        # global self.inputTabelTesseractConfig  # = tk.StringVar(value=self.default_input_tabel_tesseract_config)
        # global self.default_input_measuringRuler_tesseract_config  # = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        # global self.input_measuringRuler_tesseract_config  # = self.default_input_measuringRuler_tesseract_config
        # global self.inputMeasuringRulerTesseractConfig  # = tk.StringVar(value=self.default_input_measuringRuler_tesseract_config)
        # global self.inputTrain_path
        # global self.inputTrain_File_Array
        # global self.inputValidation_path
        # global self.inputValidation_File_Array
        # # global self.inputTest_path
        # # global self.inputTest_File_Array
        # # global self.outputTest_path
        # # global self.outputTest_File_Array
        # # global self.outputTest_URL

        # global self.complete_Number
        self.complete_Number = int(0)

        # global self.is_Runing
        self.is_Runing = not self.is_Runing
        if self.is_Runing:

            if self.is_Concurrent == "Multi-Threading":
                if self.outqueue_from_host_to_task:
                    self.outqueue_from_host_to_task.put(
                        [
                            "is_Runing_True",
                            ""
                        ],
                        block=False,
                        timeout=None
                    )

            self.Button_start_and_stop_Train['text'] = "Stop Train"
            # self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            self.Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        else:

            # print("程式被中止.")
            if self.is_Concurrent == "Multi-Threading":
                if self.outqueue_from_host_to_task:
                    self.outqueue_from_host_to_task.put(
                        [
                            "is_Runing_False",
                            ""
                        ],
                        block=False,
                        timeout=None
                    )

            if self.is_Concurrent == "0" or self.is_Concurrent == 0:
                # sys.stdout.write('\n')
                # sys.stdout.write("Discontinue," + str(self.complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTest_path + "," + self.outputTest_path)  # 將字符串輸出寫到操作系統控制臺;
                print("Discontinue," + str(self.complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTest_path + "," + self.outputTest_path)  # 將字符串輸出寫到操作系統控制臺;
                # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                # self.Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + self.inputTest_path + " ]." + "\n" + "Output: [ " + self.outputTest_path + " ]." + "\n" + "discontinue [ " + str(self.complete_Number) + " ]."
                self.Label_State['text'] = "Stand by"

                self.Button_start_and_stop_Test['text'] = "Start Test"
                self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

                # 使用消息提示框控件給出溫馨提示;
                tk_messagebox.showinfo(
                    title = "溫馨提示",
                    message = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + self.inputTest_path + " ]." + "\n" + "Output: [ " + self.outputTest_path + " ]." + "\n" + "Discontinue [ " + str(self.complete_Number) + " ]."
                )

            return "Discontinue," + str(self.complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTrain_path + "," + self.inputValidation_path  # None

        # global self.Error_Log
        self.Error_Log = []

        self.input_tabel_tesseract_config = str(self.Entry_tabel_tesseract_config.get())  # 讀取表格（tabel）内的文本識別（Google tesseract）的參數（tesseract config）文本輸入框輸入的内容; # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        global input_tabel_tesseract_config
        input_tabel_tesseract_config = self.input_tabel_tesseract_config
        self.input_measuringRuler_tesseract_config = str(self.Entry_measuringRuler_tesseract_config.get())  # 讀取測量尺（Measuring Ruler）標識的文本識別（Google tesseract）的參數（tesseract config）文本框輸入的内容; # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        global input_measuringRuler_tesseract_config
        input_measuringRuler_tesseract_config = self.input_measuringRuler_tesseract_config
        optical_character_recognition.tabel_tesseract_config = self.input_tabel_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        optical_character_recognition.measuringRuler_tesseract_config = self.input_measuringRuler_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;

        self.inputTrain_path = str(self.Entry_inputTrain_path.get())  # 讀取訓練集樣本位置文本框輸入的内容;

        if len(self.inputTrain_path) == 0:

            # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.inputTrain_path))  # 將字符串輸出寫到操作系統控制臺;
            print("參數錯誤." + "\n" + "訓練集樣本傳入路徑: " + "\n" + "[ " + self.inputTrain_path + " ]" + "\n" + "爲空.")
            # self.Label_State['text'] = "參數錯誤." + "\n" + "訓練集樣本傳入路徑: " + "\n" + "[ " + self.inputTrain_path + " ]" + "\n" + "爲空."
            self.Label_State['text'] = "Stand by"

            # self.Error_Log.append(self.inputTrain_path)

            if self.is_Runing:
                self.is_Runing = not self.is_Runing
            if self.is_Runing:
                self.Button_start_and_stop_Train['text'] = "Stop Train"
                # self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            else:
                self.Button_start_and_stop_Train['text'] = "Start Train"
                # self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Button_start_and_stop_Test['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

            # 使用消息提示框控件給出溫馨提示;
            tk_messagebox.showinfo(
                title = "溫馨提示",
                message = "參數錯誤." + "\n" + "訓練集樣本傳入路徑: " + "\n" + "[ " + self.inputTrain_path + " ]" + "\n" + "爲空."
            )

            return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTrain_path

        self.inputTrain_path = str(self.inputTrain_path).replace('\\', '/')
        # print("input train path:", self.inputTrain_path)

        self.inputValidation_path = str(self.Entry_inputValidation_path.get())  # 讀取驗證集樣本位置文本框輸入的内容;

        if len(self.inputValidation_path) == 0:

            # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.inputValidation_path))  # 將字符串輸出寫到操作系統控制臺;
            print("參數錯誤." + "\n" + "驗證集樣本傳入路徑: " + "\n" + "[ " + self.inputValidation_path + " ]" + "\n" + "爲空.")
            # self.Label_State['text'] = "參數錯誤." + "\n" + "驗證集樣本傳入路徑: " + "\n" + "[ " + self.inputValidation_path + " ]" + "\n" + "爲空."
            self.Label_State['text'] = "Stand by"

            # self.Error_Log.append(self.inputValidation_path)

            if self.is_Runing:
                self.is_Runing = not self.is_Runing
            if self.is_Runing:
                self.Button_start_and_stop_Train['text'] = "Stop Train"
                # self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            else:
                self.Button_start_and_stop_Train['text'] = "Start Train"
                # self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Button_start_and_stop_Test['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

            # 使用消息提示框控件給出溫馨提示;
            tk_messagebox.showinfo(
                title = "溫馨提示",
                message = "參數錯誤." + "\n" + "驗證集樣本傳入路徑: " + "\n" + "[ " + self.inputValidation_path + " ]" + "\n" + "爲空."
            )

            return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputValidation_path

        self.inputValidation_path = str(self.inputValidation_path).replace('\\', '/')
        # print("input validation path:", self.inputValidation_path)

        # self.inputTest_path = str(self.Entry_inputTest_path.get())  # 讀取測試集樣本位置文本框輸入的内容;

        # if len(self.inputTest_path) == 0:

        #     # sys.stdout.write("Error," + + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," str(self.inputTest_path))  # 將字符串輸出寫到操作系統控制臺;
        #     print("參數錯誤." + "\n" + "測試集樣本傳入路徑: " + "\n" + "[ " + self.inputTest_path + " ]" + "\n" + "爲空.")
        #     # self.Label_State['text'] = "參數錯誤." + "\n" + "測試集樣本傳入路徑: " + "\n" + "[ " + self.inputTest_path + " ]" + "\n" + "爲空."
        #     self.Label_State['text'] = "Stand by"

        #     # self.Error_Log.append(self.inputTest_path)

        #     if self.is_Runing:
        #         self.is_Runing = not self.is_Runing
        #     if self.is_Runing:
        #         self.Button_start_and_stop_Train['text'] = "Stop Train"
        #         # self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         # self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         # self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     else:
        #         self.Button_start_and_stop_Train['text'] = "Start Train"
        #         # self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         # self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         # self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Button_start_and_stop_Test['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

        #     # 使用消息提示框控件給出溫馨提示;
        #     tk_messagebox.showinfo(
        #         title = "溫馨提示",
        #         message = "參數錯誤." + "\n" + "測試集樣本傳入路徑: " + "\n" + "[ " + self.inputTest_path + " ]" + "\n" + "爲空."
        #     )

        #     return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTest_path

        # self.inputTest_path = str(self.inputTest_path).replace('\\', '/')
        # # print("input test path:", self.inputTest_path)

        # # global self.is_storage_type
        # self.is_storage_type = str(self.Radiobutton_storage_type_Var.get())
        # # print("storage type:", self.is_storage_type)

        # self.outputTest_path = str(self.Entry_outputTest_path.get())  # 讀取結果輸出位置文本框輸入的内容;

        # if len(self.outputTest_path) == 0:

        #     if len(self.is_storage_position) == 0:
        #         self.is_storage_position = ""
        #         # self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
        #         self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
        #         # self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
        #         self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
        #     elif self.is_storage_position == "Disk":
        #         self.is_storage_position = ""
        #         # self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
        #         self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
        #         # self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
        #         self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
        #     elif self.is_storage_position == "Database_and_Disk":
        #         self.is_storage_position = "Database"
        #         # self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
        #         self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
        #         self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
        #         # self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;

        #     self.is_storage_type = ""
        #     # print("storage type:", self.is_storage_type)

        #     # self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
        #     self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
        #     # self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
        #     self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
        #     # self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
        #     self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
        #     # self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
        #     self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

        #     # # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
        #     # print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "爲空.")
        #     # # self.Label_State['text'] = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "爲空."
        #     # self.Label_State['text'] = "Stand by"

        #     # # self.Error_Log.append(self.outputTest_path)

        #     # if self.is_Runing:
        #     #     self.is_Runing = not self.is_Runing
        #     # if self.is_Runing:
        #     #     self.Button_start_and_stop_Train['text'] = "Stop Train"
        #     #     # self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     # self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     # self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     self.Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     # else:
        #     #     self.Button_start_and_stop_Train['text'] = "Start Train"
        #     #     # self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     # self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     # self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     #     self.Button_start_and_stop_Test['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     #     self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

        #     # # 使用消息提示框控件給出溫馨提示;
        #     # tk_messagebox.showinfo(
        #     #     title = "溫馨提示",
        #     #     message = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "爲空."
        #     # )

        #     # return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.outputTest_path

        # self.outputTest_path = str(self.outputTest_path).replace('\\', '/')
        # # print("output test path:", self.outputTest_path)

        # if len(self.outputTest_path) > 0:

        #     if self.outputTest_path.find(".", 0, int(len(self.outputTest_path)-1)) != -1:

        #         self.is_storage_type = str(self.outputTest_path.split('.')[len(self.outputTest_path.split('.'))-1])
        #         # print("storage type:", self.is_storage_type)
        #         if self.is_storage_type == "json":
        #             self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
        #             self.Radiobutton_storage_type_txt.deselect()
        #             self.Radiobutton_storage_type_Excel.deselect()
        #             self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
        #         elif self.is_storage_type == "csv":
        #             self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
        #             self.Radiobutton_storage_type_txt.deselect()
        #             self.Radiobutton_storage_type_Excel.deselect()
        #             self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
        #         elif self.is_storage_type == "txt":
        #             self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
        #             self.Radiobutton_storage_type_csv.deselect()
        #             self.Radiobutton_storage_type_Excel.deselect()
        #             self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
        #         elif self.is_storage_type == "xlsx":
        #             self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
        #             self.Radiobutton_storage_type_csv.deselect()
        #             self.Radiobutton_storage_type_txt.deselect()
        #             self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
        #         elif len(self.is_storage_type) == 0:
        #             self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
        #             self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
        #             self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
        #             self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
        #         else:

        #             # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
        #             print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規.")
        #             # self.Label_State['text'] = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規."
        #             self.Label_State['text'] = "Stand by"

        #             # self.Error_Log.append(self.outputTest_path)

        #             if self.is_Runing:
        #                 self.is_Runing = not self.is_Runing
        #             if self.is_Runing:
        #                 self.Button_start_and_stop_Train['text'] = "Stop Train"
        #                 # self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 # self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 # self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 self.Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             else:
        #                 self.Button_start_and_stop_Train['text'] = "Start Train"
        #                 # self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 # self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 # self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #                 self.Button_start_and_stop_Test['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #                 self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

        #             # 使用消息提示框控件給出溫馨提示;
        #             tk_messagebox.showinfo(
        #                 title = "溫馨提示",
        #                 message = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規."
        #             )

        #             return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.outputTest_path

        #     else:

        #         # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
        #         print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規.")
        #         # self.Label_State['text'] = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規."
        #         self.Label_State['text'] = "Stand by"

        #         # self.Error_Log.append(self.outputTest_path)

        #         if self.is_Runing:
        #             self.is_Runing = not self.is_Runing
        #         if self.is_Runing:
        #             self.Button_start_and_stop_Train['text'] = "Stop Train"
        #             # self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             # self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             # self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             self.Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         else:
        #             self.Button_start_and_stop_Train['text'] = "Start Train"
        #             # self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             # self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             # self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #             self.Button_start_and_stop_Test['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #             self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

        #         # 使用消息提示框控件給出溫馨提示;
        #         tk_messagebox.showinfo(
        #             title = "溫馨提示",
        #             message = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規."
        #         )

        #         return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.outputTest_path

        # global self.time_sleep
        # global self.file_Data
        # # global self.file_Data_bytes
        # # global self.file_Data_len
        self.file_Data = ""
        # # self.file_Data_bytes = self.file_Data.encode("utf-8")
        # # self.file_Data = self.file_Data_bytes.decode("utf-8")
        # # self.file_Data = str(self.file_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
        # # self.file_Data_len = len(bytes(self.file_Data, "utf-8"))
        # global self.result_Data
        self.result_Data = ""
        # # self.result_Data_bytes = self.result_Data.encode("utf-8")
        # # self.result_Data = self.result_Data_bytes.decode("utf-8")
        # # self.result_Data = str(self.result_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
        # # self.result_Data_len = len(bytes(self.result_Data, "utf-8"))
        # global self.image_sample
        self.image_sample = []

        # print(self.inputTrain_path)
        if len(self.inputTrain_File_Array) == 0:
            if len(self.inputTrain_path) > 0:
                # self.inputTrain_File_Array = []
                self.inputTrain_File_Array = self.Path_Conversion(self.inputTrain_path, self.time_sleep)[0]

        # print(self.inputValidation_path)
        if len(self.inputValidation_File_Array) == 0:
            if len(self.inputValidation_path) > 0:
                # self.inputValidation_File_Array = []
                self.inputValidation_File_Array = self.Path_Conversion(self.inputValidation_path, self.time_sleep)[0]

        # print(self.inputTest_path)
        # if len(self.inputTest_File_Array) == 0:
        #     if len(self.inputTest_path) > 0:
        #         # self.inputTest_File_Array = []
        #         self.inputTest_File_Array = self.Path_Conversion(self.inputTest_path, self.time_sleep)[0]

        # print(self.outputTest_path)
        # if len(self.outputTest_File_Array) == 0:
        #     if len(self.outputTest_path) > 0:
        #         # # self.outputTest_File_Array = []
        #         # self.outputTest_File_Array = self.Path_Conversion(self.outputTest_path, self.time_sleep)[0]
        #         self.outputTest_File_Array = [self.outputTest_path]

        # 讀取多行文本輸入框中的内容;
        Text_display_result_value = self.Text_display_result.get(
            "0.0",  # 表示讀取多行文本輸入框 .Text 控件中的全部值，如果設定參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始讀取;
            "end"  # 表示讀取至多行文本輸入框 .Text 控件中全部值的最後一個字符爲止;
        )
        Text_display_result_value = str(Text_display_result_value)
        # print(Text_display_result_value)

        if len(Text_display_result_value) > 0:

            # 刪除多行文本輸入框中的内容;
            self.Text_display_result.delete(
                "1.0",  # 參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始刪除;
                "end"  # 參數爲 "end" 表示刪除直至最後一個字符，即清空輸入框;
            )

            self.Text_display_result.see("end"),  # 表示將 .Text 組件中聚焦在文本末行，即顯示末尾;

        # # 將字符串寫入多行文本輸入框;
        # self.Text_display_result.insert(
        #     "end",  # 參數 "1.0" 表示從第一行第一列開始插入，參數 "insert" 表示在當前光標位置處插入一個字符串，參數 "end" 表示在末尾位置處追加寫入一個字符串;
        #     str(new_Text_display_result_value)
        # )

        return_value = ""

        if self.is_Concurrent == "Multi-Threading":

            # if not self.is_window:
            #     self.screenwidth = int(0)
            #     self.screenheight = int(0)
            # self.outqueue_from_task_to_host = queue.Queue(maxsize=0)
            # self.outqueue_from_host_to_task = queue.Queue(maxsize=0)

            # print("process-" + str(multiprocessing.current_process().pid) + " thread-" + str(threading.currentThread().ident) + " ( name: " + str(threading.currentThread().name) + " )")

            # # 使用 Python 原生的多執行緒（綫程）支持 threading 庫的 threading.Thread(target=do_Function, args=(args1, args2)) 創建一個子綫程，用於調用讀取指定文檔並處理數據函數;
            # # 第一個參數 target=do_Function 是子執行緒（綫程）函數變量，第二個參數 args=(args1, args2) 是一個數組變量參數，如果只傳遞一個參數就只需要 args1，如果要傳遞多個參數，可以使用元組，當元組中只包含一個元素時，需要在元素後面添加逗號，例如 args=(args1,) 形式;
            # t = threading.Thread(target=read_file_do_Function, args=(monitor_file,), daemon=True)
            # # 參數：daemon=True，表示把創建的子綫程設爲守護綫程，當主綫程關閉時，子綫程同時關閉，這個標識必須在 .start() 方法調用之前設置;
            # t.start()  # 啓動子綫程;
            # # threading.Condition()

            # # 使用 Python 原生的多進程支持 multiprocessing 庫的 multiprocessing.Process(target=do_Function, args=(args1, args2)) 創建一個子進程，用於調用讀取指定文檔並處理數據函數;
            # # 第一個參數 target=do_Function 是子進程函數變量，第二個參數 args=(args1, args2) 是一個數組變量參數，如果只傳遞一個參數就只需要 args1，如果要傳遞多個參數，可以使用元組，當元組中只包含一個元素時，需要在元素後面添加逗號，例如 args=(args1,) 形式;
            # p = multiprocessing.Process(target=read_file_do_Function, args=(monitor_file, monitor_dir, do_Function, output_dir, output_file, to_executable, to_script))
            # p.setDaemon(True)  # 把創建的子進程設爲守護進程，當主綫程關閉時，子進程同時關閉，這個標識必須在 .start() 方法調用之前設置;
            # p.start()  # 啓動子進程;
            # P.close()  # 關閉Process物件，並釋放與之關聯的所有資源，如果底層進程仍在運行，則會引發ValueError。而且，一旦close()方法成功返回，Process物件的大多數方法和屬性也可能會引發ValueError;
            # # P.terminate  # 强制終止進程子進程，如果調用此函數,進程P將被立即終止，同時不會進行任何清理動作，在Unix上使用的是SIGTERM信號，在Windows上使用的是TerminateProcess()。注意，進程的後代進程不會被終止（會變成“孤兒”進程）。另外，如果被終止的進程在使用Pipe或Queue時，它們有可能會被損害，並無法被其他進程使用；如果被終止的進程已獲得鎖或信號量等，則有可能導致其他進程鎖死。所以請謹慎使用此方法，如果p保存了一個鎖或參與了進程間通信，那麼終止它可能會導致鎖死或I/O損壞;
            # p.join()  # .join() 函數會使得主進程阻塞等待，直到該被調用的子進程運行結束或超時，才繼續執行主進程，要在 .close() 和 .terminate 方法之後使用;
            # # p.pid
            # # p.name
            # # p.ident
            # # p.sentinel

            self.initializer_Window.after(5, self.Queue_update, self.outqueue_from_task_to_host)

            thr = threading.Thread(
                target = self.Run_Input_and_Output_Function,
                args = (
                    self.Path_Conversion,
                    self.Input_and_Output_Function,
                    self.is_window,
                    self.screenwidth,
                    self.screenheight,
                    self.is_Concurrent,
                    self.is_storage_position,
                    self.is_storage_type,
                    self.inputTrain_path,
                    self.inputTrain_File_Array,
                    self.inputTest_path,
                    self.inputTest_File_Array,
                    self.do_Function,
                    self.outputTest_path,
                    self.outputTest_File_Array,
                    self.outputTest_URL,
                    self.time_sleep,
                    self.outqueue_from_task_to_host,
                    self.outqueue_from_host_to_task,
                    self.is_Runing,
                    self.file_Data,
                    self.result_Data,
                    self.complete_Number,
                    self.Error_Log,
                    self.Label_State,
                    self.Text_display_result,
                    self.image_sample,
                    self.Canvas_display_sample,
                    self.Label_display_sample
                ),
                daemon = True  # 把創建的子綫程設爲守護綫程，當主綫程關閉時，子綫程同時關閉，這個標識必須在 .start() 方法調用之前設置;
            )
            thr.start()

        if self.is_Concurrent == "0" or self.is_Concurrent == 0:

            # if not self.is_window:
            #     self.screenwidth = int(0)
            #     self.screenheight = int(0)
            # self.outqueue_from_task_to_host = None
            # self.outqueue_from_host_to_task = None

            return_value = self.Run_Input_and_Output_Function(
                self.Path_Conversion,
                self.Input_and_Output_Function,
                self.is_window,
                self.screenwidth,
                self.screenheight,
                self.is_Concurrent,
                self.is_storage_position,
                self.is_storage_type,
                self.inputTrain_path,
                self.inputTrain_File_Array,
                self.inputTest_path,
                self.inputTest_File_Array,
                self.do_Function,
                self.outputTest_path,
                self.outputTest_File_Array,
                self.outputTest_URL,
                self.time_sleep,
                self.outqueue_from_task_to_host,
                self.outqueue_from_host_to_task,
                self.is_Runing,
                self.file_Data,
                self.result_Data,
                self.complete_Number,
                self.Error_Log,
                self.Label_State,
                self.Text_display_result,
                self.image_sample,
                self.Canvas_display_sample,
                self.Label_display_sample
            )
            # print(return_value)

            # self.inputTrain_File_Array = []
            # self.inputValidation_File_Array = []
            self.inputTest_File_Array = []
            self.outputTest_File_Array = []

            if self.is_Runing:
                self.is_Runing = not self.is_Runing
            if self.is_Runing:
                self.Button_start_and_stop_Test['text'] = "Stop Test"
                self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            else:
                self.Button_start_and_stop_Test['text'] = "Start Test"
                self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

            # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
            # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
            print(return_value)
            # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
            self.Label_State['text'] = str('\n'.join(return_value.split(',')))
            # self.Label_State['text'] = "Stand by"

            self.Label_display_sample['text'] = "Input file"  # "悟空，您好.",
            self.Canvas_display_sample.delete("all")

            # 使用消息提示框控件給出溫馨提示;
            tk_messagebox.showinfo(
                title = "溫馨提示",
                message = str('\n'.join(return_value.split(',')))
            )

            return return_value  # None

    def click_Button_start_and_stop_Test(self):

        # global self.screenwidth
        # global self.screenheight
        # global self.is_storage_position
        # global self.is_storage_type
        # global default_input_tabel_tesseract_config  # = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        # global input_tabel_tesseract_config  # = self.default_input_tabel_tesseract_config
        # global inputTabelTesseractConfig  # = tk.StringVar(value=self.default_input_tabel_tesseract_config)
        # global default_input_measuringRuler_tesseract_config  # = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        # global input_measuringRuler_tesseract_config  # = self.default_input_measuringRuler_tesseract_config
        # global inputMeasuringRulerTesseractConfig  # = tk.StringVar(value=self.default_input_measuringRuler_tesseract_config)
        # global self.default_input_tabel_tesseract_config  # = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        # global self.input_tabel_tesseract_config  # = self.default_input_tabel_tesseract_config
        # global self.inputTabelTesseractConfig  # = tk.StringVar(value=self.default_input_tabel_tesseract_config)
        # global self.default_input_measuringRuler_tesseract_config  # = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        # global self.input_measuringRuler_tesseract_config  # = self.default_input_measuringRuler_tesseract_config
        # global self.inputMeasuringRulerTesseractConfig  # = tk.StringVar(value=self.default_input_measuringRuler_tesseract_config)
        # global self.inputTrain_path
        # global self.inputTrain_File_Array
        # # global self.inputValidation_path
        # # global self.inputValidation_File_Array
        # global self.inputTest_path
        # global self.inputTest_File_Array
        # global self.outputTest_path
        # global self.outputTest_File_Array
        # global self.outputTest_URL

        # global self.complete_Number
        self.complete_Number = int(0)

        # global self.is_Concurrent
        # if self.is_Concurrent == "Multi-Threading":
        #     if not self.outqueue_from_task_to_host:
        #         self.outqueue_from_task_to_host = queue.Queue(maxsize=0)
        #     if not self.outqueue_from_host_to_task:
        #         self.outqueue_from_host_to_task = queue.Queue(maxsize=0)

        # global self.is_Runing
        self.is_Runing = not self.is_Runing
        if self.is_Runing:

            if self.is_Concurrent == "Multi-Threading":
                if self.outqueue_from_host_to_task:
                    self.outqueue_from_host_to_task.put(
                        [
                            "is_Runing_True",
                            ""
                        ],
                        block=False,
                        timeout=None
                    )

            self.Button_start_and_stop_Test['text'] = "Stop Test"
            self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # self.Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

        else:
            # print("程式被中止.")
            if self.is_Concurrent == "Multi-Threading":
                if self.outqueue_from_host_to_task:
                    self.outqueue_from_host_to_task.put(
                        [
                            "is_Runing_False",
                            ""
                        ],
                        block=False,
                        timeout=None
                    )

            if self.is_Concurrent == "0" or self.is_Concurrent == 0:
                # sys.stdout.write('\n')
                # sys.stdout.write("Discontinue," + str(self.complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTest_path + "," + self.outputTest_path)  # 將字符串輸出寫到操作系統控制臺;
                print("Discontinue," + str(self.complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTest_path + "," + self.outputTest_path)  # 將字符串輸出寫到操作系統控制臺;
                # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                # self.Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + self.inputTest_path + " ]." + "\n" + "Output: [ " + self.outputTest_path + " ]." + "\n" + "discontinue [ " + str(self.complete_Number) + " ]."
                self.Label_State['text'] = "Stand by"

                self.Button_start_and_stop_Test['text'] = "Start Test"
                self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

                # 使用消息提示框控件給出溫馨提示;
                tk_messagebox.showinfo(
                    title = "溫馨提示",
                    message = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + self.inputTest_path + " ]." + "\n" + "Output: [ " + self.outputTest_path + " ]." + "\n" + "Discontinue [ " + str(self.complete_Number) + " ]."
                )

            return "Discontinue," + str(self.complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTest_path + "," + self.outputTest_path  # None

        # global self.Error_Log
        self.Error_Log = []

        self.input_tabel_tesseract_config = str(self.Entry_tabel_tesseract_config.get())  # 讀取表格（tabel）内的文本識別（Google tesseract）的參數（tesseract config）文本輸入框輸入的内容; # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        global input_tabel_tesseract_config
        input_tabel_tesseract_config = self.input_tabel_tesseract_config
        self.input_measuringRuler_tesseract_config = str(self.Entry_measuringRuler_tesseract_config.get())  # 讀取測量尺（Measuring Ruler）標識的文本識別（Google tesseract）的參數（tesseract config）文本框輸入的内容; # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        global input_measuringRuler_tesseract_config
        input_measuringRuler_tesseract_config = self.input_measuringRuler_tesseract_config
        optical_character_recognition.tabel_tesseract_config = self.input_tabel_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        optical_character_recognition.measuringRuler_tesseract_config = self.input_measuringRuler_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;

        self.inputTrain_path = str(self.Entry_inputTrain_path.get())  # 讀取訓練集樣本位置文本框輸入的内容;

        if len(self.inputTrain_path) == 0:

            # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.inputTrain_path))  # 將字符串輸出寫到操作系統控制臺;
            print("運行錯誤." + "\n" + "訓練集樣本傳入路徑: " + "\n" + "[ " + self.inputTrain_path + " ]" + "\n" + "爲空.")
            # self.Label_State['text'] = "參數錯誤." + "\n" + "訓練集樣本傳入路徑: " + "\n" + "[ " + self.inputTrain_path + " ]" + "\n" + "爲空."
            self.Label_State['text'] = "Stand by"

            # self.Error_Log.append(self.inputTrain_path)

            if self.is_Runing:
                self.is_Runing = not self.is_Runing
            if self.is_Runing:
                self.Button_start_and_stop_Test['text'] = "Stop Test"
                self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            else:
                self.Button_start_and_stop_Test['text'] = "Start Test"
                self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

            # 使用消息提示框控件給出溫馨提示;
            tk_messagebox.showinfo(
                title = "溫馨提示",
                message = "參數錯誤." + "\n" + "訓練集樣本傳入路徑: " + "\n" + "[ " + self.inputTrain_path + " ]" + "\n" + "爲空."
            )

            return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTrain_path

        self.inputTrain_path = str(self.inputTrain_path).replace('\\', '/')
        # print("input train path:", self.inputTrain_path)

        # self.inputValidation_path = str(self.Entry_inputValidation_path.get())  # 讀取驗證集樣本位置文本框輸入的内容;

        # if len(self.inputValidation_path) == 0:

        #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.inputValidation_path))  # 將字符串輸出寫到操作系統控制臺;
        #     print("運行錯誤." + "\n" + "驗證集樣本傳入路徑: " + "\n" + "[ " + self.inputValidation_path + " ]" + "\n" + "爲空.")
        #     # self.Label_State['text'] = "參數錯誤." + "\n" + "驗證集樣本傳入路徑: " + "\n" + "[ " + self.inputValidation_path + " ]" + "\n" + "爲空."
        #     self.Label_State['text'] = "Stand by"

        #     # self.Error_Log.append(self.inputValidation_path)

        #     if self.is_Runing:
        #         self.is_Runing = not self.is_Runing
        #     if self.is_Runing:
        #         self.Button_start_and_stop_Test['text'] = "Stop Test"
        #         self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         # self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         # self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     else:
        #         self.Button_start_and_stop_Test['text'] = "Start Test"
        #         self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #         # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #         self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

        #     # 使用消息提示框控件給出溫馨提示;
        #     tk_messagebox.showinfo(
        #         title = "溫馨提示",
        #         message = "參數錯誤." + "\n" + "驗證集樣本傳入路徑: " + "\n" + "[ " + self.inputValidation_path + " ]" + "\n" + "爲空."
        #     )

        #     return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputValidation_path

        # self.inputValidation_path = str(self.inputValidation_path).replace('\\', '/')
        # # print("input validation path:", self.inputValidation_path)

        self.inputTest_path = str(self.Entry_inputTest_path.get())  # 讀取測試集樣本位置文本框輸入的内容;

        if len(self.inputTest_path) == 0:

            # sys.stdout.write("Error," + + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," str(self.inputTest_path))  # 將字符串輸出寫到操作系統控制臺;
            print("運行錯誤." + "\n" + "測試集樣本傳入路徑: " + "\n" + "[ " + self.inputTest_path + " ]" + "\n" + "爲空.")
            # self.Label_State['text'] = "參數錯誤." + "\n" + "測試集樣本傳入路徑: " + "\n" + "[ " + self.inputTest_path + " ]" + "\n" + "爲空."
            self.Label_State['text'] = "Stand by"

            # self.Error_Log.append(self.inputTest_path)

            if self.is_Runing:
                self.is_Runing = not self.is_Runing
            if self.is_Runing:
                self.Button_start_and_stop_Test['text'] = "Stop Test"
                self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            else:
                self.Button_start_and_stop_Test['text'] = "Start Test"
                self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

            # 使用消息提示框控件給出溫馨提示;
            tk_messagebox.showinfo(
                title = "溫馨提示",
                message = "參數錯誤." + "\n" + "測試集樣本傳入路徑: " + "\n" + "[ " + self.inputTest_path + " ]" + "\n" + "爲空."
            )

            return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.inputTest_path

        self.inputTest_path = str(self.inputTest_path).replace('\\', '/')
        # print("input test path:", self.inputTest_path)

        # global self.is_storage_type
        self.is_storage_type = str(self.Radiobutton_storage_type_Var.get())
        # print("storage type:", self.is_storage_type)

        self.outputTest_path = str(self.Entry_outputTest_path.get())  # 讀取結果輸出位置文本框輸入的内容;

        if len(self.outputTest_path) == 0:

            if len(self.is_storage_position) == 0:
                self.is_storage_position = ""
                # self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                # self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            elif self.is_storage_position == "Disk":
                self.is_storage_position = ""
                # self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                # self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            elif self.is_storage_position == "Database_and_Disk":
                self.is_storage_position = "Database"
                # self.Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                self.Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                self.Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                # self.Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;

            self.is_storage_type = ""
            # print("storage type:", self.is_storage_type)

            # self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
            self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
            # self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
            self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
            # self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
            self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
            # self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
            self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

            # # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
            # print("運行錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "爲空.")
            # # self.Label_State['text'] = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "爲空."
            # self.Label_State['text'] = "Stand by"

            # # self.Error_Log.append(self.outputTest_path)

            # if self.is_Runing:
            #     self.is_Runing = not self.is_Runing
            # if self.is_Runing:
            #     self.Button_start_and_stop_Test['text'] = "Stop Test"
            #     self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     # self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     # self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     # self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     # self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     # self.Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # else:
            #     self.Button_start_and_stop_Test['text'] = "Start Test"
            #     self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            #     # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            #     self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

            # # 使用消息提示框控件給出溫馨提示;
            # tk_messagebox.showinfo(
            #     title = "溫馨提示",
            #     message = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "爲空."
            # )

            # return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.outputTest_path

        self.outputTest_path = str(self.outputTest_path).replace('\\', '/')
        # print("output test path:", self.outputTest_path)

        if len(self.outputTest_path) > 0:

            if self.outputTest_path.find(".", 0, int(len(self.outputTest_path)-1)) != -1:

                self.is_storage_type = str(self.outputTest_path.split('.')[len(self.outputTest_path.split('.'))-1])
                # print("storage type:", self.is_storage_type)
                if self.is_storage_type == "json":
                    self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_txt.deselect()
                    self.Radiobutton_storage_type_Excel.deselect()
                    self.Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                elif self.is_storage_type == "csv":
                    self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_txt.deselect()
                    self.Radiobutton_storage_type_Excel.deselect()
                    self.Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                elif self.is_storage_type == "txt":
                    self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_csv.deselect()
                    self.Radiobutton_storage_type_Excel.deselect()
                    self.Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                elif self.is_storage_type == "xlsx":
                    self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_csv.deselect()
                    self.Radiobutton_storage_type_txt.deselect()
                    self.Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                elif len(self.is_storage_type) == 0:
                    self.Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    self.Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                else:
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                    print("運行錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規.")
                    # self.Label_State['text'] = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規."
                    self.Label_State['text'] = "Stand by"

                    # self.Error_Log.append(self.outputTest_path)

                    if self.is_Runing:
                        self.is_Runing = not self.is_Runing
                    if self.is_Runing:
                        self.Button_start_and_stop_Test['text'] = "Stop Test"
                        self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    else:
                        self.Button_start_and_stop_Test['text'] = "Start Test"
                        self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

                    # 使用消息提示框控件給出溫馨提示;
                    tk_messagebox.showinfo(
                        title = "溫馨提示",
                        message = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規."
                    )

                    return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.outputTest_path

            else:

                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                print("運行錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規.")
                # self.Label_State['text'] = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規."
                self.Label_State['text'] = "Stand by"

                # self.Error_Log.append(self.outputTest_path)

                if self.is_Runing:
                    self.is_Runing = not self.is_Runing
                if self.is_Runing:
                    self.Button_start_and_stop_Test['text'] = "Stop Test"
                    self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # self.Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                else:
                    self.Button_start_and_stop_Test['text'] = "Start Test"
                    self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

                # 使用消息提示框控件給出溫馨提示;
                tk_messagebox.showinfo(
                    title = "溫馨提示",
                    message = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + self.outputTest_path + " ]" + "\n" + "類型不合規."
                )

                return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + self.outputTest_path

        # global self.time_sleep
        # global self.file_Data
        # # global self.file_Data_bytes
        # # global self.file_Data_len
        self.file_Data = ""
        # # self.file_Data_bytes = self.file_Data.encode("utf-8")
        # # self.file_Data = self.file_Data_bytes.decode("utf-8")
        # # self.file_Data = str(self.file_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
        # # self.file_Data_len = len(bytes(self.file_Data, "utf-8"))
        # global self.result_Data
        self.result_Data = ""
        # # self.result_Data_bytes = self.result_Data.encode("utf-8")
        # # self.result_Data = self.result_Data_bytes.decode("utf-8")
        # # self.result_Data = str(self.result_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
        # # self.result_Data_len = len(bytes(self.result_Data, "utf-8"))
        # global self.image_sample
        self.image_sample = []

        # print(self.inputTrain_path)
        if len(self.inputTrain_File_Array) == 0:
            if len(self.inputTrain_path) > 0:
                # self.inputTrain_File_Array = []
                self.inputTrain_File_Array = self.Path_Conversion(self.inputTrain_path, self.time_sleep)[0]

        # print(self.inputValidation_path)
        # if len(self.inputValidation_File_Array) == 0:
        #     if len(self.inputValidation_path) > 0:
        #         # self.inputValidation_File_Array = []
        #         self.inputValidation_File_Array = self.Path_Conversion(self.inputValidation_path, self.time_sleep)[0]

        # print(self.inputTest_path)
        if len(self.inputTest_File_Array) == 0:
            if len(self.inputTest_path) > 0:
                # self.inputTest_File_Array = []
                self.inputTest_File_Array = self.Path_Conversion(self.inputTest_path, self.time_sleep)[0]

        # print(self.outputTest_path)
        if len(self.outputTest_File_Array) == 0:
            if len(self.outputTest_path) > 0:
                # # self.outputTest_File_Array = []
                # self.outputTest_File_Array = self.Path_Conversion(self.outputTest_path, self.time_sleep)[0]
                self.outputTest_File_Array = [self.outputTest_path]

        # 讀取多行文本輸入框中的内容;
        Text_display_result_value = self.Text_display_result.get(
            "0.0",  # 表示讀取多行文本輸入框 .Text 控件中的全部值，如果設定參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始讀取;
            "end"  # 表示讀取至多行文本輸入框 .Text 控件中全部值的最後一個字符爲止;
        )
        Text_display_result_value = str(Text_display_result_value)
        # print(Text_display_result_value)

        if len(Text_display_result_value) > 0:

            # 刪除多行文本輸入框中的内容;
            self.Text_display_result.delete(
                "1.0",  # 參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始刪除;
                "end"  # 參數爲 "end" 表示刪除直至最後一個字符，即清空輸入框;
            )

            self.Text_display_result.see("end"),  # 表示將 .Text 組件中聚焦在文本末行，即顯示末尾;

        # # 將字符串寫入多行文本輸入框;
        # self.Text_display_result.insert(
        #     "end",  # 參數 "1.0" 表示從第一行第一列開始插入，參數 "insert" 表示在當前光標位置處插入一個字符串，參數 "end" 表示在末尾位置處追加寫入一個字符串;
        #     str(new_Text_display_result_value)
        # )

        return_value = ""

        if self.is_Concurrent == "Multi-Threading":

            # if not self.is_window:
            #     self.screenwidth = int(0)
            #     self.screenheight = int(0)
            # self.outqueue_from_task_to_host = queue.Queue(maxsize=0)
            # self.outqueue_from_host_to_task = queue.Queue(maxsize=0)

            # print("process-" + str(multiprocessing.current_process().pid) + " thread-" + str(threading.currentThread().ident) + " ( name: " + str(threading.currentThread().name) + " )")

            # # 使用 Python 原生的多執行緒（綫程）支持 threading 庫的 threading.Thread(target=do_Function, args=(args1, args2)) 創建一個子綫程，用於調用讀取指定文檔並處理數據函數;
            # # 第一個參數 target=do_Function 是子執行緒（綫程）函數變量，第二個參數 args=(args1, args2) 是一個數組變量參數，如果只傳遞一個參數就只需要 args1，如果要傳遞多個參數，可以使用元組，當元組中只包含一個元素時，需要在元素後面添加逗號，例如 args=(args1,) 形式;
            # t = threading.Thread(target=read_file_do_Function, args=(monitor_file,), daemon=True)
            # # 參數：daemon=True，表示把創建的子綫程設爲守護綫程，當主綫程關閉時，子綫程同時關閉，這個標識必須在 .start() 方法調用之前設置;
            # t.start()  # 啓動子綫程;
            # # threading.Condition()

            # # 使用 Python 原生的多進程支持 multiprocessing 庫的 multiprocessing.Process(target=do_Function, args=(args1, args2)) 創建一個子進程，用於調用讀取指定文檔並處理數據函數;
            # # 第一個參數 target=do_Function 是子進程函數變量，第二個參數 args=(args1, args2) 是一個數組變量參數，如果只傳遞一個參數就只需要 args1，如果要傳遞多個參數，可以使用元組，當元組中只包含一個元素時，需要在元素後面添加逗號，例如 args=(args1,) 形式;
            # p = multiprocessing.Process(target=read_file_do_Function, args=(monitor_file, monitor_dir, do_Function, output_dir, output_file, to_executable, to_script))
            # p.setDaemon(True)  # 把創建的子進程設爲守護進程，當主綫程關閉時，子進程同時關閉，這個標識必須在 .start() 方法調用之前設置;
            # p.start()  # 啓動子進程;
            # P.close()  # 關閉Process物件，並釋放與之關聯的所有資源，如果底層進程仍在運行，則會引發ValueError。而且，一旦close()方法成功返回，Process物件的大多數方法和屬性也可能會引發ValueError;
            # # P.terminate  # 强制終止進程子進程，如果調用此函數,進程P將被立即終止，同時不會進行任何清理動作，在Unix上使用的是SIGTERM信號，在Windows上使用的是TerminateProcess()。注意，進程的後代進程不會被終止（會變成“孤兒”進程）。另外，如果被終止的進程在使用Pipe或Queue時，它們有可能會被損害，並無法被其他進程使用；如果被終止的進程已獲得鎖或信號量等，則有可能導致其他進程鎖死。所以請謹慎使用此方法，如果p保存了一個鎖或參與了進程間通信，那麼終止它可能會導致鎖死或I/O損壞;
            # p.join()  # .join() 函數會使得主進程阻塞等待，直到該被調用的子進程運行結束或超時，才繼續執行主進程，要在 .close() 和 .terminate 方法之後使用;
            # # p.pid
            # # p.name
            # # p.ident
            # # p.sentinel

            self.initializer_Window.after(5, self.Queue_update, self.outqueue_from_task_to_host)

            thr = threading.Thread(
                target = self.Run_Input_and_Output_Function,
                args = (
                    self.Path_Conversion,
                    self.Input_and_Output_Function,
                    self.is_window,
                    self.screenwidth,
                    self.screenheight,
                    self.is_Concurrent,
                    self.is_storage_position,
                    self.is_storage_type,
                    self.inputTrain_path,
                    self.inputTrain_File_Array,
                    self.inputTest_path,
                    self.inputTest_File_Array,
                    self.do_Function,
                    self.outputTest_path,
                    self.outputTest_File_Array,
                    self.outputTest_URL,
                    self.time_sleep,
                    self.outqueue_from_task_to_host,
                    self.outqueue_from_host_to_task,
                    self.is_Runing,
                    self.file_Data,
                    self.result_Data,
                    self.complete_Number,
                    self.Error_Log,
                    self.Label_State,
                    self.Text_display_result,
                    self.image_sample,
                    self.Canvas_display_sample,
                    self.Label_display_sample
                ),
                daemon = True  # 把創建的子綫程設爲守護綫程，當主綫程關閉時，子綫程同時關閉，這個標識必須在 .start() 方法調用之前設置;
            )
            thr.start()

        if self.is_Concurrent == "0" or self.is_Concurrent == 0:

            # if not self.is_window:
            #     self.screenwidth = int(0)
            #     self.screenheight = int(0)
            # self.outqueue_from_task_to_host = None
            # self.outqueue_from_host_to_task = None

            return_value = self.Run_Input_and_Output_Function(
                self.Path_Conversion,
                self.Input_and_Output_Function,
                self.is_window,
                self.screenwidth,
                self.screenheight,
                self.is_Concurrent,
                self.is_storage_position,
                self.is_storage_type,
                self.inputTrain_path,
                self.inputTrain_File_Array,
                self.inputTest_path,
                self.inputTest_File_Array,
                self.do_Function,
                self.outputTest_path,
                self.outputTest_File_Array,
                self.outputTest_URL,
                self.time_sleep,
                self.outqueue_from_task_to_host,
                self.outqueue_from_host_to_task,
                self.is_Runing,
                self.file_Data,
                self.result_Data,
                self.complete_Number,
                self.Error_Log,
                self.Label_State,
                self.Text_display_result,
                self.image_sample,
                self.Canvas_display_sample,
                self.Label_display_sample
            )
            # print(return_value)

            # self.inputTrain_File_Array = []
            # self.inputValidation_File_Array = []
            self.inputTest_File_Array = []
            self.outputTest_File_Array = []

            if self.is_Runing:
                self.is_Runing = not self.is_Runing
            if self.is_Runing:
                self.Button_start_and_stop_Test['text'] = "Stop Test"
                self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            else:
                self.Button_start_and_stop_Test['text'] = "Start Test"
                self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

            # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
            # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
            print(return_value)
            # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
            self.Label_State['text'] = str('\n'.join(return_value.split(',')))
            # self.Label_State['text'] = "Stand by"

            self.Label_display_sample['text'] = "Input file"  # "悟空，您好.",
            self.Canvas_display_sample.delete("all")

            # 使用消息提示框控件給出溫馨提示;
            tk_messagebox.showinfo(
                title = "溫馨提示",
                message = str('\n'.join(return_value.split(',')))
            )

            return return_value  # None

    def click_Button_shut_down(self):

        self.initializer_Window.quit()  # 關閉窗口，可以從窗口小部件取值;
        # self.initializer_Window.destroy()  # 關閉窗口，不能再從窗口小部件取值;
        # self.initializer_Window.iconify()  # 窗口最小化;
        # self.initializer_Window.maxsize()  # 窗口最大化;

        return None

    def Queue_update(self, outqueue_from_task_to_host):

        # # global self.inputTrain_File_Array
        # # global self.inputValidation_File_Array
        # global self.inputTest_File_Array
        # global self.outputTest_File_Array
        # global self.image_sample
        # global self.is_Runing
        # global self.is_window
    
        # self.outqueue_from_task_to_host = outqueue[0]
        # self.outqueue_from_host_to_task = outqueue[1]

        try:

            if outqueue_from_task_to_host.empty():
                self.initializer_Window.after(5, self.Queue_update, outqueue_from_task_to_host)
                pass

            if not outqueue_from_task_to_host.empty():

                msg = outqueue_from_task_to_host.get(
                    block=False,
                    timeout=None
                )

                if msg[0] == "Complete":

                    # self.inputTrain_File_Array = []
                    # self.inputValidation_File_Array = []
                    self.inputTest_File_Array = []
                    self.outputTest_File_Array = []

                    if self.is_Runing:
                        self.is_Runing = not self.is_Runing
                    if self.is_Runing:
                        self.Button_start_and_stop_Test['text'] = "Stop Test"
                        self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;















                        self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;














                        # self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    else:
                        self.Button_start_and_stop_Test['text'] = "Start Test"
                        self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;














                        self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;















                        # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

                    return_value = str(','.join(msg))
                    # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                    # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                    print(return_value)
                    # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                    self.Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
                    # self.Label_State['text'] = "Stand by"
                    self.Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                    self.Canvas_display_sample.delete("all")

                    # 使用消息提示框控件給出溫馨提示;
                    tk_messagebox.showinfo(
                        title = "溫馨提示",
                        message = str('\n'.join(return_value.split(',')))
                    )

                    return return_value  # None

                elif msg[0] == "Error":

                    # self.inputTrain_File_Array = []
                    # self.inputValidation_File_Array = []
                    self.inputTest_File_Array = []
                    self.outputTest_File_Array = []

                    if self.is_Runing:
                        self.is_Runing = not self.is_Runing
                    if self.is_Runing:
                        self.Button_start_and_stop_Test['text'] = "Stop Test"
                        self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
















                        self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
















                        # self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    else:
                        self.Button_start_and_stop_Test['text'] = "Start Test"
                        self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;


















                        self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

















                        # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

                    return_value = str(','.join(msg))
                    # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                    # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                    print(return_value)
                    # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                    self.Label_State['text'] = str('\n'.join(str(','.join(msg)).split(',')))
                    # self.Label_State['text'] = "Stand by"
                    self.Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                    self.Canvas_display_sample.delete("all")

                    # 使用消息提示框控件給出溫馨提示;
                    tk_messagebox.showinfo(
                        title = "溫馨提示",
                        message = str('\n'.join(return_value.split(',')))
                    )

                    return return_value  # None

                elif msg[0] == "Discontinue":

                    # self.inputTrain_File_Array = []
                    # self.inputValidation_File_Array = []
                    self.inputTest_File_Array = []
                    self.outputTest_File_Array = []

                    if self.is_Runing:
                        self.is_Runing = not self.is_Runing
                    if self.is_Runing:
                        self.Button_start_and_stop_Test['text'] = "Stop Test"
                        self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;


















                        self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

















                        # self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    else:
                        self.Button_start_and_stop_Test['text'] = "Start Test"
                        self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;












                        self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;












                        # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                        # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                        self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

                    return_value = str(','.join(msg))
                    # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                    # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                    print(return_value)
                    # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                    self.Label_State['text'] = str('\n'.join(str(','.join(msg)).split(',')))
                    # self.Label_State['text'] = "Stand by"
                    self.Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                    self.Canvas_display_sample.delete("all")

                    # 使用消息提示框控件給出溫馨提示;
                    tk_messagebox.showinfo(
                        title = "溫馨提示",
                        message = str('\n'.join(return_value.split(',')))
                    )

                    return return_value  # None

                elif msg[0] == "Runing":

                    return_value = str(','.join(msg))
                    # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                    # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                    # print(return_value)
                    # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                    self.Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
                    # self.Label_State['text'] = "Stand by"
                    # self.Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                    # self.Canvas_display_sample.delete("all")

                    self.initializer_Window.after(5, self.Queue_update, outqueue_from_task_to_host)

                elif msg[0] == "image_sample_delete":

                    # return_value = str(','.join(msg))
                    # # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                    # # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                    # print(return_value)
                    # # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                    # self.Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
                    # self.Label_State['text'] = "Stand by"
                    self.Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                    self.Canvas_display_sample.delete("all")
                    self.image_sample = []

                    self.initializer_Window.after(5, self.Queue_update, outqueue_from_task_to_host)

                elif msg[0] == "image_sample":

                    # return_value = str(','.join(msg))
                    # # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                    # # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                    # print(return_value)
                    # # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                    # self.Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
                    # self.Label_State['text'] = "Stand by"
                    self.Label_display_sample['text'] = str(msg[1])  # "悟空，您好.",
                    self.image_sample = msg[2]
                    self.Canvas_display_sample.delete("all")
                    # self.Canvas_display_sample.delete(tag="one")
                    self.Canvas_display_sample.create_image(
                        0,
                        0,
                        anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
                        image=self.image_sample,
                        # fill="red",
                        tag="one"
                    )

                    self.initializer_Window.after(5, self.Queue_update, outqueue_from_task_to_host)

                elif msg[0] == "Succeed":

                    return_value = str(','.join(str(msg[5]).split('\n')))
                    print(return_value)

                    # 將運算結果寫入用於展示結果的多行文本輸入框;
                    # self.Label_State['text'] = "Succeed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(input_Test_File_Array[i])
                    # self.Label_State['text'] = "Succeed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
                    self.Label_State['text'] = msg[5]

                    # # 讀取多行文本輸入框中的内容;
                    # Text_display_result_value = self.Text_display_result.get(
                    #     "0.0",  # 表示讀取多行文本輸入框 .Text 控件中的全部值，如果設定參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始讀取;
                    #     "end"  # 表示讀取至多行文本輸入框 .Text 控件中全部值的最後一個字符爲止;
                    # )
                    # Text_display_result_value = str(Text_display_result_value)
                    # print(Text_display_result_value)

                    # # 刪除多行文本輸入框中的内容;
                    # self.Text_display_result.delete(
                    #     "1.0",  # 參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始刪除;
                    #     "end"  # 參數爲 "end" 表示刪除直至最後一個字符，即清空輸入框;
                    # )

                    # new_Text_display_result_value = Text_display_result_value + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.input_Test_File_Array[i]) + "," + str(self.result_Data)

                    # new_Text_display_result_value = str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(self.input_Test_File_Array[i]) + "," + str(self.result_Data) + "\n"
                    # new_Text_display_result_value = str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(self.input_Test_File_Array[i]))).replace('\\', '/') + "\n"
                    # print(new_Text_display_result_value)

                    # 將字符串寫入多行文本輸入框;
                    self.Text_display_result.insert(
                        "end",  # 參數 "1.0" 表示從第一行第一列開始插入，參數 "insert" 表示在當前光標位置處插入一個字符串，參數 "end" 表示在末尾位置處追加寫入一個字符串;
                        str(msg[4])  # str(new_Text_display_result_value)
                    )

                    self.Text_display_result.see("end"),  # 表示將 .Text 組件中聚焦在文本末行，即顯示末尾;

                    # return_value = str(','.join(msg))
                    # # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                    # # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                    # print(return_value)
                    # # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                    # self.Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
                    # # self.Label_State['text'] = "Stand by"

                    # self.Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                    # self.Canvas_display_sample.delete("all")

                    self.initializer_Window.after(5, self.Queue_update, outqueue_from_task_to_host)

                elif msg[0] == "Wrong":

                    return_value = str(','.join(msg))
                    # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                    # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                    print(return_value)
                    # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                    self.Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
                    # self.Label_State['text'] = "Stand by"
                    # self.Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                    # self.Canvas_display_sample.delete("all")

                    self.initializer_Window.after(5, self.Queue_update, outqueue_from_task_to_host)

            # else:
            #     # By not calling self.initializer_Window.after here, we allow update to
            #     # truly end
            #     self.initializer_Window.after(50, self.Queue_update, (outqueue_from_task_to_host, outqueue_from_host_to_task))
            #     pass
        except queue.Empty:
            self.initializer_Window.after(5, self.Queue_update, outqueue_from_task_to_host)

    # 將任何按鍵都綁定到 break 功能，以使多行輸入文本框（tkinter.Text）組件中的内容設置爲只讀，除了「Ctrl」+「c」和「Shift」+「↑」+「↓」+「←」+「→」鍵，從而不鎖定文本複製的功能;
    def ctrlEvent(self, event):
        if (12==event.state and event.keysym=='c') or (event.keysym=='Up') or (event.keysym=='Down') or (event.keysym=='Left') or (event.keysym=='Right'):
            return
        else:
            return "break"

    def on_closing(self):

        # 使用消息提示框控件給出溫馨提示;
        # tk_messagebox.showinfo(
        #     title="溫馨提示",
        #     message="窗口關閉事件被觸發：WM_DELETE_WINDOW"
        # )

        # # 使用消息問詢框控件做確認動作;
        # if tk_messagebox.askokcancel("Quit", "Do you want to quit?"):
        #     self.initializer_Window.quit()  # 關閉窗口，可以從窗口小部件取值;
        #     # self.initializer_Window.destroy()  # 關閉窗口，不能再從窗口小部件取值;

        self.initializer_Window.quit()  # 關閉窗口，可以從窗口小部件取值;
        # self.initializer_Window.destroy()  # 關閉窗口，不能再從窗口小部件取值;
        # self.initializer_Window.iconify()  # 窗口最小化;
        # self.initializer_Window.maxsize()  # 窗口最大化;

        return None

    # 子進程中的初始化預設值（默認值）配置函數;
    def initializer(self):

        """Ignore SIGINT in child workers. 忽略子進程中的信號."""
        # 忽略子進程中的信號，不然鍵盤輸入 [Ctrl]+[c] 中止主進程運行時，會報 Traceback (most recent call last) 和 KeyboardInterrupt 的錯誤;
        signal.signal(signal.SIGINT, signal.SIG_IGN)  # 忽略子進程中的信號，不然鍵盤輸入 [Ctrl]+[c] 中止主進程運行時，會報 Traceback (most recent call last) 和 KeyboardInterrupt 的錯誤;

    def start(self):

        result_tuple = None  # multiprocessing.current_process();

        # # 主窗口循環顯示;
        # self.initializer_Window.mainloop()
        # # 注意，loop 是循環的意思，該行代碼會讓窗口（window）不斷地刷新，如果沒有 .mainloop() ，就會是一個靜態的窗口（window），所有的窗口對象 tk.TK() 都必須有 .mainloop() 函數;

        return result_tuple

    def run(self):

        return_value = ""

        # if self.is_Concurrent == "Multi-Threading":

        #     # if not self.is_window:
        #     #     self.screenwidth = int(0)
        #     #     self.screenheight = int(0)
        #     # self.outqueue_from_task_to_host = queue.Queue(maxsize=0)
        #     # self.outqueue_from_host_to_task = queue.Queue(maxsize=0)

        #     # print("process-" + str(multiprocessing.current_process().pid) + " thread-" + str(threading.currentThread().ident) + " ( name: " + str(threading.currentThread().name) + " )")

        #     # # 使用 Python 原生的多執行緒（綫程）支持 threading 庫的 threading.Thread(target=do_Function, args=(args1, args2)) 創建一個子綫程，用於調用讀取指定文檔並處理數據函數;
        #     # # 第一個參數 target=do_Function 是子執行緒（綫程）函數變量，第二個參數 args=(args1, args2) 是一個數組變量參數，如果只傳遞一個參數就只需要 args1，如果要傳遞多個參數，可以使用元組，當元組中只包含一個元素時，需要在元素後面添加逗號，例如 args=(args1,) 形式;
        #     # t = threading.Thread(target=read_file_do_Function, args=(monitor_file,), daemon=True)
        #     # # 參數：daemon=True，表示把創建的子綫程設爲守護綫程，當主綫程關閉時，子綫程同時關閉，這個標識必須在 .start() 方法調用之前設置;
        #     # t.start()  # 啓動子綫程;
        #     # # threading.Condition()

        #     # # 使用 Python 原生的多進程支持 multiprocessing 庫的 multiprocessing.Process(target=do_Function, args=(args1, args2)) 創建一個子進程，用於調用讀取指定文檔並處理數據函數;
        #     # # 第一個參數 target=do_Function 是子進程函數變量，第二個參數 args=(args1, args2) 是一個數組變量參數，如果只傳遞一個參數就只需要 args1，如果要傳遞多個參數，可以使用元組，當元組中只包含一個元素時，需要在元素後面添加逗號，例如 args=(args1,) 形式;
        #     # p = multiprocessing.Process(target=read_file_do_Function, args=(monitor_file, monitor_dir, do_Function, output_dir, output_file, to_executable, to_script))
        #     # p.setDaemon(True)  # 把創建的子進程設爲守護進程，當主綫程關閉時，子進程同時關閉，這個標識必須在 .start() 方法調用之前設置;
        #     # p.start()  # 啓動子進程;
        #     # P.close()  # 關閉Process物件，並釋放與之關聯的所有資源，如果底層進程仍在運行，則會引發ValueError。而且，一旦close()方法成功返回，Process物件的大多數方法和屬性也可能會引發ValueError;
        #     # # P.terminate  # 强制終止進程子進程，如果調用此函數,進程P將被立即終止，同時不會進行任何清理動作，在Unix上使用的是SIGTERM信號，在Windows上使用的是TerminateProcess()。注意，進程的後代進程不會被終止（會變成“孤兒”進程）。另外，如果被終止的進程在使用Pipe或Queue時，它們有可能會被損害，並無法被其他進程使用；如果被終止的進程已獲得鎖或信號量等，則有可能導致其他進程鎖死。所以請謹慎使用此方法，如果p保存了一個鎖或參與了進程間通信，那麼終止它可能會導致鎖死或I/O損壞;
        #     # p.join()  # .join() 函數會使得主進程阻塞等待，直到該被調用的子進程運行結束或超時，才繼續執行主進程，要在 .close() 和 .terminate 方法之後使用;
        #     # # p.pid
        #     # # p.name
        #     # # p.ident
        #     # # p.sentinel

        #     self.initializer_Window.after(5, self.Queue_update, self.outqueue_from_task_to_host)

        #     thr = threading.Thread(
        #         target = self.Run_Input_and_Output_Function,
        #         args = (
        #             self.Path_Conversion,
        #             self.Input_and_Output_Function,
        #             self.is_window,
        #             self.screenwidth,
        #             self.screenheight,
        #             self.is_Concurrent,
        #             self.is_storage_position,
        #             self.is_storage_type,
        #             self.inputTrain_path,
        #             self.inputTrain_File_Array,
        #             self.inputTest_path,
        #             self.inputTest_File_Array,
        #             self.do_Function,
        #             self.outputTest_path,
        #             self.outputTest_File_Array,
        #             self.outputTest_URL,
        #             self.time_sleep,
        #             self.outqueue_from_task_to_host,
        #             self.outqueue_from_host_to_task,
        #             self.is_Runing,
        #             self.file_Data,
        #             self.result_Data,
        #             self.complete_Number,
        #             self.Error_Log,
        #             self.Label_State,
        #             self.Text_display_result,
        #             self.image_sample,
        #             self.Canvas_display_sample,
        #             self.Label_display_sample
        #         ),
        #         daemon = True  # 把創建的子綫程設爲守護綫程，當主綫程關閉時，子綫程同時關閉，這個標識必須在 .start() 方法調用之前設置;
        #     )
        #     thr.start()

        if self.is_Concurrent == "0" or self.is_Concurrent == 0:

            return_value = self.Run_Input_and_Output_Function(
                self.Path_Conversion,
                self.Input_and_Output_Function,
                self.is_window,
                self.screenwidth,
                self.screenheight,
                self.is_Concurrent,
                self.is_storage_position,
                self.is_storage_type,
                self.inputTrain_path,
                self.inputTrain_File_Array,
                self.inputTest_path,
                self.inputTest_File_Array,
                self.do_Function,
                self.outputTest_path,
                self.outputTest_File_Array,
                self.outputTest_URL,
                self.time_sleep,
                self.outqueue_from_task_to_host,
                self.outqueue_from_host_to_task,
                self.is_Runing,
                self.file_Data,
                self.result_Data,
                self.complete_Number,
                self.Error_Log,
                self.Label_State,
                self.Text_display_result,
                self.image_sample,
                self.Canvas_display_sample,
                self.Label_display_sample
            )
            # print(return_value)

            # self.inputTrain_File_Array = []
            # self.inputValidation_File_Array = []
            self.inputTest_File_Array = []
            self.outputTest_File_Array = []

            if self.is_Runing:
                self.is_Runing = not self.is_Runing
            if self.is_Runing:
                self.Button_start_and_stop_Test['text'] = "Stop Test"
                self.Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;















                self.Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;















                # self.Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            else:
                self.Button_start_and_stop_Test['text'] = "Start Test"
                self.Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;













                self.Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;














                # self.Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                self.Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # self.Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # self.Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                self.Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

            # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
            # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
            print(return_value)
            # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
            self.Label_State['text'] = str('\n'.join(return_value.split(',')))
            # self.Label_State['text'] = "Stand by"

            self.Label_display_sample['text'] = "Input file"  # "悟空，您好.",
            self.Canvas_display_sample.delete("all")

            # 使用消息提示框控件給出溫馨提示;
            tk_messagebox.showinfo(
                title = "溫馨提示",
                message = str('\n'.join(return_value.split(',')))
            )

            # return return_value  # None

        return return_value  # None



# # 函數使用示例;
# # 控制臺命令行使用:
# # C:\Criss\OCR-Measuring-Scale\Scripts\python.exe C:\Criss\OCR-Measuring-Scale\src\py\window_tkinter.py is_window=False is_Concurrent=Multi-Threading
# # 啓動運行;
# # 參數 C:\Criss\OCR-Measuring-Scale\Scripts\python.exe 表示使用隔離環境 OCR-Measuring-Scale 中的 python.exe 啓動運行;
# # 使用示例，自定義類 Window_Optical_Character_Recognition 圖形化用戶交互介面使用説明;
# if __name__ == '__main__':
#     # os.chdir(monitor_dir)  # 可以先改變工作目錄到 static 路徑;
#     try:
#         Input_and_Output_Function = Input_and_Output_Function  # 操作硬盤文檔的函數讀取或寫入;
#         do_Function = do_data  # 用於接收執行功能的函數;
#         do_Function_obj = {
#             "do_Function": do_Function  # 用於接收執行功能的函數;
#         }
#         time_sleep = float(0.01)  # 用於監聽程序的輪詢延遲參數，單位（秒）;
#         outqueue_from_task_to_host = queue.Queue(maxsize=0)
#         outqueue_from_host_to_task = queue.Queue(maxsize=0)
#         is_Concurrent = "Multi-Threading"  # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程），可取值：0、"0"、"Multi-Threading"、"Multi-Processes";
#         is_storage_position = "Disk"  # "Database", "Database_and_Disk", "Disk" 判斷存儲位置;
#         is_storage_type = "csv"  # "json", "csv", "txt", "xlsx", 判斷存儲類型;
#         # is_window = True  # bool(True), bool(False) 判斷只需要執行一次還是啓動監聽服務器功能;
#         # screenwidth =  int(0)  # int(tk.Tk().winfo_screenwidth())  # 獲取顯示器屏幕寬度;
#         # screenheight =  int(0)  # int(tk.Tk().winfo_screenheight())  # 獲取顯示器屏幕高度;
#         # size_XY = '{}x{}+{}+{}'.format(str(int(int(screenwidth)*0.6)), str(int(int(screenheight)*0.6)), str(int(int(screenwidth)*0.2)), str(int(int(screenheight)*0.2)))
#         iconbitmap_path = ""
#         # 判斷是否爲打包（.exe）後的環境;
#         if getattr(sys, 'frozen', False):
#             iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "Icon", "iconbitmap.png"))).replace('\\', '/')
#             # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "Icon", "iconbitmap.png"))).replace('\\', '/')
#             # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "Icon", "iconbitmap.png"))).replace('\\', '/')
#             # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "Icon", "iconbitmap.png"))).replace('\\', '/')
#         else:
#             # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "Icon", "iconbitmap.png"))).replace('\\', '/')
#             # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "Icon", "iconbitmap.png"))).replace('\\', '/')
#             # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "Icon", "iconbitmap.png"))).replace('\\', '/')
#             iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "Icon", "iconbitmap.png"))).replace('\\', '/')
#         # print(iconbitmap_path)  # "C:/Criss/OCR/src/Icon/iconbitmap.png"
#         inputTrain_path = ""
#         # 判斷是否爲打包（.exe）後的環境;
#         if getattr(sys, 'frozen', False):
#             inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')
#             # inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTrain"))).replace('\\', '/')
#             # inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTrain"))).replace('\\', '/')
#             # inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTrain"))).replace('\\', '/')
#         else:
#             inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')
#             # inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTrain"))).replace('\\', '/')
#             # inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTrain"))).replace('\\', '/')
#             # inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTrain"))).replace('\\', '/')
#         # print(inputTrain_path)
#         inputTrain_File_Array = []
#         if len(inputTrain_File_Array) == 0:
#             if len(inputTrain_path) > 0:
#                 # inputTrain_File_Array = []
#                 inputTrain_File_Array = Path_Conversion(inputTrain_path, time_sleep)[0]
#         inputValidation_path = ""
#         # 判斷是否爲打包（.exe）後的環境;
#         if getattr(sys, 'frozen', False):
#             inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')
#             # inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputValidation"))).replace('\\', '/')
#             # inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputValidation"))).replace('\\', '/')
#             # inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputValidation"))).replace('\\', '/')
#         else:
#             inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')
#             # inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputValidation"))).replace('\\', '/')
#             # inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputValidation"))).replace('\\', '/')
#             # inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputValidation"))).replace('\\', '/')
#         # print(inputValidation_path)
#         inputValidation_File_Array = []
#         if len(inputValidation_File_Array) == 0:
#             if len(inputValidation_path) > 0:
#                 # inputValidation_File_Array = []
#                 inputValidation_File_Array = Path_Conversion(inputValidation_path, time_sleep)[0]
#         inputTest_path = ""
#         # 判斷是否爲打包（.exe）後的環境;
#         if getattr(sys, 'frozen', False):
#             inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
#             # inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTest"))).replace('\\', '/')
#             # inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTest"))).replace('\\', '/')
#             # inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTest"))).replace('\\', '/')
#         else:
#             inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
#             # inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTest"))).replace('\\', '/')
#             # inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTest"))).replace('\\', '/')
#             # inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTest"))).replace('\\', '/')
#         # print(inputTest_path)
#         inputTest_File_Array = []
#         if len(inputTest_File_Array) == 0:
#             if len(inputTest_path) > 0:
#                 # inputTest_File_Array = []
#                 inputTest_File_Array = Path_Conversion(inputTest_path, time_sleep)[0]
#         # input_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
#         outputTest_path = ""
#         # 判斷是否爲打包（.exe）後的環境;
#         if getattr(sys, 'frozen', False):
#             outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
#             # outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
#             # outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
#             # outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
#         else:
#             outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
#             # outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
#             # outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
#             # outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
#         # print(outputTest_path)
#         outputTest_File_Array = []
#         if len(outputTest_File_Array) == 0:
#             if len(outputTest_path) > 0:
#                 # # outputTest_File_Array = []
#                 # outputTest_File_Array = Path_Conversion(outputTest_path, time_sleep)[0]
#                 outputTest_File_Array = [outputTest_path]
#         # output_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')
#         outputTest_URL = "mongodb://username:password@127.0.0.1:27017/testDB"

#         # pid = multiprocessing.current_process().pid, threading.currentThread().ident;

#         init_window = tk.Tk()  # 創建 tkinter 的窗體介面;

#         # 獲取顯示器屏幕寬度;
#         screenwidth = int(init_window.winfo_screenwidth())  # int(0)  # int(tk.Tk().winfo_screenwidth())  # 獲取顯示器屏幕寬度;
#         # print(screenwidth)
#         # 獲取顯示器屏幕高度;
#         screenheight = int(init_window.winfo_screenheight())  # int(0)  # int(tk.Tk().winfo_screenheight())  # 獲取顯示器屏幕高度;
#         # print(screenheight)
#         size_XY = '{}x{}+{}+{}'.format(str(int(int(screenwidth)*0.6)), str(int(int(screenheight)*0.6)), str(int(int(screenwidth)*0.2)), str(int(int(screenheight)*0.2)))
#         # print(size_XY)

#         # 創建自定義的人機交互介面窗口;
#         OCR_GUI = Window_Optical_Character_Recognition(
#             initializer_Window=init_window,
#             # screenwidth=screenwidth,
#             # screenheight=screenheight,
#             # size_XY=size_XY,
#             iconbitmap_path=iconbitmap_path,
#             outqueue_from_task_to_host=outqueue_from_task_to_host,
#             outqueue_from_host_to_task=outqueue_from_host_to_task,
#             is_Concurrent=is_Concurrent,
#             is_storage_position=is_storage_position,
#             is_storage_type=is_storage_type,
#             input_tabel_tesseract_config=input_tabel_tesseract_config,  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
#             input_measuringRuler_tesseract_config=input_measuringRuler_tesseract_config,  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
#             inputTrain_path=inputTrain_path,
#             # inputTrain_File_Array=inputTrain_File_Array,
#             inputValidation_path=inputValidation_path,
#             # inputValidation_File_Array=inputValidation_File_Array,
#             inputTest_path=inputTest_path,
#             # inputTest_File_Array=inputTest_File_Array,
#             outputTest_path=outputTest_path,
#             # outputTest_File_Array=outputTest_File_Array,
#             outputTest_URL=outputTest_URL,
#             Input_and_Output_Function=Input_and_Output_Function,
#             do_Function=do_Function,
#             # do_Function_obj=do_Function_obj,
#             time_sleep=time_sleep
#         )

#         init_window.mainloop()  # 循環刷新 tkinter 窗體，實時顯示窗體變化;

#     except Exception as error:
#         print(error)



# 通過命令列工具進入 app 目錄下，在該目錄下執行如下命令：
# root@localhost:~# pyinstaller -F -w ./test.py
# 上面命令中的「-F」選項指定生成單個的可執行程式，「-w」選項指定生成圖形化使用者介面程式（不需要命令列介面）。運行上面命令，該工具同樣在「app」目錄下生成了一個「dist」子目錄，並在該子目錄下生成了一個「app-window.exe」文件。
# 直接按兩下運行「app-window.exe」程式（該程式有圖形化使用者介面，因此可以按兩下運行），可查看運行結果。
