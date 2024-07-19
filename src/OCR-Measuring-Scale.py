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

# 使用説明：
# 控制臺命令列運行指令：
# C:\> C:\OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter\Scripts\python.exe C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/main.py configFile=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt is_window=False is_Concurrent=Multi-Threading is_storage_position=Disk is_storage_type=csv tesseract_timeout=0.0 input_dir=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/inputTest/ outputTest_path=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/outputTest/test.csv tesseract_cmd=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/tesseract.exe tesseract_tessdata_dir=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tessdata tesseract_user_words=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tesswords input_tabel_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert" input_measuringRuler_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert"
# root@localhost:~# /usr/bin/python3 /home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/main.py configFile=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt is_window=False is_Concurrent=Multi-Threading is_storage_position=Disk is_storage_type=csv tesseract_timeout=0.0 input_dir=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/inputTest/ outputTest_path=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/outputTest/test.csv tesseract_cmd=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/tesseract.exe tesseract_tessdata_dir=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tessdata tesseract_user_words=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tesswords input_tabel_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert" input_measuringRuler_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert"

#################################################################################


import os  # 加載 Python 原生的操作系統接口模組「os」;
import sys  # 加載 Python 原生的使用或維護的變量的接口模組「sys」;
import signal, stat  # 加載Python原生的「」;
import math  # 導入 Python 原生包「math」，用於數學計算;
# import random  # 導入 Python 原生包「random」，用於生成隨機數;
import json  # 導入 Python 原生模組「json」，用於解析 JSON 文檔;
# import platform  # 加載Python原生的與平臺屬性有關的模組;
# import inspect  # from inspect import isfunction 加載Python原生的模組、用於判斷對象是否為函數類型;
# import multiprocessing  # 加載Python原生的支持多進程模組;
# # from multiprocessing import Process, Pool;
# import subprocess  # 加載Python原生的創建子進程模組;
import threading  # 加載Python原生的支持多缐程（執行緒）模組;
# from queue import Queue
import queue
# from socketserver import ThreadingMixIn  #, ForkingMixIn
# from queue import Queue
# import inspect, ctypes  # 用於强制終止缐程;
# import string  # 加載Python原生的字符串處理模組;
import datetime, time  # 加載Python原生的日期數據處理模組;
# import re  # 加載Python原生的正則表達式對象
# from tempfile import TemporaryFile, TemporaryDirectory, NamedTemporaryFile  # 用於創建臨時目錄和臨時文檔;
import pathlib  # from pathlib import Path 用於檢查判斷指定的路徑對象是目錄還是文檔;
# import struct  # 用於讀、寫、操作二進制本地硬盤文檔;
# import shutil  # 用於刪除完整硬盤目錄樹，清空文件夾;
# import urllib  # 加載Python原生的創建客戶端訪問請求連接模組，urllib 用於對 URL 進行編解碼;
# import urllib.request as urllib_request
from urllib import request as urllib_request
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
# from scipy import stats as scipy_stats  # 導入第三方擴展包「scipy」中的統計運算模組「stats」，用於實現 beta 分佈概率密度函數;
# import scipy.stats as scipy_stats
from scipy import ndimage as scipy_ndimage  # 導入第三方擴展包「scipy」中的圖片處理模組「ndimage」，用於實現圖形旋轉矯正操作;
# from scipy import optimize as scipy_optimize  # 導入第三方擴展包「scipy」中的最優化模組「optimize」，用於方程擬合;
# from scipy.interpolate import make_interp_spline as scipy_interpolate_make_interp_spline  # 導入第三方擴展包「scipy」中的插值模組「interpolate」中的「make_interp_spline()」函數，用於擬合插值函數;
# from scipy import special as scipy_special  # 導入第三方擴展包「scipy」中的最優化模組「special」，用於使用「special」模組中的「comb()」函數計算組合數;
from PIL import Image, ImageTk  # 導入第三方擴展包「PIL」，用於從硬盤讀取圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;
# 需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 OpenCV 應用成功：root@localhost:~# apt install libavcodec-dev libavformat-dev libswscale-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libgtk2.0-dev libgtk-3-dev libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev libjasper-dev libopencv-dev python3-opencv ;
# 注意，因爲函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，而且因爲庫「opencv-python」與「opencv-contrib-python」之間互相衝突，二者不能同時存在，只能選其一安裝，所以，只能安裝「opencv-contrib-python」庫：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
import cv2  # 導入第三方擴展包「opencv-contrib-python」，用於驅動 OpenCV 光學圖形處理庫，需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 OpenCV 應用成功：root@localhost:~# apt install libavcodec-dev libavformat-dev libswscale-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libgtk2.0-dev libgtk-3-dev libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev libjasper-dev libopencv-dev python3-opencv ;
# 需要事先在控制臺安裝配置成功：root@localhost:~# pip install pytesseract -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 Tesseract-OCR 應用成功：root@localhost:~# apt install tesseract-ocr libtesseract-dev tesseract-ocr-chi-tra tesseract-ocr-chi_tra_vert tesseract-ocr-chi-sim tesseract-ocr-chi_sim_vert ;
import pytesseract  # 導入第三方擴展包「pytesseract」，用於驅動 Tesseract-OCR 文字（Character）識別庫，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pytesseract -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 Tesseract-OCR 應用成功：root@localhost:~# apt install tesseract-ocr libtesseract-dev tesseract-ocr-chi-tra tesseract-ocr-chi_tra_vert tesseract-ocr-chi-sim tesseract-ocr-chi_sim_vert ;
import openpyxl  # 導入第三方擴展包「openpyxl」，用於 Python 的 pandas 工具與 MicroSoft Office Excel 軟體通信互傳數據時的解析引擎; 需要事先安裝配置成功： pip3 install openpyxl -i https://mirrors.aliyun.com/pypi/simple/
# import xlwt  # 導入第三方擴展包「xlwt」，用於 Python 的 pandas 工具寫入 MicroSoft Office Excel 軟體通信時的解析引擎; 需要事先安裝配置成功： pip3 install xlwt -i https://mirrors.aliyun.com/pypi/simple/
# import xlrd  # 導入第三方擴展包「xlrd」，用於 Python 的 pandas 工具讀取 MicroSoft Office Excel 軟體通信時的解析引擎; 需要事先安裝配置成功： pip3 install xlrd -i https://mirrors.aliyun.com/pypi/simple/


# # 匯入自定義路由模組脚本文檔「./Router.py」;
# # os.getcwd() # 獲取當前工作目錄路徑;
# # os.path.abspath("..")  # 當前運行脚本所在目錄上一層的絕對路徑;
# # os.path.join(os.path.abspath("."), 'Router.py')  # 拼接路徑字符串;
# # pathlib.Path(os.path.join(os.path.abspath("."), Router.py)  # 返回路徑對象;
# # sys.path.append(os.path.abspath(".."))  # 將上一層目錄加入系統的搜索清單，當導入脚本時會增加搜索這個自定義添加的路徑;
# import optical_character_recognition as optical_character_recognition  # 導入當前運行代碼所在目錄的，自定義脚本文檔「./optical_character_recognition.py」;
# import Interface as Interface  # 導入當前運行代碼所在目錄的，自定義脚本文檔「./Router.py」;
# # 注意導入本地 Python 脚本，只寫文檔名不要加文檔的擴展名「.py」，如果不使用 sys.path.append() 函數添加自定義其它的搜索路徑，則只能放在當前的工作目錄「"."」
# File_Monitor = Router.Interface_File_Monitor
# http_Server = Router.Interface_http_Server
# http_Client = Router.Interface_http_Client
# check_json_format = Router.check_json_format
# win_file_is_Used = Router.win_file_is_Used
# clear_Directory = Router.clear_Directory
# formatByte = Router.formatByte

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



# 圖像旋轉方位調整矯正 ORIENTATION CORRECTION/ADJUSTMENT;
# import math  # 導入 Python 原生包「math」，用於數學計算;
# import cv2  # 導入第三方擴展包「opencv-contrib-python」，用於驅動 OpenCV 光學圖形處理庫，需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 OpenCV 應用成功：root@localhost:~# apt install libavcodec-dev libavformat-dev libswscale-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libgtk2.0-dev libgtk-3-dev libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev libjasper-dev libopencv-dev python3-opencv ;
# import numpy as np
# from scipy import ndimage as scipy_ndimage  # 導入第三方擴展包「scipy」中的圖片（Image）處理模組「ndimage」，用於實現圖形旋轉矯正操作;
def orientation_correction(img, save_image=""):

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 使用 Canny 算灋做圖像灰度轉換 GrayScale Conversion for the Canny Algorithm;
    img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)  # 使用 Canny 算灋做圖形邊緣檢測 Canny Algorithm for edge detection was developed by John F. Canny not Kennedy!! :);
    lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)  # 使用 Houghlines 算灋檢測線條 Using Houghlines to detect lines;

    # 判斷是否一條都沒有識別出缐段;
    if len(lines) == 0:
        print('line not detected.')
        img_rotated = img
        return img_rotated

    # 計算極座標中缐條的傾角 Finding angle of lines in polar coordinates;
    angles = []
    for x1, y1, x2, y2 in lines[0]:
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        # if math.atan2(y2 - y1, x2 - x1) != 0.0 and math.atan2(y2 - y1, x2 - x1) != 1.5707963267948966 and math.atan2(y2 - y1, x2 - x1) != 3.141592653589793 and math.atan2(y2 - y1, x2 - x1) != -1.5707963267948966:
        # if angle != 0.0 and angle != 90.0 and angle != 180.0 and angle != -90.0:
        if angle != math.degrees(0.0) and angle != math.degrees(math.pi/2) and angle != math.degrees(math.pi) and angle != math.degrees(-math.pi/2):
            angles.append(angle)

    if len(angles) > 0:
        median_angle = np.median(angles)  # 獲取傾角中值 Getting the median angle;
        img_rotated = scipy_ndimage.rotate(img, median_angle)  # 對圖像做旋轉操作，旋轉角度爲傾角中值 Rotating the image with this median angle;
    else:
        img_rotated = img

    if save_image != "":
        cv2.imwrite(save_image, img_rotated)

    return img_rotated


# 截取圖片（Image）中使用滑鼠自定義選擇的感興趣的區域 REGION OF INTEREST (ROI) SELECTION;
# 爲鼠標設置一個事件偵聽器，使用戶能夠自定義手動選擇圖片（Image）中感興趣的區域，在這裏設置了兩個條件，一個是滑鼠左鍵「按下」事件，一個是滑鼠左鍵「釋放按下」事件;
# 程序存儲「按下」滑鼠左鍵時的起始座標點，和存儲「釋放按下」的滑鼠左鍵時的座標點，然後，在按下鍵盤中的「Enter」鍵時，截取這些起始座標和結束座標之間的區域，如果按下鍵盤中的「Esc」鍵時，則刪除存儲的座標;
# import cv2  # 導入第三方擴展包「opencv-contrib-python」，用於驅動 OpenCV 光學圖形處理庫，需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 OpenCV 應用成功：root@localhost:~# apt install libavcodec-dev libavformat-dev libswscale-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libgtk2.0-dev libgtk-3-dev libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev libjasper-dev libopencv-dev python3-opencv ;
def region_selection(img, save_image=""):

    coordinates = []  # 初始化用於存儲選中座標點值的清單 initializing the list for storing the coordinates;
    # 定義事件偵聽器回調函數 Defining the event listener (callback function);

    def shape_selection(event, x, y, flags, param):
        global coordinates  # making coordinates global;

        # 按下滑鼠左鍵時存儲（x1，y1）座標 Storing the (x1,y1) coordinates when left mouse button is pressed;
        if event == cv2.EVENT_LBUTTONDOWN:
            coordinates = [(x, y)]
        # 釋放滑鼠左鍵時存儲（x2，y2）座標，並在選定區域上繪製矩形 Storing the (x2,y2) coordinates when the left mouse button is released and make a rectangle on the selected region;
        elif event == cv2.EVENT_LBUTTONUP:
            coordinates.append((x, y))

        # 在選定區域上繪製矩形 Drawing a rectangle around the region of interest (roi);
        cv2.rectangle(image_copy, coordinates[0], coordinates[1], (0,0,255), 2)  # 使用 cv2.rectangle() 函數繪製矩形，參數：image_copy 表示原圖片的副本;
        cv2.imshow("image", image_copy)  # 在名稱爲 "image" 的窗口中顯示圖片：image_copy ;

    # 載入圖片，創建圖片副本，調用回調函數 load the image, clone it, and setup the mouse callback function;
    image_copy = img.copy()  # 創建圖片副本;
    cv2.namedWindow("image")  # 創建圖片展示窗口;
    cv2.setMouseCallback("image", shape_selection)

    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", image_copy)
        key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;

        # If 'Enter' is pressed, apply OCR
        # chr(13) == 'enter'
        # ord("\n") == 13
        # if key == ord('\n'):
        if key == 13:
            break

        # Clear the selection when 'Esc' is pressed
        # chr(27) == 'esc'
        # ord("\x1b") == 27
        # if key == ord('\x1b'):
        if key == 27:
            img = image_copy.copy()

        # 回車鍵（Enter）的 ASCII 碼爲：ord('\n')
        # 空格鍵的 ASCII 碼爲：ord(' ')
        # Tab 鍵的 ASCII 碼爲：ord('\t')
        # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
        # 換行鍵的 ASCII 碼爲：ord('\r')
        # Esc 鍵的 ASCII 碼爲：ord('\x1b')

    # 截取選中區域;
    image_select = []
    if len(coordinates) == 2:
        image_select = image_copy[coordinates[0][1]:coordinates[1][1], coordinates[0][0]:coordinates[1][0]]
    cv2.imshow("Selected Region of Interest - Press any key to proceed", image_select)

    if save_image != "":
        cv2.imwrite(save_image, image_select)

    # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;

    cv2.destroyAllWindows()  # closing all open windows

    return image_select


# 識別橫向分隔缐段;
# 使用第三方庫「OpenCV」中的概率霍夫變換「Probabilistic Hough Transform」演算法進行直缐檢測，來識別圖片（Image）表格（Table）中的橫向分隔缐段;
def LinesDetect_Hough(
    img,
    Canny_threshold1,  # cv2.Canny()：第一次閾值；
    Canny_threshold2,  # cv2.Canny()：第二次閾值；
    Canny_apertureSize,  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
    Canny_L2gradient,  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
    HoughLinesP_rho,  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
    HoughLinesP_theta,  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
    HoughLinesP_threshold,  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
    HoughLinesP_minLineLength,  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
    HoughLinesP_maxLineGap  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
):
    # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;

    # edges = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])
    # 其中參數：
    # image：待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）；
    # threshold1：第一次閾值；
    # threshold2：第二次閾值；
    # apertureSize：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
    # L2gradient：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
    # 函數返回值是一個輸出圖像，與輸入圖像大小及類型相同。
    # 函數「cv2.canny()」的實現原理主要基於以下幾個步驟：
    # Step 1：圖像灰度化。首先將輸入圖像轉換爲單通道的灰度圖像，可以通過函數「cv2.cvtColor」函數來完成。
    # Step 2：邊緣強度梯度計算。使用索伯爾運算元（Sobel）（算子）計算每個圖元（pixel）（像素）點在水平和垂直方向上的梯度值，並通過勾股定理（Pythagorean theorem）計算梯度幅值和方向。
    # Step 3：非極大值抑制。爲了減少邊緣（輪廓）圖元（pixel）（像素）數量，需要對梯度圖像中的強度值進行非極大值抑制，即只保留局部最大值點。
    # Step 4：滯後閾值處理。根據設定的閾值大小，將梯度幅值大於閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）。接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點也標記爲邊緣（輪廓）點。
    # Step 5：輸出邊緣（輪廓）圖像。最後將所有被標記爲邊緣（輪廓）的圖元（pixel）（像素）點輸出爲邊緣（輪廓）圖像。

    # 使用第三方庫「OpenCV」中的函數「cv2.Canny()」做圖形邊緣（輪廓）檢測，並將邊緣（輪廓）標記為白色圖元（pixel）（像素），黑色圖元（pixel）（像素）則表示非邊緣（輪廓）;
    edges = cv2.Canny(
        grayImage,  # 待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）;
        Canny_threshold1,  # 30,  # 第一次閾值，將梯度幅值大於第一次閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）;
        Canny_threshold2,  # 240,  # 第二次閾值，接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點，梯度幅值大於第二次閾值的，也標記爲邊緣（輪廓）點;
        apertureSize = Canny_apertureSize,  # 3,  # 用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3;
        L2gradient = Canny_L2gradient  # False  # 計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法;
    )

    # 第三方庫「OpenCV」中，有兩種算法檢測直缐或缐段，即「cv2.HoughLines()」標準霍夫缐變換「Hough Transform」和「cv2.HoughLinesP()」概率霍夫缐變換「Probabilistic Hough Transform」;
    # 標準霍夫缐變換「Hough Transform」函數「cv2.HoughLines()」返回值爲直綫的方程，即檢測結果爲「直綫」;
    # lines = cv2.HoughLines(image, rho, theta, threshold)
    # 概率霍夫缐變換「Probabilistic Hough Transform」函數「cv2.HoughLinesP()」返回值爲缐段起點與終點的座標值列表，即檢測結果爲「缐段」;
    # lines = cv2.HoughLinesP(image, rho, theta, threshold, minLineLength=None, maxLineGap=None)
    # 其中參數：
    # image：待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測；
    # rho：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
    # theta：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
    # threshold：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
    # minLineLength：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
    # maxLineGap：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
    # 函數返回值是一個三維陣列，其中每個元素表示一條直線，格式爲列表：(x1, y1, x2, y2），表示直線的兩個端點座標。

    # 使用第三方庫「OpenCV」中的函數「cv2.HoughLinesP()」概率霍夫變換「Probabilistic Hough Transform」演算法識別圖片（Image）表格（Table）中的橫向分隔缐段;
    # minLineLength = 500  # 要求識別的缐段最小長度值（單位：圖元 pixel 也稱像素），比這個長度值小的缐段將會被忽略，自定義設定爲：500 個圖元;
    # maxLineGap = 30  # 要求識別的線段之間的最大間隔上限值（單位：圖元 pixel 也稱像素），小於這個間隔上限值的缐段將被連接爲一條直綫，自定義設定爲：30 個圖元;
    lines = cv2.HoughLinesP(
        edges,  # 待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測;
        HoughLinesP_rho,  # 1,  # 距離解析度（分辨率），單位爲：圖元（pixel）（像素）;
        HoughLinesP_theta,  # np.pi/180,  # 角度解析度（分辨率），單位爲：弧度;
        HoughLinesP_threshold,  # 100,  # 閾值參數，只有累加器中的值高於閾值才會被認為是一條直線;
        minLineLength = HoughLinesP_minLineLength,  # 要求識別的缐段最小長度值（單位：圖元 pixel 也稱像素），比這個長度值小的缐段將會被忽略，自定義設定爲：500 個圖元;
        maxLineGap = HoughLinesP_maxLineGap  # 要求識別的線段之間的最大間隔上限值（單位：圖元 pixel 也稱像素），小於這個間隔上限值的缐段將被連接爲一條直綫，自定義設定爲：30 個圖元;
    ).tolist()
    # lines.append([[13, 102, 756, 102]])  # 可以追加畫出一條自定義位置的橫向缐段;
    sorted_lines = sorted(lines, key=lambda x: x[0])

    # horizontal_lines = []  # 存儲在圖像表格（Table）中檢測到的橫向分隔缐段座標的列表;
    # for line in sorted_lines:
    #     for x1, y1, x2, y2 in line:
    #         if y1 == y2:
    #             # print(line)
    #             horizontal_lines.append([x1, y1, x2, y2])  # 存儲在圖像表格（Table）中檢測到的橫向分隔缐段座標;
    #             # cv2.line(self.image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 在源圖像上繪製識別出的表格（Table）橫向分隔缐段;
    # # 在源圖像上繪製所有識別出的表格（Table）橫向分隔缐段;
    # for line in horizontal_lines:
    #     for x1, y1, x2, y2 in line:
    #         if y1 == y2:
    #             # print(line)
    #             cv2.line(self.image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 在源圖像上繪製識別出的表格（Table）橫向分隔缐段;

    return sorted_lines


# 重叠缐過濾器;
# 較粗的缐條由多個相同位置，長度不同的缐條組成，爲了消除此重叠缐，定義一個重叠缐過濾器，如果下一行的間隔小於一定距離，則將其視爲與上一行相同的缐條;
def OverlappingFilter(
    lines,
    separationThresholdSlope = float(0),  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
    separationThresholdIntercept = float(0)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
):
    filtered_lines = []  # 存儲過濾掉重叠缐之後的缐段座標的列表;

    for i in range(0, int(len(lines) - int(1)), 1):

        l_curr = lines[i]

        if i > 0:

            l_prev = lines[i - int(1)]

            separation_Intercept = float(0)  # 表示兩條缐條截距之間的間距，單位：圖元（像素）點個數;
            separation_Slope = float(0)  # 表示兩條缐條斜率之間的間距，單位：角度（0 ~ 90）;

            # 兩點式直缐方程：(y-Y1)/(Y2-Y1) = (x-X1)/(X2-X1)  (X1 ≠ X2, Y1 ≠ Y2);
            # Slope = (Y2-Y1)/(X2-X1)
            # Slope_X = (X2-X1)/(Y2-Y1)
            # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
            # Intercept_X = (X2·Y1-X1·Y2)/(Y2-Y1)
            # 一般式直缐方程：A·x + B·y + C = 0 （A ≠ 0, B ≠ 0）;
            # Slope = -A/B
            # Intercept = -C/B
            # A = C·(Slope/Intercept) = C·(Y2-Y1)/(X2·Y1-X1·Y2)
            # B = -C/Intercept = -C·(X2-X1)/(X2·Y1-X1·Y2)
            # C = any one (for example: C = 1)

            # 當缐：l_curr 與缐：l_prev 都爲橫向水平缐時，只與截距閾值：separationThresholdIntercept 比較大小：
            if l_curr[1] == l_curr[3] and l_curr[0] != l_curr[2] and l_prev[1] == l_prev[3] and l_prev[0] != l_prev[2]:
                l_curr_Slope = float(0)  # Slope = (Y2-Y1)/(X2-X1)
                l_curr_Intercept = float(l_curr[1])  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                l_prev_Slope = float(0)  # Slope = (Y2-Y1)/(X2-X1)
                l_prev_Intercept = float(l_prev[1])  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                # separation_Intercept = math.fabs(math.fabs(l_curr[1]) - math.fabs(l_prev[1]))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                separation_Intercept = math.fabs(math.fabs(l_curr_Intercept) - math.fabs(l_prev_Intercept))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                if float(separation_Intercept) > float(separationThresholdIntercept):
                    filtered_lines.append(l_curr)

            # 當缐：l_curr 與缐：l_prev 都爲縱向垂直缐時，只與截距閾值：separationThresholdIntercept 比較大小：
            if l_curr[1] != l_curr[3] and l_curr[0] == l_curr[2] and l_prev[1] != l_prev[3] and l_prev[0] == l_prev[2]:
                l_curr_Slope =  math.inf  # +∞ 正無窮大 inf 全稱爲：infinity; # Slope = (Y2-Y1)/(X2-X1)
                l_curr_Slope_X = float(0)  # 與 Y 軸夾角的正切值：= (X2-X1)/(Y2-Y1)，注意，不是斜率，與 X 軸夾角的正切值：= (Y2-Y1)/(X2-X1);
                l_curr_Intercept = math.inf  # +∞ 正無窮大 inf 全稱爲：infinity; # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                l_curr_Intercept_X = float(l_curr[0])  # 與 X 軸的交點：=(X2·Y1-X1·Y2)/(Y2-Y1)，注意，不是截距，與 Y 軸的交點：=(X2·Y1-X1·Y2)/(X2-X1);
                l_prev_Slope =  math.inf  # +∞ 正無窮大 inf 全稱爲：infinity; # Slope = (Y2-Y1)/(X2-X1)
                l_prev_Slope_X = float(0)  # 與 Y 軸夾角的正切值：= (X2-X1)/(Y2-Y1)，注意，不是斜率，與 X 軸夾角的正切值：= (Y2-Y1)/(X2-X1);
                l_prev_Intercept = math.inf  # +∞ 正無窮大 inf 全稱爲：infinity; # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                l_prev_Intercept_X = float(l_prev[0])  # 與 X 軸的交點：=(X2·Y1-X1·Y2)/(Y2-Y1)，注意，不是截距，與 Y 軸的交點：=(X2·Y1-X1·Y2)/(X2-X1);
                # separation_Intercept = math.fabs(math.fabs(l_curr[0]) - math.fabs(l_prev[0]))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                separation_Intercept = math.fabs(math.fabs(l_curr_Intercept_X) - math.fabs(l_prev_Intercept_X))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                if float(separation_Intercept) > float(separationThresholdIntercept):
                    filtered_lines.append(l_curr)

            # 當缐：l_curr 爲橫向水平缐，缐：l_prev 即不是橫向水平缐，也不是縱向垂直缐時，先與截距閾值：separationThresholdIntercept 比較大小，然後再與斜率閾值：separationThresholdSlope 比較大小：
            if l_curr[1] == l_curr[3] and l_curr[0] != l_curr[2] and l_prev[1] != l_prev[3] and l_prev[0] != l_prev[2]:
                l_curr_Slope = float(0)
                l_curr_Intercept = float(l_curr[1])
                l_prev_Slope = float((l_prev[3] - l_prev[1]) / (l_prev[2] - l_prev[0]))  # Slope = (Y2-Y1)/(X2-X1)
                l_prev_Intercept = float((l_prev[2] * l_prev[1] - l_prev[0] * l_prev[3]) / (l_prev[2] - l_prev[0]))  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                separation_Intercept = math.fabs(math.fabs(l_curr_Intercept) - math.fabs(l_prev_Intercept))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                separation_Slope = math.fabs(float(math.fabs(l_prev_Slope) - math.fabs(l_curr_Slope)))
                # 判斷表示兩條缐條之間的間距是否大於自定義設置的斜率（Slope）閾值：separationThresholdSlope，若大於則保存，若小於等於則濾過捨棄;
                # 函數：math.tan() 表示求正切值，函數：math.atan() 表示求反正切值，函數：math.degrees() 表示將弧度角度值轉換爲角度值，函數：math.radians() 表示將角度值轉換爲弧度值;
                if float(separation_Slope) > float(math.tan(math.radians(separationThresholdSlope))):
                    # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                    if float(separation_Intercept) > float(separationThresholdIntercept):
                        filtered_lines.append(l_curr)

            # 當缐：l_curr 爲縱向垂直缐，缐：l_prev 即不是縱向垂直缐，也不是橫向水平缐時，先與截距閾值：separationThresholdIntercept 比較大小，然後再與斜率閾值：separationThresholdSlope 比較大小：
            if l_curr[1] != l_curr[3] and l_curr[0] == l_curr[2] and l_prev[1] != l_prev[3] and l_prev[0] != l_prev[2]:
                l_curr_Slope = math.inf  # +∞ 正無窮大 inf 全稱爲：infinity;
                l_curr_Slope_X = float(0)  # 與 Y 軸夾角的正切值：= (X2-X1)/(Y2-Y1)，注意，不是斜率，與 X 軸夾角的正切值：= (Y2-Y1)/(X2-X1);
                l_curr_Intercept = math.inf # +∞ 正無窮大 inf 全稱爲：infinity;
                l_curr_Intercept_X = float(l_curr[0])  # 與 X 軸的交點：=(X2·Y1-X1·Y2)/(Y2-Y1)，注意，不是截距，與 Y 軸的交點：=(X2·Y1-X1·Y2)/(X2-X1);
                l_prev_Slope = float((l_prev[3] - l_prev[1]) / (l_prev[2] - l_prev[0]))  # Slope = (Y2-Y1)/(X2-X1)
                l_prev_Slope_X = float((l_prev[2] - l_prev[0]) / (l_prev[3] - l_prev[1]))  # 與 Y 軸夾角的正切值：= (X2-X1)/(Y2-Y1)，注意，不是斜率，與 X 軸夾角的正切值：= (Y2-Y1)/(X2-X1);
                l_prev_Intercept = float((l_prev[2] * l_prev[1] - l_prev[0] * l_prev[3]) / (l_prev[2] - l_prev[0]))  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                l_prev_Intercept_X = float((l_prev[2] * l_prev[1] - l_prev[0] * l_prev[3]) / (l_prev[3] - l_prev[1]))  # 與 X 軸的交點：=(X2·Y1-X1·Y2)/(Y2-Y1)，注意，不是截距，與 Y 軸的交點：=(X2·Y1-X1·Y2)/(X2-X1);
                separation_Intercept = math.fabs(math.fabs(l_curr_Intercept_X) - math.fabs(l_prev_Intercept_X))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                separation_Slope = math.fabs(float(math.fabs(l_prev_Slope_X) - math.fabs(l_curr_Slope_X)))
                # 判斷表示兩條缐條之間的間距是否大於自定義設置的斜率（Slope）閾值：separationThresholdSlope，若大於則保存，若小於等於則濾過捨棄;
                # 函數：math.tan() 表示求正切值，函數：math.atan() 表示求反正切值，函數：math.degrees() 表示將弧度角度值轉換爲角度值，函數：math.radians() 表示將角度值轉換爲弧度值;
                if float(separation_Slope) > float(math.tan(math.radians(separationThresholdSlope))):
                    # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                    if float(separation_Intercept) > float(separationThresholdIntercept):
                        filtered_lines.append(l_curr)

            # 當缐：l_curr 即不是橫向水平缐，也不是縱向垂直缐，缐：l_prev 爲橫向水平缐時，先與截距閾值：separationThresholdIntercept 比較大小，然後再與斜率閾值：separationThresholdSlope 比較大小：
            if l_curr[1] != l_curr[3] and l_curr[0] != l_curr[2] and l_prev[1] == l_prev[3] and l_prev[0] != l_prev[2]:
                l_curr_Slope = float((l_curr[3] - l_curr[1]) / (l_curr[2] - l_curr[0]))  # Slope = (Y2-Y1)/(X2-X1)
                l_curr_Intercept = float((l_curr[2] * l_curr[1] - l_curr[0] * l_curr[3]) / (l_curr[2] - l_curr[0]))  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                l_prev_Slope = float(0)
                l_prev_Intercept = float(l_prev[1])
                separation_Intercept = math.fabs(math.fabs(l_curr_Intercept) - math.fabs(l_prev_Intercept))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                separation_Slope = math.fabs(float(math.fabs(l_prev_Slope) - math.fabs(l_curr_Slope)))
                # 判斷表示兩條缐條之間的間距是否大於自定義設置的斜率（Slope）閾值：separationThresholdSlope，若大於則保存，若小於等於則濾過捨棄;
                # 函數：math.tan() 表示求正切值，函數：math.atan() 表示求反正切值，函數：math.degrees() 表示將弧度角度值轉換爲角度值，函數：math.radians() 表示將角度值轉換爲弧度值;
                if float(separation_Slope) > float(math.tan(math.radians(separationThresholdSlope))):
                    # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                    if float(separation_Intercept) > float(separationThresholdIntercept):
                        filtered_lines.append(l_curr)

            # 當缐：l_curr 即不是縱向垂直缐，也不是橫向水平缐，缐：l_prev 爲縱向垂直缐時，先與截距閾值：separationThresholdIntercept 比較大小，然後再與斜率閾值：separationThresholdSlope 比較大小：
            if l_curr[1] != l_curr[3] and l_curr[0] != l_curr[2] and l_prev[1] != l_prev[3] and l_prev[0] == l_prev[2]:
                l_curr_Slope = float((l_curr[3] - l_curr[1]) / (l_curr[2] - l_curr[0]))  # Slope = (Y2-Y1)/(X2-X1)
                l_curr_Slope_X = float((l_curr[2] - l_curr[0]) / (l_curr[3] - l_curr[1]))  # 與 Y 軸夾角的正切值：= (X2-X1)/(Y2-Y1)，注意，不是斜率，與 X 軸夾角的正切值：= (Y2-Y1)/(X2-X1);
                l_curr_Intercept = float((l_curr[2] * l_curr[1] - l_curr[0] * l_curr[3]) / (l_curr[2] - l_curr[0]))  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                l_curr_Intercept_X = float((l_curr[2] * l_curr[1] - l_curr[0] * l_curr[3]) / (l_curr[3] - l_curr[1]))  # 與 X 軸的交點：=(X2·Y1-X1·Y2)/(Y2-Y1)，注意，不是截距，與 Y 軸的交點：=(X2·Y1-X1·Y2)/(X2-X1);
                l_prev_Slope = math.inf  # +∞ 正無窮大 inf 全稱爲：infinity;
                l_prev_Slope_X = float(0)  # 與 Y 軸夾角的正切值：= (X2-X1)/(Y2-Y1)，注意，不是斜率，與 X 軸夾角的正切值：= (Y2-Y1)/(X2-X1);
                l_prev_Intercept = math.inf # +∞ 正無窮大 inf 全稱爲：infinity;
                l_prev_Intercept_X = float(l_prev[0])  # 與 X 軸的交點：=(X2·Y1-X1·Y2)/(Y2-Y1)，注意，不是截距，與 Y 軸的交點：=(X2·Y1-X1·Y2)/(X2-X1);
                separation_Intercept = math.fabs(math.fabs(l_curr_Intercept_X) - math.fabs(l_prev_Intercept_X))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                separation_Slope = math.fabs(float(math.fabs(l_prev_Slope_X) - math.fabs(l_curr_Slope_X)))
                # 判斷表示兩條缐條之間的間距是否大於自定義設置的斜率（Slope）閾值：separationThresholdSlope，若大於則保存，若小於等於則濾過捨棄;
                # 函數：math.tan() 表示求正切值，函數：math.atan() 表示求反正切值，函數：math.degrees() 表示將弧度角度值轉換爲角度值，函數：math.radians() 表示將角度值轉換爲弧度值;
                if float(separation_Slope) > float(math.tan(math.radians(separationThresholdSlope))):
                    # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                    if float(separation_Intercept) > float(separationThresholdIntercept):
                        filtered_lines.append(l_curr)

            # 當缐：l_curr 即不是橫向水平缐，也不是縱向垂直缐，缐：l_prev 即不是橫向水平缐，也不是縱向垂直缐時，既與截距閾值：separationThresholdIntercept 比較大小，也同時與斜率閾值：separationThresholdSlope 比較大小：
            if l_curr[1] != l_curr[3] and l_curr[0] != l_curr[2] and l_prev[1] != l_prev[3] and l_prev[0] != l_prev[2]:
                l_curr_Slope = float((l_curr[3] - l_curr[1]) / (l_curr[2] - l_curr[0]))  # Slope = (Y2-Y1)/(X2-X1)
                l_curr_Intercept = float((l_curr[2] * l_curr[1] - l_curr[0] * l_curr[3]) / (l_curr[2] - l_curr[0]))  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                l_prev_Slope = float((l_prev[3] - l_prev[1]) / (l_prev[2] - l_prev[0]))  # Slope = (Y2-Y1)/(X2-X1)
                l_prev_Intercept = float((l_prev[2] * l_prev[1] - l_prev[0] * l_prev[3]) / (l_prev[2] - l_prev[0]))  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                separation_Intercept = math.fabs(math.fabs(l_curr_Intercept) - math.fabs(l_prev_Intercept))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                separation_Slope = math.fabs(float(math.fabs(l_prev_Slope) - math.fabs(l_curr_Slope)))
                # 判斷表示兩條缐條之間的間距是否大於自定義設置的斜率（Slope）閾值：separationThresholdSlope，若大於則保存，若小於等於則濾過捨棄;
                # 函數：math.tan() 表示求正切值，函數：math.atan() 表示求反正切值，函數：math.degrees() 表示將弧度角度值轉換爲角度值，函數：math.radians() 表示將角度值轉換爲弧度值;
                if float(separation_Slope) > float(math.tan(math.radians(separationThresholdSlope))):
                    # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                    if float(separation_Intercept) > float(separationThresholdIntercept):
                        filtered_lines.append(l_curr)

        else:

            filtered_lines.append(l_curr)

    return filtered_lines


# 使用第三方擴展包「OpenCV」（opencv-contrib-python）和「Tesseract-OCR」（pytesseract），把圖片（Image）中表格（Table）中單元格（Cell）中數據識別爲字符（character）;
class ComputerVision():
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
        # if not("sys" in imported_package_list):
        #     import sys  # 加載Python原生的操作系統接口模組os、使用或維護的變量的接口模組sys;
        # if not("signal" in imported_package_list):
        #     import signal  # 加載Python原生的操作系統接口模組os、使用或維護的變量的接口模組sys;
        # if not("stat" in imported_package_list):
        #     import stat  # 加載Python原生的操作系統接口模組os、使用或維護的變量的接口模組sys;
        # if not("platform" in imported_package_list):
        #     import platform  # 加載Python原生的與平臺屬性有關的模組;
        # if not("subprocess" in imported_package_list):
        #     import subprocess  # 加載Python原生的創建子進程模組;
        # if not("string" in imported_package_list):
        #     import string  # 加載Python原生的字符串處理模組;
        # if not("datetime" in imported_package_list):
        #     import datetime  # 加載Python原生的日期數據處理模組;
        # if not("time" in imported_package_list):
        #     import time  # 加載Python原生的日期數據處理模組;
        # if not("json" in imported_package_list):
        #     import json  # import the module of json. 加載Python原生的Json處理模組;
        # if not("re" in imported_package_list):
        #     import re  # 加載Python原生的正則表達式對象
        # if not("tempfile" in imported_package_list):
        #     import tempfile  # from tempfile import TemporaryFile, TemporaryDirectory, NamedTemporaryFile  # 用於創建臨時目錄和臨時文檔;
        # if not("pathlib" in imported_package_list):
        #     import pathlib  # from pathlib import Path 用於檢查判斷指定的路徑對象是目錄還是文檔;
        # if not("shutil" in imported_package_list):
        #     import shutil  # 用於刪除完整硬盤目錄樹，清空文件夾;
        # if not("multiprocessing" in imported_package_list):
        #     import multiprocessing  # 加載Python原生的支持多進程模組 from multiprocessing import Process, Pool;
        # if not("threading" in imported_package_list):
        #     import threading  # 加載Python原生的支持多綫程（執行緒）模組;
        # if not("inspect" in imported_package_list):
        #     import inspect  # from inspect import isfunction 加載Python原生的模組、用於判斷對象是否為函數類型，以及用於强制終止綫程;
        # if not("ctypes" in imported_package_list):
        #     import ctypes  # 用於强制終止綫程;
        # if not("socketserver" in imported_package_list):
        #     import socketserver  # from socketserver import ThreadingMixIn  #, ForkingMixIn
        # if not("urllib" in imported_package_list):
        #     import urllib  # 加載Python原生的創建客戶端訪問請求連接模組，urllib 用於對 URL 進行編解碼;
        if not("request" in imported_package_list):
            # import urllib.request as urllib_request
            from urllib import request as urllib_request  # 加載Python原生的創建客戶端訪問請求連接模組，urllib 用於對 URL 進行編解碼;
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
        #     import base64  # 加載用於加密與解密的模組;
        if not("math" in imported_package_list):
            import math  # 加載 Python 原生模組包「math」，用於數學計算;

        # # 檢查函數需要用到的 Python 第三方模組是否已經安裝成功(pip install)，如果還沒安裝，則執行安裝操作;
        # if "os" in dir(list):
        #     installed_package_list = os.popen("pip list").read()
        # if isinstance(installed_package_list, list) and not("numpy" in installed_package_list):
        #     os_popen_read = os.popen("pip install numpy --trusted-host -i https://pypi.tuna.tsinghua.edu.cn/simple").read()
        #     print(os_popen_read)
        # if isinstance(installed_package_list, list) and not("scipy" in installed_package_list):
        #     os_popen_read = os.popen("pip install scipy --trusted-host -i https://pypi.tuna.tsinghua.edu.cn/simple").read()
        #     print(os_popen_read)
        # if isinstance(installed_package_list, list) and not("pytesseract" in installed_package_list):
        #     os_popen_read = os.popen("pip install pytesseract --trusted-host -i https://pypi.tuna.tsinghua.edu.cn/simple").read()
        #     print(os_popen_read)
        # if isinstance(installed_package_list, list) and not("cv2" in installed_package_list):
        #     os_popen_read = os.popen("pip install opencv-contrib-python --trusted-host -i https://pypi.tuna.tsinghua.edu.cn/simple").read()
        #     print(os_popen_read)

        # 檢查函數需要用到的 Python 第三方模組是否已經載入(import)，如果還沒載入，則執行載入操作;
        imported_package_list = dir(list)
        if not("numpy" in imported_package_list):
            import numpy as np  # 加載 Python 語言的第三方模組「numpy」，用於向量計算;
        # if not("scipy" in imported_package_list):
        #     import scipy  # 加載 Python 語言的第三方模組「scipy」，用於統計運算;
        if not("ndimage" in imported_package_list):
            from scipy import ndimage as scipy_ndimage  # 導入第三方擴展包「scipy」中的圖片（Image）處理模組「ndimage」，用於實現圖形旋轉矯正操作;
        if not("pytesseract" in imported_package_list):
            import pytesseract  # 導入第三方擴展包「pytesseract」，用於驅動 Tesseract-OCR 文字（Character）識別庫，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pytesseract -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 Tesseract-OCR 應用成功：root@localhost:~# apt install tesseract-ocr libtesseract-dev tesseract-ocr-chi-tra tesseract-ocr-chi_tra_vert tesseract-ocr-chi-sim tesseract-ocr-chi_sim_vert ;
        if not("cv2" in imported_package_list):
            import cv2  # 導入第三方擴展包「opencv-contrib-python」，用於驅動 OpenCV 光學圖形處理庫，需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 OpenCV 應用成功：root@localhost:~# apt install libavcodec-dev libavformat-dev libswscale-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libgtk2.0-dev libgtk-3-dev libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev libjasper-dev libopencv-dev python3-opencv ;

        # 配置預設值;
        self.purpose = "tableRecognition"  # "tableRecognition", "lineMeasuring"  # 取值 purpose = "tableRecognition" 表示識別圖片（Image）表格（Tabel）單元格（Cell）中的字符（Character）；取值 purpose = "lineMeasuring" 表示測量圖片（Image）缐段（Line segment）的長度（length），單位是：圖片（Image）缐段（Line segment）所占圖元（像素）（Pixel）點的數量（Number）;
        self.imageUrl = ""  # 待識別檢測的圖片的 Web 請求網址 URL 字符串;
        # response = urllib_request.urlopen(self.imageUrl)  # 使用 Python 語言的原生模組「urllib」中的「request」中的「urlopen()」函數向服務器請求下載圖片數據;
        # img_array = np.array(bytearray(response.read()), dtype = np.uint8)  # 把從服務器下載的圖片數據轉換爲二進位 8 位字節數組的形式;
        # self.imageData = cv2.imdecode(img_array, -1)  # 使用 Python 語言的第三方擴展模組「opencv」中的「cv2.imdecode()」函數解析二進位 8 位字節數組形式的图片數據，RGB 模式;
        self.imagePath = ""  # 待識別檢測的圖片的硬盤保存位置路徑字符串;
        self.imageData = []  # cv2.imread(self.imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
        self.img_height = int(0)
        self.img_width = int(0)
        # if len(self.imageData) > 0:
        #     # 獲取圖像的高度和寬度：
        #     # print(self.imageData.shape)
        #     self.img_height, self.img_width, img_dimension = self.imageData.shape
        #     # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;
        #     # 遍歷每個像素：
        #     for i in range(img_height):
        #         for j in range(img_width):
        #             pixel_value = self.imageData[i, j]  # 在這個示例中：self.imageData[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
        #             print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))
        # print("Image height:", str(self.img_height))
        # print("Image width:", str(self.img_width))
        self.grayImageData = []  # cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
        self.binaryImageData = []  # cv2.threshold(self.grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) 或者 cv2.threshold(self.grayImageData, 127, 255, cv2.THRESH_BINARY_INV)  # 過濾轉化爲二值化（非黑即白）的圖片;
        # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
        # self.binaryImageData = cv2.ximgproc.thinning(self.binaryImageData, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;
        self.HorizontalLineDetect = "Hough"  # "PixelDifference";
        self.VerticalLineDetect = "Hough"  # "PixelDifference";
        self.Canny_threshold1 = int(30)  # cv2.Canny()：第一次閾值；
        self.Canny_threshold2 = int(240)  # cv2.Canny()：第二次閾值；
        self.Canny_apertureSize = int(3)  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        self.Canny_L2gradient = bool(False)  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        self.HoughLinesP_rho = int(1)  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        self.HoughLinesP_theta = float(np.pi/180)  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        self.HoughLinesP_threshold = int(100)  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        self.HoughLinesP_minLineLength = None  # int(150)  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        self.HoughLinesP_maxLineGap = None  # int(15)  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        self.tableRecognition_HorizontalLineDetect_Canny_threshold1 = int(30)
        self.tableRecognition_HorizontalLineDetect_Canny_threshold2 = int(240)
        self.tableRecognition_HorizontalLineDetect_Canny_apertureSize = int(3)
        self.tableRecognition_HorizontalLineDetect_Canny_L2gradient = bool(False)
        self.tableRecognition_HorizontalLineDetect_HoughLinesP_rho = int(1)
        self.tableRecognition_HorizontalLineDetect_HoughLinesP_theta = float(np.pi/180)
        self.tableRecognition_HorizontalLineDetect_HoughLinesP_threshold = int(100)
        self.tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength = int(150)
        self.tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap = int(15)
        self.tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope = float(0)  # float(5)  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        self.tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept = float(0)  # float(5)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        self.tableRecognition_VerticalLineDetect_Canny_threshold1 = int(30)
        self.tableRecognition_VerticalLineDetect_Canny_threshold2 = int(240)
        self.tableRecognition_VerticalLineDetect_Canny_apertureSize = int(3)
        self.tableRecognition_VerticalLineDetect_Canny_L2gradient = bool(False)
        self.tableRecognition_VerticalLineDetect_HoughLinesP_rho = int(1)
        self.tableRecognition_VerticalLineDetect_HoughLinesP_theta = float(np.pi/180)
        self.tableRecognition_VerticalLineDetect_HoughLinesP_threshold = int(100)
        self.tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength = int(150)
        self.tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap = int(15)
        self.tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope = float(0)  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        self.tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept = float(0)  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        self.tableRecognition_Cell_Top_embedded = int(0)  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        self.tableRecognition_Cell_Bottom_embedded = int(0)  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        self.tableRecognition_Cell_Left_embedded = int(0)  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        self.tableRecognition_Cell_Right_embedded = int(0)  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        self.lineMeasuring_HorizontalLineDetect_Canny_threshold1 = int(30)
        self.lineMeasuring_HorizontalLineDetect_Canny_threshold2 = int(240)
        self.lineMeasuring_HorizontalLineDetect_Canny_apertureSize = int(3)
        self.lineMeasuring_HorizontalLineDetect_Canny_L2gradient = bool(False)
        self.lineMeasuring_HorizontalLineDetect_HoughLinesP_rho = int(1)
        self.lineMeasuring_HorizontalLineDetect_HoughLinesP_theta = float(np.pi/180)
        self.lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold = int(100)
        self.lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength = int(100)
        self.lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap = int(10)
        self.lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope = float(0)  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        self.lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept = float(0)  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        self.lineMeasuring_VerticalLineDetect_Canny_threshold1 = int(30)
        self.lineMeasuring_VerticalLineDetect_Canny_threshold2 = int(240)
        self.lineMeasuring_VerticalLineDetect_Canny_apertureSize = int(3)
        self.lineMeasuring_VerticalLineDetect_Canny_L2gradient = bool(False)
        self.lineMeasuring_VerticalLineDetect_HoughLinesP_rho = int(1)
        self.lineMeasuring_VerticalLineDetect_HoughLinesP_theta = float(np.pi/180)
        self.lineMeasuring_VerticalLineDetect_HoughLinesP_threshold = int(20)
        self.lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength = int(15)
        self.lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap = int(10)
        self.lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope = float(0)  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        self.lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept = float(0)  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        self.lineMeasuring_Cell_Top_extension = int(0)  # int(-45)  # 截取圖片單元區域的上邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        self.lineMeasuring_Cell_Left_extension = int(0)  # int(-90)  # 截取圖片單元區域的左邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        self.lineMeasuring_Cell_Bottom_extension = int(0)  # int(0)  # 截取圖片單元區域的下邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        self.lineMeasuring_Cell_Right_extension = int(0)  # int(90)  # 截取圖片單元區域的右邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        self.lineMeasuring_Cell_Top_embedded = int(0)  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        self.lineMeasuring_Cell_Bottom_embedded = int(0)  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        self.lineMeasuring_Cell_Left_embedded = int(0)  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        self.lineMeasuring_Cell_Right_embedded = int(0)  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        self.CV_parameter = {}
        self.save_image = False  # True
        self.OCRmethod = "teressact"
        self.tesseract_cmd = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tesseract")).replace('\\', '/')  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
        # self.tesseract_cmd = str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
        # self.tesseract_cmd = str(pathlib.Path(os.path.abspath("..") + "/Tesseract-OCR/" + "/tesseract/"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
        # os.path.abspath(".")  # 獲取當前文檔所在的絕對路徑;
        # os.path.abspath("..")  # 獲取當前文檔所在目錄的上一層路徑;
        # pytesseract.pytesseract.tesseract_cmd = tesseract_cmd  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
        self.tesseract_lang = 'chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選多語言混合識別，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
        self.tesseract_config = '--psm 3 --oem 3'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        self.tesseract_output_type = pytesseract.Output.STRING  # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
        self.tesseract_timeout = float(0.0)  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
        self.tesseract_tessdata_dir = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tessdata", "chi_tra.traineddata")).replace('\\', '/')   # "/usr/share/tessdata" # File PATH：用戶自定義指定本地訓練完畢的數據集文檔（tessdata）的儲存路徑位置，使用 Tesseract 識別，需要使用訓練好的數據集，如果不指定該參數，則預設使用系統預設的數據集文檔目錄 Specify the location of tessdata path.
        self.tesseract_user_words = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tesswords")).replace('\\', '/')  # File PATH：用戶自定義指定的詞庫（字典）文檔的存儲位置，用戶字典可以包含一些特定的詞匯，以提高對特定詞匯的識別準確性，用戶字典文件應爲純文本文檔，每行一個詞匯 Specify the location of user words file.
        self.tesseract_user_patterns = ""  # File PATH：用戶自定義指定的特定格式文本的文檔的存儲位置，即每行使用「某種正則表達式」，例如，正在掃描具有相同格式數據的多張頁面，即可使用此參數，特定格式文本的文檔應爲純文本文檔，每行一個正則表達式模式 Specify the location of user patterns file.
        self.OCR_parameter = {}
        self.do_Function = None

        if "purpose" in kwargs:
            self.purpose = str(kwargs["purpose"])

        if "imageUrl" in kwargs:
            self.imageUrl = str(kwargs["imageUrl"])

        if "imagePath" in kwargs:
            self.imagePath = str(kwargs["imagePath"])

        if "imageData" in kwargs:
            self.imageData = kwargs["imageData"]

        if "grayImageData" in kwargs:
            self.grayImageData = kwargs["grayImageData"]

        if "binaryImageData" in kwargs:
            self.binaryImageData = kwargs["binaryImageData"]

        if "save_image" in kwargs:
            self.save_image = bool(kwargs["save_image"])

        # # 用於監聽程序的輪詢延遲參數，單位（秒） and isinstance(time_sleep, str);
        # if "time_sleep" in kwargs:
        #     self.time_sleep = float(kwargs["time_sleep"])  # 延遲時長;

        # # 用於判斷監聽創建子進程池數目的參數  and isinstance(number_Worker_process, str);
        # if "number_Worker_process" in kwargs:
        #     self.number_Worker_process = int(kwargs["number_Worker_process"])  # 子進程數目默認 0 個;

        # 使用 OpenCV 分割處理圖片的參數;
        # self.CV_parameter = {}
        if "CV_parameter" in kwargs and isinstance(kwargs["CV_parameter"], dict) and any(kwargs["CV_parameter"]):
            # # isinstance(CV_parameter, dict) type(CV_parameter) == dict CV_parameter != {} any(CV_parameter)
            # for key in kwargs["CV_parameter"]:
            #     # isinstance(CV_parameter[key], FunctionType)  # 使用原生模組 inspect 中的 isfunction() 方法判斷對象是否是一個函數，或者使用 hasattr(var, '__call__') 判斷變量 var 是否為函數或類的方法，如果是函數返回 True 否則返回 False;
            #     if key == "HorizontalLineDetect" and inspect.isfunction(kwargs["CV_parameter"][key]):
            #         self.CV_parameter[key] = kwargs["CV_parameter"][key]
            CV_parameter = kwargs["CV_parameter"]

        for key in CV_parameter:
            if key == "HorizontalLineDetect":
                self.HorizontalLineDetect = str(CV_parameter[key])
            if key == "VerticalLineDetect":
                self.VerticalLineDetect = str(CV_parameter[key])
            if key == "Canny_threshold1":
                self.Canny_threshold1 = CV_parameter[key]
            if key == "Canny_threshold2":
                self.Canny_threshold2 = CV_parameter[key]
            if key == "Canny_apertureSize":
                self.Canny_apertureSize = CV_parameter[key]
            if key == "Canny_L2gradient":
                self.Canny_L2gradient = bool(CV_parameter[key])
            if key == "HoughLinesP_rho":
                self.HoughLinesP_rho = CV_parameter[key]
            if key == "HoughLinesP_theta":
                self.HoughLinesP_theta = CV_parameter[key]
            if key == "HoughLinesP_threshold":
                self.HoughLinesP_threshold = CV_parameter[key]
            if key == "HoughLinesP_minLineLength":
                self.HoughLinesP_minLineLength = CV_parameter[key]
            if key == "HoughLinesP_maxLineGap":
                self.HoughLinesP_maxLineGap = CV_parameter[key]
            if key == "tableRecognition_HorizontalLineDetect_Canny_threshold1":
                self.tableRecognition_HorizontalLineDetect_Canny_threshold1 = CV_parameter[key]
            if key == "tableRecognition_HorizontalLineDetect_Canny_threshold2":
                self.tableRecognition_HorizontalLineDetect_Canny_threshold2 = CV_parameter[key]
            if key == "tableRecognition_HorizontalLineDetect_Canny_apertureSize":
                self.tableRecognition_HorizontalLineDetect_Canny_apertureSize = CV_parameter[key]
            if key == "tableRecognition_HorizontalLineDetect_Canny_L2gradient":
                self.tableRecognition_HorizontalLineDetect_Canny_L2gradient = bool(CV_parameter[key])
            if key == "tableRecognition_HorizontalLineDetect_HoughLinesP_rho":
                self.tableRecognition_HorizontalLineDetect_HoughLinesP_rho = CV_parameter[key]
            if key == "tableRecognition_HorizontalLineDetect_HoughLinesP_theta":
                self.tableRecognition_HorizontalLineDetect_HoughLinesP_theta = CV_parameter[key]
            if key == "tableRecognition_HorizontalLineDetect_HoughLinesP_threshold":
                self.tableRecognition_HorizontalLineDetect_HoughLinesP_threshold = CV_parameter[key]
            if key == "tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength":
                self.tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength = CV_parameter[key]
            if key == "tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap":
                self.tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap = CV_parameter[key]
            if key == "tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope":
                self.tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope = float(CV_parameter[key])
            if key == "tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept":
                self.tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept = float(CV_parameter[key])
            if key == "tableRecognition_VerticalLineDetect_Canny_threshold1":
                self.tableRecognition_VerticalLineDetect_Canny_threshold1 = CV_parameter[key]
            if key == "tableRecognition_VerticalLineDetect_Canny_threshold2":
                self.tableRecognition_VerticalLineDetect_Canny_threshold2 = CV_parameter[key]
            if key == "tableRecognition_VerticalLineDetect_Canny_apertureSize":
                self.tableRecognition_VerticalLineDetect_Canny_apertureSize = CV_parameter[key]
            if key == "tableRecognition_VerticalLineDetect_Canny_L2gradient":
                self.tableRecognition_VerticalLineDetect_Canny_L2gradient = bool(CV_parameter[key])
            if key == "tableRecognition_VerticalLineDetect_HoughLinesP_rho":
                self.tableRecognition_VerticalLineDetect_HoughLinesP_rho = CV_parameter[key]
            if key == "tableRecognition_VerticalLineDetect_HoughLinesP_theta":
                self.tableRecognition_VerticalLineDetect_HoughLinesP_theta = CV_parameter[key]
            if key == "tableRecognition_VerticalLineDetect_HoughLinesP_threshold":
                self.tableRecognition_VerticalLineDetect_HoughLinesP_threshold = CV_parameter[key]
            if key == "tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength":
                self.tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength = CV_parameter[key]
            if key == "tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap":
                self.tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap = CV_parameter[key]
            if key == "tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope":
                self.tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope = float(CV_parameter[key])
            if key == "tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept":
                self.tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept = float(CV_parameter[key])
            if key == "tableRecognition_Cell_Top_embedded":
                self.tableRecognition_Cell_Top_embedded = int(CV_parameter[key])
            if key == "tableRecognition_Cell_Bottom_embedded":
                self.tableRecognition_Cell_Bottom_embedded = int(CV_parameter[key])
            if key == "tableRecognition_Cell_Left_embedded":
                self.tableRecognition_Cell_Left_embedded = int(CV_parameter[key])
            if key == "tableRecognition_Cell_Right_embedded":
                self.tableRecognition_Cell_Right_embedded = int(CV_parameter[key])
            if key == "lineMeasuring_HorizontalLineDetect_Canny_threshold1":
                self.lineMeasuring_HorizontalLineDetect_Canny_threshold1 = CV_parameter[key]
            if key == "lineMeasuring_HorizontalLineDetect_Canny_threshold2":
                self.lineMeasuring_HorizontalLineDetect_Canny_threshold2 = CV_parameter[key]
            if key == "lineMeasuring_HorizontalLineDetect_Canny_apertureSize":
                self.lineMeasuring_HorizontalLineDetect_Canny_apertureSize = CV_parameter[key]
            if key == "lineMeasuring_HorizontalLineDetect_Canny_L2gradient":
                self.lineMeasuring_HorizontalLineDetect_Canny_L2gradient = bool(CV_parameter[key])
            if key == "lineMeasuring_HorizontalLineDetect_HoughLinesP_rho":
                self.lineMeasuring_HorizontalLineDetect_HoughLinesP_rho = CV_parameter[key]
            if key == "lineMeasuring_HorizontalLineDetect_HoughLinesP_theta":
                self.lineMeasuring_HorizontalLineDetect_HoughLinesP_theta = CV_parameter[key]
            if key == "lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold":
                self.lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold = CV_parameter[key]
            if key == "lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength":
                self.lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength = CV_parameter[key]
            if key == "lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap":
                self.lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap = CV_parameter[key]
            if key == "lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope":
                self.lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope = float(CV_parameter[key])
            if key == "lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept":
                self.lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept = float(CV_parameter[key])
            if key == "lineMeasuring_VerticalLineDetect_Canny_threshold1":
                self.lineMeasuring_VerticalLineDetect_Canny_threshold1 = CV_parameter[key]
            if key == "lineMeasuring_VerticalLineDetect_Canny_threshold2":
                self.lineMeasuring_VerticalLineDetect_Canny_threshold2 = CV_parameter[key]
            if key == "lineMeasuring_VerticalLineDetect_Canny_apertureSize":
                self.lineMeasuring_VerticalLineDetect_Canny_apertureSize = CV_parameter[key]
            if key == "lineMeasuring_VerticalLineDetect_Canny_L2gradient":
                self.lineMeasuring_VerticalLineDetect_Canny_L2gradient = bool(CV_parameter[key])
            if key == "lineMeasuring_VerticalLineDetect_HoughLinesP_rho":
                self.lineMeasuring_VerticalLineDetect_HoughLinesP_rho = CV_parameter[key]
            if key == "lineMeasuring_VerticalLineDetect_HoughLinesP_theta":
                self.lineMeasuring_VerticalLineDetect_HoughLinesP_theta = CV_parameter[key]
            if key == "lineMeasuring_VerticalLineDetect_HoughLinesP_threshold":
                self.lineMeasuring_VerticalLineDetect_HoughLinesP_threshold = CV_parameter[key]
            if key == "lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength":
                self.lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength = CV_parameter[key]
            if key == "lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap":
                self.lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap = CV_parameter[key]
            if key == "lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope":
                self.lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope = float(CV_parameter[key])
            if key == "lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept":
                self.lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept = float(CV_parameter[key])
            if key == "lineMeasuring_Cell_Top_extension":
                self.lineMeasuring_Cell_Top_extension = int(CV_parameter[key])
            if key == "lineMeasuring_Cell_Left_extension":
                self.lineMeasuring_Cell_Left_extension = int(CV_parameter[key])
            if key == "lineMeasuring_Cell_Bottom_extension":
                self.lineMeasuring_Cell_Bottom_extension = int(CV_parameter[key])
            if key == "lineMeasuring_Cell_Right_extension":
                self.lineMeasuring_Cell_Right_extension = int(CV_parameter[key])
            if key == "lineMeasuring_Cell_Top_embedded":
                self.lineMeasuring_Cell_Top_embedded = int(CV_parameter[key])
            if key == "lineMeasuring_Cell_Bottom_embedded":
                self.lineMeasuring_Cell_Bottom_embedded = int(CV_parameter[key])
            if key == "lineMeasuring_Cell_Left_embedded":
                self.lineMeasuring_Cell_Left_embedded = int(CV_parameter[key])
            if key == "lineMeasuring_Cell_Right_embedded":
                self.lineMeasuring_Cell_Right_embedded = int(CV_parameter[key])

        if "HorizontalLineDetect" in kwargs:
            self.HorizontalLineDetect = str(kwargs["HorizontalLineDetect"])

        if "VerticalLineDetect" in kwargs:
            self.VerticalLineDetect = str(kwargs["VerticalLineDetect"])

        if "Canny_threshold1" in kwargs:
            self.Canny_threshold1 = kwargs["Canny_threshold1"]

        if "Canny_threshold2" in kwargs:
            self.Canny_threshold2 = kwargs["Canny_threshold2"]

        if "Canny_apertureSize" in kwargs:
            self.Canny_apertureSize = kwargs["Canny_apertureSize"]

        if "Canny_L2gradient" in kwargs:
            self.Canny_L2gradient = bool(kwargs["Canny_L2gradient"])

        if "HoughLinesP_rho" in kwargs:
            self.HoughLinesP_rho = kwargs["HoughLinesP_rho"]

        if "HoughLinesP_theta" in kwargs:
            self.HoughLinesP_theta = kwargs["HoughLinesP_theta"]

        if "HoughLinesP_threshold" in kwargs:
            self.HoughLinesP_threshold = kwargs["HoughLinesP_threshold"]

        if "HoughLinesP_minLineLength" in kwargs:
            self.HoughLinesP_minLineLength = kwargs["HoughLinesP_minLineLength"]

        if "HoughLinesP_maxLineGap" in kwargs:
            self.HoughLinesP_maxLineGap = kwargs["HoughLinesP_maxLineGap"]

        if "tableRecognition_HorizontalLineDetect_Canny_threshold1" in kwargs:
            self.tableRecognition_HorizontalLineDetect_Canny_threshold1 = kwargs["tableRecognition_HorizontalLineDetect_Canny_threshold1"]

        if "tableRecognition_HorizontalLineDetect_Canny_threshold2" in kwargs:
            self.tableRecognition_HorizontalLineDetect_Canny_threshold2 = kwargs["tableRecognition_HorizontalLineDetect_Canny_threshold2"]

        if "tableRecognition_HorizontalLineDetect_Canny_apertureSize" in kwargs:
            self.tableRecognition_HorizontalLineDetect_Canny_apertureSize = kwargs["tableRecognition_HorizontalLineDetect_Canny_apertureSize"]

        if "tableRecognition_HorizontalLineDetect_Canny_L2gradient" in kwargs:
            self.tableRecognition_HorizontalLineDetect_Canny_L2gradient = bool(kwargs["tableRecognition_HorizontalLineDetect_Canny_L2gradient"])

        if "tableRecognition_HorizontalLineDetect_HoughLinesP_rho" in kwargs:
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_rho = kwargs["tableRecognition_HorizontalLineDetect_HoughLinesP_rho"]

        if "tableRecognition_HorizontalLineDetect_HoughLinesP_theta" in kwargs:
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_theta = kwargs["tableRecognition_HorizontalLineDetect_HoughLinesP_theta"]

        if "tableRecognition_HorizontalLineDetect_HoughLinesP_threshold" in kwargs:
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_threshold = kwargs["tableRecognition_HorizontalLineDetect_HoughLinesP_threshold"]

        if "tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength" in kwargs:
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength = kwargs["tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength"]

        if "tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap" in kwargs:
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap = kwargs["tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap"]

        if "tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope" in kwargs:
            self.tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope = float(kwargs["tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope"])

        if "tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept" in kwargs:
            self.tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept = float(kwargs["tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept"])

        if "tableRecognition_VerticalLineDetect_Canny_threshold1" in kwargs:
            self.tableRecognition_VerticalLineDetect_Canny_threshold1 = kwargs["tableRecognition_VerticalLineDetect_Canny_threshold1"]

        if "tableRecognition_VerticalLineDetect_Canny_threshold2" in kwargs:
            self.tableRecognition_VerticalLineDetect_Canny_threshold2 = kwargs["tableRecognition_VerticalLineDetect_Canny_threshold2"]

        if "tableRecognition_VerticalLineDetect_Canny_apertureSize" in kwargs:
            self.tableRecognition_VerticalLineDetect_Canny_apertureSize = kwargs["tableRecognition_VerticalLineDetect_Canny_apertureSize"]

        if "tableRecognition_VerticalLineDetect_Canny_L2gradient" in kwargs:
            self.tableRecognition_VerticalLineDetect_Canny_L2gradient = bool(kwargs["tableRecognition_VerticalLineDetect_Canny_L2gradient"])

        if "tableRecognition_VerticalLineDetect_HoughLinesP_rho" in kwargs:
            self.tableRecognition_VerticalLineDetect_HoughLinesP_rho = kwargs["tableRecognition_VerticalLineDetect_HoughLinesP_rho"]

        if "tableRecognition_VerticalLineDetect_HoughLinesP_theta" in kwargs:
            self.tableRecognition_VerticalLineDetect_HoughLinesP_theta = kwargs["tableRecognition_VerticalLineDetect_HoughLinesP_theta"]

        if "tableRecognition_VerticalLineDetect_HoughLinesP_threshold" in kwargs:
            self.tableRecognition_VerticalLineDetect_HoughLinesP_threshold = kwargs["tableRecognition_VerticalLineDetect_HoughLinesP_threshold"]

        if "tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength" in kwargs:
            self.tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength = kwargs["tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength"]

        if "tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap" in kwargs:
            self.tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap = kwargs["tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap"]

        if "tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope" in kwargs:
            self.tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope = float(kwargs["tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope"])

        if "tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept" in kwargs:
            self.tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept = float(kwargs["tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept"])

        if "tableRecognition_Cell_Top_embedded" in kwargs:
            self.tableRecognition_Cell_Top_embedded = int(kwargs["tableRecognition_Cell_Top_embedded"])

        if "tableRecognition_Cell_Bottom_embedded" in kwargs:
            self.tableRecognition_Cell_Bottom_embedded = int(kwargs["tableRecognition_Cell_Bottom_embedded"])

        if "tableRecognition_Cell_Left_embedded" in kwargs:
            self.tableRecognition_Cell_Left_embedded = int(kwargs["tableRecognition_Cell_Left_embedded"])

        if "tableRecognition_Cell_Right_embedded" in kwargs:
            self.tableRecognition_Cell_Right_embedded = int(kwargs["tableRecognition_Cell_Right_embedded"])

        if "lineMeasuring_HorizontalLineDetect_Canny_threshold1" in kwargs:
            self.lineMeasuring_HorizontalLineDetect_Canny_threshold1 = kwargs["lineMeasuring_HorizontalLineDetect_Canny_threshold1"]

        if "lineMeasuring_HorizontalLineDetect_Canny_threshold2" in kwargs:
            self.lineMeasuring_HorizontalLineDetect_Canny_threshold2 = kwargs["lineMeasuring_HorizontalLineDetect_Canny_threshold2"]

        if "lineMeasuring_HorizontalLineDetect_Canny_apertureSize" in kwargs:
            self.lineMeasuring_HorizontalLineDetect_Canny_apertureSize = kwargs["lineMeasuring_HorizontalLineDetect_Canny_apertureSize"]

        if "lineMeasuring_HorizontalLineDetect_Canny_L2gradient" in kwargs:
            self.lineMeasuring_HorizontalLineDetect_Canny_L2gradient = bool(kwargs["lineMeasuring_HorizontalLineDetect_Canny_L2gradient"])

        if "lineMeasuring_HorizontalLineDetect_HoughLinesP_rho" in kwargs:
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_rho = kwargs["lineMeasuring_HorizontalLineDetect_HoughLinesP_rho"]

        if "lineMeasuring_HorizontalLineDetect_HoughLinesP_theta" in kwargs:
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_theta = kwargs["lineMeasuring_HorizontalLineDetect_HoughLinesP_theta"]

        if "lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold" in kwargs:
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold = kwargs["lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold"]

        if "lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength" in kwargs:
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength = kwargs["lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength"]

        if "lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap" in kwargs:
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap = kwargs["lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap"]

        if "lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope" in kwargs:
            self.lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope = float(kwargs["lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope"])

        if "lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept" in kwargs:
            self.lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept = float(kwargs["lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept"])

        if "lineMeasuring_VerticalLineDetect_Canny_threshold1" in kwargs:
            self.lineMeasuring_VerticalLineDetect_Canny_threshold1 = kwargs["lineMeasuring_VerticalLineDetect_Canny_threshold1"]

        if "lineMeasuring_VerticalLineDetect_Canny_threshold2" in kwargs:
            self.lineMeasuring_VerticalLineDetect_Canny_threshold2 = kwargs["lineMeasuring_VerticalLineDetect_Canny_threshold2"]

        if "lineMeasuring_VerticalLineDetect_Canny_apertureSize" in kwargs:
            self.lineMeasuring_VerticalLineDetect_Canny_apertureSize = kwargs["lineMeasuring_VerticalLineDetect_Canny_apertureSize"]

        if "lineMeasuring_VerticalLineDetect_Canny_L2gradient" in kwargs:
            self.lineMeasuring_VerticalLineDetect_Canny_L2gradient = bool(kwargs["lineMeasuring_VerticalLineDetect_Canny_L2gradient"])

        if "lineMeasuring_VerticalLineDetect_HoughLinesP_rho" in kwargs:
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_rho = kwargs["lineMeasuring_VerticalLineDetect_HoughLinesP_rho"]

        if "lineMeasuring_VerticalLineDetect_HoughLinesP_theta" in kwargs:
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_theta = kwargs["lineMeasuring_VerticalLineDetect_HoughLinesP_theta"]

        if "lineMeasuring_VerticalLineDetect_HoughLinesP_threshold" in kwargs:
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_threshold = kwargs["lineMeasuring_VerticalLineDetect_HoughLinesP_threshold"]

        if "lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength" in kwargs:
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength = kwargs["lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength"]

        if "lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap" in kwargs:
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap = kwargs["lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap"]

        if "lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope" in kwargs:
            self.lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope = float(kwargs["lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope"])

        if "lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept" in kwargs:
            self.lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept = float(kwargs["lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept"])

        if "lineMeasuring_Cell_Top_extension" in kwargs:
            self.lineMeasuring_Cell_Top_extension = int(kwargs["lineMeasuring_Cell_Top_extension"])

        if "lineMeasuring_Cell_Left_extension" in kwargs:
            self.lineMeasuring_Cell_Left_extension = int(kwargs["lineMeasuring_Cell_Left_extension"])

        if "lineMeasuring_Cell_Bottom_extension" in kwargs:
            self.lineMeasuring_Cell_Bottom_extension = int(kwargs["lineMeasuring_Cell_Bottom_extension"])

        if "lineMeasuring_Cell_Right_extension" in kwargs:
            self.lineMeasuring_Cell_Right_extension = int(kwargs["lineMeasuring_Cell_Right_extension"])

        if "lineMeasuring_Cell_Top_embedded" in kwargs:
            self.lineMeasuring_Cell_Top_embedded = int(kwargs["lineMeasuring_Cell_Top_embedded"])

        if "lineMeasuring_Cell_Bottom_embedded" in kwargs:
            self.lineMeasuring_Cell_Bottom_embedded = int(kwargs["lineMeasuring_Cell_Bottom_embedded"])

        if "lineMeasuring_Cell_Left_embedded" in kwargs:
            self.lineMeasuring_Cell_Left_embedded = int(kwargs["lineMeasuring_Cell_Left_embedded"])

        if "lineMeasuring_Cell_Right_embedded" in kwargs:
            self.lineMeasuring_Cell_Right_embedded = int(kwargs["lineMeasuring_Cell_Right_embedded"])

        # 使用 Tesseract-OCR 識別圖片中的字符（Character）的參數;
        # self.OCR_parameter = {}
        if "OCR_parameter" in kwargs and isinstance(kwargs["OCR_parameter"], dict) and any(kwargs["OCR_parameter"]):
            # # isinstance(OCR_parameter, dict) type(OCR_parameter) == dict OCR_parameter != {} any(OCR_parameter)
            # for key in kwargs["OCR_parameter"]:
            #     if key == "teressact":
            #         self.OCR_parameter[key] = kwargs["OCR_parameter"][key]
            OCR_parameter = kwargs["OCR_parameter"]

        for key in OCR_parameter:
            if key == "OCRmethod":
                self.OCRmethod = str(OCR_parameter[key])
            if key == "tesseract_cmd":
                self.tesseract_cmd = str(OCR_parameter[key])
            if key == "tesseract_lang":
                self.tesseract_lang = str(OCR_parameter[key])
            if key == "tesseract_config":
                self.tesseract_config = str(OCR_parameter[key])
            if key == "tesseract_timeout":
                self.tesseract_timeout = int(OCR_parameter[key])
            if key == "tesseract_tessdata_dir":
                self.tesseract_tessdata_dir = str(OCR_parameter[key])
            if key == "tesseract_user_words":
                self.tesseract_user_words = str(OCR_parameter[key])
            if key == "tesseract_user_patterns":
                self.tesseract_user_patterns = str(OCR_parameter[key])
            if key == "tesseract_output_type":
                if str(OCR_parameter[key]) == 'pytesseract.Output.STRING':
                    self.tesseract_output_type = pytesseract.Output.STRING
                if str(OCR_parameter[key]) == 'pytesseract.Output.BYTES':
                    self.tesseract_output_type = pytesseract.Output.BYTES
                if str(OCR_parameter[key]) == 'pytesseract.Output.DICT':
                    self.tesseract_output_type = pytesseract.Output.DICT
                if str(OCR_parameter[key]) == 'pytesseract.Output.DATAFRAME':
                    self.tesseract_output_type = pytesseract.Output.DATAFRAME

        if "tesseract_cmd" in kwargs:
            self.tesseract_cmd = str(kwargs["tesseract_cmd"])

        if "OCRmethod" in kwargs:
            self.OCRmethod = str(kwargs["OCRmethod"])

        if "tesseract_lang" in kwargs:
            self.tesseract_lang = str(kwargs["tesseract_lang"])

        if "tesseract_config" in kwargs:
            self.tesseract_config = str(kwargs["tesseract_config"])

        if "tesseract_timeout" in kwargs:
            self.tesseract_timeout = int(kwargs["tesseract_timeout"])

        if "tesseract_tessdata_dir" in kwargs:
            self.tesseract_tessdata_dir = str(kwargs["tesseract_tessdata_dir"])

        if "tesseract_user_words" in kwargs:
            self.tesseract_user_words = str(kwargs["tesseract_user_words"])

        if "tesseract_user_patterns" in kwargs:
            self.tesseract_user_patterns = str(kwargs["tesseract_user_patterns"])

        if "tesseract_output_type" in kwargs:
            if str(kwargs["tesseract_output_type"]) == 'pytesseract.Output.STRING':
                self.tesseract_output_type = pytesseract.Output.STRING
            if str(kwargs["tesseract_output_type"]) == 'pytesseract.Output.BYTES':
                self.tesseract_output_type = pytesseract.Output.BYTES
            if str(kwargs["tesseract_output_type"]) == 'pytesseract.Output.DICT':
                self.tesseract_output_type = pytesseract.Output.DICT
            if str(kwargs["tesseract_output_type"]) == 'pytesseract.Output.DATAFRAME':
                self.tesseract_output_type = pytesseract.Output.DATAFRAME

        # # 具體處理數據的函數;
        # # self.do_Function = None
        # if "do_Function" in kwargs and inspect.isfunction(kwargs["do_Function"]):
        #     self.do_Function = kwargs["do_Function"]

        # # 傳入處理完數據後的，輸出參數;
        # # self.output_dir = ""
        # # self.output_file = ""
        # # self.to_executable = ""
        # # self.to_script = ""
        # if "return_obj" in kwargs and isinstance (kwargs["return_obj"], dict) and any(kwargs["return_obj"]):
        #     # isinstance(return_obj, dict) type(return_obj) == dict return_obj != {} any(return_obj)
        #     for key in kwargs["return_obj"]:
        #         # isinstance(return_obj[key], FunctionType)  # 使用原生模組 inspect 中的 isfunction() 方法判斷對象是否是一個函數;
        #         if key == "output_dir" and type(kwargs["return_obj"][key]) == str:
        #             self.output_dir = kwargs["return_obj"][key]
        #         if key == "output_file" and type(kwargs["return_obj"][key]) == str:
        #             self.output_file = kwargs["return_obj"][key]
        #         if key == "to_executable" and type(kwargs["return_obj"][key]) == str:
        #             self.to_executable = kwargs["return_obj"][key]
        #         if key == "to_script" and type(kwargs["return_obj"][key]) == str:
        #             self.to_script = kwargs["return_obj"][key]

        # 如果參數中未傳入圖片數據，而傳入了圖片文檔的存儲路徑位置字符串，則從圖片文檔的存儲路徑位置讀取圖片數據;
        if len(self.imageData) > 0:
            # 獲取圖像的高度和寬度：
            # print(self.imageData.shape)
            self.img_height, self.img_width, _ = self.imageData.shape
            # self.img_height, self.img_width, img_dimension = self.imageData.shape
            # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;
            # # 遍歷每個像素：
            # for i in range(img_height):
            #     for j in range(img_width):
            #         pixel_value = self.imageData[i, j]  # 在這個示例中：self.imageData[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
            #         print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))
            if len(self.grayImageData) == 0:
                self.grayImageData = cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
                if len(self.binaryImageData) == 0:
                    # self.binaryImageData = cv2.threshold(self.grayImageData, 127, 255, cv2.THRESH_BINARY_INV)  # 使用自定義閾值：「127」，過濾轉化爲二值化（非黑即白）的圖片;
                    self.binaryImageData = cv2.threshold(self.grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
                    # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
                    # self.binaryImageData = cv2.ximgproc.thinning(self.binaryImageData, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;
        if len(self.imageData) == 0:
            if len(self.imagePath) > 0:
                self.imageData = cv2.imread(self.imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
                if len(self.imageData) > 0:
                    # 獲取圖像的高度和寬度：
                    # print(self.imageData.shape)
                    self.img_height, self.img_width, _ = self.imageData.shape
                    # self.img_height, self.img_width, img_dimension = self.imageData.shape
                    # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;
                    # # 遍歷每個像素：
                    # for i in range(img_height):
                    #     for j in range(img_width):
                    #         pixel_value = self.imageData[i, j]  # 在這個示例中：self.imageData[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
                    #         print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))
                if len(self.grayImageData) == 0:
                    self.grayImageData = cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
                    if len(self.binaryImageData) == 0:
                        # self.binaryImageData = cv2.threshold(self.grayImageData, 127, 255, cv2.THRESH_BINARY_INV)  # 使用自定義閾值：「127」，過濾轉化爲二值化（非黑即白）的圖片;
                        self.binaryImageData = cv2.threshold(self.grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
                        # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
                        # self.binaryImageData = cv2.ximgproc.thinning(self.binaryImageData, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;
            elif len(self.imageUrl) > 0:
                response = urllib_request.urlopen(self.imageUrl)  # 使用 Python 語言的原生模組「urllib」中的「request」中的「urlopen()」函數向服務器請求下載圖片數據;
                img_array = np.array(bytearray(response.read()), dtype = np.uint8)  # 把從服務器下載的圖片數據轉換爲二進位 8 位字節數組的形式;
                self.imageData = cv2.imdecode(img_array, -1)  # 使用 Python 語言的第三方擴展模組「opencv」中的「cv2.imdecode()」函數解析二進位 8 位字節數組形式的图片數據，RGB 模式;
                if len(self.imageData) > 0:
                    # 獲取圖像的高度和寬度：
                    # print(self.imageData.shape)
                    self.img_height, self.img_width, _ = self.imageData.shape
                    # self.img_height, self.img_width, img_dimension = self.imageData.shape
                    # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;
                    # # 遍歷每個像素：
                    # for i in range(img_height):
                    #     for j in range(img_width):
                    #         pixel_value = self.imageData[i, j]  # 在這個示例中：self.imageData[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
                    #         print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))
                if len(self.grayImageData) == 0:
                    self.grayImageData = cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
                    if len(self.binaryImageData) == 0:
                        # self.binaryImageData = cv2.threshold(self.grayImageData, 127, 255, cv2.THRESH_BINARY_INV)  # 使用自定義閾值：「127」，過濾轉化爲二值化（非黑即白）的圖片;
                        self.binaryImageData = cv2.threshold(self.grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
                        # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
                        # self.binaryImageData = cv2.ximgproc.thinning(self.binaryImageData, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;
            # else:
            #     print("Image data empty.")

        if "img_height" in kwargs:
            self.img_height = int(kwargs["img_height"])
        # print("Image height:", str(self.img_height))

        if "img_width" in kwargs:
            self.img_width = int(kwargs["img_width"])
        # print("Image width:", str(self.img_width))

        # if self.OCRmethod == "teressact":
        #     if len(self.tesseract_cmd) > 0:
        #         # self.tesseract_cmd == r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # tesseract_cmd = r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
        #         pytesseract.pytesseract.tesseract_cmd = self.tesseract_cmd  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;

        if len(self.tesseract_tessdata_dir) > 0:
            self.tesseract_config = str(str(self.tesseract_config) + ' --tessdata-dir=' + str(self.tesseract_tessdata_dir))

        if len(self.tesseract_user_words) > 0:
            self.tesseract_config = str(str(self.tesseract_config) + ' --user-words=' + str(self.tesseract_user_words))

        if len(self.tesseract_user_patterns) > 0:
            self.tesseract_config = str(str(self.tesseract_config) + ' --user-patterns=' + str(self.tesseract_user_patterns))

    # 圖像旋轉方位調整矯正 ORIENTATION CORRECTION/ADJUSTMENT;
    # import math  # 導入 Python 原生包「math」，用於數學計算;
    # import cv2  # 導入第三方擴展包「opencv-contrib-python」，用於驅動 OpenCV 光學圖形處理庫，需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 OpenCV 應用成功：root@localhost:~# apt install libavcodec-dev libavformat-dev libswscale-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libgtk2.0-dev libgtk-3-dev libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev libjasper-dev libopencv-dev python3-opencv ;
    # import numpy as np
    # from scipy import ndimage as scipy_ndimage  # 導入第三方擴展包「scipy」中的圖片（Image）處理模組「ndimage」，用於實現圖形旋轉矯正操作;
    def orientation_correction(
        self,
        img,
        save_image = ""
    ):
        # image = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
        
        img_rotated = []  # 存儲對圖形做旋轉矯正操作之後的圖片數據;

        img_edges = cv2.Canny(grayImage, 100, 100, apertureSize=3)  # 使用 Canny 算灋做圖形邊緣檢測 Canny Algorithm for edge detection was developed by John F. Canny not Kennedy!! :);
        lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)  # 使用 Houghlines 算灋檢測線條 Using Houghlines to detect lines;

        # 判斷是否一條都沒有識別出缐段;
        if len(lines) == 0:
            print('line not detected.')
            img_rotated = img
            return img_rotated

        # 計算極座標中缐條的傾角 Finding angle of lines in polar coordinates;
        angles = []
        for x1, y1, x2, y2 in lines[0]:
            angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
            # if math.atan2(y2 - y1, x2 - x1) != 0.0 and math.atan2(y2 - y1, x2 - x1) != 1.5707963267948966 and math.atan2(y2 - y1, x2 - x1) != 3.141592653589793 and math.atan2(y2 - y1, x2 - x1) != -1.5707963267948966:
            # if angle != 0.0 and angle != 90.0 and angle != 180.0 and angle != -90.0:
            if angle != math.degrees(0.0) and angle != math.degrees(math.pi/2) and angle != math.degrees(math.pi) and angle != math.degrees(-math.pi/2):
                angles.append(angle)

        if len(angles) > 0:
            median_angle = np.median(angles)  # 獲取傾角中值 Getting the median angle;
            img_rotated = scipy_ndimage.rotate(img, median_angle)  # 對圖像做旋轉操作，旋轉角度爲傾角中值 Rotating the image with this median angle;
        else:
            img_rotated = img

        if save_image != "":
            cv2.imwrite(save_image, img_rotated)

        return img_rotated

    # 截取圖片（Image）中使用滑鼠自定義選擇的感興趣的區域 REGION OF INTEREST (ROI) SELECTION;
    # 爲鼠標設置一個事件偵聽器，使用戶能夠自定義手動選擇圖片（Image）中感興趣的區域，在這裏設置了兩個條件，一個是滑鼠左鍵「按下」事件，一個是滑鼠左鍵「釋放按下」事件;
    # 程序存儲「按下」滑鼠左鍵時的起始座標點，和存儲「釋放按下」的滑鼠左鍵時的座標點，然後，在按下鍵盤中的「Enter」鍵時，截取這些起始座標和結束座標之間的區域，如果按下鍵盤中的「Esc」鍵時，則刪除存儲的座標;
    # import cv2  # 導入第三方擴展包「opencv-contrib-python」，用於驅動 OpenCV 光學圖形處理庫，需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 OpenCV 應用成功：root@localhost:~# apt install libavcodec-dev libavformat-dev libswscale-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libgtk2.0-dev libgtk-3-dev libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev libjasper-dev libopencv-dev python3-opencv ;
    def region_selection(
        self,
        img,
        save_image = ""
    ):
        coordinates = []  # 初始化用於存儲選中座標點值的清單 initializing the list for storing the coordinates;
        # 定義事件偵聽器回調函數 Defining the event listener (callback function);

        def shape_selection(event, x, y, flags, param):
            global coordinates  # making coordinates global;

            # 按下滑鼠左鍵時存儲（x1，y1）座標 Storing the (x1,y1) coordinates when left mouse button is pressed;
            if event == cv2.EVENT_LBUTTONDOWN:
                coordinates = [(x, y)]
            # 釋放滑鼠左鍵時存儲（x2，y2）座標，並在選定區域上繪製矩形 Storing the (x2,y2) coordinates when the left mouse button is released and make a rectangle on the selected region;
            elif event == cv2.EVENT_LBUTTONUP:
                coordinates.append((x, y))

            # 在選定區域上繪製矩形 Drawing a rectangle around the region of interest (roi);
            cv2.rectangle(image_copy, coordinates[0], coordinates[1], (0,0,255), 2)  # 使用 cv2.rectangle() 函數繪製矩形，參數：image_copy 表示原圖片的副本;
            cv2.imshow("image", image_copy)  # 在名稱爲 "image" 的窗口中顯示圖片：image_copy ;

        # 載入圖片，創建圖片副本，調用回調函數 load the image, clone it, and setup the mouse callback function;
        image_copy = img.copy()  # 創建圖片副本;
        cv2.namedWindow("image")  # 創建圖片展示窗口;
        cv2.setMouseCallback("image", shape_selection)

        # keep looping until the 'q' key is pressed
        while True:
            # display the image and wait for a keypress
            cv2.imshow("image", image_copy)
            key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;

            # If 'Enter' is pressed, apply OCR
            # chr(13) == 'enter'
            # ord("\n") == 13
            # if key == ord('\n'):
            if key == 13:
                break

            # Clear the selection when 'Esc' is pressed
            # chr(27) == 'esc'
            # ord("\x1b") == 27
            # if key == ord('\x1b'):
            if key == 27:
                img = image_copy.copy()

            # 回車鍵（Enter）的 ASCII 碼爲：ord('\n')
            # 空格鍵的 ASCII 碼爲：ord(' ')
            # Tab 鍵的 ASCII 碼爲：ord('\t')
            # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
            # 換行鍵的 ASCII 碼爲：ord('\r')
            # Esc 鍵的 ASCII 碼爲：ord('\x1b')

        # 截取選中區域;
        image_select = []
        if len(coordinates) == 2:
            image_select = image_copy[coordinates[0][1]:coordinates[1][1], coordinates[0][0]:coordinates[1][0]]
        cv2.imshow("Selected Region of Interest - Press any key to proceed", image_select)

        if save_image != "":
            cv2.imwrite(save_image, image_select)

        # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;

        cv2.destroyAllWindows()  # closing all open windows

        return image_select

    # 重叠缐過濾器;
    # 較粗的缐條由多個相同位置，長度不同的缐條組成，爲了消除此重叠缐，定義一個重叠缐過濾器，如果下一行的間隔小於一定距離，則將其視爲與上一行相同的缐條;
    def OverlappingFilter(
        self,
        lines,
        separationThresholdSlope = float(0),  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        separationThresholdIntercept = float(0)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
    ):
        filtered_lines = []  # 存儲過濾掉重叠缐之後的缐段座標的列表;

        for i in range(0, int(len(lines) - int(1)), 1):

            l_curr = lines[i]

            if i > 0:

                l_prev = lines[i - int(1)]

                separation_Intercept = float(0)  # 表示兩條缐條截距之間的間距，單位：圖元（像素）點個數;
                separation_Slope = float(0)  # 表示兩條缐條斜率之間的間距，單位：角度（0 ~ 90）;

                # 兩點式直缐方程：(y-Y1)/(Y2-Y1) = (x-X1)/(X2-X1)  (X1 ≠ X2, Y1 ≠ Y2);
                # Slope = (Y2-Y1)/(X2-X1)
                # Slope_X = (X2-X1)/(Y2-Y1)
                # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                # Intercept_X = (X2·Y1-X1·Y2)/(Y2-Y1)
                # 一般式直缐方程：A·x + B·y + C = 0 （A ≠ 0, B ≠ 0）;
                # Slope = -A/B
                # Intercept = -C/B
                # A = C·(Slope/Intercept) = C·(Y2-Y1)/(X2·Y1-X1·Y2)
                # B = -C/Intercept = -C·(X2-X1)/(X2·Y1-X1·Y2)
                # C = any one (for example: C = 1)

                # 當缐：l_curr 與缐：l_prev 都爲橫向水平缐時，只與截距閾值：separationThresholdIntercept 比較大小：
                if l_curr[1] == l_curr[3] and l_curr[0] != l_curr[2] and l_prev[1] == l_prev[3] and l_prev[0] != l_prev[2]:
                    l_curr_Slope = float(0)  # Slope = (Y2-Y1)/(X2-X1)
                    l_curr_Intercept = float(l_curr[1])  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                    l_prev_Slope = float(0)  # Slope = (Y2-Y1)/(X2-X1)
                    l_prev_Intercept = float(l_prev[1])  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                    # separation_Intercept = math.fabs(math.fabs(l_curr[1]) - math.fabs(l_prev[1]))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                    separation_Intercept = math.fabs(math.fabs(l_curr_Intercept) - math.fabs(l_prev_Intercept))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                    # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                    if float(separation_Intercept) > float(separationThresholdIntercept):
                        filtered_lines.append(l_curr)

                # 當缐：l_curr 與缐：l_prev 都爲縱向垂直缐時，只與截距閾值：separationThresholdIntercept 比較大小：
                if l_curr[1] != l_curr[3] and l_curr[0] == l_curr[2] and l_prev[1] != l_prev[3] and l_prev[0] == l_prev[2]:
                    l_curr_Slope =  math.inf  # +∞ 正無窮大 inf 全稱爲：infinity; # Slope = (Y2-Y1)/(X2-X1)
                    l_curr_Slope_X = float(0)  # 與 Y 軸夾角的正切值：= (X2-X1)/(Y2-Y1)，注意，不是斜率，與 X 軸夾角的正切值：= (Y2-Y1)/(X2-X1);
                    l_curr_Intercept = math.inf  # +∞ 正無窮大 inf 全稱爲：infinity; # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                    l_curr_Intercept_X = float(l_curr[0])  # 與 X 軸的交點：=(X2·Y1-X1·Y2)/(Y2-Y1)，注意，不是截距，與 Y 軸的交點：=(X2·Y1-X1·Y2)/(X2-X1);
                    l_prev_Slope =  math.inf  # +∞ 正無窮大 inf 全稱爲：infinity; # Slope = (Y2-Y1)/(X2-X1)
                    l_prev_Slope_X = float(0)  # 與 Y 軸夾角的正切值：= (X2-X1)/(Y2-Y1)，注意，不是斜率，與 X 軸夾角的正切值：= (Y2-Y1)/(X2-X1);
                    l_prev_Intercept = math.inf  # +∞ 正無窮大 inf 全稱爲：infinity; # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                    l_prev_Intercept_X = float(l_prev[0])  # 與 X 軸的交點：=(X2·Y1-X1·Y2)/(Y2-Y1)，注意，不是截距，與 Y 軸的交點：=(X2·Y1-X1·Y2)/(X2-X1);
                    # separation_Intercept = math.fabs(math.fabs(l_curr[0]) - math.fabs(l_prev[0]))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                    separation_Intercept = math.fabs(math.fabs(l_curr_Intercept_X) - math.fabs(l_prev_Intercept_X))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                    # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                    if float(separation_Intercept) > float(separationThresholdIntercept):
                        filtered_lines.append(l_curr)

                # 當缐：l_curr 爲橫向水平缐，缐：l_prev 即不是橫向水平缐，也不是縱向垂直缐時，先與截距閾值：separationThresholdIntercept 比較大小，然後再與斜率閾值：separationThresholdSlope 比較大小：
                if l_curr[1] == l_curr[3] and l_curr[0] != l_curr[2] and l_prev[1] != l_prev[3] and l_prev[0] != l_prev[2]:
                    l_curr_Slope = float(0)
                    l_curr_Intercept = float(l_curr[1])
                    l_prev_Slope = float((l_prev[3] - l_prev[1]) / (l_prev[2] - l_prev[0]))  # Slope = (Y2-Y1)/(X2-X1)
                    l_prev_Intercept = float((l_prev[2] * l_prev[1] - l_prev[0] * l_prev[3]) / (l_prev[2] - l_prev[0]))  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                    separation_Intercept = math.fabs(math.fabs(l_curr_Intercept) - math.fabs(l_prev_Intercept))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                    separation_Slope = math.fabs(float(math.fabs(l_prev_Slope) - math.fabs(l_curr_Slope)))
                    # 判斷表示兩條缐條之間的間距是否大於自定義設置的斜率（Slope）閾值：separationThresholdSlope，若大於則保存，若小於等於則濾過捨棄;
                    # 函數：math.tan() 表示求正切值，函數：math.atan() 表示求反正切值，函數：math.degrees() 表示將弧度角度值轉換爲角度值，函數：math.radians() 表示將角度值轉換爲弧度值;
                    if float(separation_Slope) > float(math.tan(math.radians(separationThresholdSlope))):
                        # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                        if float(separation_Intercept) > float(separationThresholdIntercept):
                            filtered_lines.append(l_curr)

                # 當缐：l_curr 爲縱向垂直缐，缐：l_prev 即不是縱向垂直缐，也不是橫向水平缐時，先與截距閾值：separationThresholdIntercept 比較大小，然後再與斜率閾值：separationThresholdSlope 比較大小：
                if l_curr[1] != l_curr[3] and l_curr[0] == l_curr[2] and l_prev[1] != l_prev[3] and l_prev[0] != l_prev[2]:
                    l_curr_Slope = math.inf  # +∞ 正無窮大 inf 全稱爲：infinity;
                    l_curr_Slope_X = float(0)  # 與 Y 軸夾角的正切值：= (X2-X1)/(Y2-Y1)，注意，不是斜率，與 X 軸夾角的正切值：= (Y2-Y1)/(X2-X1);
                    l_curr_Intercept = math.inf # +∞ 正無窮大 inf 全稱爲：infinity;
                    l_curr_Intercept_X = float(l_curr[0])  # 與 X 軸的交點：=(X2·Y1-X1·Y2)/(Y2-Y1)，注意，不是截距，與 Y 軸的交點：=(X2·Y1-X1·Y2)/(X2-X1);
                    l_prev_Slope = float((l_prev[3] - l_prev[1]) / (l_prev[2] - l_prev[0]))  # Slope = (Y2-Y1)/(X2-X1)
                    l_prev_Slope_X = float((l_prev[2] - l_prev[0]) / (l_prev[3] - l_prev[1]))  # 與 Y 軸夾角的正切值：= (X2-X1)/(Y2-Y1)，注意，不是斜率，與 X 軸夾角的正切值：= (Y2-Y1)/(X2-X1);
                    l_prev_Intercept = float((l_prev[2] * l_prev[1] - l_prev[0] * l_prev[3]) / (l_prev[2] - l_prev[0]))  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                    l_prev_Intercept_X = float((l_prev[2] * l_prev[1] - l_prev[0] * l_prev[3]) / (l_prev[3] - l_prev[1]))  # 與 X 軸的交點：=(X2·Y1-X1·Y2)/(Y2-Y1)，注意，不是截距，與 Y 軸的交點：=(X2·Y1-X1·Y2)/(X2-X1);
                    separation_Intercept = math.fabs(math.fabs(l_curr_Intercept_X) - math.fabs(l_prev_Intercept_X))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                    separation_Slope = math.fabs(float(math.fabs(l_prev_Slope_X) - math.fabs(l_curr_Slope_X)))
                    # 判斷表示兩條缐條之間的間距是否大於自定義設置的斜率（Slope）閾值：separationThresholdSlope，若大於則保存，若小於等於則濾過捨棄;
                    # 函數：math.tan() 表示求正切值，函數：math.atan() 表示求反正切值，函數：math.degrees() 表示將弧度角度值轉換爲角度值，函數：math.radians() 表示將角度值轉換爲弧度值;
                    if float(separation_Slope) > float(math.tan(math.radians(separationThresholdSlope))):
                        # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                        if float(separation_Intercept) > float(separationThresholdIntercept):
                            filtered_lines.append(l_curr)

                # 當缐：l_curr 即不是橫向水平缐，也不是縱向垂直缐，缐：l_prev 爲橫向水平缐時，先與截距閾值：separationThresholdIntercept 比較大小，然後再與斜率閾值：separationThresholdSlope 比較大小：
                if l_curr[1] != l_curr[3] and l_curr[0] != l_curr[2] and l_prev[1] == l_prev[3] and l_prev[0] != l_prev[2]:
                    l_curr_Slope = float((l_curr[3] - l_curr[1]) / (l_curr[2] - l_curr[0]))  # Slope = (Y2-Y1)/(X2-X1)
                    l_curr_Intercept = float((l_curr[2] * l_curr[1] - l_curr[0] * l_curr[3]) / (l_curr[2] - l_curr[0]))  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                    l_prev_Slope = float(0)
                    l_prev_Intercept = float(l_prev[1])
                    separation_Intercept = math.fabs(math.fabs(l_curr_Intercept) - math.fabs(l_prev_Intercept))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                    separation_Slope = math.fabs(float(math.fabs(l_prev_Slope) - math.fabs(l_curr_Slope)))
                    # 判斷表示兩條缐條之間的間距是否大於自定義設置的斜率（Slope）閾值：separationThresholdSlope，若大於則保存，若小於等於則濾過捨棄;
                    # 函數：math.tan() 表示求正切值，函數：math.atan() 表示求反正切值，函數：math.degrees() 表示將弧度角度值轉換爲角度值，函數：math.radians() 表示將角度值轉換爲弧度值;
                    if float(separation_Slope) > float(math.tan(math.radians(separationThresholdSlope))):
                        # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                        if float(separation_Intercept) > float(separationThresholdIntercept):
                            filtered_lines.append(l_curr)

                # 當缐：l_curr 即不是縱向垂直缐，也不是橫向水平缐，缐：l_prev 爲縱向垂直缐時，先與截距閾值：separationThresholdIntercept 比較大小，然後再與斜率閾值：separationThresholdSlope 比較大小：
                if l_curr[1] != l_curr[3] and l_curr[0] != l_curr[2] and l_prev[1] != l_prev[3] and l_prev[0] == l_prev[2]:
                    l_curr_Slope = float((l_curr[3] - l_curr[1]) / (l_curr[2] - l_curr[0]))  # Slope = (Y2-Y1)/(X2-X1)
                    l_curr_Slope_X = float((l_curr[2] - l_curr[0]) / (l_curr[3] - l_curr[1]))  # 與 Y 軸夾角的正切值：= (X2-X1)/(Y2-Y1)，注意，不是斜率，與 X 軸夾角的正切值：= (Y2-Y1)/(X2-X1);
                    l_curr_Intercept = float((l_curr[2] * l_curr[1] - l_curr[0] * l_curr[3]) / (l_curr[2] - l_curr[0]))  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                    l_curr_Intercept_X = float((l_curr[2] * l_curr[1] - l_curr[0] * l_curr[3]) / (l_curr[3] - l_curr[1]))  # 與 X 軸的交點：=(X2·Y1-X1·Y2)/(Y2-Y1)，注意，不是截距，與 Y 軸的交點：=(X2·Y1-X1·Y2)/(X2-X1);
                    l_prev_Slope = math.inf  # +∞ 正無窮大 inf 全稱爲：infinity;
                    l_prev_Slope_X = float(0)  # 與 Y 軸夾角的正切值：= (X2-X1)/(Y2-Y1)，注意，不是斜率，與 X 軸夾角的正切值：= (Y2-Y1)/(X2-X1);
                    l_prev_Intercept = math.inf # +∞ 正無窮大 inf 全稱爲：infinity;
                    l_prev_Intercept_X = float(l_prev[0])  # 與 X 軸的交點：=(X2·Y1-X1·Y2)/(Y2-Y1)，注意，不是截距，與 Y 軸的交點：=(X2·Y1-X1·Y2)/(X2-X1);
                    separation_Intercept = math.fabs(math.fabs(l_curr_Intercept_X) - math.fabs(l_prev_Intercept_X))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                    separation_Slope = math.fabs(float(math.fabs(l_prev_Slope_X) - math.fabs(l_curr_Slope_X)))
                    # 判斷表示兩條缐條之間的間距是否大於自定義設置的斜率（Slope）閾值：separationThresholdSlope，若大於則保存，若小於等於則濾過捨棄;
                    # 函數：math.tan() 表示求正切值，函數：math.atan() 表示求反正切值，函數：math.degrees() 表示將弧度角度值轉換爲角度值，函數：math.radians() 表示將角度值轉換爲弧度值;
                    if float(separation_Slope) > float(math.tan(math.radians(separationThresholdSlope))):
                        # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                        if float(separation_Intercept) > float(separationThresholdIntercept):
                            filtered_lines.append(l_curr)

                # 當缐：l_curr 即不是橫向水平缐，也不是縱向垂直缐，缐：l_prev 即不是橫向水平缐，也不是縱向垂直缐時，既與截距閾值：separationThresholdIntercept 比較大小，也同時與斜率閾值：separationThresholdSlope 比較大小：
                if l_curr[1] != l_curr[3] and l_curr[0] != l_curr[2] and l_prev[1] != l_prev[3] and l_prev[0] != l_prev[2]:
                    l_curr_Slope = float((l_curr[3] - l_curr[1]) / (l_curr[2] - l_curr[0]))  # Slope = (Y2-Y1)/(X2-X1)
                    l_curr_Intercept = float((l_curr[2] * l_curr[1] - l_curr[0] * l_curr[3]) / (l_curr[2] - l_curr[0]))  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                    l_prev_Slope = float((l_prev[3] - l_prev[1]) / (l_prev[2] - l_prev[0]))  # Slope = (Y2-Y1)/(X2-X1)
                    l_prev_Intercept = float((l_prev[2] * l_prev[1] - l_prev[0] * l_prev[3]) / (l_prev[2] - l_prev[0]))  # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                    separation_Intercept = math.fabs(math.fabs(l_curr_Intercept) - math.fabs(l_prev_Intercept))  # 計算兩條缐條之間的間距，單位：圖元（像素）點個數;
                    separation_Slope = math.fabs(float(math.fabs(l_prev_Slope) - math.fabs(l_curr_Slope)))
                    # 判斷表示兩條缐條之間的間距是否大於自定義設置的斜率（Slope）閾值：separationThresholdSlope，若大於則保存，若小於等於則濾過捨棄;
                    # 函數：math.tan() 表示求正切值，函數：math.atan() 表示求反正切值，函數：math.degrees() 表示將弧度角度值轉換爲角度值，函數：math.radians() 表示將角度值轉換爲弧度值;
                    if float(separation_Slope) > float(math.tan(math.radians(separationThresholdSlope))):
                        # 判斷表示兩條缐條之間的間距是否大於自定義設置的截距（Intercept）閾值：separationThresholdIntercept，若大於則保存，若小於等於則濾過捨棄;
                        if float(separation_Intercept) > float(separationThresholdIntercept):
                            filtered_lines.append(l_curr)

            else:

                filtered_lines.append(l_curr)

        return filtered_lines

    # 查找綫條的兩個端點;
    # 原理：必須爲經過二值化（非黑即白）過濾轉化處理過的圖片數據，不能是 RGB 形式的原始圖片數據，查找缐條上的每個點（圖元/像素）的相鄰點（圖元/像素）（查找四面八方 8 個方向），若缐條上的某個點（圖元/像素）只有 1 個相鄰點（圖元/像素），那麽該點即爲該缐條的一個端點; if neighbours count equals 1 --> the point is an end point;
    def getCurvesEnd(
        self,
        # img,
        CurvesImage
    ):
        # 第三方庫「OpenCV」中，邊緣（輪廓）檢測「cv2.Canny()」;
        # edges = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])
        # 其中參數：
        # image：待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）；
        # threshold1：第一次閾值；
        # threshold2：第二次閾值；
        # apertureSize：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        # L2gradient：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        # 函數返回值是一個輸出圖像，與輸入圖像大小及類型相同。
        # 函數「cv2.canny()」的實現原理主要基於以下幾個步驟：
        # Step 1：圖像灰度化。首先將輸入圖像轉換爲單通道的灰度圖像，可以通過函數「cv2.cvtColor」函數來完成。
        # Step 2：邊緣強度梯度計算。使用索伯爾運算元（Sobel）（算子）計算每個圖元（pixel）（像素）點在水平和垂直方向上的梯度值，並通過勾股定理（Pythagorean theorem）計算梯度幅值和方向。
        # Step 3：非極大值抑制。爲了減少邊緣（輪廓）圖元（pixel）（像素）數量，需要對梯度圖像中的強度值進行非極大值抑制，即只保留局部最大值點。
        # Step 4：滯後閾值處理。根據設定的閾值大小，將梯度幅值大於閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）。接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點也標記爲邊緣（輪廓）點。
        # Step 5：輸出邊緣（輪廓）圖像。最後將所有被標記爲邊緣（輪廓）的圖元（pixel）（像素）點輸出爲邊緣（輪廓）圖像。

        # 第三方庫「OpenCV」中，有兩種算法檢測直缐或缐段，即「cv2.HoughLines()」標準霍夫缐變換「Hough Transform」和「cv2.HoughLinesP()」概率霍夫缐變換「Probabilistic Hough Transform」;
        # 標準霍夫缐變換「Hough Transform」函數「cv2.HoughLines()」返回值爲直綫的方程，即檢測結果爲「直綫」;
        # lines = cv2.HoughLines(image, rho, theta, threshold)
        # 概率霍夫缐變換「Probabilistic Hough Transform」函數「cv2.HoughLinesP()」返回值爲缐段起點與終點的座標值列表，即檢測結果爲「缐段」;
        # lines = cv2.HoughLinesP(image, rho, theta, threshold, minLineLength=None, maxLineGap=None)
        # 其中參數：
        # image：待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測；
        # rho：距離解析度（分辨率），單位爲：圖元（pixel）（像素）每英寸，通常情況下，將距離解析度設為 1 即可，即每英寸 1 個；
        # theta：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        # threshold：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        # minLineLength：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        # maxLineGap：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        # 函數返回值是一個三維陣列，其中每個元素表示一條直線，格式爲列表：(x1, y1, x2, y2），表示直線的兩個端點座標。

        # 第三方庫「OpenCV」中，查找圖片（Image）中的所有輪廓「cv2.findContours()」;
        # contours, hierarchy = cv2.findContours(binaryImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 查找圖片（Image）中的所有輪廓;

        # # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        # # grayImage = cv2.imread("./testImage.jpg", cv2.IMREAD_GRAYSCALE)  # 读取硬盤中的图片，RGB 模式，並把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
        # grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
        # binaryImage = cv2.threshold(grayImage, 128, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)  # 將圖像過濾轉化爲二值化（非黑即白）的圖片;
        # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
        # # binaryImage = cv2.ximgproc.thinning(binaryImage)  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;

        # CurvesImage = cv2.imread("./testCurvesImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        # grayCurvesImage = cv2.imread("./testCurvesImage.jpg", cv2.IMREAD_GRAYSCALE)  # 读取硬盤中的图片，RGB 模式，並把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
        grayCurvesImage = cv2.cvtColor(CurvesImage, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
        binaryCurvesImage = cv2.threshold(grayCurvesImage, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 過濾轉化爲二值化（非黑即白）的圖片;
        # binaryCurvesImage = cv2.threshold(grayCurvesImage, 127, 255, cv2.THRESH_BINARY_INV)  # 過濾轉化爲二值化（非黑即白）的圖片;
        # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
        binaryCurvesImage = cv2.ximgproc.thinning(binaryCurvesImage, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;
        Curves = cv2.findNonZero(binaryCurvesImage)  # 查找非零圖元（像素）;
        Curves = np.squeeze(Curves)  # 將表示向量的數組轉換爲秩爲 1 的數組，函數：numpy.squeeze() 用於從數組的形狀中刪除單維條目，即把 numpy.shape 中爲 1 的維度去掉，用於降低維度;

        # # 截取缐條圖形數據;
        # detectCurvesImage = img[CurvesImage[1]:CurvesImage[3], CurvesImage[0]:CurvesImage[2]]

        extremes = []  # 存儲找到的綫條端點的坐標列表;

        for point in Curves:

            x = point[0]  # 缐條上點（圖元/像素）的橫向坐標值;
            y = point[1]  # 缐條上點（圖元/像素）的縱向坐標值;

            number_Adjacent = 0  # 記錄找到的相鄰點的數目;

            whitePoint = 255  # 在二值化（非黑即白）過濾轉化後的圖片上，當某個圖元（像素）值 = 255 時，表示該點爲白色（White）存在;
            blackPoint = 0  # 在二值化（非黑即白）過濾轉化後的圖片上，當某個圖元（像素）值 = 0 時表示該點爲黑色（Black）不存在;

            # 查找判斷「下 ↓」方相鄰點是否存在，若存在。則對記錄相鄰點的數目 + 1，在二值化（非黑即白）過濾轉化後的圖片上，當某個圖元（像素）值 = 255 時，表示該點爲白色（White）存在，當某個圖元（像素）值 = 0 時表示該點爲黑色（Black）不存在;
            if binaryCurvesImage[y - 1, x] == whitePoint:
                number_Adjacent = number_Adjacent + 1
            # 查找判斷「左下 ↙」方相鄰點是否存在，若存在。則對記錄相鄰點的數目 + 1;
            if binaryCurvesImage[y - 1, x - 1] == whitePoint:
                number_Adjacent = number_Adjacent + 1
            # 查找判斷「左 ←」方相鄰點是否存在，若存在。則對記錄相鄰點的數目 + 1;
            if binaryCurvesImage[y, x - 1] == whitePoint:
                number_Adjacent = number_Adjacent + 1
            # 查找判斷「左上 ↖」方相鄰點是否存在，若存在。則對記錄相鄰點的數目 + 1;
            if binaryCurvesImage[y + 1, x - 1] == whitePoint:
                number_Adjacent = number_Adjacent + 1
            # 查找判斷「上 ↑」方相鄰點是否存在，若存在。則對記錄相鄰點的數目 + 1;
            if binaryCurvesImage[y + 1, x] == whitePoint:
                number_Adjacent = number_Adjacent + 1
            # 查找判斷「右上 ↗」方相鄰點是否存在，若存在。則對記錄相鄰點的數目 + 1;
            if binaryCurvesImage[y + 1, x + 1] == whitePoint:
                number_Adjacent = number_Adjacent + 1
            # 查找判斷「右 →」方相鄰點是否存在，若存在。則對記錄相鄰點的數目 + 1;
            if binaryCurvesImage[y, x + 1] == whitePoint:
                number_Adjacent = number_Adjacent + 1
            # 查找判斷「右下 ↘」方相鄰點是否存在，若存在。則對記錄相鄰點的數目 + 1;
            if binaryCurvesImage[y - 1, x + 1] == whitePoint:
                number_Adjacent = number_Adjacent + 1

            # 判斷是否只有 1 個相鄰點（圖元/像素），若只有 1 個相鄰點（圖元/像素），則保存記錄該點爲缐條的一個端點;
            if number_Adjacent == 1:
                extremes.append(point)
                # cv2.circle(self.image, point, 1, (255, 255, 0), 2)  # 在源圖像上繪製識別出缐條的「端點」;

        # # 在源圖像上繪製所有識別出缐條的「端點」;
        # for point in extremes:
        #     cv2.circle(self.image, point, 1, (255, 255, 0), 2)

        return extremes

    # 圖片（Image）中表格（Table）的橫向直缐檢測;
    # 當圖片（Image）表格（Table）中兩個橫向相鄰的記錄（橫向兩個橫行）之間的顏色是不一致時，識別圖片（Image）表格（Table）中的分割兩條記錄的橫線；原理是：利用圖片（Image）灰度化後，每一橫行圖元的平均值的差的絕對值來作為相鄰兩條記錄的分割線，這樣就可以檢測出分割兩條記錄的橫線;
    def tableRecognition_HorizontalLineDetect_PixelDifference(
        self,
        grayImage
    ):
        # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        # grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;

        ret, thresh1 = cv2.threshold(grayImage, 240, 255, cv2.THRESH_BINARY)  # 圖像二值化;

        # 兩次使用中值濾波，目的是爲了使相鄰兩條記錄之間的像素區別盡可能的大;
        blur = cv2.medianBlur(thresh1, 3)  # 使用中值濾波，模板大小爲：3 × 3;
        blur = cv2.medianBlur(blur, 3)  # 使用中值濾波，模板大小爲：3 × 3;

        h, w = grayImage.shape  # 讀取圖片（Image）橫向像素的行數目、縱向列像素的數目;
        # self.img_height, self.img_width, img_dimension = img.shape
        # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;

        horizontal_lines = []  # 存儲在圖像表格（Table）中檢測到的橫向直缐座標的列表;
        for i in range(h - 1):
            # 找到表格（Table）兩條記錄的橫向分隔缐段，以相鄰兩行的平均像素差值大於 120 作爲判定標準;
            if abs(np.mean(blur[i, :]) - np.mean(blur[i + 1, :])) > 120:
                horizontal_lines.append([0, i, w, i])  # 存儲在圖像表格（Table）中檢測到的橫向直缐座標;
                # cv2.line(self.image, (0, i), (w, i), (0, 255, 0), 2)  # 在源圖像上繪製識別出的表格（Table）橫向分隔缐段;

        horizontal_lines = horizontal_lines[1:]  # 存儲識別出的表格（Table）橫向分隔缐段的座標值;
        # print(horizontal_lines)

        return horizontal_lines

    # 識別表格（Table）中的橫向分隔缐段;
    # 使用第三方庫「OpenCV」中的概率霍夫變換「Probabilistic Hough Transform」演算法進行直缐檢測，來識別圖片（Image）表格（Table）中的橫向分隔缐段;
    def tableRecognition_HorizontalLineDetect_Hough(
        self,
        grayImage,
        Canny_threshold1,  # cv2.Canny()：第一次閾值；
        Canny_threshold2,  # cv2.Canny()：第二次閾值；
        Canny_apertureSize,  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        Canny_L2gradient,  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        HoughLinesP_rho,  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        HoughLinesP_theta,  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        HoughLinesP_threshold,  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        HoughLinesP_minLineLength,  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        HoughLinesP_maxLineGap  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
    ):
        # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        # grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;

        # edges = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])
        # 其中參數：
        # image：待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）；
        # threshold1：第一次閾值；
        # threshold2：第二次閾值；
        # apertureSize：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        # L2gradient：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        # 函數返回值是一個輸出圖像，與輸入圖像大小及類型相同。
        # 函數「cv2.canny()」的實現原理主要基於以下幾個步驟：
        # Step 1：圖像灰度化。首先將輸入圖像轉換爲單通道的灰度圖像，可以通過函數「cv2.cvtColor」函數來完成。
        # Step 2：邊緣強度梯度計算。使用索伯爾運算元（Sobel）（算子）計算每個圖元（pixel）（像素）點在水平和垂直方向上的梯度值，並通過勾股定理（Pythagorean theorem）計算梯度幅值和方向。
        # Step 3：非極大值抑制。爲了減少邊緣（輪廓）圖元（pixel）（像素）數量，需要對梯度圖像中的強度值進行非極大值抑制，即只保留局部最大值點。
        # Step 4：滯後閾值處理。根據設定的閾值大小，將梯度幅值大於閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）。接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點也標記爲邊緣（輪廓）點。
        # Step 5：輸出邊緣（輪廓）圖像。最後將所有被標記爲邊緣（輪廓）的圖元（pixel）（像素）點輸出爲邊緣（輪廓）圖像。

        # 使用第三方庫「OpenCV」中的函數「cv2.Canny()」做圖形邊緣（輪廓）檢測，並將邊緣（輪廓）標記為白色圖元（pixel）（像素），黑色圖元（pixel）（像素）則表示非邊緣（輪廓）;
        edges = cv2.Canny(
            grayImage,  # 待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）;
            Canny_threshold1,  # 30,  # 第一次閾值，將梯度幅值大於第一次閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）;
            Canny_threshold2,  # 240,  # 第二次閾值，接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點，梯度幅值大於第二次閾值的，也標記爲邊緣（輪廓）點;
            apertureSize = Canny_apertureSize,  # 3,  # 用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3;
            L2gradient = Canny_L2gradient  # False  # 計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法;
        )

        # 第三方庫「OpenCV」中，有兩種算法檢測直缐或缐段，即「cv2.HoughLines()」標準霍夫缐變換「Hough Transform」和「cv2.HoughLinesP()」概率霍夫缐變換「Probabilistic Hough Transform」;
        # 標準霍夫缐變換「Hough Transform」函數「cv2.HoughLines()」返回值爲直綫的方程，即檢測結果爲「直綫」;
        # lines = cv2.HoughLines(image, rho, theta, threshold)
        # 概率霍夫缐變換「Probabilistic Hough Transform」函數「cv2.HoughLinesP()」返回值爲缐段起點與終點的座標值列表，即檢測結果爲「缐段」;
        # lines = cv2.HoughLinesP(image, rho, theta, threshold, minLineLength=None, maxLineGap=None)
        # 其中參數：
        # image：待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測；
        # rho：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        # theta：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        # threshold：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        # minLineLength：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        # maxLineGap：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        # 函數返回值是一個三維陣列，其中每個元素表示一條直線，格式爲列表：(x1, y1, x2, y2），表示直線的兩個端點座標。

        # 使用第三方庫「OpenCV」中的函數「cv2.HoughLinesP()」概率霍夫變換「Probabilistic Hough Transform」演算法識別圖片（Image）表格（Table）中的橫向分隔缐段;
        # minLineLength = 500  # 要求識別的缐段最小長度值（單位：圖元 pixel 也稱像素），比這個長度值小的缐段將會被忽略，自定義設定爲：500 個圖元;
        # maxLineGap = 30  # 要求識別的線段之間的最大間隔上限值（單位：圖元 pixel 也稱像素），小於這個間隔上限值的缐段將被連接爲一條直綫，自定義設定爲：30 個圖元;
        lines = cv2.HoughLinesP(
            edges,  # 待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測;
            HoughLinesP_rho,  # 1,  # 距離解析度（分辨率），單位爲：圖元（pixel）（像素）;
            HoughLinesP_theta,  # np.pi/180,  # 角度解析度（分辨率），單位爲：弧度;
            HoughLinesP_threshold,  # 100,  # 閾值參數，只有累加器中的值高於閾值才會被認為是一條直線;
            minLineLength = HoughLinesP_minLineLength,  # 要求識別的缐段最小長度值（單位：圖元 pixel 也稱像素），比這個長度值小的缐段將會被忽略，自定義設定爲：500 個圖元;
            maxLineGap = HoughLinesP_maxLineGap  # 要求識別的線段之間的最大間隔上限值（單位：圖元 pixel 也稱像素），小於這個間隔上限值的缐段將被連接爲一條直綫，自定義設定爲：30 個圖元;
        ).tolist()
        # lines.append([[13, 102, 756, 102]])  # 可以追加畫出一條自定義位置的橫向缐段;
        sorted_lines = sorted(lines, key=lambda x: x[0])

        horizontal_lines = []  # 存儲在圖像表格（Table）中檢測到的橫向分隔缐段座標的列表;
        for line in sorted_lines:
            for x1, y1, x2, y2 in line:
                if y1 == y2:
                    # print(line)
                    horizontal_lines.append([x1, y1, x2, y2])  # 存儲在圖像表格（Table）中檢測到的橫向分隔缐段座標;
                    # cv2.line(self.image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 在源圖像上繪製識別出的表格（Table）橫向分隔缐段;
        # # 在源圖像上繪製所有識別出的表格（Table）橫向分隔缐段;
        # for line in horizontal_lines:
        #     for x1, y1, x2, y2 in line:
        #         if y1 == y2:
        #             # print(line)
        #             cv2.line(self.image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 在源圖像上繪製識別出的表格（Table）橫向分隔缐段;

        return horizontal_lines

    # 圖片（Image）中表格（Table）的縱向竪直缐檢測;
    # 當圖片（Image）表格（Table）中兩個橫向相鄰的記錄（縱向兩個豎行）之間的顏色是不一致時，識別圖片（Image）表格（Table）中的分割兩條記錄的竪線；原理是：利用圖片（Image）灰度化後，每一竪行圖元的平均值的差的絕對值來作為相鄰兩條記錄的分割線，這樣就可以檢測出分割兩條記錄的竪線;
    def tableRecognition_VerticalLineDetect_PixelDifference(
        self,
        grayImage
    ):
        # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        # grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;

        ret, thresh1 = cv2.threshold(grayImage, 240, 255, cv2.THRESH_BINARY)  # 圖像二值化;

        # 兩次使用中值濾波，目的是爲了使相鄰兩條記錄之間的像素區別盡可能的大;
        blur = cv2.medianBlur(thresh1, 3)  # 使用中值濾波，模板大小爲：3 × 3;
        blur = cv2.medianBlur(blur, 3)  # 使用中值濾波，模板大小爲：3 × 3;

        h, w, _ = grayImage.shape  # 讀取圖片（Image）橫向像素的行數目、縱向列像素的數目;
        # self.img_height, self.img_width, img_dimension = img.shape
        # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;

        vertical_lines = []  # 存儲在圖像表格（Table）中檢測到的縱向直缐座標的列表;
        for i in range(w - 1):
            # 找到表格（Table）兩條記錄的縱向分隔缐段，以相鄰兩豎行的平均像素差值大於 120 作爲判定標準;
            if abs(np.mean(blur[:, i]) - np.mean(blur[:, i + 1])) > 120:
                vertical_lines.append([i, 0, i, h])  # 存儲在圖像表格（Table）中檢測到的縱向直缐座標;
                # cv2.line(self.image, (i, 0), (i, h), (255, 0, 0), 2)  # 在源圖像上繪製識別出的表格（Table）縱向分隔缐段;

        vertical_lines = vertical_lines[:1]  # 存儲識別出的表格（Table）縱向分隔缐段的座標值;
        # print(vertical_lines)

        return vertical_lines

    # 識別表格（Table）中的縱向分隔竪缐段;
    # 使用第三方庫「OpenCV」中的概率霍夫變換「Probabilistic Hough Transform」演算法進行直缐檢測，來識別圖片（Image）表格（Table）中的縱向分隔竪缐段;
    def tableRecognition_VerticalLineDetect_Hough(
        self,
        grayImage,
        Canny_threshold1,  # cv2.Canny()：第一次閾值；
        Canny_threshold2,  # cv2.Canny()：第二次閾值；
        Canny_apertureSize,  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        Canny_L2gradient,  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        HoughLinesP_rho,  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        HoughLinesP_theta,  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        HoughLinesP_threshold,  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        HoughLinesP_minLineLength,  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        HoughLinesP_maxLineGap  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
    ):
        # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        # grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;

        # edges = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])
        # 其中參數：
        # image：待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）；
        # threshold1：第一次閾值；
        # threshold2：第二次閾值；
        # apertureSize：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        # L2gradient：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        # 函數返回值是一個輸出圖像，與輸入圖像大小及類型相同。
        # 函數「cv2.canny()」的實現原理主要基於以下幾個步驟：
        # Step 1：圖像灰度化。首先將輸入圖像轉換爲單通道的灰度圖像，可以通過函數「cv2.cvtColor」函數來完成。
        # Step 2：邊緣強度梯度計算。使用索伯爾運算元（Sobel）（算子）計算每個圖元（pixel）（像素）點在水平和垂直方向上的梯度值，並通過勾股定理（Pythagorean theorem）計算梯度幅值和方向。
        # Step 3：非極大值抑制。爲了減少邊緣（輪廓）圖元（pixel）（像素）數量，需要對梯度圖像中的強度值進行非極大值抑制，即只保留局部最大值點。
        # Step 4：滯後閾值處理。根據設定的閾值大小，將梯度幅值大於閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）。接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點也標記爲邊緣（輪廓）點。
        # Step 5：輸出邊緣（輪廓）圖像。最後將所有被標記爲邊緣（輪廓）的圖元（pixel）（像素）點輸出爲邊緣（輪廓）圖像。

        # 使用第三方庫「OpenCV」中的函數「cv2.Canny()」做圖形邊緣（輪廓）檢測，並將邊緣（輪廓）標記為白色圖元（pixel）（像素），黑色圖元（pixel）（像素）則表示非邊緣（輪廓）;
        edges = cv2.Canny(
            grayImage,  # 待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）;
            Canny_threshold1,  # 30,  # 第一次閾值，將梯度幅值大於第一次閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）;
            Canny_threshold2,  # 240,  # 第二次閾值，接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點，梯度幅值大於第二次閾值的，也標記爲邊緣（輪廓）點;
            apertureSize = Canny_apertureSize,  # 3,  # 用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3;
            L2gradient = Canny_L2gradient  # False  # 計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法;
        )

        # 第三方庫「OpenCV」中，有兩種算法檢測直缐或缐段，即「cv2.HoughLines()」標準霍夫缐變換「Hough Transform」和「cv2.HoughLinesP()」概率霍夫缐變換「Probabilistic Hough Transform」;
        # 標準霍夫缐變換「Hough Transform」函數「cv2.HoughLines()」返回值爲直綫的方程，即檢測結果爲「直綫」;
        # lines = cv2.HoughLines(image, rho, theta, threshold)
        # 概率霍夫缐變換「Probabilistic Hough Transform」函數「cv2.HoughLinesP()」返回值爲缐段起點與終點的座標值列表，即檢測結果爲「缐段」;
        # lines = cv2.HoughLinesP(image, rho, theta, threshold, minLineLength=None, maxLineGap=None)
        # 其中參數：
        # image：待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測；
        # rho：距離解析度（分辨率），單位爲：圖元（pixel）（像素）每英寸，通常情況下，將距離解析度設為 1 即可，即每英寸 1 個；
        # theta：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        # threshold：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        # minLineLength：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        # maxLineGap：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        # 函數返回值是一個三維陣列，其中每個元素表示一條直線，格式爲列表：(x1, y1, x2, y2），表示直線的兩個端點座標。

        # 使用第三方庫「OpenCV」中的函數「cv2.HoughLinesP()」概率霍夫變換「Probabilistic Hough Transform」演算法識別圖片（Image）表格（Table）中的縱向分隔竪缐段;
        # minLineLength = 10  # 要求識別的缐段最小長度值（單位：圖元 pixel 也稱像素），比這個長度值小的缐段將會被忽略，自定義設定爲：10 個圖元;
        # maxLineGap = 10  # 要求識別的線段之間的最大間隔上限值（單位：圖元 pixel 也稱像素），小於這個間隔上限值的缐段將被連接爲一條直綫，自定義設定爲：10 個圖元;
        lines = cv2.HoughLinesP(
            edges,  # 待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測;
            HoughLinesP_rho,  # 1,  # 距離解析度（分辨率），單位爲：圖元（pixel）（像素）;
            HoughLinesP_theta,  # np.pi/180,  # 角度解析度（分辨率），單位爲：弧度;
            HoughLinesP_threshold,  # 100,  # 閾值參數，只有累加器中的值高於閾值才會被認為是一條直線;
            minLineLength = HoughLinesP_minLineLength,  # 要求識別的缐段最小長度值（單位：圖元 pixel 也稱像素），比這個長度值小的缐段將會被忽略，自定義設定爲：500 個圖元;
            maxLineGap = HoughLinesP_maxLineGap  # 要求識別的線段之間的最大間隔上限值（單位：圖元 pixel 也稱像素），小於這個間隔上限值的缐段將被連接爲一條直綫，自定義設定爲：30 個圖元;
        ).tolist()
        # lines.append([[13, 937, 13, 102]])  # 可以追加畫出一條自定義位置的縱向竪缐段;
        sorted_lines = sorted(lines, key=lambda x: x[0])

        vertical_lines = []  # 存儲在圖像表格（Table）中檢測到的縱向分隔竪缐段座標的列表;
        for line in sorted_lines:
            for x1, y1, x2, y2 in line:
                if x1 == x2:
                    # print(line)
                    vertical_lines.append([x1, y1, x2, y2])  # 存儲在圖像表格（Table）中檢測到的縱向分隔竪缐段座標;
                    # cv2.line(self.image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 在源圖像上繪製識別出的表格（Table）縱向分隔竪缐段;
        # # 在源圖像上繪製所有識別出的表格（Table）縱向分隔缐段;
        # for line in vertical_lines:
        #     for x1, y1, x2, y2 in line:
        #         if x1 == x2:
        #             # print(line)
        #             cv2.line(self.image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 在源圖像上繪製識別出的表格（Table）縱向分隔缐段;

        return vertical_lines

    # 識別圖片（Image）表格（Table）中單元格（Cell），在識別圖片（Image）表格（Table）中單元格（Cell）之前，先識別出每個單元格（Cell）的四個角的「頂點」，也就是上述識別後的橫縱向缐條的交點;
    def tableRecognition_VertexDetect(
        self,
        horizontal_lines,
        vertical_lines,
        img,
        img_height,
        img_width
    ):
        # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        # grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;

        # horizontal_lines = HorizontalLineDetect(img)  # HorizontalLineDetect(img) 爲自定義函數，識別出圖片（Image）中的橫向分隔缐段座標列表;
        # vertical_lines = VerticalLineDetect(img)  # VerticalLineDetect(img) 爲自定義函數，識別出圖片（Image）中的縱向分隔竪缐段座標列表;

        # vertexs = []  # 存儲圖片（Image）表格（Table）中識別出的單元格（Cell）的四個角的「頂點」座標的一維列表（向量）（縱向 → 橫向）;
        # for v_line in vertical_lines:
        #     for h_line in horizontal_lines:
        #         vertexs.append((v_line[0], h_line[1]))
        #         # print((v_line[0], h_line[1]))
        #         # cv2.circle(self.image, (v_line[0], h_line[1]), 1, (255, 0, 0), 2)  # # 在源圖像上繪製識別出的圖片（Image）表格（Table）中單元格（Cell）的四個角的「頂點」;
        # print(vertexs)
        # # 在源圖像上繪製所有識別出的圖片（Image）表格（Table）中單元格（Cell）的四個角的「頂點」;
        # for point in vertexs:
        #     cv2.circle(self.image, point, 1, (255, 0, 0), 2)

        vertexs = []  # 存儲圖片（Image）表格（Table）中識別出的單元格（Cell）的四個角的「頂點」座標的二維列表（行列式）（縱向 → 橫向）;
        vertexs_all = []  # 存儲圖片（Image）量尺（Measuring Ruler）缐段（Line segment）中識別出的橫、竪線條的理論上所有的焦點座標的二維列表（行列式）（縱向 → 橫向）;

        for v_line in vertical_lines:

            vertexs_all_line_Array = []  # 縱向的一竪行的交點「頂點」座標列表;
            vertical_line_Array = []  # 縱向的一竪行的交點「頂點」座標列表;

            for h_line in horizontal_lines:

                X_intersection = None
                Y_intersection = None

                # 兩點式直缐方程：(y-Y1)/(Y2-Y1) = (x-X1)/(X2-X1)  (X1 ≠ X2, Y1 ≠ Y2);
                # Slope = (Y2-Y1)/(X2-X1)
                # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                # 一般式直缐方程：A·x + B·y + C = 0 （A ≠ 0, B ≠ 0）;
                # Slope = -A/B
                # Intercept = -C/B
                # A = C·(Slope/Intercept) = C·(Y2-Y1)/(X2·Y1-X1·Y2)
                # B = -C/Intercept = -C·(X2-X1)/(X2·Y1-X1·Y2)
                # C = any one (for example: C = 1)

                # # 聯立兩條直缐方程，求解兩條直缐交點的橫座標（X 軸）值，兩點式直缐方程爲：(x - X1) / (X2 - X1) = (y - Y1) / (Y2 - Y1)  (X1 ≠ X2, Y1 ≠ Y2);
                # X_intersection = (v_line[1] - h_line[1] + ((h_line[3] - h_line[1]) * h_line[0] / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) * v_line[0] / (v_line[2] - v_line[0]))) / (((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0])))  # 兩直缐交點的橫座標（X 軸）值;

                # # 聯立兩條直缐方程，求解兩條直缐交點的縱座標（Y 軸）值，兩點式直缐方程爲：(x - X1) / (X2 - X1) = (y - Y1) / (Y2 - Y1)  (X1 ≠ X2, Y1 ≠ Y2);
                # Y_intersection = ((((v_line[1] - h_line[1] + ((h_line[3] - h_line[1]) * h_line[0] / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) * v_line[0] / (v_line[2] - v_line[0]))) / (((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0])))) - v_line[0]) * (v_line[3] - v_line[1]) / (v_line[2] - v_line[0])) + v_line[1]  # 兩直缐交點的縱座標（Y 軸）值;

                # 特殊式，當兩條直綫互相垂直，且與橫縱座標平行時，即當：一條直缐的：X2 = X1（即：v_line[2] == v_line[0]）且另一條直缐的：Y2 = Y1（即：h_line[3] == h_line[1]）時，即一條直缐方程爲：x = a 且另一條直缐方程爲：y = b 時，交點座標即爲：(a, b) ;

                # 當傳入參數：horizontal_lines 爲橫向水平缐，vertical_lines 爲縱向垂直缐時：
                if h_line[0] != h_line[2] and h_line[1] == h_line[3] and v_line[0] == v_line[2] and v_line[1] != v_line[3]:
                    X_intersection = v_line[0]
                    Y_intersection = h_line[1]
                if h_line[0] != h_line[2] and h_line[1] == h_line[3] and v_line[0] != v_line[2] and v_line[1] != v_line[3]:
                    X_intersection = int(round((h_line[1] * (v_line[2] - v_line[0]) - v_line[2] * v_line[1] + v_line[0] * v_line[3]) / (v_line[3] - v_line[1]), 0))  # x = (y - Intercept)/Slope = (y·(X2-X1) - X2·Y1 + X1·Y2)/(Y2-Y1)
                    # X_intersection = (h_line[1] * (v_line[2] - v_line[0]) - v_line[2] * v_line[1] + v_line[0] * v_line[3]) / (v_line[3] - v_line[1])  # x = (y - Intercept)/Slope = (y·(X2-X1) - X2·Y1 + X1·Y2)/(Y2-Y1)
                    Y_intersection = h_line[1]
                if h_line[0] != h_line[2] and h_line[1] != h_line[3] and v_line[0] == v_line[2] and v_line[1] != v_line[3]:
                    X_intersection = v_line[0]
                    # Y_intersection = (v_line[0] * (h_line[3] - h_line[1]) + h_line[2] * h_line[1] - h_line[0] * h_line[3]) / (h_line[2] - h_line[0])  # y = x·Slope + Intercept = (x·(Y2-Y1) + X2·Y1 - X1·Y2)/(X2-X1)
                    Y_intersection = int(round((v_line[0] * (h_line[3] - h_line[1]) + h_line[2] * h_line[1] - h_line[0] * h_line[3]) / (h_line[2] - h_line[0]), 0))  # y = x·Slope + Intercept = (x·(Y2-Y1) + X2·Y1 - X1·Y2)/(X2-X1)

                # 當傳入參數：horizontal_lines 爲縱向垂直缐，vertical_lines 爲橫向水平缐時：
                if h_line[0] == h_line[2] and h_line[1] != h_line[3] and v_line[0] != v_line[2] and v_line[1] == v_line[3]:
                    X_intersection = h_line[0]
                    Y_intersection = v_line[1]
                if h_line[0] == h_line[2] and h_line[1] != h_line[3] and v_line[0] != v_line[2] and v_line[1] != v_line[3]:
                    X_intersection = h_line[0]
                    # Y_intersection = (h_line[0] * (v_line[3] - v_line[1]) + v_line[2] * v_line[1] - v_line[0] * v_line[3]) / (v_line[2] - v_line[0])  # y = x·Slope + Intercept = (x·(Y2-Y1) + X2·Y1 - X1·Y2)/(X2-X1)
                    Y_intersection = int(round((h_line[0] * (v_line[3] - v_line[1]) + v_line[2] * v_line[1] - v_line[0] * v_line[3]) / (v_line[2] - v_line[0]), 0))  # y = x·Slope + Intercept = (x·(Y2-Y1) + X2·Y1 - X1·Y2)/(X2-X1)
                if h_line[0] != h_line[2] and h_line[1] != h_line[3] and v_line[0] != v_line[2] and v_line[1] == v_line[3]:
                    X_intersection = int(round((v_line[1] * (h_line[2] - h_line[0]) - h_line[2] * h_line[1] + h_line[0] * h_line[3]) / (h_line[3] - h_line[1]), 0))  # x = (y - Intercept)/Slope = (y·(X2-X1) - X2·Y1 + X1·Y2)/(Y2-Y1)
                    # X_intersection = (v_line[1] * (h_line[2] - h_line[0]) - h_line[2] * h_line[1] + h_line[0] * h_line[3]) / (h_line[3] - h_line[1])  # x = (y - Intercept)/Slope = (y·(X2-X1) - X2·Y1 + X1·Y2)/(Y2-Y1)
                    Y_intersection = v_line[1]

                # 聯立兩條直缐方程，求解兩條直缐交點的座標（橫 X 軸，縱 Y 軸）值，兩點式直缐方程爲：(x - X1) / (X2 - X1) = (y - Y1) / (Y2 - Y1)  (X1 ≠ X2, Y1 ≠ Y2);
                if h_line[0] != h_line[2] and h_line[1] != h_line[3] and v_line[0] != v_line[2] and v_line[1] != v_line[3]:
                    # 判斷兩條直綫不平行，即兩條直綫的斜率不相等，Slope = (Y2-Y1)/(X2-X1)
                    if ((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) != ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0])):
                        # X_intersection = (v_line[1] - h_line[1] + ((h_line[3] - h_line[1]) * h_line[0] / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) * v_line[0] / (v_line[2] - v_line[0]))) / (((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0])))  # 兩直缐交點的橫座標（X 軸）值;
                        X_intersection = int(round((v_line[1] - h_line[1] + ((h_line[3] - h_line[1]) * h_line[0] / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) * v_line[0] / (v_line[2] - v_line[0]))) / (((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0]))), 0))  # 兩直缐交點的橫座標（X 軸）值;
                        # Y_intersection = ((((v_line[1] - h_line[1] + ((h_line[3] - h_line[1]) * h_line[0] / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) * v_line[0] / (v_line[2] - v_line[0]))) / (((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0])))) - v_line[0]) * (v_line[3] - v_line[1]) / (v_line[2] - v_line[0])) + v_line[1]  # 兩直缐交點的縱座標（Y 軸）值;
                        Y_intersection = int(round(((((v_line[1] - h_line[1] + ((h_line[3] - h_line[1]) * h_line[0] / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) * v_line[0] / (v_line[2] - v_line[0]))) / (((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0])))) - v_line[0]) * (v_line[3] - v_line[1]) / (v_line[2] - v_line[0])) + v_line[1], 0))  # 兩直缐交點的縱座標（Y 軸）值;

                if (not (X_intersection is None)) and (not (Y_intersection is None)):

                    # print(X_intersection, Y_intersection)
                    vertexs_all_line_Array.append((X_intersection, Y_intersection))
                    vertical_line_Array.append((X_intersection, Y_intersection))

                    # # 判斷交點是否在圖片範圍内;
                    # if int(X_intersection) >= int(0) and int(Y_intersection) >= int(0) and int(X_intersection) <= int(img_width) and int(Y_intersection) <= int(img_height):
                    #     # print('Intersection position: (' + str(X_intersection) + ', ' + str(Y_intersection) + ')')
                    #     # cv2.circle(self.image, (X_intersection, Y_intersection), 1, (255, 0, 0), 2)  # # 在源圖像上繪製識別出的圖片（Image）表格（Table）中單元格（Cell）的四個角的「頂點」;
                    #     # 判斷交點是否在缐段：horizontal_lines 上;
                    #     if int(X_intersection) >= int(h_line[0]) and int(X_intersection) <= int(h_line[2]) and int(Y_intersection) >= int(h_line[1]) and int(Y_intersection) <= int(h_line[3]):
                    #         # 判斷交點是否在缐段：vertical_lines 上;
                    #         if int(X_intersection) >= int(v_line[2]) and int(X_intersection) <= int(v_line[0]) and int(Y_intersection) >= int(v_line[3]) and int(Y_intersection) <= int(v_line[1]):
                    #             # print('Intersection position: (' + str(X_intersection) + ', ' + str(Y_intersection) + ')')
                    #             vertical_line_Array.append((X_intersection, Y_intersection))
                    #             # cv2.circle(self.image, (X_intersection, Y_intersection), 1, (255, 0, 0), 2)  # # 在源圖像上繪製識別出的圖片（Image）表格（Table）中單元格（Cell）的四個角的「頂點」;

            vertexs_all.append(vertexs_all_line_Array)
            vertexs.append(vertical_line_Array)

        # print(vertexs_all)
        # print(vertexs)

        # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        # # 獲取圖像的高度和寬度：
        # img_height, img_width = img.shape
        # self.img_height, self.img_width, img_dimension = img.shape
        # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;
        # # 遍歷每個像素：
        # for i in range(img_height):
        #     for j in range(img_width):
        #         pixel_value = img[i, j]  # 在這個示例中：img[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
        #         print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))

        # # 在源圖像上繪製所有識別出的圖片（Image）表格（Table）中單元格（Cell）的四個角的「頂點」;
        # for v_point in vertexs:
        #     for h_point in v_point:
        #         cv2.circle(self.image, h_point, 1, (255, 0, 0), 2)

        return vertexs, vertexs_all

    # 然後，再把這些識別出四個角「頂點」的單元格（Cell）截取出來;
    # 截取圖片（Image）表格（Table）中單元格（Cell）;
    def tableRecognition_CellDetect(
        self,
        img,
        vertexs,
        Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        # HorizontalLineDetect,
        # VerticalLineDetect,
        # tableRecognition_VertexDetect
    ):
        # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;

        # vertexs = tableRecognition_VertexDetect(img, HorizontalLineDetect, VerticalLineDetect)  # tableRecognition_VertexDetect(img, HorizontalLineDetect, VerticalLineDetect) 爲自定義函數，識別出每個單元格（Cell）的四個角的「頂點」，也就是上述識別後的橫縱向缐條的交點座標列表;

        rects = []  # 存儲截取出的單元格（Cell）座標的列表;
        cellImages = []  # 存儲截取出的單元格（Cell）圖片（Image）數據本身的列表;

        for i in range(0, int(len(vertexs) - int(1)), 1):
            if i < int(len(vertexs) - int(1)):
                vertical_line_rects = []
                vertical_line_cellImages = []
                for j in range(0, int(len(vertexs[i]) - int(1)), 1):
                    if j < int(len(vertexs[i]) - int(1)):
                        vertical_line_rects.append(
                            (
                                vertexs[i][j][0],
                                vertexs[i][j][1],
                                vertexs[int(i + int(1))][int(j + int(1))][0],
                                vertexs[int(i + int(1))][int(j + int(1))][1]
                            )
                        )
                        # print((vertexs[i][j][0], vertexs[i][j][1], vertexs[int(i + int(1))][int(j + int(1))][0], vertexs[int(i + int(1))][int(j + int(1))][1]))
                        # vertical_line_cellImages.append(img[int(int(vertexs[i][j][1]) + Cell_Top_embedded):int(int(vertexs[int(i + int(1))][int(j + int(1))][1]) - Cell_Bottom_embedded), int(int(vertexs[i][j][0]) + Cell_Left_embedded):int(int(vertexs[int(i + int(1))][int(j + int(1))][0]) - Cell_Right_embedded)])
                        # cv2.imshow("CellImage", img[int(int(vertexs[i][j][1]) + Cell_Top_embedded):int(int(vertexs[int(i + int(1))][int(j + int(1))][1]) - Cell_Bottom_embedded), int(int(vertexs[i][j][0]) + Cell_Left_embedded):int(int(vertexs[int(i + int(1))][int(j + int(1))][0]) - Cell_Right_embedded)])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
                        # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
                        X1 = int(int(vertexs[i][j][1]) + Cell_Top_embedded)
                        Y1 = int(int(vertexs[i][j][0]) + Cell_Left_embedded)
                        X2 = int(int(vertexs[int(i + int(1))][int(j + int(1))][1]) - Cell_Bottom_embedded)
                        Y2 = int(int(vertexs[int(i + int(1))][int(j + int(1))][0]) - Cell_Right_embedded)
                        vertical_line_cellImages.append(img[X1:X2, Y1:Y2])
                        # cv2.imshow("CellImage", img[X1:X2, Y1:Y2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
                    # if j == int(len(vertexs[i]) - int(1)):
                    #     continue
                rects.append(vertical_line_rects)
                cellImages.append(vertical_line_cellImages)
                # for j in range(0, int(len(vertexs[i]) - int(1)), 1):
                #     if j < int(len(vertexs[i]) - int(1)):
                #         rects.append(
                #             (
                #                 vertexs[i][j][0],
                #                 vertexs[i][j][1],
                #                 vertexs[int(i + int(1))][int(j + int(1))][0],
                #                 vertexs[int(i + int(1))][int(j + int(1))][1]
                #             )
                #         )
                #         # print((vertexs[i][j][0], vertexs[i][j][1], vertexs[int(i + int(1))][int(j + int(1))][0], vertexs[int(i + int(1))][int(j + int(1))][1]))
                #         # cellImages.append(img[int(int(vertexs[i][j][1]) + Cell_Top_embedded):int(int(vertexs[int(i + int(1))][int(j + int(1))][1]) - Cell_Bottom_embedded), int(int(vertexs[i][j][0]) + Cell_Left_embedded):int(int(vertexs[int(i + int(1))][int(j + int(1))][0]) - Cell_Right_embedded)])
                #         # cv2.imshow("CellImage", img[int(int(vertexs[i][j][1]) + Cell_Top_embedded):int(int(vertexs[int(i + int(1))][int(j + int(1))][1]) - Cell_Bottom_embedded), int(int(vertexs[i][j][0]) + Cell_Left_embedded):int(int(vertexs[int(i + int(1))][int(j + int(1))][0]) - Cell_Right_embedded)])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
                #         # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
                #         X1 = int(int(vertexs[i][j][1]) + Cell_Top_embedded)
                #         Y1 = int(int(vertexs[i][j][0]) + Cell_Left_embedded)
                #         X2 = int(int(vertexs[int(i + int(1))][int(j + int(1))][1]) - Cell_Bottom_embedded)
                #         Y2 = int(int(vertexs[int(i + int(1))][int(j + int(1))][0]) - Cell_Right_embedded)
                #         vertical_line_cellImages.append(img[X1:X2, Y1:Y2])
                #         # cv2.imshow("CellImage", img[X1:X2, Y1:Y2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
                #     # if j == int(len(vertexs[i]) - int(1)):
                #     #     continue
            # if i == int(len(vertexs) - int(1)):
            #     break
        # print(rects)
        # # 依次顯示所有截取出的單元格（Cell）圖片（Image）;
        # for vertical_line_cellImages in cellImages:
        #     for cellImage in vertical_line_cellImages:
        #         cv2.imshow("CellImage", cellImage)  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;

        # horizontal_lines = HorizontalLineDetect(img)  # HorizontalLineDetect(img) 爲自定義函數，識別出圖片（Image）中的橫向分隔缐段座標列表;
        # vertical_lines = VerticalLineDetect(img)  # VerticalLineDetect(img) 爲自定義函數，識別出圖片（Image）中的縱向分隔竪缐段座標列表;

        # for i in range(0, len(vertical_lines) - 1, 2):
        #     for j in range(len(horizontal_lines) - 1):
        #         rects.append((vertical_lines[i][0], horizontal_lines[j][1], vertical_lines[i + 1][0], horizontal_lines[j + 1][1]))
        #         # print((vertical_lines[i][0], horizontal_lines[j][1], vertical_lines[i + 1][0], horizontal_lines[j + 1][1]))
        #         # cellImages.append(img[int(int(vertexs[i][j][1]) + Cell_Top_embedded):int(int(vertexs[int(i + int(1))][int(j + int(1))][1]) - Cell_Bottom_embedded), int(int(vertexs[i][j][0]) + Cell_Left_embedded):int(int(vertexs[int(i + int(1))][int(j + int(1))][0]) - Cell_Right_embedded)])
        #         # cv2.imshow("CellImage", img[int(int(vertexs[i][j][1]) + Cell_Top_embedded):int(int(vertexs[int(i + int(1))][int(j + int(1))][1]) - Cell_Bottom_embedded), int(int(vertexs[i][j][0]) + Cell_Left_embedded):int(int(vertexs[int(i + int(1))][int(j + int(1))][0]) - Cell_Right_embedded)])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
        #         # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
        #         X1 = int(int(vertexs[i][j][1]) + Cell_Top_embedded)
        #         Y1 = int(int(vertexs[i][j][0]) + Cell_Left_embedded)
        #         X2 = int(int(vertexs[int(i + int(1))][int(j + int(1))][1]) - Cell_Bottom_embedded)
        #         Y2 = int(int(vertexs[int(i + int(1))][int(j + int(1))][0]) - Cell_Right_embedded)
        #         vertical_line_cellImages.append(img[X1:X2, Y1:Y2])
        #         # cv2.imshow("CellImage", img[X1:X2, Y1:Y2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
        # # print(rects)

        # # 依次顯示所有截取出的單元格（Cell）圖片（Image）;
        # for i in range(0, len(cellImages), 1):
        #     for j in range(0, len(cellImages[i]), 1):
        #         cv2.imshow("CellImage", cellImages[i][j])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;

        return rects, cellImages

    # 識別測量尺（Measureing Rule）圖片（Image）中的橫向缐段;
    # 使用第三方庫「OpenCV」中的概率霍夫變換「Probabilistic Hough Transform」演算法進行直缐檢測，來識別圖片（Image）測量尺（Measureing Rule）中的橫向缐段;
    def lineMeasuring_HorizontalLineDetect(
        self,
        img,
        Canny_threshold1,  # cv2.Canny()：第一次閾值；
        Canny_threshold2,  # cv2.Canny()：第二次閾值；
        Canny_apertureSize,  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        Canny_L2gradient,  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        HoughLinesP_rho,  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        HoughLinesP_theta,  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        HoughLinesP_threshold,  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        HoughLinesP_minLineLength,  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        HoughLinesP_maxLineGap  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
    ):
        # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;

        # edges = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])
        # 其中參數：
        # image：待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）；
        # threshold1：第一次閾值；
        # threshold2：第二次閾值；
        # apertureSize：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        # L2gradient：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        # 函數返回值是一個輸出圖像，與輸入圖像大小及類型相同。
        # 函數「cv2.canny()」的實現原理主要基於以下幾個步驟：
        # Step 1：圖像灰度化。首先將輸入圖像轉換爲單通道的灰度圖像，可以通過函數「cv2.cvtColor」函數來完成。
        # Step 2：邊緣強度梯度計算。使用索伯爾運算元（Sobel）（算子）計算每個圖元（pixel）（像素）點在水平和垂直方向上的梯度值，並通過勾股定理（Pythagorean theorem）計算梯度幅值和方向。
        # Step 3：非極大值抑制。爲了減少邊緣（輪廓）圖元（pixel）（像素）數量，需要對梯度圖像中的強度值進行非極大值抑制，即只保留局部最大值點。
        # Step 4：滯後閾值處理。根據設定的閾值大小，將梯度幅值大於閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）。接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點也標記爲邊緣（輪廓）點。
        # Step 5：輸出邊緣（輪廓）圖像。最後將所有被標記爲邊緣（輪廓）的圖元（pixel）（像素）點輸出爲邊緣（輪廓）圖像。

        # 使用第三方庫「OpenCV」中的函數「cv2.Canny()」做圖形邊緣（輪廓）檢測，並將邊緣（輪廓）標記為白色圖元（pixel）（像素），黑色圖元（pixel）（像素）則表示非邊緣（輪廓）;
        edges = cv2.Canny(
            grayImage,  # 待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）;
            Canny_threshold1,  # 30,  # 第一次閾值，將梯度幅值大於第一次閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）;
            Canny_threshold2,  # 240,  # 第二次閾值，接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點，梯度幅值大於第二次閾值的，也標記爲邊緣（輪廓）點;
            apertureSize = Canny_apertureSize,  # 3,  # 用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3;
            L2gradient = Canny_L2gradient  # False  # 計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法;
        )

        # 第三方庫「OpenCV」中，有兩種算法檢測直缐或缐段，即「cv2.HoughLines()」標準霍夫缐變換「Hough Transform」和「cv2.HoughLinesP()」概率霍夫缐變換「Probabilistic Hough Transform」;
        # 標準霍夫缐變換「Hough Transform」函數「cv2.HoughLines()」返回值爲直綫的方程，即檢測結果爲「直綫」;
        # lines = cv2.HoughLines(image, rho, theta, threshold)
        # 概率霍夫缐變換「Probabilistic Hough Transform」函數「cv2.HoughLinesP()」返回值爲缐段起點與終點的座標值列表，即檢測結果爲「缐段」;
        # lines = cv2.HoughLinesP(image, rho, theta, threshold, minLineLength=None, maxLineGap=None)
        # 其中參數：
        # image：待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測；
        # rho：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        # theta：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        # threshold：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        # minLineLength：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        # maxLineGap：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        # 函數返回值是一個三維陣列，其中每個元素表示一條直線，格式爲列表：(x1, y1, x2, y2），表示直線的兩個端點座標。

        # 使用第三方庫「OpenCV」中的函數「cv2.HoughLinesP()」概率霍夫變換「Probabilistic Hough Transform」演算法識別圖片（Image）表格（Table）中的橫向分隔缐段;
        # minLineLength = 500  # 要求識別的缐段最小長度值（單位：圖元 pixel 也稱像素），比這個長度值小的缐段將會被忽略，自定義設定爲：500 個圖元;
        # maxLineGap = 30  # 要求識別的線段之間的最大間隔上限值（單位：圖元 pixel 也稱像素），小於這個間隔上限值的缐段將被連接爲一條直綫，自定義設定爲：30 個圖元;
        lines = cv2.HoughLinesP(
            edges,  # 待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測;
            HoughLinesP_rho,  # 1,  # 距離解析度（分辨率），單位爲：圖元（pixel）（像素）;
            HoughLinesP_theta,  # np.pi/180,  # 角度解析度（分辨率），單位爲：弧度;
            HoughLinesP_threshold,  # 100,  # 閾值參數，只有累加器中的值高於閾值才會被認為是一條直線;
            minLineLength = HoughLinesP_minLineLength,  # 要求識別的缐段最小長度值（單位：圖元 pixel 也稱像素），比這個長度值小的缐段將會被忽略，自定義設定爲：500 個圖元;
            maxLineGap = HoughLinesP_maxLineGap  # 要求識別的線段之間的最大間隔上限值（單位：圖元 pixel 也稱像素），小於這個間隔上限值的缐段將被連接爲一條直綫，自定義設定爲：30 個圖元;
        ).tolist()
        # lines.append([[13, 102, 756, 102]])  # 可以追加畫出一條自定義位置的橫向缐段;
        sorted_lines = sorted(lines, key=lambda x: x[0])

        horizontal_lines = []  # 存儲在圖像表格（Table）中檢測到的橫向分隔缐段座標的列表;
        for line in sorted_lines:
            for x1, y1, x2, y2 in line:
                if y1 == y2:
                    # print(line)
                    horizontal_lines.append([x1, y1, x2, y2])  # 存儲在圖像表格（Table）中檢測到的橫向分隔缐段座標;
                    # cv2.line(self.image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 在源圖像上繪製識別出的表格（Table）橫向分隔缐段;
        # # 在源圖像上繪製所有識別出的表格（Table）橫向分隔缐段;
        # for line in horizontal_lines:
        #     for x1, y1, x2, y2 in line:
        #         if y1 == y2:
        #             # print(line)
        #             cv2.line(self.image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 在源圖像上繪製識別出的表格（Table）橫向分隔缐段;

        return horizontal_lines

    # 識別測量尺（Measureing Rule）圖片（Image）中的縱向分隔竪缐段;
    # 使用第三方庫「OpenCV」中的概率霍夫變換「Probabilistic Hough Transform」演算法進行直缐檢測，來識別圖片（Image）測量尺（Measureing Rule）中的縱向分隔竪缐段;
    def lineMeasuring_VerticalLineDetect(
        self,
        img,
        Canny_threshold1,  # cv2.Canny()：第一次閾值；
        Canny_threshold2,  # cv2.Canny()：第二次閾值；
        Canny_apertureSize,  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        Canny_L2gradient,  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        HoughLinesP_rho,  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        HoughLinesP_theta,  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        HoughLinesP_threshold,  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        HoughLinesP_minLineLength,  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        HoughLinesP_maxLineGap  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
    ):
        # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
        # binaryImage = cv2.threshold(grayImage, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 過濾轉化爲二值化（非黑即白）的圖片;
        # binaryImage = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY_INV)  # 過濾轉化爲二值化（非黑即白）的圖片;
        # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
        # binaryImage = cv2.ximgproc.thinning(binaryImage, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;

        # edges = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])
        # 其中參數：
        # image：待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）；
        # threshold1：第一次閾值；
        # threshold2：第二次閾值；
        # apertureSize：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        # L2gradient：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        # 函數返回值是一個輸出圖像，與輸入圖像大小及類型相同。
        # 函數「cv2.canny()」的實現原理主要基於以下幾個步驟：
        # Step 1：圖像灰度化。首先將輸入圖像轉換爲單通道的灰度圖像，可以通過函數「cv2.cvtColor」函數來完成。
        # Step 2：邊緣強度梯度計算。使用索伯爾運算元（Sobel）（算子）計算每個圖元（pixel）（像素）點在水平和垂直方向上的梯度值，並通過勾股定理（Pythagorean theorem）計算梯度幅值和方向。
        # Step 3：非極大值抑制。爲了減少邊緣（輪廓）圖元（pixel）（像素）數量，需要對梯度圖像中的強度值進行非極大值抑制，即只保留局部最大值點。
        # Step 4：滯後閾值處理。根據設定的閾值大小，將梯度幅值大於閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）。接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點也標記爲邊緣（輪廓）點。
        # Step 5：輸出邊緣（輪廓）圖像。最後將所有被標記爲邊緣（輪廓）的圖元（pixel）（像素）點輸出爲邊緣（輪廓）圖像。

        # 使用第三方庫「OpenCV」中的函數「cv2.Canny()」做圖形邊緣（輪廓）檢測，並將邊緣（輪廓）標記為白色圖元（pixel）（像素），黑色圖元（pixel）（像素）則表示非邊緣（輪廓）;
        edges = cv2.Canny(
            grayImage,  # 待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）;
            Canny_threshold1,  # 30,  # 第一次閾值，將梯度幅值大於第一次閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）;
            Canny_threshold2,  # 240,  # 第二次閾值，接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點，梯度幅值大於第二次閾值的，也標記爲邊緣（輪廓）點;
            apertureSize = Canny_apertureSize,  # 3,  # 用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3;
            L2gradient = Canny_L2gradient  # False  # 計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法;
        )

        # 第三方庫「OpenCV」中，有兩種算法檢測直缐或缐段，即「cv2.HoughLines()」標準霍夫缐變換「Hough Transform」和「cv2.HoughLinesP()」概率霍夫缐變換「Probabilistic Hough Transform」;
        # 標準霍夫缐變換「Hough Transform」函數「cv2.HoughLines()」返回值爲直綫的方程，即檢測結果爲「直綫」;
        # lines = cv2.HoughLines(image, rho, theta, threshold)
        # 概率霍夫缐變換「Probabilistic Hough Transform」函數「cv2.HoughLinesP()」返回值爲缐段起點與終點的座標值列表，即檢測結果爲「缐段」;
        # lines = cv2.HoughLinesP(image, rho, theta, threshold, minLineLength=None, maxLineGap=None)
        # 其中參數：
        # image：待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測；
        # rho：距離解析度（分辨率），單位爲：圖元（pixel）（像素）每英寸，通常情況下，將距離解析度設為 1 即可，即每英寸 1 個；
        # theta：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        # threshold：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        # minLineLength：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        # maxLineGap：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        # 函數返回值是一個三維陣列，其中每個元素表示一條直線，格式爲列表：(x1, y1, x2, y2），表示直線的兩個端點座標。

        # 使用第三方庫「OpenCV」中的函數「cv2.HoughLinesP()」概率霍夫變換「Probabilistic Hough Transform」演算法識別圖片（Image）表格（Table）中的縱向分隔竪缐段;
        # minLineLength = 10  # 要求識別的缐段最小長度值（單位：圖元 pixel 也稱像素），比這個長度值小的缐段將會被忽略，自定義設定爲：10 個圖元;
        # maxLineGap = 10  # 要求識別的線段之間的最大間隔上限值（單位：圖元 pixel 也稱像素），小於這個間隔上限值的缐段將被連接爲一條直綫，自定義設定爲：10 個圖元;
        lines = cv2.HoughLinesP(
            edges,  # 待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測;
            HoughLinesP_rho,  # 1,  # 距離解析度（分辨率），單位爲：圖元（pixel）（像素）;
            HoughLinesP_theta,  # np.pi/180,  # 角度解析度（分辨率），單位爲：弧度;
            HoughLinesP_threshold,  # 100,  # 閾值參數，只有累加器中的值高於閾值才會被認為是一條直線;
            minLineLength = HoughLinesP_minLineLength,  # 要求識別的缐段最小長度值（單位：圖元 pixel 也稱像素），比這個長度值小的缐段將會被忽略，自定義設定爲：500 個圖元;
            maxLineGap = HoughLinesP_maxLineGap  # 要求識別的線段之間的最大間隔上限值（單位：圖元 pixel 也稱像素），小於這個間隔上限值的缐段將被連接爲一條直綫，自定義設定爲：30 個圖元;
        ).tolist()
        # lines.append([[13, 937, 13, 102]])  # 可以追加畫出一條自定義位置的縱向竪缐段;
        sorted_lines = sorted(lines, key=lambda x: x[0])

        vertical_lines = []  # 存儲在圖像表格（Table）中檢測到的縱向分隔竪缐段座標的列表;
        for line in sorted_lines:
            for x1, y1, x2, y2 in line:
                if x1 == x2:
                    # print(line)
                    vertical_lines.append([x1, y1, x2, y2])  # 存儲在圖像表格（Table）中檢測到的縱向分隔竪缐段座標;
                    # cv2.line(self.image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 在源圖像上繪製識別出的表格（Table）縱向分隔竪缐段;
        # # 在源圖像上繪製所有識別出的表格（Table）縱向分隔缐段;
        # for line in vertical_lines:
        #     for x1, y1, x2, y2 in line:
        #         if x1 == x2:
        #             # print(line)
        #             cv2.line(self.image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 在源圖像上繪製識別出的表格（Table）縱向分隔缐段;

        return vertical_lines

    # 識別圖片（Image）測量尺（Measureing Rule）中「標識點」，也就是上述識別後的橫縱向缐條的交點;
    def lineMeasuring_VertexDetect(
        self,
        horizontal_lines,
        vertical_lines,
        img,
        img_height,
        img_width
    ):
        # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        # grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;

        vertexs = []  # 存儲圖片（Image）量尺（Measuring Ruler）缐段（Line segment）中識別出的刻度「標識點」座標的二維列表（行列式）（縱向 → 橫向）;
        vertexs_all = []  # 存儲圖片（Image）量尺（Measuring Ruler）缐段（Line segment）中識別出的橫、竪線條的理論上所有的焦點座標的二維列表（行列式）（縱向 → 橫向）;

        # 量尺（Measuring Ruler）缐段（Line segment）圖片（Image）的左端點（起點）座標值;
        X_left_endpoint = horizontal_lines[0][0]
        Y_left_endpoint = horizontal_lines[0][1]
        # vertexs.append([(horizontal_lines[0][0], horizontal_lines[0][1])])
        vertexs.append((X_left_endpoint, Y_left_endpoint))
        # print(vertexs)

        for v_line in vertical_lines:

            for h_line in horizontal_lines:

                X_intersection = None
                Y_intersection = None

                # 兩點式直缐方程：(y-Y1)/(Y2-Y1) = (x-X1)/(X2-X1)  (X1 ≠ X2, Y1 ≠ Y2);
                # Slope = (Y2-Y1)/(X2-X1)
                # Intercept = Y1 - X1·(Y2-Y1)/(X2-X1) = (X2·Y1-X1·Y2)/(X2-X1)
                # 一般式直缐方程：A·x + B·y + C = 0 （A ≠ 0, B ≠ 0）;
                # Slope = -A/B
                # Intercept = -C/B
                # A = C·(Slope/Intercept) = C·(Y2-Y1)/(X2·Y1-X1·Y2)
                # B = -C/Intercept = -C·(X2-X1)/(X2·Y1-X1·Y2)
                # C = any one (for example: C = 1)

                # # 聯立兩條直缐方程，求解兩條直缐交點的橫座標（X 軸）值，兩點式直缐方程爲：(x - X1) / (X2 - X1) = (y - Y1) / (Y2 - Y1)  (X1 ≠ X2, Y1 ≠ Y2);
                # X_intersection = (v_line[1] - h_line[1] + ((h_line[3] - h_line[1]) * h_line[0] / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) * v_line[0] / (v_line[2] - v_line[0]))) / (((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0])))  # 兩直缐交點的橫座標（X 軸）值;

                # # 聯立兩條直缐方程，求解兩條直缐交點的縱座標（Y 軸）值，兩點式直缐方程爲：(x - X1) / (X2 - X1) = (y - Y1) / (Y2 - Y1)  (X1 ≠ X2, Y1 ≠ Y2);
                # Y_intersection = ((((v_line[1] - h_line[1] + ((h_line[3] - h_line[1]) * h_line[0] / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) * v_line[0] / (v_line[2] - v_line[0]))) / (((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0])))) - v_line[0]) * (v_line[3] - v_line[1]) / (v_line[2] - v_line[0])) + v_line[1]  # 兩直缐交點的縱座標（Y 軸）值;

                # 特殊式，當兩條直綫互相垂直，且與橫縱座標平行時，即當：一條直缐的：X2 = X1（即：v_line[2] == v_line[0]）且另一條直缐的：Y2 = Y1（即：h_line[3] == h_line[1]）時，即一條直缐方程爲：x = a 且另一條直缐方程爲：y = b 時，交點座標即爲：(a, b) ;

                # 當傳入參數：horizontal_lines 爲橫向水平缐，vertical_lines 爲縱向垂直缐時：
                if h_line[0] != h_line[2] and h_line[1] == h_line[3] and v_line[0] == v_line[2] and v_line[1] != v_line[3]:
                    X_intersection = v_line[0]
                    Y_intersection = h_line[1]
                if h_line[0] != h_line[2] and h_line[1] == h_line[3] and v_line[0] != v_line[2] and v_line[1] != v_line[3]:
                    X_intersection = int(round((h_line[1] * (v_line[2] - v_line[0]) - v_line[2] * v_line[1] + v_line[0] * v_line[3]) / (v_line[3] - v_line[1]), 0))  # x = (y - Intercept)/Slope = (y·(X2-X1) - X2·Y1 + X1·Y2)/(Y2-Y1)
                    # X_intersection = (h_line[1] * (v_line[2] - v_line[0]) - v_line[2] * v_line[1] + v_line[0] * v_line[3]) / (v_line[3] - v_line[1])  # x = (y - Intercept)/Slope = (y·(X2-X1) - X2·Y1 + X1·Y2)/(Y2-Y1)
                    Y_intersection = h_line[1]
                if h_line[0] != h_line[2] and h_line[1] != h_line[3] and v_line[0] == v_line[2] and v_line[1] != v_line[3]:
                    X_intersection = v_line[0]
                    # Y_intersection = (v_line[0] * (h_line[3] - h_line[1]) + h_line[2] * h_line[1] - h_line[0] * h_line[3]) / (h_line[2] - h_line[0])  # y = x·Slope + Intercept = (x·(Y2-Y1) + X2·Y1 - X1·Y2)/(X2-X1)
                    Y_intersection = int(round((v_line[0] * (h_line[3] - h_line[1]) + h_line[2] * h_line[1] - h_line[0] * h_line[3]) / (h_line[2] - h_line[0]), 0))  # y = x·Slope + Intercept = (x·(Y2-Y1) + X2·Y1 - X1·Y2)/(X2-X1)

                # 當傳入參數：horizontal_lines 爲縱向垂直缐，vertical_lines 爲橫向水平缐時：
                if h_line[0] == h_line[2] and h_line[1] != h_line[3] and v_line[0] != v_line[2] and v_line[1] == v_line[3]:
                    X_intersection = h_line[0]
                    Y_intersection = v_line[1]
                if h_line[0] == h_line[2] and h_line[1] != h_line[3] and v_line[0] != v_line[2] and v_line[1] != v_line[3]:
                    X_intersection = h_line[0]
                    # Y_intersection = (h_line[0] * (v_line[3] - v_line[1]) + v_line[2] * v_line[1] - v_line[0] * v_line[3]) / (v_line[2] - v_line[0])  # y = x·Slope + Intercept = (x·(Y2-Y1) + X2·Y1 - X1·Y2)/(X2-X1)
                    Y_intersection = int(round((h_line[0] * (v_line[3] - v_line[1]) + v_line[2] * v_line[1] - v_line[0] * v_line[3]) / (v_line[2] - v_line[0]), 0))  # y = x·Slope + Intercept = (x·(Y2-Y1) + X2·Y1 - X1·Y2)/(X2-X1)
                if h_line[0] != h_line[2] and h_line[1] != h_line[3] and v_line[0] != v_line[2] and v_line[1] == v_line[3]:
                    X_intersection = int(round((v_line[1] * (h_line[2] - h_line[0]) - h_line[2] * h_line[1] + h_line[0] * h_line[3]) / (h_line[3] - h_line[1]), 0))  # x = (y - Intercept)/Slope = (y·(X2-X1) - X2·Y1 + X1·Y2)/(Y2-Y1)
                    # X_intersection = (v_line[1] * (h_line[2] - h_line[0]) - h_line[2] * h_line[1] + h_line[0] * h_line[3]) / (h_line[3] - h_line[1])  # x = (y - Intercept)/Slope = (y·(X2-X1) - X2·Y1 + X1·Y2)/(Y2-Y1)
                    Y_intersection = v_line[1]

                # 聯立兩條直缐方程，求解兩條直缐交點的座標（橫 X 軸，縱 Y 軸）值，兩點式直缐方程爲：(x - X1) / (X2 - X1) = (y - Y1) / (Y2 - Y1)  (X1 ≠ X2, Y1 ≠ Y2);
                if h_line[0] != h_line[2] and h_line[1] != h_line[3] and v_line[0] != v_line[2] and v_line[1] != v_line[3]:
                    # 判斷兩條直綫不平行，即兩條直綫的斜率不相等，Slope = (Y2-Y1)/(X2-X1)
                    if ((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) != ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0])):
                        # X_intersection = (v_line[1] - h_line[1] + ((h_line[3] - h_line[1]) * h_line[0] / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) * v_line[0] / (v_line[2] - v_line[0]))) / (((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0])))  # 兩直缐交點的橫座標（X 軸）值;
                        X_intersection = int(round((v_line[1] - h_line[1] + ((h_line[3] - h_line[1]) * h_line[0] / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) * v_line[0] / (v_line[2] - v_line[0]))) / (((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0]))), 0))  # 兩直缐交點的橫座標（X 軸）值;
                        # Y_intersection = ((((v_line[1] - h_line[1] + ((h_line[3] - h_line[1]) * h_line[0] / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) * v_line[0] / (v_line[2] - v_line[0]))) / (((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0])))) - v_line[0]) * (v_line[3] - v_line[1]) / (v_line[2] - v_line[0])) + v_line[1]  # 兩直缐交點的縱座標（Y 軸）值;
                        Y_intersection = int(round(((((v_line[1] - h_line[1] + ((h_line[3] - h_line[1]) * h_line[0] / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) * v_line[0] / (v_line[2] - v_line[0]))) / (((h_line[3] - h_line[1]) / (h_line[2] - h_line[0])) - ((v_line[3] - v_line[1]) / (v_line[2] - v_line[0])))) - v_line[0]) * (v_line[3] - v_line[1]) / (v_line[2] - v_line[0])) + v_line[1], 0))  # 兩直缐交點的縱座標（Y 軸）值;

                if (not (X_intersection is None)) and (not (Y_intersection is None)):

                    # print(X_intersection, Y_intersection)
                    vertexs_all.append((X_intersection, Y_intersection))
                    vertexs.append((X_intersection, Y_intersection))

                    # # 判斷交點是否在圖片範圍内;
                    # if int(X_intersection) >= int(0) and int(Y_intersection) >= int(0) and int(X_intersection) <= int(img_width) and int(Y_intersection) <= int(img_height):
                    #     # print('Intersection position: (' + str(X_intersection) + ', ' + str(Y_intersection) + ')')
                    #     # cv2.circle(self.image, (X_intersection, Y_intersection), 1, (255, 0, 0), 2)  # # 在源圖像上繪製識別出的圖片（Image）表格（Table）中單元格（Cell）的四個角的「頂點」;
                    #     # 判斷交點是否在缐段：horizontal_lines 上;
                    #     if int(X_intersection) >= int(h_line[0]) and int(X_intersection) <= int(h_line[2]) and int(Y_intersection) >= int(h_line[1]) and int(Y_intersection) <= int(h_line[3]):
                    #         # 判斷交點是否在缐段：vertical_lines 上;
                    #         if int(X_intersection) >= int(v_line[2]) and int(X_intersection) <= int(v_line[0]) and int(Y_intersection) >= int(v_line[3]) and int(Y_intersection) <= int(v_line[1]):
                    #             # print('Intersection position: (' + str(X_intersection) + ', ' + str(Y_intersection) + ')')
                    #             vertexs.append((X_intersection, Y_intersection))
                    #             # cv2.circle(self.image, (X_intersection, Y_intersection), 1, (255, 0, 0), 2)  # # 在源圖像上繪製識別出的圖片（Image）表格（Table）中單元格（Cell）的四個角的「頂點」;

        # print(vertexs_all)
        # print(vertexs)

        # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        # # 獲取圖像的高度和寬度：
        # img_height, img_width = img.shape
        # self.img_height, self.img_width, img_dimension = img.shape
        # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;
        # # 遍歷每個像素：
        # for i in range(img_height):
        #     for j in range(img_width):
        #         pixel_value = img[i, j]  # 在這個示例中：img[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
        #         print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))

        # 量尺（Measuring Ruler）缐段（Line segment）圖片（Image）的右端點（終點）座標值;
        X_right_endpoint = horizontal_lines[0][2]
        Y_right_endpoint = horizontal_lines[0][3]
        # vertexs.append([(horizontal_lines[0][2], horizontal_lines[0][3])])
        vertexs.append((X_right_endpoint, Y_right_endpoint))
        # print(vertexs)

        # # 在源圖像上繪製所有識別出的圖片（Image）表格（Table）中單元格（Cell）的四個角的「頂點」;
        # for point in vertexs:
        #     cv2.circle(self.image, point, 1, (255, 0, 0), 2)

        return vertexs, vertexs_all

    # 然後，再把這些識別出測量尺（Measureing Rule）中「標識點」的區域截取出來;
    # 截取圖片（Image）測量尺（Measureing Rule）中「標識點」區域;
    def lineMeasuring_ScaleDetect(
        self,
        img,
        horizontal_lines,
        vertical_lines,
        vertexs,
        Cell_Top_extension,  # int(-45)  # 截取圖片單元區域的上邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        Cell_Left_extension,  # int(-90)  # 截取圖片單元區域的左邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        Cell_Bottom_extension,  # int(0)  # 截取圖片單元區域的下邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        Cell_Right_extension,  # int(90)  # 截取圖片單元區域的右邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        # HorizontalLineDetect,
        # VerticalLineDetect,
        # tableRecognition_VertexDetect
    ):
        # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        # grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;

        rects = []  # 存儲截取出的量尺（Measuring Ruler）圖片（Image）各個標識區域的座標值的列表;
        cellImages = []  # 存儲截取出的量尺（Measuring Ruler）圖片（Image）各個標識區本身的列表;

        # 識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的標識區域;
        Identification_rects = []  # 存儲識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的標識區域的座標值的列表;
        Identification_cellImages = []  # 存儲識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的標識區域本身的列表;

        for i in range(0, len(vertical_lines), 1):
            # 識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
            X1 = int(int(vertical_lines[i][2]) + Cell_Left_extension)  # int(-90)
            Y1 = int(int(vertical_lines[i][3]) + Cell_Top_extension)  # int(-45)
            X2 = int(int(vertical_lines[i][2]) + Cell_Right_extension)  # int(90)
            Y2 = int(int(vertical_lines[i][3]) + Cell_Bottom_extension)  # int(0)
            Identification_rects.append((X1, Y1, X2, Y2))
            # print((X1, Y1, X2, Y2))
            # Identification_cellImages.append(img[Y1:Y2, X1:X2])
            # cv2.imshow("CellImage", img[Y1:Y2, X1:X2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
            # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
            X1 = int(int(X1) + Cell_Left_embedded)
            Y1 = int(int(Y1) + Cell_Top_embedded)
            X2 = int(int(X2) - Cell_Right_embedded)
            Y2 = int(int(Y2) - Cell_Bottom_embedded)
            Identification_cellImages.append(img[Y1:Y2, X1:X2])
            # cv2.imshow("CellImage", img[Y1:Y2, X1:X2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
            # if i == 0:
            #     continue
            # if i == int(len(vertical_lines) - int(1)):
            #     break
            # if i > 0 and i < int(len(vertical_lines) - int(1)):
            #     X1 = int(int(vertical_lines[i][2]) + Cell_Left_extension)
            #     Y1 = int(int(vertical_lines[i][3]) + Cell_Top_extension)
            #     X2 = int(int(vertical_lines[i][2]) + Cell_Right_extension)
            #     Y2 = int(int(vertical_lines[i][3]) + Cell_Bottom_extension)
            #     Identification_rects.append((X1, Y1, X2, Y2))
            #     # print((X1, Y1, X2, Y2))
            #     # Identification_cellImages.append(img[Y1:Y2, X1:X2])
            #     # cv2.imshow("CellImage", img[Y1:Y2, X1:X2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
            #     # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
            #     X1 = int(int(X1) + Cell_Left_embedded)
            #     Y1 = int(int(Y1) + Cell_Top_embedded)
            #     X2 = int(int(X2) - Cell_Right_embedded)
            #     Y2 = int(int(Y2) - Cell_Bottom_embedded)
            #     Identification_cellImages.append(img[Y1:Y2, X1:X2])
            #     # cv2.imshow("CellImage", img[Y1:Y2, X1:X2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
        rects.append(Identification_rects)
        cellImages.append(Identification_cellImages)

        # 識別出的量尺（Measuring Ruler）缐段（Line segment）圖片（Image）的標識區域;
        measuring_ruler_rects = []  # 存儲識別出的量尺（Measuring Ruler）缐段（Line segment）圖片（Image）的標識區域的座標值的列表;
        measuring_ruler_cellImages = []  # 存儲識別出的量尺（Measuring Ruler）缐段（Line segment）圖片（Image）的標識區域本身的列表;

        # 識別出的量尺（Measuring Ruler）缐段（Line segment）圖片（Image）的左端點（起點）的左側的標識區域;
        X1 = int(int(horizontal_lines[0][0]) + int(-135))  # Cell_Left_extension)
        Y1 = int(int(horizontal_lines[0][1]) + int(-30))  # Cell_Top_extension)
        X2 = int(int(horizontal_lines[0][0]) + int(0))  # Cell_Right_extension)
        Y2 = int(int(horizontal_lines[0][1]) + int(30))  # Cell_Bottom_extension)
        measuring_ruler_rects.append((X1, Y1, X2, Y2))
        # print((X1, Y1, X2, Y2))
        # measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])
        # cv2.imshow("CellImage", img[Y1:Y2, X1:X2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
        # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
        X1 = int(int(X1) + Cell_Left_embedded)
        Y1 = int(int(Y1) + Cell_Top_embedded)
        X2 = int(int(X2) - Cell_Right_embedded)
        Y2 = int(int(Y2) - Cell_Bottom_embedded)
        measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])

        # 識別出的量尺（Measuring Ruler）缐段（Line segment）圖片（Image）的左端第 1 刻度點（起點）（-1）的下側的標識區域;
        X1 = int(int(horizontal_lines[0][0]) + int(-30))  # Cell_Left_extension)
        Y1 = int(int(horizontal_lines[0][1]) + int(0))  # Cell_Top_extension)
        X2 = int(int(horizontal_lines[0][0]) + int(30))  # Cell_Right_extension)
        Y2 = int(int(horizontal_lines[0][1]) + int(65))  # Cell_Bottom_extension)
        measuring_ruler_rects.append((X1, Y1, X2, Y2))
        # print((X1, Y1, X2, Y2))
        # measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])
        # cv2.imshow("CellImage", img[Y1:Y2, X1:X2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
        # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
        X1 = int(int(X1) + Cell_Left_embedded)
        Y1 = int(int(Y1) + Cell_Top_embedded)
        X2 = int(int(X2) - Cell_Right_embedded)
        Y2 = int(int(Y2) - Cell_Bottom_embedded)
        measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])

        # 識別出的量尺（Measuring Ruler）缐段（Line segment）圖片（Image）的左端第 2 刻度點（-0.5）的下側的標識區域;
        X1 = int(int(int(int(horizontal_lines[int(len(horizontal_lines) - int(1))][2]) + 3 * int(horizontal_lines[0][0])) / 4) + int(-30))  # Cell_Left_extension)
        Y1 = int(int(horizontal_lines[0][1]) + int(0))  # Cell_Top_extension)
        X2 = int(int(int(int(horizontal_lines[int(len(horizontal_lines) - int(1))][2]) + 3 * int(horizontal_lines[0][0])) / 4) + int(30))  # Cell_Right_extension)
        Y2 = int(int(horizontal_lines[0][1]) + int(65))  # Cell_Bottom_extension)
        measuring_ruler_rects.append((X1, Y1, X2, Y2))
        # print((X1, Y1, X2, Y2))
        # measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])
        # cv2.imshow("CellImage", img[Y1:Y2, X1:X2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
        # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
        X1 = int(int(X1) + Cell_Left_embedded)
        Y1 = int(int(Y1) + Cell_Top_embedded)
        X2 = int(int(X2) - Cell_Right_embedded)
        Y2 = int(int(Y2) - Cell_Bottom_embedded)
        measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])

        # 識別出的量尺（Measuring Ruler）缐段（Line segment）圖片（Image）的左端第 3 刻度點（0）的下側的標識區域;
        X1 = int(int(int(int(horizontal_lines[int(len(horizontal_lines) - int(1))][2]) + int(horizontal_lines[0][0])) / 2) + int(-30))  # Cell_Left_extension)
        Y1 = int(int(horizontal_lines[0][1]) + int(0))  # Cell_Top_extension)
        X2 = int(int(int(int(horizontal_lines[int(len(horizontal_lines) - int(1))][2]) + int(horizontal_lines[0][0])) / 2) + int(30))  # Cell_Right_extension)
        Y2 = int(int(horizontal_lines[0][1]) + int(65))  # Cell_Bottom_extension)
        measuring_ruler_rects.append((X1, Y1, X2, Y2))
        # print((X1, Y1, X2, Y2))
        # measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])
        # cv2.imshow("CellImage", img[Y1:Y2, X1:X2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
        # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
        X1 = int(int(X1) + Cell_Left_embedded)
        Y1 = int(int(Y1) + Cell_Top_embedded)
        X2 = int(int(X2) - Cell_Right_embedded)
        Y2 = int(int(Y2) - Cell_Bottom_embedded)
        measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])

        # 識別出的量尺（Measuring Ruler）缐段（Line segment）圖片（Image）的左端第 4 刻度點（0.5）的下側的標識區域;
        X1 = int(int(int(3 * int(horizontal_lines[int(len(horizontal_lines) - int(1))][2]) + int(horizontal_lines[0][0])) / 4) + int(-30))  # Cell_Left_extension)
        Y1 = int(int(horizontal_lines[0][1]) + int(0))  # Cell_Top_extension)
        X2 = int(int(int(3 * int(horizontal_lines[int(len(horizontal_lines) - int(1))][2]) + int(horizontal_lines[0][0])) / 4) + int(30))  # Cell_Right_extension)
        Y2 = int(int(horizontal_lines[0][1]) + int(65))  # Cell_Bottom_extension)
        measuring_ruler_rects.append((X1, Y1, X2, Y2))
        # print((X1, Y1, X2, Y2))
        # measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])
        # cv2.imshow("CellImage", img[Y1:Y2, X1:X2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
        # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
        X1 = int(int(X1) + Cell_Left_embedded)
        Y1 = int(int(Y1) + Cell_Top_embedded)
        X2 = int(int(X2) - Cell_Right_embedded)
        Y2 = int(int(Y2) - Cell_Bottom_embedded)
        measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])

        # 識別出的量尺（Measuring Ruler）缐段（Line segment）圖片（Image）的左端第 5 刻度點（終點）（1）的下側的標識區域;
        X1 = int(int(horizontal_lines[int(len(horizontal_lines) - int(1))][2]) + int(-30))  # Cell_Left_extension)
        Y1 = int(int(horizontal_lines[int(len(horizontal_lines) - int(1))][3]) + int(0))  # Cell_Top_extension)
        X2 = int(int(horizontal_lines[int(len(horizontal_lines) - int(1))][2]) + int(30))  # Cell_Right_extension)
        Y2 = int(int(horizontal_lines[int(len(horizontal_lines) - int(1))][3]) + int(65))  # Cell_Bottom_extension)
        measuring_ruler_rects.append((X1, Y1, X2, Y2))
        # print((X1, Y1, X2, Y2))
        # measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])
        # cv2.imshow("CellImage", img[Y1:Y2, X1:X2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
        # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
        X1 = int(int(X1) + Cell_Left_embedded)
        Y1 = int(int(Y1) + Cell_Top_embedded)
        X2 = int(int(X2) - Cell_Right_embedded)
        Y2 = int(int(Y2) - Cell_Bottom_embedded)
        measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])

        # 識別出的量尺（Measuring Ruler）缐段（Line segment）圖片（Image）的右端點（終點）的右側的標識區域;
        X1 = int(int(horizontal_lines[int(len(horizontal_lines) - int(1))][2]) + int(0))  # Cell_Left_extension)
        Y1 = int(int(horizontal_lines[int(len(horizontal_lines) - int(1))][3]) + int(-30))  # Cell_Top_extension)
        X2 = int(int(horizontal_lines[int(len(horizontal_lines) - int(1))][2]) + int(135))  # Cell_Right_extension)
        Y2 = int(int(horizontal_lines[int(len(horizontal_lines) - int(1))][3]) + int(30))  # Cell_Bottom_extension)
        measuring_ruler_rects.append((X1, Y1, X2, Y2))
        # print((X1, Y1, X2, Y2))
        # measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])
        # cv2.imshow("CellImage", img[Y1:Y2, X1:X2])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
        # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
        X1 = int(int(X1) + Cell_Left_embedded)
        Y1 = int(int(Y1) + Cell_Top_embedded)
        X2 = int(int(X2) - Cell_Right_embedded)
        Y2 = int(int(Y2) - Cell_Bottom_embedded)
        measuring_ruler_cellImages.append(img[Y1:Y2, X1:X2])

        rects.append(measuring_ruler_rects)
        cellImages.append(measuring_ruler_cellImages)

        # # 依次顯示所有截取出的單元格（Cell）圖片（Image）;
        # for i in range(0, len(cellImages), 1):
        #     for j in range(0, len(cellImages[i]), 1):
        #         cv2.imshow("CellImage", cellImages[i][j])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;

        return rects, cellImages

    # 使用 Google 公司出品的「Teressact-OCR」工具對單元格（Cell）圖片（Image）做文字（Character）識別;
    def OCRteressact(
        self,
        cellImage,
        # cellImages,
        # rects,
        tesseract_cmd,  # str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # str(pathlib.Path(os.path.abspath("..") + "/Tesseract-OCR/" + "/tesseract/"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
        tesseract_lang,  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
        tesseract_config,  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 6 --oem 2'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 6' 爲預設值，表示自動分段，'--psm 7' 表示强調圖像中爲單行文字，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 2' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '--ctessedit_char_whitelist=0123456789' 表示限制爲識別的字符只是阿拉伯數字：0 ~ 9;
        tesseract_timeout,  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
        tesseract_output_type,  # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
        # img,
        # HorizontalLineDetect,
        # VerticalLineDetect,
        # tableRecognition_VertexDetect,
        # tableRecognition_CellDetect
    ):
        # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
        if len(tesseract_cmd) > 0:
            # tesseract_cmd == r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # tesseract_cmd = r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;

        special_char_list = ' `~!@#$%^&*()-_=+[]{\}|;:‘’，。《》/？ˇ'  # 自定義的特殊字符列表，用於識別判定是否需要摘除特殊字符不保存;

        # img = cv2.imread("./testImage.jpg", 1)  # 读取硬盤中的图片，RGB 模式;
        # grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;

        # rects, cellImages = tableRecognition_CellDetect(img, vertexs)
        # # for i in range(0, len(rects), 1):
        # #     for j in range(0, len(rects[i]), 1):
        # #         cellImage = grayImage[rects[i][j][1]:rects[i][j][3], rects[i][j][0]:rects[i][j][2]]
        # #         cv2.imshow("CellImage", cellImage)  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
        # #         cellImages.append(grayImage[rects[i][j][1]:rects[i][j][3], rects[i][j][0]:rects[i][j][2]])

        # # 將 RGB 模式的單元格（Cell）圖片（Image），轉換爲灰度（Gray）模式的單元格（Cell）圖片（Image）;
        # grayCellImages = []  # 用於存儲轉換之後的，灰度（Gray）模式的單元格（Cell）圖片（Image）;
        # for i in range(0, len(cellImages), 1):
        #     Vertical_CellImages = []
        #     for j in range(0, len(cellImages[i]), 1):
        #         gray_Cell_Image = cv2.cvtColor(cellImages[i][j], cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
        #         # cv2.imshow("CellImage", gray_Cell_Image)  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
        #         Vertical_CellImages.append(gray_Cell_Image)
        #     grayCellImages.append(Vertical_CellImages)

        # characters_Tabel = []  # 用於存儲識別出的字符（Characters）數據的二維表格（Tabel）（行列式）;
        # # 依次識別圖片（Image）表格（Tabel）中的單元格（Cell）中的字符（Character），識別表格（Tabel）的二維行列式的依次順序爲：縱向 → 橫向;
        # for i in range(0, len(grayCellImages), 1):
        #     vertical_line_rects = []  # 縱向的一個豎排的識別出的字符（Characters）數據;
        #     for j in range(0, len(grayCellImages[i]), 1):
        #         # 使用第三方 pytesseract 模組的 pytesseract.image_to_string() 函數識別圖片（Image）中的字符（Character）;
        #         text = pytesseract.image_to_string(
        #             grayCellImages[i][j],
        #             lang = tesseract_lang,  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選多語言混合識別，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
        #             config = tesseract_config,  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        #             timeout = tesseract_timeout,  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
        #             output_type = tesseract_output_type  # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
        #         )
        #         # text = ''.join([char for char in text if char not in special_char_list])  # 識別判定是否爲特殊字符（是否在自定義設置的特殊字符列表中），如果爲特殊字符，則摘除不保存;
        #         # print(text, end = '-->')
        #         vertical_line_rects.append(text)
        #     characters_Tabel.append(vertical_line_rects)
        # return characters_Tabel


        # gray_Cell_Image = cv2.cvtColor(cellImage, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
        # cv2.imshow("CellImage", gray_Cell_Image)  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;

        text = ""  # 用於存儲識別出的單元格（Cell）圖片（Image）中的字符（Characters）數據;
        time_consuming = int(0)  # 用於存儲識別單元格（Cell）圖片（Image）中的字符（Characters）所消耗的時長（單位：毫秒 ms）;
        now_time = time.process_time()  # float，記錄當前 CPU 時間，單位：秒 s，用於計算進程所花費的 CPU 運算時長，注意不包括休眠時間;

        # 使用第三方 pytesseract 模組的 pytesseract.image_to_string() 函數識別圖片（Image）中的字符（Character）;
        text = pytesseract.image_to_string(
            cellImage,  # gray_Cell_Image,
            lang = tesseract_lang,  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選多語言混合識別，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
            config = tesseract_config,  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
            timeout = tesseract_timeout,  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
            output_type = tesseract_output_type  # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
        )
        # text = ''.join([char for char in text if char not in special_char_list])  # 識別判定是否爲特殊字符（是否在自定義設置的特殊字符列表中），如果爲特殊字符，則摘除不保存;
        # print(text, end = '-->')

        # 使用第三方 pytesseract 模組的 pytesseract.image_to_string() 函數説明：
        # pytesseract.image_to_string(image, lang = 'eng', config = '--psm 6', output_type = pytesseract.Output.STRING, timeout = 0)
        # 參數：image，表示待執行識別的圖像數據，通常使用 pillow 庫（PIL）讀取圖片文檔，再將其傳遞給此參數，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;
        # 參數：lang = 'eng'，表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選多語言混合識別，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
        # 參數：output_type = pytesseract.Output.STRING，預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
        # 參數：timeout = 0，表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
        # 參數：config = '--psm 3 --oem 3'，取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        # 使用 pytesseract 庫做 OCR，其中參數 config 可以的選項：
        # --tessdata-dir PATH：用戶自定義指定本地訓練完畢的數據集文檔（tessdata）的儲存路徑位置，使用 Tesseract 識別，需要使用訓練好的數據集，如果不指定該參數，則預設使用系統預設的數據集文檔目錄 Specify the location of tessdata path.
        # --user-words PATH：用戶自定義指定的詞庫（字典）文檔的存儲位置，用戶字典可以包含一些特定的詞匯，以提高對特定詞匯的識別準確性，用戶字典文件應爲純文本文檔，每行一個詞匯 Specify the location of user words file.
        # --user-patterns PATH：用戶自定義指定的特定格式文本的文檔的存儲位置，即每行使用「某種正則表達式」，例如，正在掃描具有相同格式數據的多張頁面，即可使用此參數，特定格式文本的文檔應爲純文本文檔，每行一個正則表達式模式 Specify the location of user patterns file.
        # --dpi VALUE：指定輸入影像的 DPI（Dots Per Inch）值，解析度（分辨率），即每英寸的包含點（Point）的數目 Specify DPI for input image.
        # --loglevel LEVEL：指定日誌記錄級別 Specify logging level. LEVEL can be ALL, TRACE, DEBUG, INFO, WARN, ERROR, FATAL or OFF.
        # -l LANG[+LANG]：指定用於 OCR 的語言，可以多選 Specify language(s) used for OCR.
        # -c VAR=VALUE：設定配寘變量的值，允許使用多個 -c 參數 Set value for config variables. Multiple -c arguments are allowed.
        # --psm NUM：指定圖片分割模式 Specify page segmentation mode.
        # --oem NUM：指定 OCR 引擎模式 Specify OCR Engine mode.
        # 圖片分割模式（PSM）
        # tesseract有13種圖片分割模式（page segmentation mode，psm）：
        # 0 -- 方向及語言檢測（Orientation and script detection，OSD) Orientation and script detection (OSD) only.
        # 1 -- 自動圖片分割 Automatic page segmentation with OSD.
        # 2 -- 自動圖片分割，沒有OSD和OCR Automatic page segmentation, but no OSD, or OCR.
        # 3 -- 預設值，完全的自動圖片分割，沒有OSD Fully automatic page segmentation, but no OSD. (Default)
        # 4 -- 假設有一列不同大小的文本 Assume a single column of text of variable sizes.
        # 5 -- 假設有一個垂直對齊的文字區塊 Assume a single uniform block of vertically aligned text.
        # 6 -- 假設有一個對齊的文字區塊 Assume a single uniform block of text.
        # 7 -- 圖片為單行文本 Treat the image as a single text line.
        # 8 -- 圖片為單詞 Treat the image as a single word.
        # 9 -- 圖片為圓形的單詞 Treat the image as a single word in a circle.
        # 10 -- 圖片為單個字元 Treat the image as a single character.
        # 11 -- 稀疏文本，查找盡可能多的文本，沒有特定的順序 Sparse text. Find as much text as possible in no particular order.
        # 12 -- OSD稀疏文本 Sparse text with OSD.
        # 13 -- 原始行，將圖像視為單個文本行 Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.
        # OCR引擎模式（OEM）
        # 有4種OCR引擎模式：
        # 0  --  Legacy engine only.
        # 1  --  Neural nets LSTM engine only.
        # 2  --  Legacy + LSTM engines.
        # 3  --  Default, based on what is available.
        # 另外，pytesseract 庫還有如下函數：
        # pytesseract.image_to_boxes(img, output_type=Output.STRING, lang='chi_sim')
        # 函數 pytesseract.image_to_boxes() 方法返回識別到的字元及字元邊框資訊；
        # pytesseract.image_to_data(img, output_type=Output.STRING, lang='chi_sim')
        # 函數 pytesseract.image_to_data() 返回單詞及單詞位置資訊
        # 如果默認使用ISO-8859-1（latin-1）編碼，而中文需要使用UTF-8編碼，因此需要設置指定字體及編碼格式；Windows中，字體存放路徑一般為C:\Windows\Fonts，若該路徑已經添加到了環境變數，則直接寫字體名稱就可以，例如 simsun.ttc 表示宋體漢字；如果不知道字體對應名稱可以進入註冊表查看：運行視窗或者命令列視窗輸入regedit打開註冊表，進入如下路徑：HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts ，可以查看對應字體檔案名稱。
        # pytesseract 還支持將圖片轉換為PDF、HOCR以及ALTO XML格式：
        # pdf = pytesseract.image_to_pdf_or_hocr('testimg2.png', extension='pdf')
        # with open('test.pdf', 'w+b') as f:
        #     f.write(pdf)
        # hocr = pytesseract.image_to_pdf_or_hocr('testimg2.png', extension='hocr')
        # xml = pytesseract.image_to_alto_xml('testimg2.png')

        # 計算識別單元格（Cell）圖片（Image）中的字符（Characters）所消耗的時長（單位：毫秒 ms），函數：math.ceil() 表示向上取整，例如：math.ceil(2.3) → 3;
        time_consuming = int(math.ceil((float(time.process_time()) - float(now_time)) * 1000)) # 計算識別單元格（Cell）圖片（Image）中的字符（Characters）所消耗的時長（單位：毫秒 ms）;

        return text, time_consuming

    def start(
        self,
        purpose,  # "tableRecognition", "lineMeasuring"
        imageUrl,  # 待識別檢測的圖片的 Web 請求網址 URL 字符串;
        imagePath,  # 待識別檢測的圖片的硬盤保存位置路徑字符串;
        imageData,  # cv2.imread(self.imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
        img_height,
        img_width,
        grayImageData,  # cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
        binaryImageData,  # cv2.threshold(grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
        # CV_parameter,
        HorizontalLineDetect,  # "Hough", "PixelDifference";
        VerticalLineDetect,  # "Hough", "PixelDifference";
        Canny_threshold1,  # cv2.Canny()：第一次閾值；
        Canny_threshold2,  # cv2.Canny()：第二次閾值；
        Canny_apertureSize,  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        Canny_L2gradient,  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        HoughLinesP_rho,  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        HoughLinesP_theta,  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        HoughLinesP_threshold,  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        HoughLinesP_minLineLength,  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        HoughLinesP_maxLineGap,  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        tableRecognition_HorizontalLineDetect_Canny_threshold1,
        tableRecognition_HorizontalLineDetect_Canny_threshold2,
        tableRecognition_HorizontalLineDetect_Canny_apertureSize,
        tableRecognition_HorizontalLineDetect_Canny_L2gradient,
        tableRecognition_HorizontalLineDetect_HoughLinesP_rho,
        tableRecognition_HorizontalLineDetect_HoughLinesP_theta,
        tableRecognition_HorizontalLineDetect_HoughLinesP_threshold,
        tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength,
        tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap,
        tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5)  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        tableRecognition_VerticalLineDetect_Canny_threshold1,
        tableRecognition_VerticalLineDetect_Canny_threshold2,
        tableRecognition_VerticalLineDetect_Canny_apertureSize,
        tableRecognition_VerticalLineDetect_Canny_L2gradient,
        tableRecognition_VerticalLineDetect_HoughLinesP_rho,
        tableRecognition_VerticalLineDetect_HoughLinesP_theta,
        tableRecognition_VerticalLineDetect_HoughLinesP_threshold,
        tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength,
        tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap,
        tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        tableRecognition_Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        tableRecognition_Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        tableRecognition_Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        tableRecognition_Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        lineMeasuring_HorizontalLineDetect_Canny_threshold1,
        lineMeasuring_HorizontalLineDetect_Canny_threshold2,
        lineMeasuring_HorizontalLineDetect_Canny_apertureSize,
        lineMeasuring_HorizontalLineDetect_Canny_L2gradient,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_rho,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_theta,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap,
        lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        lineMeasuring_VerticalLineDetect_Canny_threshold1,
        lineMeasuring_VerticalLineDetect_Canny_threshold2,
        lineMeasuring_VerticalLineDetect_Canny_apertureSize,
        lineMeasuring_VerticalLineDetect_Canny_L2gradient,
        lineMeasuring_VerticalLineDetect_HoughLinesP_rho,
        lineMeasuring_VerticalLineDetect_HoughLinesP_theta,
        lineMeasuring_VerticalLineDetect_HoughLinesP_threshold,
        lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength,
        lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap,
        lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        lineMeasuring_Cell_Top_extension,  # int(-45)  # 截取圖片單元區域的上邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Left_extension,  # int(-90)  # 截取圖片單元區域的左邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Bottom_extension,  # int(0)  # 截取圖片單元區域的下邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Right_extension,  # int(90)  # 截取圖片單元區域的右邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        lineMeasuring_Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        lineMeasuring_Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        lineMeasuring_Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        save_image,  # False, True;
        # OCR_parameter,
        OCRmethod,  # "teressact";
        tesseract_cmd,  # str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # str(pathlib.Path(os.path.abspath("..") + "/Tesseract-OCR/" + "/tesseract/"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
        tesseract_lang,  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
        tesseract_config,  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        tesseract_output_type,  # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
        tesseract_timeout,  # int(0)  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
        # do_Function,
        region_selection,
        orientation_correction,
        OverlappingFilter,
        getCurvesEnd,
        tableRecognition_HorizontalLineDetect_PixelDifference,
        tableRecognition_HorizontalLineDetect_Hough,
        tableRecognition_VerticalLineDetect_PixelDifference,
        tableRecognition_VerticalLineDetect_Hough,
        tableRecognition_VertexDetect,
        tableRecognition_CellDetect,
        lineMeasuring_HorizontalLineDetect,
        lineMeasuring_VerticalLineDetect,
        lineMeasuring_VertexDetect,
        lineMeasuring_ScaleDetect,
        OCRteressact,
    ):
        # OpenCV 提供函數「cv2.imread()」用於读取硬盤中的图片，預設以 RGB 彩色圖像模式讀取圖片檔：
        # ImageData = cv2.imread("./testImage.jpg", 1)
        # 也可以使用灰化（黑白）圖像模式讀取圖片檔：
        # grayImageData = cv2.imread("./testImage.jpg", cv2.COLOR_BGR2GRAY)

        # OpenCV 提供函數「cv2.cvtColor()」用於圖像顔色空間轉換，函數的基本語法爲：
        # cv2.cvtColor(img, code, dst, dstCn)
        # 參數説明：
        # 參數：img 表示輸入圖像，可以是 NumPy 數組或 OpenCV 中的 Mat 對象。
        # 參數：code 表示顔色空間轉換代碼，表示目標色彩空間。可以使用 OpenCV 中的 cv2.COLOR_* 常量來指定，例如：取「cv2.COLOR_BGR2GRAY」值表示將 RGB 彩色圖像轉換爲灰化（黑白）圖像，取「cv2.COLOR_GRAY2BGR」值表示將灰化（黑白）圖像轉換爲 RGB 彩色圖像，取「cv2.COLOR_RGB2RGBA」值表示對 RGB 圖像添加 alpha 通道（alpha 通道表示圖像透明屬性），取「cv2.COLOR_RGBA2RGB」值表示從 RGB 圖像通道内刪除 alpha 通道。
        # 參數：dst 爲可選參數，表示輸出圖像，可以是 NumPy 數組或 Mat 對象。如果未提供，將會創建一個新的圖像來保存轉換後的結果。
        # 參數：dstCn 爲可選參數，表示目標圖像的通道數，預設值爲：0，表示與輸入圖像通道數保持一致。

        # OpenCV 使用「cv2.threshold()」函數進行閾值化處理，該函數的語法格式爲：
        # retval, dst = cv2.threshold(img, thresh, maxval, type )
        # 式中：
        # 返回值：retval 代表返回的閾值。
        # 返回值：dst 代表閾值分割結果圖像，與原始圖像具有相同的大小和類型。
        # 參數：img 代表要進行閾值分割的圖像，可以是多通道的，8位或32位浮點型數值。
        # 參數：thresh 代表要設定的閾值，例如設定爲：127。
        # 參數：maxval 代表當type參數爲THRESH_BINARY或者THRESH_BINARY_INV類型時，需要設定的最大值，例如設定爲：255。
        # 參數：type 代表閾值分割的類型，具體類型值如表所示；可以取值如下：
        # 參數 type 取 cv2.THRESH_BINARY 值，表示二值化閾值處理。
        # 參數 type 取 cv2. THRESH_BINARY_INV 值，表示反二值化閾值處理。
        # 參數 type 取 cv2. THRESH_TRUNC 值，表示截斷閾值化處理。
        # 參數 type 取 cv2. THRESH_TOZERO_INV 值，表示超閾值零處理。
        # 參數 type 取 cv2. THRESH_TOZERO 值，表示低閾值零處理。
        # 代碼實例：
        # retval, rst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        # 注意，在使用函數「cv2.threshold()」進行閾值處理時，需要自定義傳入一個閾值，並以此閾值作爲圖像閾值處理的依據。通常情況下處理的圖像都是色彩均衡的，這時直接將閾值設爲「127」是比較合適的。但是，有時圖像灰度級的分佈是不均衡的，如果此時還將閾值設置爲「127」，那麼閾值處理的結果就是失敗的。
        # 使用「cv2.THRESH_OTSU」方法能夠根據當前圖像給出最佳的類間分割閾值。簡而言之，「cv2.THRESH_OTSU」方法會遍歷所有可能閾值，從而找到最佳的閾值。在OpenCV中，通過在函數「cv2.threshold()」中對參數「type」的類型多傳遞一個參數「cv2.THRESH_OTSU」，即可實現「cv2.THRESH_OTSU」方式的閾值分割。需要注意：在使用「cv2.THRESH_OTSU」方法時，要把閾值參數「thresh」設爲「0」。此時的函數「cv2.threshold()」會自動尋找最優閾值，並將該閾值返回。例如，下麵的語句讓函數「cv2.threshold()」採用「cv2.THRESH_OTSU」方法進行閾值分割：
        # t, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        # OpenCV提供了函數「cv2.adaptiveThreshold()」來實現自適應調整閾值處理，該函數的語法格式爲：
        # dst = cv.adaptiveThreshold(img, maxValue, adaptiveMethod, thresholdType, blockSize, C)
        # 式中：
        # 返回值：dst 代表自適應調整閾值處理結果。
        # 參數：img 代表要進行處理的原始圖像。需要注意的是，該圖像必須是8位元單通道的圖像。
        # 參數：maxValue 代表最大值。
        # 參數：adaptiveMethod 代表自我調整方法。
        # 參數：thresholdType 代表閾值處理方式，該值必須是「cv2.THRESH_BINARY」或者「cv2.THRESH_BINARY_INV」中的一個。
        # 參數：blockSize 代表塊大小。表示一個圖元在計算其閾值時所使用的鄰域尺寸，通常爲3、5、7等。
        # 參數：C 是常量。函數「cv2.adaptiveThreshold()」根據參數「adaptiveMethod」來確定自我調整閾值的計算方法，函數包含「cv2.ADAPTIVE_THRESH_MEAN_C」和「cv2.ADAPTIVE_THRESH_GAUSSIAN_C」兩種不同的方法。這兩種方法都是逐個圖元地計算自我調整閾值，自我調整閾值等於每個圖元由參數：blockSize 所指定鄰域的加權平均值減去常量：C。兩種不同的方法在計算鄰域的加權平均值時所採用的方式不同，其中：
        # 取值：cv2.ADAPTIVE_THRESH_MEAN_C 表示鄰域所有圖元點的權重值是一致的。
        # 取值：cv2.ADAPTIVE_THRESH_GAUSSIAN_C 表示與鄰域各個圖元點到中心點的距離有關，通過高斯方程得到各個點的權重值。
        # 代碼實例：
        # athdMEAN = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)
        # athdGAUS = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3)

        # OpenCV 提供「cv2imgproc.thinning()」函數，用於將二值圖像中的線條細化爲單圖元（像素）（pixel）寬度。
        # 注意，因爲函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中内置，而且因爲庫「opencv-python」與「opencv-contrib-python」之間互相衝突，二者不能同時存在，只能選其一安裝，所以，只能安裝「opencv-contrib-python」庫：
        # root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
        # 細化處理的基本原理是，通過對二值圖像中的像進行反覆迭代運算處理，將線條逐漸細化爲單圖元（像素）（pixel）寬度。細化處理的結果是一張黑白圖像，其中白色圖元表示細化後的線條，黑色圖元表示背景。函數的基本語法如下：
        # thinned = cv2imgproc.thinning(binaryImage, thinningType)
        # 其中，
        # 返回值：thinned 表示細化處理之後的圖像。
        # 參數：binaryImage 表示待細化處理的二值圖像。
        # 參數：thinningType 表示細化處理的類型。函數「cv2imgproc.thinning()」實現了兩種細化演算法，取值：「cv2.ximgproc.THINNING_ZHANGSUEN」表示爲並行演算法，取值：「cv2.ximgproc.THINNING_GUOHALL」表示爲串行演算法；串行算法和並行算法的共同點是進行第n次反覆運算時都需要第n-1次處理的結果，區別是串行算法還需要本次反覆運算已經處理過的圖元（像素）（pixel）點情況。也就是說：並行的反覆運算演算法，理論上可以在每一步多開n個執行緒增加處理速度，以空間換時間。
        # 代碼實例：
        # thinned = cv2.ximgproc.thinning([binaryImageData], cv2.ximgproc.THINNING_ZHANGSUEN)

        # 第三方庫「OpenCV」中，邊緣（輪廓）檢測「cv2.Canny()」;
        # edges = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])
        # 其中參數：
        # image：待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）；
        # threshold1：第一次閾值；
        # threshold2：第二次閾值；
        # apertureSize：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        # L2gradient：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        # 函數返回值是一個輸出圖像，與輸入圖像大小及類型相同。
        # 函數「cv2.canny()」的實現原理主要基於以下幾個步驟：
        # Step 1：圖像灰度化。首先將輸入圖像轉換爲單通道的灰度圖像，可以通過函數「cv2.cvtColor」函數來完成。
        # Step 2：邊緣強度梯度計算。使用索伯爾運算元（Sobel）（算子）計算每個圖元（pixel）（像素）點在水平和垂直方向上的梯度值，並通過勾股定理（Pythagorean theorem）計算梯度幅值和方向。
        # Step 3：非極大值抑制。爲了減少邊緣（輪廓）圖元（pixel）（像素）數量，需要對梯度圖像中的強度值進行非極大值抑制，即只保留局部最大值點。
        # Step 4：滯後閾值處理。根據設定的閾值大小，將梯度幅值大於閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）。接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點也標記爲邊緣（輪廓）點。
        # Step 5：輸出邊緣（輪廓）圖像。最後將所有被標記爲邊緣（輪廓）的圖元（pixel）（像素）點輸出爲邊緣（輪廓）圖像。

        # 第三方庫「OpenCV」中，有兩種算法檢測直缐或缐段，即「cv2.HoughLines()」標準霍夫缐變換「Hough Transform」和「cv2.HoughLinesP()」概率霍夫缐變換「Probabilistic Hough Transform」;
        # 標準霍夫缐變換「Hough Transform」函數「cv2.HoughLines()」返回值爲直綫的方程，即檢測結果爲「直綫」;
        # lines = cv2.HoughLines(image, rho, theta, threshold)
        # 概率霍夫缐變換「Probabilistic Hough Transform」函數「cv2.HoughLinesP()」返回值爲缐段起點與終點的座標值列表，即檢測結果爲「缐段」;
        # lines = cv2.HoughLinesP(image, rho, theta, threshold, minLineLength=None, maxLineGap=None)
        # 其中參數：
        # image：待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測；
        # rho：距離解析度（分辨率），單位爲：圖元（pixel）（像素）每英寸，通常情況下，將距離解析度設為 1 即可，即每英寸 1 個；
        # theta：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        # threshold：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        # minLineLength：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        # maxLineGap：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        # 函數返回值是一個三維陣列，其中每個元素表示一條直線，格式爲列表：(x1, y1, x2, y2），表示直線的兩個端點座標。

        # 第三方庫「OpenCV」中，查找圖片（Image）中的所有輪廓「cv2.findContours()」;
        # contours, hierarchy = cv2.findContours(binaryImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 查找圖片（Image）中的所有輪廓;

        result_tuple = None  # (Character_Data, OCR_time_consuming, OCR_parameter_optimization);

        # 如果參數中未傳入圖片數據，而傳入了圖片文檔的存儲路徑位置字符串，則從圖片文檔的存儲路徑位置讀取圖片數據;
        if len(grayImageData) == 0:
            if len(imageData) > 0:
                grayImageData = cv2.cvtColor(imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
            if len(imageData) == 0:
                if len(imagePath) > 0:
                    imageData = cv2.imread(imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
                    grayImageData = cv2.cvtColor(imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
                elif len(imageUrl) > 0:
                    response = urllib_request.urlopen(imageUrl)  # 使用 Python 語言的原生模組「urllib」中的「request」中的「urlopen()」函數向服務器請求下載圖片數據;
                    img_array = np.array(bytearray(response.read()), dtype = np.uint8)  # 把從服務器下載的圖片數據轉換爲二進位 8 位字節數組的形式;
                    imageData = cv2.imdecode(img_array, -1)  # 使用 Python 語言的第三方擴展模組「opencv」中的「cv2.imdecode()」函數解析二進位 8 位字節數組形式的图片數據，RGB 模式;
                    grayImageData = cv2.cvtColor(imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
                else:
                    print("Image data empty.")

        # 判斷灰化轉換（gray）後圖片數據是否爲空;
        if len(grayImageData) == 0:
            return result_tuple

        # # 圖像旋轉方位調整矯正 ORIENTATION CORRECTION/ADJUSTMENT;
        # grayImageData = orientation_correction(grayImageData)
        # imageData = orientation_correction(imageData)

        # 取值 purpose = "tableRecognition" 表示識別圖片（Image）表格（Tabel）單元格（Cell）中的字符（Character）;
        if purpose == "tableRecognition":

            # 識別圖片（Image）表格（Table）中的橫向分隔缐段;
            # HoughLinesP_rho = int(1)  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
            # HoughLinesP_theta = float(np.pi/180)  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
            # HoughLinesP_threshold = int(100)  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
            # HoughLinesP_minLineLength = int(150)  # int(200)  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
            # HoughLinesP_maxLineGap = int(15)  # int(15)  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
            horizontal_lines = []  # 存儲在圖像表格（Table）中檢測到的橫向分隔缐段座標的列表;
            if HorizontalLineDetect == "Hough":
                horizontal_lines = tableRecognition_HorizontalLineDetect_Hough(
                    grayImageData,
                    tableRecognition_HorizontalLineDetect_Canny_threshold1,  # cv2.Canny()：第一次閾值；
                    tableRecognition_HorizontalLineDetect_Canny_threshold2,  # cv2.Canny()：第二次閾值；
                    tableRecognition_HorizontalLineDetect_Canny_apertureSize,  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
                    tableRecognition_HorizontalLineDetect_Canny_L2gradient,  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
                    tableRecognition_HorizontalLineDetect_HoughLinesP_rho,  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
                    tableRecognition_HorizontalLineDetect_HoughLinesP_theta,  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
                    tableRecognition_HorizontalLineDetect_HoughLinesP_threshold,  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
                    tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength,  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
                    tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
                )
            elif HorizontalLineDetect == "PixelDifference":
                horizontal_lines = tableRecognition_HorizontalLineDetect_PixelDifference(grayImageData)
            else:
                print('HorizontalLineDetect method cannot be recognized, only allowe: "Hough" or "PixelDifference".')
                return result_tuple
            # print("Horizontal Lines:\n", horizontal_lines)

            # 判斷是否一條都沒有識別出橫向分隔缐段;
            if len(horizontal_lines) == 0:
                print('horizontal lines not detected.')
                return result_tuple

            # 刪除重複（圖片中的綫條比較寬，誤識別爲兩條較細的綫條）的橫向分隔缐段;
            horizontal_lines = OverlappingFilter(
                horizontal_lines,
                separationThresholdSlope = tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5)  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
                separationThresholdIntercept = tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept  # float(5)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
            )
            # print("Horizontal Lines:\n", horizontal_lines)

            # # 用於調試 #########################################################################
            # # 在源圖像上繪製識別出的表格（Table）橫向分隔缐段;
            # for line in horizontal_lines:
            #     x1 = line[0]
            #     y1 = line[1]
            #     x2 = line[2]
            #     y2 = line[3]
            #     # print(x1, y1, x2, y2)
            #     cv2.line(imageData, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 在源圖像上繪製識別出的表格（Table）橫向分隔缐段;
            #     # if y1 == y2:
            #     #     # print(line)
            #     #     cv2.line(imageData, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 在源圖像上繪製識別出的表格（Table）橫向分隔缐段;
            # # 顯示圖片;
            # cv2.namedWindow("Image")  # 創建圖片展示窗口;
            # cv2.imshow("Image", imageData)  # 顯示圖片 display the image and wait for a keypress
            # # key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;
            # # if key == 27:
            # #     break
            # # # 回車鍵（Enter）的 ASCII 碼爲：ord('\n') == 13
            # # # 空格鍵的 ASCII 碼爲：ord(' ')
            # # # Tab 鍵的 ASCII 碼爲：ord('\t')
            # # # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
            # # # 換行鍵的 ASCII 碼爲：ord('\r')
            # # # Esc 鍵的 ASCII 碼爲：ord('\x1b') == 27
            # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
            # # cv2.destroyAllWindows()  # 關閉所有窗口 closing all open windows
            # cv2.destroyWindow("Image")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;
            # # 用於調試 #########################################################################

            # 識別圖片（Image）表格（Table）中的縱向分隔竪缐段;
            # HoughLinesP_rho = int(1)  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
            # HoughLinesP_theta = float(np.pi/180)  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
            # HoughLinesP_threshold = int(100)  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
            # HoughLinesP_minLineLength = int(150)  # int(200)  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
            # HoughLinesP_maxLineGap = int(15)  # int(15)  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
            vertical_lines = []  # 存儲在圖像表格（Table）中檢測到的縱向分隔竪缐段座標的列表;
            if VerticalLineDetect == "Hough":
                vertical_lines = tableRecognition_VerticalLineDetect_Hough(
                    grayImageData,
                    tableRecognition_VerticalLineDetect_Canny_threshold1,  # cv2.Canny()：第一次閾值；
                    tableRecognition_VerticalLineDetect_Canny_threshold2,  # cv2.Canny()：第二次閾值；
                    tableRecognition_VerticalLineDetect_Canny_apertureSize,  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
                    tableRecognition_VerticalLineDetect_Canny_L2gradient,  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
                    tableRecognition_VerticalLineDetect_HoughLinesP_rho,  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
                    tableRecognition_VerticalLineDetect_HoughLinesP_theta,  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
                    tableRecognition_VerticalLineDetect_HoughLinesP_threshold,  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
                    tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength,  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
                    tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
                )
            elif VerticalLineDetect == "PixelDifference":
                vertical_lines = tableRecognition_VerticalLineDetect_PixelDifference(grayImageData)
            else:
                print('VerticalLineDetect method cannot be recognized, only allowe: "Hough" or "PixelDifference".')
                return result_tuple
            # print("Vertical Lines:\n", vertical_lines)

            # 判斷是否一條都沒有識別出縱向分隔竪缐段;
            if len(vertical_lines) == 0:
                print('vertical lines not detected.')
                return result_tuple

            # 刪除重複（圖片中的綫條比較寬，誤識別爲兩條較細的綫條）的縱向分隔缐段;
            vertical_lines = OverlappingFilter(
                vertical_lines,
                separationThresholdSlope = tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
                separationThresholdIntercept = tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
            )
            # print("Vertical Lines:\n", vertical_lines)

            # # 用於調試 #########################################################################
            # # 在源圖像上繪製識別出的表格（Table）縱向分隔缐段;
            # for line in vertical_lines:
            #     x1 = line[0]
            #     y1 = line[1]
            #     x2 = line[2]
            #     y2 = line[3]
            #     # print(x1, y1, x2, y2)
            #     cv2.line(imageData, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 在源圖像上繪製識別出的表格（Table）縱向分隔缐段;
            #     # if x1 == x2:
            #     #     # print(line)
            #     #     cv2.line(imageData, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 在源圖像上繪製識別出的表格（Table）縱向分隔缐段;
            # # 顯示圖片;
            # cv2.namedWindow("Image")  # 創建圖片展示窗口;
            # cv2.imshow("Image", imageData)  # 顯示圖片 display the image and wait for a keypress
            # # key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;
            # # if key == 27:
            # #     break
            # # # 回車鍵（Enter）的 ASCII 碼爲：ord('\n') == 13
            # # # 空格鍵的 ASCII 碼爲：ord(' ')
            # # # Tab 鍵的 ASCII 碼爲：ord('\t')
            # # # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
            # # # 換行鍵的 ASCII 碼爲：ord('\r')
            # # # Esc 鍵的 ASCII 碼爲：ord('\x1b') == 27
            # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
            # # cv2.destroyAllWindows()  # 關閉所有窗口 closing all open windows
            # cv2.destroyWindow("Image")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;
            # # 用於調試 #########################################################################

            # 識別圖片（Image）表格（Table）中單元格（Cell），在識別圖片（Image）表格（Table）中單元格（Cell）之前，先識別出每個單元格（Cell）的四個角的「頂點」，也就是上述識別後的橫縱向缐條的交點;
            vertexs = []  # 存儲圖片（Image）表格（Table）中識別出的單元格（Cell）的四個角的「頂點」座標的二維列表（行列式）（縱向 → 橫向）;
            vertexs, vertexs_all = tableRecognition_VertexDetect(horizontal_lines, vertical_lines, imageData, img_height, img_width)
            # print("Vertexs:\n", vertexs)

            # 判斷是否一個都沒有識別出：單元格（Cell）的四個角的「頂點」，也就是上述識別後的橫縱向缐條的交點;
            if len(vertexs) == 0:
                print('Vertexs of Cell in Table in Image, not detected.')
                return result_tuple

            # # 用於調試 #########################################################################
            # # 在源圖像上繪製識別出的圖片（Image）表格（Table）中單元格（Cell）的四個角的「頂點」;
            # for v_point in vertexs:
            #     for h_point in v_point:
            #         cv2.circle(imageData, h_point, 1, (255, 0, 0), 2)
            # # 顯示圖片;
            # cv2.namedWindow("Image")  # 創建圖片展示窗口;
            # cv2.imshow("Image", imageData)  # 顯示圖片 display the image and wait for a keypress
            # # key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;
            # # if key == 27:
            # #     break
            # # # 回車鍵（Enter）的 ASCII 碼爲：ord('\n') == 13
            # # # 空格鍵的 ASCII 碼爲：ord(' ')
            # # # Tab 鍵的 ASCII 碼爲：ord('\t')
            # # # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
            # # # 換行鍵的 ASCII 碼爲：ord('\r')
            # # # Esc 鍵的 ASCII 碼爲：ord('\x1b') == 27
            # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
            # # cv2.destroyAllWindows()  # 關閉所有窗口 closing all open windows
            # cv2.destroyWindow("Image")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;
            # # 用於調試 #########################################################################

            # 然後，再根據這些識別出的單元格（Cell）的四個角「頂點」，截取圖片（Image）表格（Table）中單元格（Cell）區域;
            rects = []  # 存儲截取出的單元格（Cell）座標的列表;
            cellImages = []  # 存儲截取出的單元格（Cell）圖片（Image）數據本身的列表;
            # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
            # tableRecognition_Cell_Top_embedded = int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
            # tableRecognition_Cell_Bottom_embedded = int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
            # tableRecognition_Cell_Left_embedded = int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
            # tableRecognition_Cell_Right_embedded = int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
            rects, cellImages = tableRecognition_CellDetect(
                imageData,
                vertexs,
                tableRecognition_Cell_Top_embedded,  # = int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
                tableRecognition_Cell_Bottom_embedded,  # = int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
                tableRecognition_Cell_Left_embedded,  # = int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
                tableRecognition_Cell_Right_embedded  # = int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
            )
            # print("Rects Cells:\n", rects)

            # 判斷是否一個都沒有識別出：圖片（Image）表格（Table）中單元格（Cell）區域的圖元（像素）數據;
            if len(cellImages) == 0:
                print('Pixel of Cell in Table in Image, not detected.')
                return result_tuple

            # 判斷是否一個都沒有識別出：圖片（Image）表格（Table）中單元格（Cell）區域的座標值;
            if len(rects) == 0:
                print('Coordinate of Cell in Table in Image, not detected.')
                return result_tuple

            # # 用於調試 #########################################################################
            # # 顯示圖片;
            # cv2.namedWindow("CellImage")  # 創建圖片展示窗口;
            # # 依次顯示所有截取出的單元格（Cell）圖片（Image）;
            # for vertical_line_rects in cellImages:
            #     for cellImage in vertical_line_rects:
            #         cv2.imshow("CellImage", cellImage)  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image） display the image and wait for a keypress;
            #         # key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;
            #         # if key == 27:
            #         #     break
            #         # # 回車鍵（Enter）的 ASCII 碼爲：ord('\n') == 13
            #         # # 空格鍵的 ASCII 碼爲：ord(' ')
            #         # # Tab 鍵的 ASCII 碼爲：ord('\t')
            #         # # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
            #         # # 換行鍵的 ASCII 碼爲：ord('\r')
            #         # # Esc 鍵的 ASCII 碼爲：ord('\x1b') == 27
            #         cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
            # # cv2.destroyAllWindows()  # 關閉所有窗口 closing all open windows
            # cv2.destroyWindow("CellImage")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;
            # # 用於調試 #########################################################################

            # # 用於調試 #########################################################################
            # # 在源圖上繪製所有截取出的單元格（Cell）圖片（Image）的對角頂點;
            # for i in range(0, len(rects), 1):
            #     for j in range(0, len(rects[i]), 1):
            #         # cellImage = imageData[int(int(rects[i][j][1]) + int(3)):int(int(rects[int(i + int(1))][int(j + int(1))][1]) - int(3)), int(int(rects[i][j][0]) + int(3)):int(int(rects[int(i + int(1))][int(j + int(1))][0]) - int(3))]
            #         # cellImages.append(imageData[int(int(rects[i][j][1]) + int(3)):int(int(rects[int(i + int(1))][int(j + int(1))][1]) - int(3)), int(int(rects[i][j][0]) + int(3)):int(int(rects[int(i + int(1))][int(j + int(1))][0]) - int(3))])
            #         # cv2.circle(imageData, (rects[i][j][0] + int(3), rects[i][j][1] + int(3)), 1, (255, 255, 0), 2)
            #         # cv2.circle(imageData, (rects[i][j][2] + int(3), rects[i][j][3] + int(3)), 1, (255, 255, 0), 2)
            #         # cv2.line(imageData, (rects[i][j][0], rects[i][j][1]), (rects[i][j][2], rects[i][j][3]), (255, 255, 0), 2)  # 在源圖像上繪製識別出的表格（Table）縱向分隔缐段;
            #         # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
            #         X1 = int(int(rects[i][j][1]) + tableRecognition_Cell_Top_embedded)  # 上邊框位置;
            #         Y1 = int(int(rects[i][j][0]) + tableRecognition_Cell_Left_embedded)  # 左邊框位置;
            #         X2 = int(int(rects[int(i + int(1))][int(j + int(1))][1]) - tableRecognition_Cell_Bottom_embedded)  # 下邊框位置;
            #         Y2 = int(int(rects[int(i + int(1))][int(j + int(1))][0]) - tableRecognition_Cell_Right_embedded)  # 右邊框位置;
            #         # cellImage = imageData[X1:X2, Y1:Y2]
            #         # cellImages.append(imageData[X1:X2, Y1:Y2])
            #         # cv2.circle(imageData, (Y1, X1), 1, (255, 0, 255), 2)
            #         # cv2.circle(imageData, (Y2, X2), 1, (0, 255, 255), 2)
            #         cv2.line(imageData, (Y1, X1), (Y2, X2), (0, 255, 255), 2)  # 在源圖像上繪製識別出的表格（Table）縱向分隔缐段;
            # # 顯示圖片;
            # cv2.namedWindow("Image")  # 創建圖片展示窗口;
            # cv2.imshow("Image", imageData)  # 在名稱爲 "Image" 的窗口中顯示圖片（Image） display the image and wait for a keypress;
            # # key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;
            # # if key == 27:
            # #     break
            # # # 回車鍵（Enter）的 ASCII 碼爲：ord('\n') == 13
            # # # 空格鍵的 ASCII 碼爲：ord(' ')
            # # # Tab 鍵的 ASCII 碼爲：ord('\t')
            # # # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
            # # # 換行鍵的 ASCII 碼爲：ord('\r')
            # # # Esc 鍵的 ASCII 碼爲：ord('\x1b') == 27
            # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
            # # cv2.destroyAllWindows()  # 關閉所有窗口 closing all open windows
            # cv2.destroyWindow("Image")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;
            # # 用於調試 #########################################################################

            # # 當源圖片爲彩色（RGB）圖片時：
            # # 將 RGB 模式的單元格（Cell）圖片（Image），轉換爲灰度（Gray）模式的單元格（Cell）圖片（Image）;
            # grayCellImages = []  # 用於存儲轉換之後的，灰度（Gray）模式的單元格（Cell）圖片（Image）;
            # for i in range(0, len(cellImages), 1):
            #     Vertical_CellImages = []
            #     for j in range(0, len(cellImages[i]), 1):
            #         # cv2.imshow("CellImage", cellImages[i][j])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）;
            #         gray_Cell_Image = cv2.cvtColor(cellImages[i][j], cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
            #         # cv2.imshow("CellImage", gray_Cell_Image)  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的單元格（Cell）圖片（Image）灰化（Gray）轉換之後的效果;
            #         Vertical_CellImages.append(gray_Cell_Image)
            #     grayCellImages.append(Vertical_CellImages)

            # 當源圖片爲黑白（灰化 Gray）圖片時：
            grayCellImages = cellImages  # 用於存儲轉換之後的，灰度（Gray）模式的單元格（Cell）圖片（Image）;

            characters_Tabel = []  # 用於存儲識別出的字符（Characters）數據的二維表格（Tabel）（行列式）;
            time_consuming_Tabel = []  # 用於存儲識別單元格（Cell）圖片（Image）中的字符（Characters）所消耗的時長（單位：毫秒 ms）的二維表格（Tabel）（行列式）;

            # 依次識別圖片（Image）表格（Tabel）中的單元格（Cell）中的字符（Character），識別表格（Tabel）的二維行列式的依次順序爲：縱向 → 橫向;
            for i in range(0, len(grayCellImages), 1):

                vertical_line_characters_Tabel = []  # 縱向的一個豎排的識別出的字符（Characters）數據;
                vertical_line_time_consuming_Tabel = []  # 縱向的一個豎排的識別單元格（Cell）圖片（Image）中的字符（Characters）所消耗的時長（單位：毫秒 ms）;

                for j in range(0, len(grayCellImages[i]), 1):

                    text = ""  # string，用於存儲識別出的單元格（Cell）圖片（Image）中的字符（Characters）數據;
                    time_consuming = int(0)  # int，用於存儲識別單元格（Cell）圖片（Image）中的字符（Characters）所消耗的時長（單位：毫秒 ms）;

                    # 使用 Google 公司出品的「Teressact-OCR」工具對單元格（Cell）圖片（Image）做文字（Character）識別;
                    if OCRmethod == "teressact":

                        text, time_consuming = OCRteressact(
                            grayCellImages[i][j],
                            # cellImages,
                            # rects,
                            tesseract_cmd,  # str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # str(pathlib.Path(os.path.abspath("..") + "/Tesseract-OCR/" + "/tesseract/"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
                            tesseract_lang,  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
                            tesseract_config,  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 6 --oem 2'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 6' 爲預設值，表示自動分段，'--psm 7' 表示强調圖像中爲單行文字，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 2' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '--ctessedit_char_whitelist=0123456789' 表示限制爲識別的字符只是阿拉伯數字：0 ~ 9;
                            tesseract_timeout,  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
                            tesseract_output_type,  # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
                            # grayImage,
                            # HorizontalLineDetect,
                            # VerticalLineDetect,
                            # tableRecognition_VertexDetect,
                            # tableRecognition_CellDetect
                        )

                    if len(text) > 0:
                        text = text.strip()  # 刪除字符串兩端的空格;

                    # print("{", str("(" + str(int(i) + int(1)) + "," + str(int(j) + int(1)) + ")"), ": time consuming", time_consuming, "millisecond } ", text)

                    vertical_line_characters_Tabel.append(text)
                    vertical_line_time_consuming_Tabel.append(time_consuming)

                characters_Tabel.append(vertical_line_characters_Tabel)
                time_consuming_Tabel.append(vertical_line_time_consuming_Tabel)

            result_tuple = (characters_Tabel, time_consuming_Tabel)

        # 取值 purpose = "lineMeasuring" 表示測量圖片（Image）缐段（Line segment）的長度（length），單位是：圖片（Image）缐段（Line segment）所占圖元（像素）（Pixel）點的數量（Number）;
        if purpose == "lineMeasuring":

            # 識別圖片（Image）量尺（Measuring Ruler）中的橫向缐段;
            # HoughLinesP_rho = int(1)  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
            # HoughLinesP_theta = float(np.pi/180)  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
            # HoughLinesP_threshold = int(100)  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
            # HoughLinesP_minLineLength = int(150)  # int(200)  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
            # HoughLinesP_maxLineGap = int(15)  # int(15)  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
            horizontal_lines = []  # 存儲在圖像表格（Table）中檢測到的橫向分隔缐段座標的列表;
            horizontal_lines = lineMeasuring_HorizontalLineDetect(
                imageData,
                lineMeasuring_HorizontalLineDetect_Canny_threshold1,  # cv2.Canny()：第一次閾值；
                lineMeasuring_HorizontalLineDetect_Canny_threshold2,  # cv2.Canny()：第二次閾值；
                lineMeasuring_HorizontalLineDetect_Canny_apertureSize,  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
                lineMeasuring_HorizontalLineDetect_Canny_L2gradient,  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
                lineMeasuring_HorizontalLineDetect_HoughLinesP_rho,  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
                lineMeasuring_HorizontalLineDetect_HoughLinesP_theta,  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
                lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold,  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
                lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength,  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
                lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
            )
            # print("Horizontal Lines:\n", horizontal_lines)

            # 判斷是否一條都沒有識別出橫向分隔缐段;
            if len(horizontal_lines) == 0:
                print('horizontal lines not detected.')
                return result_tuple

            # 刪除重複（圖片中的綫條比較寬，誤識別爲兩條較細的綫條）的橫向缐段;
            horizontal_lines = OverlappingFilter(
                horizontal_lines,
                separationThresholdSlope = lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
                separationThresholdIntercept = lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
            )
            # print("Horizontal Lines:\n", horizontal_lines)

            # # 用於調試 #########################################################################
            # # 在源圖像上繪製識別出的量尺（Measuring Ruler）橫向缐段;
            # for line in horizontal_lines:
            #     x1 = line[0]
            #     y1 = line[1]
            #     x2 = line[2]
            #     y2 = line[3]
            #     # print(x1, y1, x2, y2)
            #     cv2.line(imageData, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 在源圖像上繪製識別出的量尺（Measuring Ruler）橫向缐段;
            #     # if y1 == y2:
            #     #     # print(line)
            #     #     cv2.line(imageData, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 在源圖像上繪製識別出的量尺（Measuring Ruler）橫向缐段;
            # # 顯示圖片;
            # cv2.namedWindow("Image")  # 創建圖片展示窗口;
            # cv2.imshow("Image", imageData)  # 顯示圖片 display the image and wait for a keypress
            # # key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;
            # # if key == 27:
            # #     break
            # # # 回車鍵（Enter）的 ASCII 碼爲：ord('\n') == 13
            # # # 空格鍵的 ASCII 碼爲：ord(' ')
            # # # Tab 鍵的 ASCII 碼爲：ord('\t')
            # # # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
            # # # 換行鍵的 ASCII 碼爲：ord('\r')
            # # # Esc 鍵的 ASCII 碼爲：ord('\x1b') == 27
            # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
            # # cv2.destroyAllWindows()  # 關閉所有窗口 closing all open windows
            # cv2.destroyWindow("Image")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;
            # # 用於調試 #########################################################################

            # 識別圖片（Image）量尺（Measuring Ruler）中的縱向竪缐段;
            # HoughLinesP_rho = int(1)  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
            # HoughLinesP_theta = float(np.pi/180)  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
            # HoughLinesP_threshold = int(20)  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
            # HoughLinesP_minLineLength = int(20)  # int(200)  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
            # HoughLinesP_maxLineGap = int(15)  # int(15)  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
            vertical_lines = []  # 存儲在圖像表格（Table）中檢測到的縱向分隔竪缐段座標的列表;
            vertical_lines = lineMeasuring_VerticalLineDetect(
                imageData,
                lineMeasuring_VerticalLineDetect_Canny_threshold1,  # cv2.Canny()：第一次閾值；
                lineMeasuring_VerticalLineDetect_Canny_threshold2,  # cv2.Canny()：第二次閾值；
                lineMeasuring_VerticalLineDetect_Canny_apertureSize,  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
                lineMeasuring_VerticalLineDetect_Canny_L2gradient,  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
                lineMeasuring_VerticalLineDetect_HoughLinesP_rho,  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
                lineMeasuring_VerticalLineDetect_HoughLinesP_theta,  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
                lineMeasuring_VerticalLineDetect_HoughLinesP_threshold,  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
                lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength,  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
                lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
            )
            # print("Vertical Lines:\n", vertical_lines)

            # 判斷是否一條都沒有識別出縱向竪缐段;
            if len(vertical_lines) == 0:
                print('vertical lines not detected.')
                return result_tuple

            # 刪除重複（圖片中的綫條比較寬，誤識別爲兩條較細的綫條）的縱向缐段;
            vertical_lines = OverlappingFilter(
                vertical_lines,
                separationThresholdSlope = lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
                separationThresholdIntercept = lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
            )
            # print("Vertical Lines:\n", vertical_lines)

            # # 用於調試 #########################################################################
            # # 在源圖像上繪製識別出的量尺（Measuring Ruler）縱向缐段;
            # for line in vertical_lines:
            #     x1 = line[0]
            #     y1 = line[1]
            #     x2 = line[2]
            #     y2 = line[3]
            #     # print(x1, y1, x2, y2)
            #     cv2.line(imageData, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 在源圖像上繪製識別出的量尺（Measuring Ruler）縱向缐段;
            #     # if x1 == x2:
            #     #     # print(line)
            #     #     cv2.line(imageData, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 在源圖像上繪製識別出的量尺（Measuring Ruler）縱向缐段;
            # # 顯示圖片;
            # cv2.namedWindow("Image")  # 創建圖片展示窗口;
            # cv2.imshow("Image", imageData)  # 顯示圖片 display the image and wait for a keypress
            # # key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;
            # # if key == 27:
            # #     break
            # # # 回車鍵（Enter）的 ASCII 碼爲：ord('\n') == 13
            # # # 空格鍵的 ASCII 碼爲：ord(' ')
            # # # Tab 鍵的 ASCII 碼爲：ord('\t')
            # # # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
            # # # 換行鍵的 ASCII 碼爲：ord('\r')
            # # # Esc 鍵的 ASCII 碼爲：ord('\x1b') == 27
            # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
            # # cv2.destroyAllWindows()  # 關閉所有窗口 closing all open windows
            # cv2.destroyWindow("Image")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;
            # # 用於調試 #########################################################################

            # 識別圖片（Image）量尺（Measuring Ruler），在識別圖片（Image）量尺（Measuring Ruler）之前，先識別出每個度量值量尺（Measuring Ruler）「標識點」，也就是上述識別後的橫縱向缐條的交點;
            vertexs = []  # 存儲圖片（Image）中識別出的量尺（Measuring Ruler）「標識點」座標的二維列表（行列式）（縱向 → 橫向）;
            vertexs, vertexs_all = lineMeasuring_VertexDetect(horizontal_lines, vertical_lines, imageData, img_height, img_width)
            # print("Vertexs:\n", vertexs)

            # 判斷是否一個都沒有識別出：量尺（Measuring Ruler）「標識點」，也就是上述識別後的橫縱向缐條的交點;
            if len(vertexs) == 0:
                print('Vertexs of Cell in Table in Image, not detected.')
                return result_tuple

            # # 用於調試 #########################################################################
            # # 在源圖像上繪製識別出的圖片（Image）量尺（Measuring Ruler）「標識點」;
            # for point in vertexs:
            #     cv2.circle(imageData, point, 1, (255, 0, 0), 2)
            # # 顯示圖片;
            # cv2.namedWindow("Image")  # 創建圖片展示窗口;
            # cv2.imshow("Image", imageData)  # 顯示圖片 display the image and wait for a keypress
            # # key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;
            # # if key == 27:
            # #     break
            # # # 回車鍵（Enter）的 ASCII 碼爲：ord('\n') == 13
            # # # 空格鍵的 ASCII 碼爲：ord(' ')
            # # # Tab 鍵的 ASCII 碼爲：ord('\t')
            # # # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
            # # # 換行鍵的 ASCII 碼爲：ord('\r')
            # # # Esc 鍵的 ASCII 碼爲：ord('\x1b') == 27
            # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
            # # cv2.destroyAllWindows()  # 關閉所有窗口 closing all open windows
            # cv2.destroyWindow("Image")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;
            # # 用於調試 #########################################################################

            # 識別出的量尺（Measuring Ruler）缐段（Line segment）圖片（Image）的總長度（length）（左端點至右端點），單位是：圖片（Image）缐段（Line segment）所占圖元（像素）（Pixel）點的數量（Number）;
            # measuring_ruler_length = int(int(vertexs[len(vertexs) - 1][0]) - int(vertexs[0][0]))  # 特例，當兩點處於一條水平直缐上時;
            # Z = √((X2 - X1)2 + (Y2 - Y1)2)
            measuring_ruler_length = int(math.sqrt(math.pow(int(int(vertexs[len(vertexs) - 1][0]) - int(vertexs[0][0])), 2) + math.pow(int(int(vertexs[len(vertexs) - 1][1]) - int(vertexs[0][1])), 2)))
            # print(measuring_ruler_length)
            # 識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的長度（length），單位是：圖片（Image）缐段（Line segment）所占圖元（像素）（Pixel）點的數量（Number）;
            Identification_length = []
            for i in range(0, len(vertexs), 1):
                if i > 0 and i < len(vertexs) - 1:
                    # 計算兩點間距離，單位是：圖片（Image）缐段（Line segment）所占圖元（像素）（Pixel）點的數量（Number）;
                    # Identification_length_i = int(int(vertexs[i][0]) - int(vertexs[0][0]))  # 特例，當兩點處於一條水平直缐上時;
                    # Z = √((X2 - X1)2 + (Y2 - Y1)2)
                    Identification_length_i = int(math.sqrt(math.pow(int(int(vertexs[i][0]) - int(vertexs[0][0])), 2) + math.pow(int(int(vertexs[i][1]) - int(vertexs[0][1])), 2)))
                    # print(Identification_length_i)
                    # Min-Max Normalization: 0 ~ 1;
                    Min_Max_normalization_Identification_length_i = float(int(Identification_length_i) / int(measuring_ruler_length))  # Min-Max Normalization: 0 ~ 1;
                    # Mean Normalization: -1 ~ +1;
                    Mean_normalization_Identification_length_i = float(float(float(Min_Max_normalization_Identification_length_i) - float(0.5)) / float(0.5))  # Mean Normalization: -1 ~ +1;
                    # if Min_Max_normalization_Identification_length_i == 0.5:
                    #     Mean_normalization_Identification_length_i = 0.0
                    # if Min_Max_normalization_Identification_length_i < 0.5:
                    #     Mean_normalization_Identification_length_i = -((0.5 - normalization_Identification_length_i) / 0.5)
                    # if Min_Max_normalization_Identification_length_i > 0.5:
                    #     Mean_normalization_Identification_length_i = (normalization_Identification_length_i - 0.5) / 0.5
                    # Mean_normalization_Identification_length_i = round(Mean_normalization_Identification_length_i, 4)  # 四捨五入保留 4 位小數;
                    Identification_length.append(Mean_normalization_Identification_length_i)
            # print(Identification_length)

            # 然後，再根據這些識別出的量尺（Measuring Ruler）「標識點」，截取圖片（Image）量尺（Measuring Ruler）「標識點」區域;
            rects = []  # 存儲截取出的量尺（Measuring Ruler）「標識點」座標的列表;
            cellImages = []  # 存儲截取出的量尺（Measuring Ruler）「標識點」圖片（Image）數據本身的列表;
            # lineMeasuring_Cell_Top_extension = int(-45)  # 截取圖片單元區域的上邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
            # lineMeasuring_Cell_Left_extension = int(-90)  # 截取圖片單元區域的左邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
            # lineMeasuring_Cell_Bottom_extension = int(0)  # 截取圖片單元區域的下邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
            # lineMeasuring_Cell_Right_extension = int(90)  # 截取圖片單元區域的右邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
            # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
            # lineMeasuring_Cell_Top_embedded = int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
            # lineMeasuring_Cell_Bottom_embedded = int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
            # lineMeasuring_Cell_Left_embedded = int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
            # lineMeasuring_Cell_Right_embedded = int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
            rects, cellImages = lineMeasuring_ScaleDetect(
                imageData,
                horizontal_lines,
                vertical_lines,
                vertexs,
                lineMeasuring_Cell_Top_extension,  # = int(-45)  # 截取圖片單元區域的上邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
                lineMeasuring_Cell_Left_extension,  # = int(-90)  # 截取圖片單元區域的左邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
                lineMeasuring_Cell_Bottom_extension,  # = int(0)  # 截取圖片單元區域的下邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
                lineMeasuring_Cell_Right_extension,  # = int(90)  # 截取圖片單元區域的右邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
                lineMeasuring_Cell_Top_embedded,  # = int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
                lineMeasuring_Cell_Bottom_embedded,  # = int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
                lineMeasuring_Cell_Left_embedded,  # = int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
                lineMeasuring_Cell_Right_embedded  # = int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
            )
            # print("Rects Cells:\n", rects)

            # 判斷是否一個都沒有識別出：圖片（Image）量尺（Measuring Ruler）「標識點」區域的圖元（像素）數據;
            if len(cellImages) == 0:
                print('Pixel of Cell in Table in Image, not detected.')
                return result_tuple

            # 判斷是否一個都沒有識別出：圖片（Image）量尺（Measuring Ruler）「標識點」區域的座標值;
            if len(rects) == 0:
                print('Coordinate of Cell in Table in Image, not detected.')
                return result_tuple

            # # 用於調試 #########################################################################
            # # 顯示圖片;
            # cv2.namedWindow("CellImage")  # 創建圖片展示窗口;
            # # 依次顯示所有截取出的量尺（Measuring Ruler）「標識點」圖片（Image）;
            # for horizontal_line_rects in cellImages:
            #     for cellImage in horizontal_line_rects:
            #         cv2.imshow("CellImage", cellImage)  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的量尺（Measuring Ruler）「標識點」圖片（Image） display the image and wait for a keypress;
            #         # key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;
            #         # if key == 27:
            #         #     break
            #         # # 回車鍵（Enter）的 ASCII 碼爲：ord('\n') == 13
            #         # # 空格鍵的 ASCII 碼爲：ord(' ')
            #         # # Tab 鍵的 ASCII 碼爲：ord('\t')
            #         # # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
            #         # # 換行鍵的 ASCII 碼爲：ord('\r')
            #         # # Esc 鍵的 ASCII 碼爲：ord('\x1b') == 27
            #         cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
            # # cv2.destroyAllWindows()  # 關閉所有窗口 closing all open windows
            # cv2.destroyWindow("CellImage")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;
            # # 用於調試 #########################################################################

            # # 用於調試 #########################################################################
            # # 在源圖上繪製所有截取出的單元格（Cell）圖片（Image）的對角頂點;
            # for i in range(0, len(rects), 1):
            #     for j in range(0, len(rects[i]), 1):
            #         # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
            #         X1 = int(int(rects[i][j][0]) + lineMeasuring_Cell_Left_embedded)  # 左邊框位置;
            #         Y1 = int(int(rects[i][j][1]) + lineMeasuring_Cell_Top_embedded)  # 上邊框位置;
            #         X2 = int(int(rects[i][j][2]) - lineMeasuring_Cell_Right_embedded)  # 右邊框位置;
            #         Y2 = int(int(rects[i][j][3]) - lineMeasuring_Cell_Bottom_embedded)  # 下邊框位置;
            #         # cellImage = imageData[Y1:Y2, X1:X2]
            #         # cellImages.append(imageData[Y1:Y2, X1:X2])
            #         # cv2.circle(imageData, (X1, Y1), 1, (255, 0, 255), 2)
            #         # cv2.circle(imageData, (X2, Y2), 1, (0, 255, 255), 2)
            #         cv2.line(imageData, (X1, Y1), (X2, Y2), (0, 255, 255), 2)  # 在源圖像上繪製識別出的表格（Table）縱向分隔缐段;
            # # 顯示圖片;
            # cv2.namedWindow("Image")  # 創建圖片展示窗口;
            # cv2.imshow("Image", imageData)  # 在名稱爲 "Image" 的窗口中顯示圖片（Image） display the image and wait for a keypress;
            # # key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;
            # # if key == 27:
            # #     break
            # # # 回車鍵（Enter）的 ASCII 碼爲：ord('\n') == 13
            # # # 空格鍵的 ASCII 碼爲：ord(' ')
            # # # Tab 鍵的 ASCII 碼爲：ord('\t')
            # # # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
            # # # 換行鍵的 ASCII 碼爲：ord('\r')
            # # # Esc 鍵的 ASCII 碼爲：ord('\x1b') == 27
            # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
            # # cv2.destroyAllWindows()  # 關閉所有窗口 closing all open windows
            # cv2.destroyWindow("Image")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;
            # # 用於調試 #########################################################################

            # # 當源圖片爲彩色（RGB）圖片時：
            # # 將 RGB 模式的量尺（Measuring Ruler）「標識點」圖片（Image），轉換爲灰度（Gray）模式的量尺（Measuring Ruler）「標識點」圖片（Image）;
            # grayCellImages = []  # 用於存儲轉換之後的，灰度（Gray）模式的量尺（Measuring Ruler）「標識點」圖片（Image）;
            # for i in range(0, len(cellImages), 1):
            #     Vertical_CellImages = []
            #     for j in range(0, len(cellImages[i]), 1):
            #         # cv2.imshow("CellImage", cellImages[i][j])  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的量尺（Measuring Ruler）「標識點」圖片（Image）;
            #         gray_Cell_Image = cv2.cvtColor(cellImages[i][j], cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
            #         # cv2.imshow("CellImage", gray_Cell_Image)  # 在名稱爲 "CellImage" 的窗口中顯示圖片顯示截取出的量尺（Measuring Ruler）「標識點」圖片（Image）灰化（Gray）轉換之後的效果;
            #         Vertical_CellImages.append(gray_Cell_Image)
            #     grayCellImages.append(Vertical_CellImages)

            # 當源圖片爲黑白（灰化 Gray）圖片時：
            grayCellImages = cellImages  # 用於存儲轉換之後的，灰度（Gray）模式的量尺（Measuring Ruler）「標識點」圖片（Image）;

            identification_Dict = {}  # 識別出的量尺（Measuring Ruler）「標識點」缐段（Line segment）圖片（Image）的長度（length）數據，單位是：圖片（Image）缐段（Line segment）所占圖元（像素）（Pixel）點的數量（Number），以及，識別出的量尺（Measuring Ruler）「標識點」缐段（Line segment）圖片（Image）中的字符（Characters）數據，用於識別字符所消耗的時長（單位：毫秒 ms），用於存儲的字典對象;
            measuringRuler_Dict = {}  # 用於存儲識別量尺（Measuring Ruler）刻度圖片（Image）中的字符（Characters）數據，以及用於識別字符所消耗的時長（單位：毫秒 ms），用於存儲的字典對象;

            # 依次識別圖片（Image）表格（Tabel）中的量尺（Measuring Ruler）「標識點」中的字符（Character），識別表格（Tabel）的二維行列式的依次順序爲：縱向 → 橫向;
            for i in range(0, len(grayCellImages), 1):

                for j in range(0, len(grayCellImages[i]), 1):

                    text = ""  # string，用於存儲識別出的量尺（Measuring Ruler）「標識點」圖片（Image）中的字符（Characters）數據;
                    time_consuming = int(0)  # int，用於存儲識別量尺（Measuring Ruler）「標識點」圖片（Image）中的字符（Characters）所消耗的時長（單位：毫秒 ms）;

                    # 使用 Google 公司出品的「Teressact-OCR」工具對量尺（Measuring Ruler）「標識點」圖片（Image）做文字（Character）識別;
                    if OCRmethod == "teressact":

                        text, time_consuming = OCRteressact(
                            grayCellImages[i][j],
                            # cellImages,
                            # rects,
                            tesseract_cmd,  # str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # str(pathlib.Path(os.path.abspath("..") + "/Tesseract-OCR/" + "/tesseract/"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
                            tesseract_lang,  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
                            tesseract_config,  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 6 --oem 2'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 6' 爲預設值，表示自動分段，'--psm 7' 表示强調圖像中爲單行文字，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 2' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '--ctessedit_char_whitelist=0123456789' 表示限制爲識別的字符只是阿拉伯數字：0 ~ 9;
                            tesseract_timeout,  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
                            tesseract_output_type,  # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
                            # grayImage,
                            # HorizontalLineDetect,
                            # VerticalLineDetect,
                            # tableRecognition_VertexDetect,
                            # tableRecognition_CellDetect
                        )

                    if len(text) > 0:
                        text = text.strip()  # 刪除字符串兩端的空格;

                    if i == 0:
                        identification_Dict[str("identification-" + str(int(j) + int(1)))] = [
                            time_consuming,  # int 單位：毫秒 # str(time_consuming);
                            text,  # str;
                            Identification_length[j]  # float # str(Identification_length[j]);
                        ]
                        # print("{ ", str("identification-" + str(int(j) + int(1))), ": time consuming", time_consuming, "millisecond } ", text, ",", str(round(Identification_length[j], 4)))
                    if i == 1:
                        measuringRuler_Dict[str("measuringRuler-" + str(int(j) + int(1)))] = [
                            time_consuming,  # int 單位：毫秒 # str(time_consuming);
                            text  # str;
                        ]
                        # print("{ ", str("measuring ruler-" + str(int(j) + int(1))), ": time consuming", time_consuming, "millisecond } ", text)

            result_tuple = (identification_Dict, measuringRuler_Dict)

        return result_tuple

    def run(
        self,
        purpose = "",  # "tableRecognition", "lineMeasuring"
        imageUrl = "",  # "http://www.tabel.jpg" 待識別檢測的圖片的 Web 請求網址 URL 字符串;
        imagePath = "",  # "./tabel.jpg" 待識別檢測的圖片的硬盤保存位置路徑字符串;
        imageData = [],  # cv2.imread(self.imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
        img_height = int(0),
        img_width = int(0),
        grayImageData = [],  # cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
        binaryImageData = [],  # cv2.threshold(self.grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
        CV_parameter = {},
        HorizontalLineDetect = "",  # "Hough", "PixelDifference";
        VerticalLineDetect = "",  # "Hough", "PixelDifference";
        Canny_threshold1 = None,  # cv2.Canny()：第一次閾值；
        Canny_threshold2 = None,  # cv2.Canny()：第二次閾值；
        Canny_apertureSize = None,  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        Canny_L2gradient = None,  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        HoughLinesP_rho = None,  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        HoughLinesP_theta = None,  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        HoughLinesP_threshold = None,  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        HoughLinesP_minLineLength = None,  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        HoughLinesP_maxLineGap = None,  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        tableRecognition_HorizontalLineDetect_Canny_threshold1 = None,
        tableRecognition_HorizontalLineDetect_Canny_threshold2 = None,
        tableRecognition_HorizontalLineDetect_Canny_apertureSize = None,
        tableRecognition_HorizontalLineDetect_Canny_L2gradient = None,
        tableRecognition_HorizontalLineDetect_HoughLinesP_rho = None,
        tableRecognition_HorizontalLineDetect_HoughLinesP_theta = None,
        tableRecognition_HorizontalLineDetect_HoughLinesP_threshold = None,
        tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength = None,
        tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap = None,
        tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope = None,  # float(5)  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept = None,  # float(5)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        tableRecognition_VerticalLineDetect_Canny_threshold1 = None,
        tableRecognition_VerticalLineDetect_Canny_threshold2 = None,
        tableRecognition_VerticalLineDetect_Canny_apertureSize = None,
        tableRecognition_VerticalLineDetect_Canny_L2gradient = None,
        tableRecognition_VerticalLineDetect_HoughLinesP_rho = None,
        tableRecognition_VerticalLineDetect_HoughLinesP_theta = None,
        tableRecognition_VerticalLineDetect_HoughLinesP_threshold = None,
        tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength = None,
        tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap = None,
        tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope = None,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept = None,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        tableRecognition_Cell_Top_embedded = int(0),  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        tableRecognition_Cell_Bottom_embedded = int(0),  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        tableRecognition_Cell_Left_embedded = int(0),  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        tableRecognition_Cell_Right_embedded = int(0),  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        lineMeasuring_HorizontalLineDetect_Canny_threshold1 = None,
        lineMeasuring_HorizontalLineDetect_Canny_threshold2 = None,
        lineMeasuring_HorizontalLineDetect_Canny_apertureSize = None,
        lineMeasuring_HorizontalLineDetect_Canny_L2gradient = None,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_rho = None,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_theta = None,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold = None,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength = None,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap = None,
        lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope = None,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept = None,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        lineMeasuring_VerticalLineDetect_Canny_threshold1 = None,
        lineMeasuring_VerticalLineDetect_Canny_threshold2 = None,
        lineMeasuring_VerticalLineDetect_Canny_apertureSize = None,
        lineMeasuring_VerticalLineDetect_Canny_L2gradient = None,
        lineMeasuring_VerticalLineDetect_HoughLinesP_rho = None,
        lineMeasuring_VerticalLineDetect_HoughLinesP_theta = None,
        lineMeasuring_VerticalLineDetect_HoughLinesP_threshold = None,
        lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength = None,
        lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap = None,
        lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope = None,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept = None,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        lineMeasuring_Cell_Top_extension = int(0),  # int(-45)  # 截取圖片單元區域的上邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Left_extension = int(0),  # int(-90)  # 截取圖片單元區域的左邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Bottom_extension = int(0),  # int(0)  # 截取圖片單元區域的下邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Right_extension = int(0),  # int(90)  # 截取圖片單元區域的右邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Top_embedded = int(0),  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        lineMeasuring_Cell_Bottom_embedded = int(0),  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        lineMeasuring_Cell_Left_embedded = int(0),  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        lineMeasuring_Cell_Right_embedded = int(0),  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        OCR_parameter = {},
        OCRmethod = "",  # "teressact";
        tesseract_cmd = "",  # str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # str(pathlib.Path(os.path.abspath("..") + "/Tesseract-OCR/" + "/tesseract/"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
        tesseract_lang = "",  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
        tesseract_config = "",  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        tesseract_timeout = None,  # int(0)  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
        tesseract_output_type = "",  # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
    ):
        if len(purpose) > 0:
            self.purpose = purpose  # "tableRecognition", "lineMeasuring"
        if len(imageUrl) > 0:
            self.imageUrl = imageUrl  # "http://www.tabel.jpg" 待識別檢測的圖片的 Web 請求網址 URL 字符串;
            response = urllib_request.urlopen(self.imageUrl)  # 使用 Python 語言的原生模組「urllib」中的「request」中的「urlopen()」函數向服務器請求下載圖片數據;
            img_array = np.array(bytearray(response.read()), dtype = np.uint8)  # 把從服務器下載的圖片數據轉換爲二進位 8 位字節數組的形式;
            self.imageData = cv2.imdecode(img_array, -1)  # 使用 Python 語言的第三方擴展模組「opencv」中的「cv2.imdecode()」函數解析二進位 8 位字節數組形式的图片數據，RGB 模式;
            if len(self.imageData) > 0:
                # 獲取圖像的高度和寬度：
                # print(self.imageData.shape)
                self.img_height, self.img_width, _ = self.imageData.shape
                # self.img_height, self.img_width, img_dimension = self.imageData.shape
                # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;
                # # 遍歷每個像素：
                # for i in range(img_height):
                #     for j in range(img_width):
                #         pixel_value = img[i, j]  # 在這個示例中：img[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
                #         print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))
            self.grayImageData = cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
            # self.binaryImageData = cv2.threshold(self.grayImageData, 127, 255, cv2.THRESH_BINARY_INV)  # 使用自定義閾值：「127」，過濾轉化爲二值化（非黑即白）的圖片;
            self.binaryImageData = cv2.threshold(self.grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
            # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
            # self.binaryImageData = cv2.ximgproc.thinning(self.binaryImageData, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;
        if len(imagePath) > 0:
            self.imagePath = imagePath  # "./tabel.jpg" 待識別檢測的圖片的硬盤保存位置路徑字符串;
            self.imageData = cv2.imread(self.imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
            if len(self.imageData) > 0:
                # 獲取圖像的高度和寬度：
                # print(self.imageData.shape)
                self.img_height, self.img_width, _ = self.imageData.shape
                # self.img_height, self.img_width, img_dimension = self.imageData.shape
                # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;
                # # 遍歷每個像素：
                # for i in range(img_height):
                #     for j in range(img_width):
                #         pixel_value = img[i, j]  # 在這個示例中：img[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
                #         print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))
            self.grayImageData = cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
            # self.binaryImageData = cv2.threshold(self.grayImageData, 127, 255, cv2.THRESH_BINARY_INV)  # 使用自定義閾值：「127」，過濾轉化爲二值化（非黑即白）的圖片;
            self.binaryImageData = cv2.threshold(self.grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
            # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
            # self.binaryImageData = cv2.ximgproc.thinning(self.binaryImageData, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;
        if len(imageData) > 0:
            self.imageData = imageData  # [],  # cv2.imread(self.imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
            if len(self.imageData) > 0:
                # 獲取圖像的高度和寬度：
                # print(self.imageData.shape)
                self.img_height, self.img_width, _ = self.imageData.shape
                # self.img_height, self.img_width, img_dimension = self.imageData.shape
                # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;
                # # 遍歷每個像素：
                # for i in range(img_height):
                #     for j in range(img_width):
                #         pixel_value = img[i, j]  # 在這個示例中：img[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
                #         print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))
            self.grayImageData = cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
            # self.binaryImageData = cv2.threshold(self.grayImageData, 127, 255, cv2.THRESH_BINARY_INV)  # 使用自定義閾值：「127」，過濾轉化爲二值化（非黑即白）的圖片;
            self.binaryImageData = cv2.threshold(self.grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
            # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
            # self.binaryImageData = cv2.ximgproc.thinning(self.binaryImageData, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;
        if len(grayImageData) > 0:
            self.grayImageData = grayImageData  # [],  # cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
            if len(self.grayImageData) > 0:
                # 獲取圖像的高度和寬度：
                # print(self.grayImageData.shape)
                self.img_height, self.img_width = self.grayImageData.shape
                # # 遍歷每個像素：
                # for i in range(img_height):
                #     for j in range(img_width):
                #         pixel_value = self.grayImageData[i, j]  # 在這個示例中：self.grayImageData[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
                #         print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))
            # self.binaryImageData = cv2.threshold(self.grayImageData, 127, 255, cv2.THRESH_BINARY_INV)  # 使用自定義閾值：「127」，過濾轉化爲二值化（非黑即白）的圖片;
            self.binaryImageData = cv2.threshold(self.grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
            # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
            # self.binaryImageData = cv2.ximgproc.thinning(self.binaryImageData, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;
        if len(binaryImageData) > 0:
            # self.binaryImageData = binaryImageData  # [],  # cv2.threshold(self.grayImageData, 127, 255, cv2.THRESH_BINARY_INV)  # 使用自定義閾值：「127」，過濾轉化爲二值化（非黑即白）的圖片;
            self.binaryImageData = binaryImageData  # [],  # cv2.threshold(self.grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
            # if len(self.binaryImageData) > 0:
            #     # 獲取圖像的高度和寬度：
            #     # print(self.binaryImageData.shape)
            #     self.img_height, self.img_width = self.binaryImageData.shape
            #     # # 遍歷每個像素：
            #     # for i in range(img_height):
            #     #     for j in range(img_width):
            #     #         pixel_value = self.binaryImageData[i, j]  # 在這個示例中：self.binaryImageData[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
            #     #         print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))
            # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
            # self.binaryImageData = cv2.ximgproc.thinning(self.binaryImageData, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;
        if int(img_height) > int(0):
            self.img_height = int(img_height)
        # print("Image height:", str(self.img_height))
        if int(img_width) > int(0):
            self.img_width = int(img_width)
        # print("Image width:", str(self.img_width))
        if len(CV_parameter) > 0:
            # self.CV_parameter = CV_parameter
            for key in CV_parameter:
                if key == "HorizontalLineDetect":
                    self.HorizontalLineDetect = str(CV_parameter[key])
                if key == "VerticalLineDetect":
                    self.VerticalLineDetect = str(CV_parameter[key])
                if key == "Canny_threshold1":
                    self.Canny_threshold1 = CV_parameter[key]
                if key == "Canny_threshold2":
                    self.Canny_threshold2 = CV_parameter[key]
                if key == "Canny_apertureSize":
                    self.Canny_apertureSize = CV_parameter[key]
                if key == "Canny_L2gradient":
                    self.Canny_L2gradient = bool(CV_parameter[key])
                if key == "HoughLinesP_rho":
                    self.HoughLinesP_rho = CV_parameter[key]
                if key == "HoughLinesP_theta":
                    self.HoughLinesP_theta = CV_parameter[key]
                if key == "HoughLinesP_threshold":
                    self.HoughLinesP_threshold = CV_parameter[key]
                if key == "HoughLinesP_minLineLength":
                    self.HoughLinesP_minLineLength = CV_parameter[key]
                if key == "HoughLinesP_maxLineGap":
                    self.HoughLinesP_maxLineGap = CV_parameter[key]
                if key == "tableRecognition_HorizontalLineDetect_Canny_threshold1":
                    self.tableRecognition_HorizontalLineDetect_Canny_threshold1 = CV_parameter[key]
                if key == "tableRecognition_HorizontalLineDetect_Canny_threshold2":
                    self.tableRecognition_HorizontalLineDetect_Canny_threshold2 = CV_parameter[key]
                if key == "tableRecognition_HorizontalLineDetect_Canny_apertureSize":
                    self.tableRecognition_HorizontalLineDetect_Canny_apertureSize = CV_parameter[key]
                if key == "tableRecognition_HorizontalLineDetect_Canny_L2gradient":
                    self.tableRecognition_HorizontalLineDetect_Canny_L2gradient = bool(CV_parameter[key])
                if key == "tableRecognition_HorizontalLineDetect_HoughLinesP_rho":
                    self.tableRecognition_HorizontalLineDetect_HoughLinesP_rho = CV_parameter[key]
                if key == "tableRecognition_HorizontalLineDetect_HoughLinesP_theta":
                    self.tableRecognition_HorizontalLineDetect_HoughLinesP_theta = CV_parameter[key]
                if key == "tableRecognition_HorizontalLineDetect_HoughLinesP_threshold":
                    self.tableRecognition_HorizontalLineDetect_HoughLinesP_threshold = CV_parameter[key]
                if key == "tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength":
                    self.tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength = CV_parameter[key]
                if key == "tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap":
                    self.tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap = CV_parameter[key]
                if key == "tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope":
                    self.tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope = float(CV_parameter[key])
                if key == "tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept":
                    self.tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept = float(CV_parameter[key])
                if key == "tableRecognition_VerticalLineDetect_Canny_threshold1":
                    self.tableRecognition_VerticalLineDetect_Canny_threshold1 = CV_parameter[key]
                if key == "tableRecognition_VerticalLineDetect_Canny_threshold2":
                    self.tableRecognition_VerticalLineDetect_Canny_threshold2 = CV_parameter[key]
                if key == "tableRecognition_VerticalLineDetect_Canny_apertureSize":
                    self.tableRecognition_VerticalLineDetect_Canny_apertureSize = CV_parameter[key]
                if key == "tableRecognition_VerticalLineDetect_Canny_L2gradient":
                    self.tableRecognition_VerticalLineDetect_Canny_L2gradient = bool(CV_parameter[key])
                if key == "tableRecognition_VerticalLineDetect_HoughLinesP_rho":
                    self.tableRecognition_VerticalLineDetect_HoughLinesP_rho = CV_parameter[key]
                if key == "tableRecognition_VerticalLineDetect_HoughLinesP_theta":
                    self.tableRecognition_VerticalLineDetect_HoughLinesP_theta = CV_parameter[key]
                if key == "tableRecognition_VerticalLineDetect_HoughLinesP_threshold":
                    self.tableRecognition_VerticalLineDetect_HoughLinesP_threshold = CV_parameter[key]
                if key == "tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength":
                    self.tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength = CV_parameter[key]
                if key == "tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap":
                    self.tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap = CV_parameter[key]
                if key == "tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope":
                    self.tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope = float(CV_parameter[key])
                if key == "tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept":
                    self.tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept = float(CV_parameter[key])
                if key == "tableRecognition_Cell_Top_embedded":
                    self.tableRecognition_Cell_Top_embedded = int(CV_parameter[key])
                if key == "tableRecognition_Cell_Bottom_embedded":
                    self.tableRecognition_Cell_Bottom_embedded = int(CV_parameter[key])
                if key == "tableRecognition_Cell_Left_embedded":
                    self.tableRecognition_Cell_Left_embedded = int(CV_parameter[key])
                if key == "tableRecognition_Cell_Right_embedded":
                    self.tableRecognition_Cell_Right_embedded = int(CV_parameter[key])
                if key == "lineMeasuring_HorizontalLineDetect_Canny_threshold1":
                    self.lineMeasuring_HorizontalLineDetect_Canny_threshold1 = CV_parameter[key]
                if key == "lineMeasuring_HorizontalLineDetect_Canny_threshold2":
                    self.lineMeasuring_HorizontalLineDetect_Canny_threshold2 = CV_parameter[key]
                if key == "lineMeasuring_HorizontalLineDetect_Canny_apertureSize":
                    self.lineMeasuring_HorizontalLineDetect_Canny_apertureSize = CV_parameter[key]
                if key == "lineMeasuring_HorizontalLineDetect_Canny_L2gradient":
                    self.lineMeasuring_HorizontalLineDetect_Canny_L2gradient = bool(CV_parameter[key])
                if key == "lineMeasuring_HorizontalLineDetect_HoughLinesP_rho":
                    self.lineMeasuring_HorizontalLineDetect_HoughLinesP_rho = CV_parameter[key]
                if key == "lineMeasuring_HorizontalLineDetect_HoughLinesP_theta":
                    self.lineMeasuring_HorizontalLineDetect_HoughLinesP_theta = CV_parameter[key]
                if key == "lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold":
                    self.lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold = CV_parameter[key]
                if key == "lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength":
                    self.lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength = CV_parameter[key]
                if key == "lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap":
                    self.lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap = CV_parameter[key]
                if key == "lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope":
                    self.lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope = float(CV_parameter[key])
                if key == "lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept":
                    self.lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept = float(CV_parameter[key])
                if key == "lineMeasuring_VerticalLineDetect_Canny_threshold1":
                    self.lineMeasuring_VerticalLineDetect_Canny_threshold1 = CV_parameter[key]
                if key == "lineMeasuring_VerticalLineDetect_Canny_threshold2":
                    self.lineMeasuring_VerticalLineDetect_Canny_threshold2 = CV_parameter[key]
                if key == "lineMeasuring_VerticalLineDetect_Canny_apertureSize":
                    self.lineMeasuring_VerticalLineDetect_Canny_apertureSize = CV_parameter[key]
                if key == "lineMeasuring_VerticalLineDetect_Canny_L2gradient":
                    self.lineMeasuring_VerticalLineDetect_Canny_L2gradient = bool(CV_parameter[key])
                if key == "lineMeasuring_VerticalLineDetect_HoughLinesP_rho":
                    self.lineMeasuring_VerticalLineDetect_HoughLinesP_rho = CV_parameter[key]
                if key == "lineMeasuring_VerticalLineDetect_HoughLinesP_theta":
                    self.lineMeasuring_VerticalLineDetect_HoughLinesP_theta = CV_parameter[key]
                if key == "lineMeasuring_VerticalLineDetect_HoughLinesP_threshold":
                    self.lineMeasuring_VerticalLineDetect_HoughLinesP_threshold = CV_parameter[key]
                if key == "lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength":
                    self.lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength = CV_parameter[key]
                if key == "lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap":
                    self.lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap = CV_parameter[key]
                if key == "lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope":
                    self.lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope = float(CV_parameter[key])
                if key == "lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept":
                    self.lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept = float(CV_parameter[key])
                if key == "lineMeasuring_Cell_Top_extension":
                    self.lineMeasuring_Cell_Top_extension = int(CV_parameter[key])
                if key == "lineMeasuring_Cell_Left_extension":
                    self.lineMeasuring_Cell_Left_extension = int(CV_parameter[key])
                if key == "lineMeasuring_Cell_Bottom_extension":
                    self.lineMeasuring_Cell_Bottom_extension = int(CV_parameter[key])
                if key == "lineMeasuring_Cell_Right_extension":
                    self.lineMeasuring_Cell_Right_extension = int(CV_parameter[key])
                if key == "lineMeasuring_Cell_Top_embedded":
                    self.lineMeasuring_Cell_Top_embedded = int(CV_parameter[key])
                if key == "lineMeasuring_Cell_Bottom_embedded":
                    self.lineMeasuring_Cell_Bottom_embedded = int(CV_parameter[key])
                if key == "lineMeasuring_Cell_Left_embedded":
                    self.lineMeasuring_Cell_Left_embedded = int(CV_parameter[key])
                if key == "lineMeasuring_Cell_Right_embedded":
                    self.lineMeasuring_Cell_Right_embedded = int(CV_parameter[key])
        if len(HorizontalLineDetect) > 0:
            self.HorizontalLineDetect = HorizontalLineDetect  # "Hough", "PixelDifference";
        if len(VerticalLineDetect) > 0:
            self.VerticalLineDetect = VerticalLineDetect  # "Hough", "PixelDifference";
        if not (Canny_threshold1 is None):
            self.Canny_threshold1 = Canny_threshold1  # cv2.Canny()：第一次閾值；
        if not (Canny_threshold2 is None):
            self.Canny_threshold2 = Canny_threshold2  # cv2.Canny()：第二次閾值；
        if not (Canny_apertureSize is None):
            self.Canny_apertureSize = Canny_apertureSize  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        if not (Canny_L2gradient is None):
            self.Canny_L2gradient = Canny_L2gradient  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        if not (HoughLinesP_rho is None):
            self.HoughLinesP_rho = HoughLinesP_rho  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        if not (HoughLinesP_theta is None):
            self.HoughLinesP_theta = HoughLinesP_theta  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        if not (HoughLinesP_threshold is None):
            self.HoughLinesP_threshold = HoughLinesP_threshold  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        if not (HoughLinesP_minLineLength is None):
            self.HoughLinesP_minLineLength = HoughLinesP_minLineLength  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        if not (HoughLinesP_maxLineGap is None):
            self.HoughLinesP_maxLineGap = HoughLinesP_maxLineGap  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        if not (tableRecognition_HorizontalLineDetect_Canny_threshold1 is None):
            self.tableRecognition_HorizontalLineDetect_Canny_threshold1 = tableRecognition_HorizontalLineDetect_Canny_threshold1
        if not (tableRecognition_HorizontalLineDetect_Canny_threshold2 is None):
            self.tableRecognition_HorizontalLineDetect_Canny_threshold2 = tableRecognition_HorizontalLineDetect_Canny_threshold2
        if not (tableRecognition_HorizontalLineDetect_Canny_apertureSize is None):
            self.tableRecognition_HorizontalLineDetect_Canny_apertureSize = tableRecognition_HorizontalLineDetect_Canny_apertureSize
        if not (tableRecognition_HorizontalLineDetect_Canny_L2gradient is None):
            self.tableRecognition_HorizontalLineDetect_Canny_L2gradient = tableRecognition_HorizontalLineDetect_Canny_L2gradient
        if not (tableRecognition_HorizontalLineDetect_HoughLinesP_rho is None):
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_rho = tableRecognition_HorizontalLineDetect_HoughLinesP_rho
        if not (tableRecognition_HorizontalLineDetect_HoughLinesP_theta is None):
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_theta = tableRecognition_HorizontalLineDetect_HoughLinesP_theta
        if not (tableRecognition_HorizontalLineDetect_HoughLinesP_threshold is None):
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_threshold = tableRecognition_HorizontalLineDetect_HoughLinesP_threshold
        if not (tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength is None):
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength = tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength
        if not (tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap is None):
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap = tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap
        if not (tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope is None):
            self.tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope = tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope
        if not (tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept is None):
            self.tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept = tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept
        if not (tableRecognition_VerticalLineDetect_Canny_threshold1 is None):
            self.tableRecognition_VerticalLineDetect_Canny_threshold1 = tableRecognition_VerticalLineDetect_Canny_threshold1
        if not (tableRecognition_VerticalLineDetect_Canny_threshold2 is None):
            self.tableRecognition_VerticalLineDetect_Canny_threshold2 = tableRecognition_VerticalLineDetect_Canny_threshold2
        if not (tableRecognition_VerticalLineDetect_Canny_apertureSize is None):
            self.tableRecognition_VerticalLineDetect_Canny_apertureSize = tableRecognition_VerticalLineDetect_Canny_apertureSize
        if not (tableRecognition_VerticalLineDetect_Canny_L2gradient is None):
            self.tableRecognition_VerticalLineDetect_Canny_L2gradient = tableRecognition_VerticalLineDetect_Canny_L2gradient
        if not (tableRecognition_VerticalLineDetect_HoughLinesP_rho is None):
            self.tableRecognition_VerticalLineDetect_HoughLinesP_rho = tableRecognition_VerticalLineDetect_HoughLinesP_rho
        if not (tableRecognition_VerticalLineDetect_HoughLinesP_theta is None):
            self.tableRecognition_VerticalLineDetect_HoughLinesP_theta = tableRecognition_VerticalLineDetect_HoughLinesP_theta
        if not (tableRecognition_VerticalLineDetect_HoughLinesP_threshold is None):
            self.tableRecognition_VerticalLineDetect_HoughLinesP_threshold = tableRecognition_VerticalLineDetect_HoughLinesP_threshold
        if not (tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength is None):
            self.tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength = tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength
        if not (tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap is None):
            self.tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap = tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap
        if not (tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope is None):
            self.tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope = tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope
        if not (tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept is None):
            self.tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept = tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept
        if int(tableRecognition_Cell_Top_embedded) != int(0):
            self.tableRecognition_Cell_Top_embedded = int(tableRecognition_Cell_Top_embedded)
        if int(tableRecognition_Cell_Bottom_embedded) != int(0):
            self.tableRecognition_Cell_Bottom_embedded = int(tableRecognition_Cell_Bottom_embedded)
        if int(tableRecognition_Cell_Left_embedded) != int(0):
            self.tableRecognition_Cell_Left_embedded = int(tableRecognition_Cell_Left_embedded)
        if int(tableRecognition_Cell_Right_embedded) != int(0):
            self.tableRecognition_Cell_Right_embedded = int(tableRecognition_Cell_Right_embedded)
        if not (lineMeasuring_HorizontalLineDetect_Canny_threshold1 is None):
            self.lineMeasuring_HorizontalLineDetect_Canny_threshold1 = lineMeasuring_HorizontalLineDetect_Canny_threshold1
        if not (lineMeasuring_HorizontalLineDetect_Canny_threshold2 is None):
            self.lineMeasuring_HorizontalLineDetect_Canny_threshold2 = lineMeasuring_HorizontalLineDetect_Canny_threshold2
        if not (lineMeasuring_HorizontalLineDetect_Canny_apertureSize is None):
            self.lineMeasuring_HorizontalLineDetect_Canny_apertureSize = lineMeasuring_HorizontalLineDetect_Canny_apertureSize
        if not (lineMeasuring_HorizontalLineDetect_Canny_L2gradient is None):
            self.lineMeasuring_HorizontalLineDetect_Canny_L2gradient = lineMeasuring_HorizontalLineDetect_Canny_L2gradient
        if not (lineMeasuring_HorizontalLineDetect_HoughLinesP_rho is None):
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_rho = lineMeasuring_HorizontalLineDetect_HoughLinesP_rho
        if not (lineMeasuring_HorizontalLineDetect_HoughLinesP_theta is None):
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_theta = lineMeasuring_HorizontalLineDetect_HoughLinesP_theta
        if not (lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold is None):
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold = lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold
        if not (lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength is None):
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength = lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength
        if not (lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap is None):
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap = lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap
        if not (lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope is None):
            self.lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope = lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope
        if not (lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept is None):
            self.lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept = lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept
        if not (lineMeasuring_VerticalLineDetect_Canny_threshold1 is None):
            self.lineMeasuring_VerticalLineDetect_Canny_threshold1 = lineMeasuring_VerticalLineDetect_Canny_threshold1
        if not (lineMeasuring_VerticalLineDetect_Canny_threshold2 is None):
            self.lineMeasuring_VerticalLineDetect_Canny_threshold2 = lineMeasuring_VerticalLineDetect_Canny_threshold2
        if not (lineMeasuring_VerticalLineDetect_Canny_apertureSize is None):
            self.lineMeasuring_VerticalLineDetect_Canny_apertureSize = lineMeasuring_VerticalLineDetect_Canny_apertureSize
        if not (lineMeasuring_VerticalLineDetect_Canny_L2gradient is None):
            self.lineMeasuring_VerticalLineDetect_Canny_L2gradient = lineMeasuring_VerticalLineDetect_Canny_L2gradient
        if not (lineMeasuring_VerticalLineDetect_HoughLinesP_rho is None):
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_rho = lineMeasuring_VerticalLineDetect_HoughLinesP_rho
        if not (lineMeasuring_VerticalLineDetect_HoughLinesP_theta is None):
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_theta = lineMeasuring_VerticalLineDetect_HoughLinesP_theta
        if not (lineMeasuring_VerticalLineDetect_HoughLinesP_threshold is None):
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_threshold = lineMeasuring_VerticalLineDetect_HoughLinesP_threshold
        if not (lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength is None):
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength = lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength
        if not (lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap is None):
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap = lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap
        if not (lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope is None):
            self.lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope = lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope
        if not (lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept is None):
            self.lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept = lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept
        if int(lineMeasuring_Cell_Top_extension) != int(0):
            self.lineMeasuring_Cell_Top_extension = int(lineMeasuring_Cell_Top_extension)
        if int(lineMeasuring_Cell_Left_extension) != int(0):
            self.lineMeasuring_Cell_Left_extension = int(lineMeasuring_Cell_Left_extension)
        if int(lineMeasuring_Cell_Bottom_extension) != int(0):
            self.lineMeasuring_Cell_Bottom_extension = int(lineMeasuring_Cell_Bottom_extension)
        if int(lineMeasuring_Cell_Right_extension) != int(0):
            self.lineMeasuring_Cell_Right_extension = int(lineMeasuring_Cell_Right_extension)
        if int(lineMeasuring_Cell_Top_embedded) != int(0):
            self.lineMeasuring_Cell_Top_embedded = int(lineMeasuring_Cell_Top_embedded)
        if int(lineMeasuring_Cell_Bottom_embedded) != int(0):
            self.lineMeasuring_Cell_Bottom_embedded = int(lineMeasuring_Cell_Bottom_embedded)
        if int(lineMeasuring_Cell_Left_embedded) != int(0):
            self.lineMeasuring_Cell_Left_embedded = int(lineMeasuring_Cell_Left_embedded)
        if int(lineMeasuring_Cell_Right_embedded) != int(0):
            self.lineMeasuring_Cell_Right_embedded = int(lineMeasuring_Cell_Right_embedded)
        if len(OCR_parameter) > 0:
            # self.OCR_parameter = OCR_parameter
            for key in OCR_parameter:
                if key == "OCRmethod":
                    self.OCRmethod = str(OCR_parameter[key])
                if key == "tesseract_cmd":
                    self.tesseract_cmd = str(OCR_parameter[key])
                if key == "tesseract_lang":
                    self.tesseract_lang = str(OCR_parameter[key])
                if key == "tesseract_config":
                    self.tesseract_config = str(OCR_parameter[key])
                if key == "tesseract_timeout":
                    self.tesseract_timeout = int(OCR_parameter[key])
                if key == "tesseract_tessdata_dir":
                    self.tesseract_tessdata_dir = str(OCR_parameter[key])
                if key == "tesseract_user_words":
                    self.tesseract_user_words = str(OCR_parameter[key])
                if key == "tesseract_user_patterns":
                    self.tesseract_user_patterns = str(OCR_parameter[key])
                if key == "tesseract_output_type":
                    if str(OCR_parameter[key]) == 'pytesseract.Output.STRING':
                        self.tesseract_output_type = pytesseract.Output.STRING
                    if str(OCR_parameter[key]) == 'pytesseract.Output.BYTES':
                        self.tesseract_output_type = pytesseract.Output.BYTES
                    if str(OCR_parameter[key]) == 'pytesseract.Output.DICT':
                        self.tesseract_output_type = pytesseract.Output.DICT
                    if str(OCR_parameter[key]) == 'pytesseract.Output.DATAFRAME':
                        self.tesseract_output_type = pytesseract.Output.DATAFRAME
        if len(OCRmethod) > 0:
            self.OCRmethod = OCRmethod  # "teressact";
        if len(tesseract_cmd) > 0:
            self.tesseract_cmd = tesseract_cmd  # str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # str(pathlib.Path(os.path.abspath("..") + "/Tesseract-OCR/" + "/tesseract/"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
            # if self.OCRmethod == "teressact":
            #     # self.tesseract_cmd == r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # tesseract_cmd = r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
            #     pytesseract.pytesseract.tesseract_cmd = self.tesseract_cmd  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
        if len(tesseract_lang) > 0:
            self.tesseract_lang = tesseract_lang  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
        if len(tesseract_config) > 0:
            self.tesseract_config = tesseract_config  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        if not (tesseract_timeout is None):
            self.tesseract_timeout = tesseract_timeout  # int(0)  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
        # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
        if len(tesseract_output_type) > 0:
            if tesseract_output_type == 'pytesseract.Output.STRING':
                self.tesseract_output_type = pytesseract.Output.STRING
            if tesseract_output_type == 'pytesseract.Output.BYTES':
                self.tesseract_output_type = pytesseract.Output.BYTES
            if tesseract_output_type == 'pytesseract.Output.DICT':
                self.tesseract_output_type = pytesseract.Output.DICT
            if tesseract_output_type == 'pytesseract.Output.DATAFRAME':
                self.tesseract_output_type = pytesseract.Output.DATAFRAME


        result_tuple = self.start(
            self.purpose,  # "tableRecognition", "lineMeasuring"
            self.imageUrl,  # 待識別檢測的圖片的 Web 請求網址 URL 字符串;
            self.imagePath,  # 待識別檢測的圖片的硬盤保存位置路徑字符串;
            self.imageData,  # cv2.imread(self.imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
            self.img_height,
            self.img_width,
            self.grayImageData,  # cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
            self.binaryImageData,  # cv2.threshold(grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
            # self.CV_parameter,
            self.HorizontalLineDetect,  # "Hough", "PixelDifference";
            self.VerticalLineDetect,  # "Hough", "PixelDifference";
            self.Canny_threshold1,  # cv2.Canny()：第一次閾值；
            self.Canny_threshold2,  # cv2.Canny()：第二次閾值；
            self.Canny_apertureSize,  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
            self.Canny_L2gradient,  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
            self.HoughLinesP_rho,  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
            self.HoughLinesP_theta,  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
            self.HoughLinesP_threshold,  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
            self.HoughLinesP_minLineLength,  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
            self.HoughLinesP_maxLineGap,  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
            self.tableRecognition_HorizontalLineDetect_Canny_threshold1,
            self.tableRecognition_HorizontalLineDetect_Canny_threshold2,
            self.tableRecognition_HorizontalLineDetect_Canny_apertureSize,
            self.tableRecognition_HorizontalLineDetect_Canny_L2gradient,
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_rho,
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_theta,
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_threshold,
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength,
            self.tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap,
            self.tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5)  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
            self.tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
            self.tableRecognition_VerticalLineDetect_Canny_threshold1,
            self.tableRecognition_VerticalLineDetect_Canny_threshold2,
            self.tableRecognition_VerticalLineDetect_Canny_apertureSize,
            self.tableRecognition_VerticalLineDetect_Canny_L2gradient,
            self.tableRecognition_VerticalLineDetect_HoughLinesP_rho,
            self.tableRecognition_VerticalLineDetect_HoughLinesP_theta,
            self.tableRecognition_VerticalLineDetect_HoughLinesP_threshold,
            self.tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength,
            self.tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap,
            self.tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
            self.tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
            self.tableRecognition_Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
            self.tableRecognition_Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
            self.tableRecognition_Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
            self.tableRecognition_Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
            self.lineMeasuring_HorizontalLineDetect_Canny_threshold1,
            self.lineMeasuring_HorizontalLineDetect_Canny_threshold2,
            self.lineMeasuring_HorizontalLineDetect_Canny_apertureSize,
            self.lineMeasuring_HorizontalLineDetect_Canny_L2gradient,
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_rho,
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_theta,
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold,
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength,
            self.lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap,
            self.lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
            self.lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
            self.lineMeasuring_VerticalLineDetect_Canny_threshold1,
            self.lineMeasuring_VerticalLineDetect_Canny_threshold2,
            self.lineMeasuring_VerticalLineDetect_Canny_apertureSize,
            self.lineMeasuring_VerticalLineDetect_Canny_L2gradient,
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_rho,
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_theta,
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_threshold,
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength,
            self.lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap,
            self.lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
            self.lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
            self.lineMeasuring_Cell_Top_extension,  # int(-45)  # 截取圖片單元區域的上邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
            self.lineMeasuring_Cell_Left_extension,  # int(-90)  # 截取圖片單元區域的左邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
            self.lineMeasuring_Cell_Bottom_extension,  # int(0)  # 截取圖片單元區域的下邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
            self.lineMeasuring_Cell_Right_extension,  # int(90)  # 截取圖片單元區域的右邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
            self.lineMeasuring_Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
            self.lineMeasuring_Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
            self.lineMeasuring_Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
            self.lineMeasuring_Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
            self.save_image,  # False, True;
            # self.OCR_parameter,
            self.OCRmethod,  # "teressact";
            self.tesseract_cmd,  # str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # str(pathlib.Path(os.path.abspath("..") + "/Tesseract-OCR/" + "/tesseract/"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
            self.tesseract_lang,  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
            self.tesseract_config,  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
            self.tesseract_output_type,  # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
            self.tesseract_timeout,  # int(0)  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
            # self.do_Function,
            self.region_selection,
            self.orientation_correction,
            self.OverlappingFilter,
            self.getCurvesEnd,
            self.tableRecognition_HorizontalLineDetect_PixelDifference,
            self.tableRecognition_HorizontalLineDetect_Hough,
            self.tableRecognition_VerticalLineDetect_PixelDifference,
            self.tableRecognition_VerticalLineDetect_Hough,
            self.tableRecognition_VertexDetect,
            self.tableRecognition_CellDetect,
            self.lineMeasuring_HorizontalLineDetect,
            self.lineMeasuring_VerticalLineDetect,
            self.lineMeasuring_VertexDetect,
            self.lineMeasuring_ScaleDetect,
            self.OCRteressact,
        )
        # print(result_tuple)

        # if not (not (result_tuple is None)):
        #     return ([], [], {})
        # else:
        #     return result_tuple

        return result_tuple



def do_data(require_data):

    # print(require_data)
    # print(typeof(require_data))
    # require_data_bytes = require_data.encode("utf-8")
    # require_data = require_data_bytes.decode("utf-8")
    # require_data = str(require_data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
    # require_data_len = len(bytes(require_data, "utf-8"))
    # print(typeof(require_data_bytes))

    # response = urllib_request.urlopen(imageUrl)  # 使用 Python 語言的原生模組「urllib」中的「request」中的「urlopen()」函數向服務器請求下載圖片數據;
    # img_array = np.array(bytearray(response.read()), dtype = np.uint8)  # 把從服務器下載的圖片數據轉換爲二進位 8 位字節數組的形式;
    # imageData = cv2.imread(imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
    # fd = open(
    #     str(os.path.normpath(str(imagePath))).replace('\\', '/'),
    #     mode="rb+",  # 讀取文本字符：mode="r"，讀取二進制字節<class 'bytes'>：mode="rb+"
    #     buffering=-1,
    #     # encoding="utf-8",
    #     errors=None,
    #     newline=None,
    #     closefd=True,
    #     opener=None
    # )
    # file_Data = fd.read()
    img_array = np.array(bytearray(require_data), dtype = np.uint8)  # 把從服務器下載的圖片數據轉換爲二進位 8 位字節數組的形式;
    # fd.close()
    imageData = cv2.imdecode(img_array, -1)  # 使用 Python 語言的第三方擴展模組「opencv」中的「cv2.imdecode()」函數解析二進位 8 位字節數組形式的图片數據，RGB 模式;

    # cv2.namedWindow("Image")  # 創建圖片展示窗口;
    # cv2.imshow("Image", imageData)  # 顯示圖片 display the image and wait for a keypress
    # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
    # cv2.destroyWindow("Image")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;

    img_height = int(0)
    img_width = int(0)
    if len(imageData) > 0:
        # 獲取圖像的高度和寬度：
        # print(imageData.shape)
        img_height, img_width, img_dimension = imageData.shape
        # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;
    #     # 遍歷每個像素：
    #     for i in range(img_height):
    #         for j in range(img_width):
    #             pixel_value = imageData[i, j]  # 在這個示例中：self.imageData[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
    #             print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))
    # print("Image height:", str(img_height))
    # print("Image width:", str(img_width))
    grayImageData = cv2.cvtColor(imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式，函數：cv2.cvtColor() 用於將圖像從一種顔色空間轉換爲另一種顔色空間 GrayScale Conversion for the Canny Algorithm;
    # binaryImageData = cv2.threshold(grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 或者 cv2.threshold(grayImageData, 127, 255, cv2.THRESH_BINARY_INV)  # 過濾轉化爲二值化（非黑即白）的圖片;
    # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
    # self.binaryImageData = cv2.ximgproc.thinning(self.binaryImageData, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;

    response_data_JSON = {}
    response_data_String = ""

    # purpose = "tableRecognition"  # "tableRecognition", "lineMeasuring"
    # # os.path.abspath(".")  # 獲取當前文檔所在的絕對路徑;
    # # os.path.abspath("..")  # 獲取當前文檔所在目錄的上一層路徑;
    # # input_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
    # input_dir = os.path.join(os.path.abspath(".."), "/inputTest/")  # "D:\\inputTest\\"，"../inputTest/" 需要注意目錄操作權限，用於輸入傳值的媒介目錄;
    # # input_dir = pathlib.Path(os.path.abspath("..") + "/inputTest/")  # pathlib.Path("../inputTest/")
    # imageUrl = ""  # "http://www.tabel.jpg" 待識別檢測的圖片的 Web 請求網址 URL 字符串;
    # # response = urllib_request.urlopen(imageUrl)  # 使用 Python 語言的原生模組「urllib」中的「request」中的「urlopen()」函數向服務器請求下載圖片數據;
    # # img_array = np.array(bytearray(response.read()), dtype = np.uint8)  # 把從服務器下載的圖片數據轉換爲二進位 8 位字節數組的形式;
    # # imageData = cv2.imdecode(img_array, -1)  # 使用 Python 語言的第三方擴展模組「opencv」中的「cv2.imdecode()」函數解析二進位 8 位字節數組形式的图片數據，RGB 模式;
    # imagePath = "C:/Criss/OCR-Measuring-Scale/src/inputTest/tabel.jpg"  # "./inputTest/tabel.jpg" 待識別檢測的圖片的硬盤保存位置路徑字符串;
    # imageData = []  # cv2.imread(self.imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
    # img_height = int(0)
    # img_width = int(0)
    # # if len(imageData) > 0:
    # #     # 獲取圖像的高度和寬度：
    # #     # print(imageData.shape)
    # #     img_height, img_width, img_dimension = imageData.shape
    # #     # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;
    # #     # # 遍歷每個像素：
    # #     # for i in range(img_height):
    # #     #     for j in range(img_width):
    # #     #         pixel_value = img[i, j]  # 在這個示例中：img[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
    # #     #         print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))
    # # print("Image height:", str(img_height))
    # # print("Image width:", str(img_width))
    # grayImageData = []  # cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
    # # binaryImageData = [],  # cv2.threshold(grayImageData, 127, 255, cv2.THRESH_BINARY_INV)  # 使用自定義閾值：「127」，過濾轉化爲二值化（非黑即白）的圖片;
    # binaryImageData = []  # cv2.threshold(grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
    # # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
    # # binaryImageData = cv2.ximgproc.thinning(binaryImageData, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;
    # HorizontalLineDetect = "Hough"  # "PixelDifference"
    # VerticalLineDetect = "Hough"  # "PixelDifference"
    # Canny_threshold1 = int(30)  # cv2.Canny()：第一次閾值；
    # Canny_threshold2 = int(240)  # cv2.Canny()：第二次閾值；
    # Canny_apertureSize = int(3)  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
    # Canny_L2gradient = bool(False)  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
    # HoughLinesP_rho = int(1)  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
    # HoughLinesP_theta = float(np.pi/180)  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
    # HoughLinesP_threshold = int(100)  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
    # HoughLinesP_minLineLength = int(150)  # int(200)  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
    # HoughLinesP_maxLineGap = int(15)  # int(15)  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
    tableRecognition_HorizontalLineDetect_Canny_threshold1 = int(30)
    tableRecognition_HorizontalLineDetect_Canny_threshold2 = int(240)
    tableRecognition_HorizontalLineDetect_Canny_apertureSize = int(3)
    tableRecognition_HorizontalLineDetect_Canny_L2gradient = bool(False)
    tableRecognition_HorizontalLineDetect_HoughLinesP_rho = int(1)
    tableRecognition_HorizontalLineDetect_HoughLinesP_theta = float(np.pi/180)
    tableRecognition_HorizontalLineDetect_HoughLinesP_threshold = int(100)
    tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength = int(150)
    tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap = int(15)
    tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope = float(10)  # float(5)  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
    tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept = float(10)  # float(5)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
    tableRecognition_VerticalLineDetect_Canny_threshold1 = int(30)
    tableRecognition_VerticalLineDetect_Canny_threshold2 = int(240)
    tableRecognition_VerticalLineDetect_Canny_apertureSize = int(3)
    tableRecognition_VerticalLineDetect_Canny_L2gradient = bool(False)
    tableRecognition_VerticalLineDetect_HoughLinesP_rho = int(1)
    tableRecognition_VerticalLineDetect_HoughLinesP_theta = float(np.pi/180)
    tableRecognition_VerticalLineDetect_HoughLinesP_threshold = int(100)
    tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength = int(150)
    tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap = int(15)
    tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope = float(10)  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
    tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept = float(10)  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
    tableRecognition_Cell_Top_embedded = int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
    tableRecognition_Cell_Bottom_embedded = int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
    tableRecognition_Cell_Left_embedded = int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
    tableRecognition_Cell_Right_embedded = int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
    lineMeasuring_HorizontalLineDetect_Canny_threshold1 = int(30)
    lineMeasuring_HorizontalLineDetect_Canny_threshold2 = int(240)
    lineMeasuring_HorizontalLineDetect_Canny_apertureSize = int(3)
    lineMeasuring_HorizontalLineDetect_Canny_L2gradient = bool(False)
    lineMeasuring_HorizontalLineDetect_HoughLinesP_rho = int(1)
    lineMeasuring_HorizontalLineDetect_HoughLinesP_theta = float(np.pi/180)
    lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold = int(100)
    lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength = int(100)
    lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap = int(10)
    lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope = float(10)  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
    lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept = float(10)  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
    lineMeasuring_VerticalLineDetect_Canny_threshold1 = int(30)
    lineMeasuring_VerticalLineDetect_Canny_threshold2 = int(240)
    lineMeasuring_VerticalLineDetect_Canny_apertureSize = int(3)
    lineMeasuring_VerticalLineDetect_Canny_L2gradient = bool(False)
    lineMeasuring_VerticalLineDetect_HoughLinesP_rho = int(1)
    lineMeasuring_VerticalLineDetect_HoughLinesP_theta = float(np.pi/180)
    lineMeasuring_VerticalLineDetect_HoughLinesP_threshold = int(20)
    lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength = int(15)
    lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap = int(10)
    lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope = float(10)  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
    lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept = float(10)  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
    lineMeasuring_Cell_Top_extension = int(-45)  # 截取圖片單元區域的上邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
    lineMeasuring_Cell_Left_extension = int(-90)  # 截取圖片單元區域的左邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
    lineMeasuring_Cell_Bottom_extension = int(0)  # 截取圖片單元區域的下邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
    lineMeasuring_Cell_Right_extension = int(90)  # 截取圖片單元區域的右邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
    lineMeasuring_Cell_Top_embedded = int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
    lineMeasuring_Cell_Bottom_embedded = int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
    lineMeasuring_Cell_Left_embedded = int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
    lineMeasuring_Cell_Right_embedded = int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
    CV_parameter = {
        # "HorizontalLineDetect": HorizontalLineDetect,  # "Hough", "PixelDifference";
        # "VerticalLineDetect": VerticalLineDetect,  # "Hough", "PixelDifference";
        # "Canny_threshold1": Canny_threshold1,  # = int(30)  # cv2.Canny()：第一次閾值；
        # "Canny_threshold2": Canny_threshold2,  # = int(240)  # cv2.Canny()：第二次閾值；
        # "Canny_apertureSize": Canny_apertureSize,  # = int(3)  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        # "Canny_L2gradient": Canny_L2gradient,  # = bool(False)  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        # "HoughLinesP_rho": HoughLinesP_rho,  # = int(1)  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        # "HoughLinesP_theta": HoughLinesP_theta,  # = float(np.pi/180)  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        # "HoughLinesP_threshold": HoughLinesP_threshold,  # = int(100)  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        # "HoughLinesP_minLineLength": HoughLinesP_minLineLength,  # = int(50)  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        # "HoughLinesP_maxLineGap": HoughLinesP_maxLineGap,  # = int(10)  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        "tableRecognition_HorizontalLineDetect_Canny_threshold1": tableRecognition_HorizontalLineDetect_Canny_threshold1,
        "tableRecognition_HorizontalLineDetect_Canny_threshold2": tableRecognition_HorizontalLineDetect_Canny_threshold2,
        "tableRecognition_HorizontalLineDetect_Canny_apertureSize": tableRecognition_HorizontalLineDetect_Canny_apertureSize,
        "tableRecognition_HorizontalLineDetect_Canny_L2gradient": tableRecognition_HorizontalLineDetect_Canny_L2gradient,
        "tableRecognition_HorizontalLineDetect_HoughLinesP_rho": tableRecognition_HorizontalLineDetect_HoughLinesP_rho,
        "tableRecognition_HorizontalLineDetect_HoughLinesP_theta": tableRecognition_HorizontalLineDetect_HoughLinesP_theta,
        "tableRecognition_HorizontalLineDetect_HoughLinesP_threshold": tableRecognition_HorizontalLineDetect_HoughLinesP_threshold,
        "tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength": tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength,
        "tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap": tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap,
        "tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope": tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5)  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        "tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept": tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        "tableRecognition_VerticalLineDetect_Canny_threshold1": tableRecognition_VerticalLineDetect_Canny_threshold1,
        "tableRecognition_VerticalLineDetect_Canny_threshold2": tableRecognition_VerticalLineDetect_Canny_threshold2,
        "tableRecognition_VerticalLineDetect_Canny_apertureSize": tableRecognition_VerticalLineDetect_Canny_apertureSize,
        "tableRecognition_VerticalLineDetect_Canny_L2gradient": tableRecognition_VerticalLineDetect_Canny_L2gradient,
        "tableRecognition_VerticalLineDetect_HoughLinesP_rho": tableRecognition_VerticalLineDetect_HoughLinesP_rho,
        "tableRecognition_VerticalLineDetect_HoughLinesP_theta": tableRecognition_VerticalLineDetect_HoughLinesP_theta,
        "tableRecognition_VerticalLineDetect_HoughLinesP_threshold": tableRecognition_VerticalLineDetect_HoughLinesP_threshold,
        "tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength": tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength,
        "tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap": tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap,
        "tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope": tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        "tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept": tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        "tableRecognition_Cell_Top_embedded": tableRecognition_Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        "tableRecognition_Cell_Bottom_embedded": tableRecognition_Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        "tableRecognition_Cell_Left_embedded": tableRecognition_Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        "tableRecognition_Cell_Right_embedded": tableRecognition_Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        "lineMeasuring_HorizontalLineDetect_Canny_threshold1": lineMeasuring_HorizontalLineDetect_Canny_threshold1,
        "lineMeasuring_HorizontalLineDetect_Canny_threshold2": lineMeasuring_HorizontalLineDetect_Canny_threshold2,
        "lineMeasuring_HorizontalLineDetect_Canny_apertureSize": lineMeasuring_HorizontalLineDetect_Canny_apertureSize,
        "lineMeasuring_HorizontalLineDetect_Canny_L2gradient": lineMeasuring_HorizontalLineDetect_Canny_L2gradient,
        "lineMeasuring_HorizontalLineDetect_HoughLinesP_rho": lineMeasuring_HorizontalLineDetect_HoughLinesP_rho,
        "lineMeasuring_HorizontalLineDetect_HoughLinesP_theta": lineMeasuring_HorizontalLineDetect_HoughLinesP_theta,
        "lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold": lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold,
        "lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength": lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength,
        "lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap": lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap,
        "lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope": lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        "lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept": lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        "lineMeasuring_VerticalLineDetect_Canny_threshold1": lineMeasuring_VerticalLineDetect_Canny_threshold1,
        "lineMeasuring_VerticalLineDetect_Canny_threshold2": lineMeasuring_VerticalLineDetect_Canny_threshold2,
        "lineMeasuring_VerticalLineDetect_Canny_apertureSize": lineMeasuring_VerticalLineDetect_Canny_apertureSize,
        "lineMeasuring_VerticalLineDetect_Canny_L2gradient": lineMeasuring_VerticalLineDetect_Canny_L2gradient,
        "lineMeasuring_VerticalLineDetect_HoughLinesP_rho": lineMeasuring_VerticalLineDetect_HoughLinesP_rho,
        "lineMeasuring_VerticalLineDetect_HoughLinesP_theta": lineMeasuring_VerticalLineDetect_HoughLinesP_theta,
        "lineMeasuring_VerticalLineDetect_HoughLinesP_threshold": lineMeasuring_VerticalLineDetect_HoughLinesP_threshold,
        "lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength": lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength,
        "lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap": lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap,
        "lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope": lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        "lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept": lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        "lineMeasuring_Cell_Top_extension": lineMeasuring_Cell_Top_extension,  # int(-45)  # 截取圖片單元區域的上邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        "lineMeasuring_Cell_Left_extension": lineMeasuring_Cell_Left_extension,  # int(-90)  # 截取圖片單元區域的左邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        "lineMeasuring_Cell_Bottom_extension": lineMeasuring_Cell_Bottom_extension,  # int(0)  # 截取圖片單元區域的下邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        "lineMeasuring_Cell_Right_extension": lineMeasuring_Cell_Right_extension,  # int(90)  # 截取圖片單元區域的右邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        "lineMeasuring_Cell_Top_embedded": lineMeasuring_Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        "lineMeasuring_Cell_Bottom_embedded": lineMeasuring_Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        "lineMeasuring_Cell_Left_embedded": lineMeasuring_Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        "lineMeasuring_Cell_Right_embedded": lineMeasuring_Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
    }
    save_image = False  # True
    OCRmethod = "teressact"
    # # tesseract_cmd = r'C:/Criss/OCR-Measuring-Scale/Tesseract-OCR/tesseract' # str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
    # tesseract_cmd = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tesseract")).replace('\\', '/')
    # # tesseract_cmd = str(pathlib.Path(os.path.abspath("..") + "/Tesseract-OCR/" + "/tesseract/"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
    # os.path.abspath(".")  # 獲取當前文檔所在的絕對路徑;
    # os.path.abspath("..")  # 獲取當前文檔所在目錄的上一層路徑;
    # pytesseract.pytesseract.tesseract_cmd = tesseract_cmd  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
    tesseract_lang = 'chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選多語言混合識別，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
    global tesseract_config
    # tesseract_config = '--psm 3 --oem 3'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    tesseract_output_type = "pytesseract.Output.STRING"  # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
    # tesseract_timeout = int(0)  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
    # tesseract_tessdata_dir = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tessdata", "chi_tra.traineddata")).replace('\\', '/')  # "/usr/share/tessdata" # File PATH：用戶自定義指定本地訓練完畢的數據集文檔（tessdata）的儲存路徑位置，使用 Tesseract 識別，需要使用訓練好的數據集，如果不指定該參數，則預設使用系統預設的數據集文檔目錄 Specify the location of tessdata path.
    # tesseract_user_words = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tesswords")).replace('\\', '/')  # File PATH：用戶自定義指定的詞庫（字典）文檔的存儲位置，用戶字典可以包含一些特定的詞匯，以提高對特定詞匯的識別準確性，用戶字典文件應爲純文本文檔，每行一個詞匯 Specify the location of user words file.
    # tesseract_user_patterns = ""  # File PATH：用戶自定義指定的特定格式文本的文檔的存儲位置，即每行使用「某種正則表達式」，例如，正在掃描具有相同格式數據的多張頁面，即可使用此參數，特定格式文本的文檔應爲純文本文檔，每行一個正則表達式模式 Specify the location of user patterns file.
    OCR_parameter = {
        "OCRmethod": OCRmethod,  # "teressact"
        "tesseract_cmd": tesseract_cmd,  # # r'C:/Tesseract-OCR/tesseract.exe'
        "tesseract_lang": tesseract_lang,  # 'chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'
        "tesseract_config": tesseract_config,  # '--psm 3 --oem 3'
        "tesseract_output_type": tesseract_output_type,  # "pytesseract.Output.STRING"
        "tesseract_timeout": tesseract_timeout,  # int(0)
        "tesseract_tessdata_dir": tesseract_tessdata_dir,
        "tesseract_user_words": tesseract_user_words,
        "tesseract_user_patterns":tesseract_user_patterns
    }
    # do_Function = lambda x:x
    # is_Window = False  # 判斷是否有開啓圖形交互介面，可取值為：True、False;
    # is_Monitor_Concurrent = "Multi-Threading"  # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程），可取值為：0、"0"、"Multi-Threading"、"Multi-Processes";
    # number_Worker_process = int(4)  # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
    # time_sleep = float(0.02)  # 用於監聽程序的輪詢延遲參數，單位（秒）;

    # pid = multiprocessing.current_process().pid, threading.currentThread().ident;
    OCR_Image_to_Characters = ComputerVision(
        # purpose = purpose,  # "tableRecognition", "lineMeasuring"
        # input_dir = input_dir,  # os.path.join(os.path.abspath(".."), "/inputTest/")  # "D:\\inputTest\\"，"../inputTest/" 需要注意目錄操作權限，用於輸入傳值的媒介目錄;
        # imageUrl = imageUrl,  # "http://www.tabel.jpg" 待識別檢測的圖片的 Web 請求網址 URL 字符串;
        # imagePath = imagePath,  # "./inputTest/tabel.jpg" 待識別檢測的圖片的硬盤保存位置路徑字符串;
        # imageData = imageData,  # [],  # cv2.imread(self.imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
        # img_height = img_height,
        # img_width = img_width,
        # grayImageData = grayImageData,  # [],  # cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
        # binaryImageData = binaryImageData,  # [],  # cv2.threshold(grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
        # HorizontalLineDetect = HorizontalLineDetect,  # "Hough", "PixelDifference";
        # VerticalLineDetect = VerticalLineDetect,  # "Hough", "PixelDifference";
        # Canny_threshold1 = Canny_threshold1,  # int(30)  # cv2.Canny()：第一次閾值；
        # Canny_threshold2 = Canny_threshold2,  # int(240)  # cv2.Canny()：第二次閾值；
        # Canny_apertureSize = Canny_apertureSize,  # int(3)  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        # Canny_L2gradient = Canny_L2gradient,  # bool(False)  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        # HoughLinesP_rho = HoughLinesP_rho,  # int(1)  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        # HoughLinesP_theta = HoughLinesP_theta,  # float(np.pi/180)  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        # HoughLinesP_threshold = HoughLinesP_threshold,  # int(100)  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        # HoughLinesP_minLineLength = HoughLinesP_minLineLength,  # int(50)  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        # HoughLinesP_maxLineGap = HoughLinesP_maxLineGap,  # int(10)  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        tableRecognition_HorizontalLineDetect_Canny_threshold1 = tableRecognition_HorizontalLineDetect_Canny_threshold1,
        tableRecognition_HorizontalLineDetect_Canny_threshold2 = tableRecognition_HorizontalLineDetect_Canny_threshold2,
        tableRecognition_HorizontalLineDetect_Canny_apertureSize = tableRecognition_HorizontalLineDetect_Canny_apertureSize,
        tableRecognition_HorizontalLineDetect_Canny_L2gradient = tableRecognition_HorizontalLineDetect_Canny_L2gradient,
        tableRecognition_HorizontalLineDetect_HoughLinesP_rho = tableRecognition_HorizontalLineDetect_HoughLinesP_rho,
        tableRecognition_HorizontalLineDetect_HoughLinesP_theta = tableRecognition_HorizontalLineDetect_HoughLinesP_theta,
        tableRecognition_HorizontalLineDetect_HoughLinesP_threshold = tableRecognition_HorizontalLineDetect_HoughLinesP_threshold,
        tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength = tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength,
        tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap = tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap,
        tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope = tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5)  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept = tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        tableRecognition_VerticalLineDetect_Canny_threshold1 = tableRecognition_VerticalLineDetect_Canny_threshold1,
        tableRecognition_VerticalLineDetect_Canny_threshold2 = tableRecognition_VerticalLineDetect_Canny_threshold2,
        tableRecognition_VerticalLineDetect_Canny_apertureSize = tableRecognition_VerticalLineDetect_Canny_apertureSize,
        tableRecognition_VerticalLineDetect_Canny_L2gradient = tableRecognition_VerticalLineDetect_Canny_L2gradient,
        tableRecognition_VerticalLineDetect_HoughLinesP_rho = tableRecognition_VerticalLineDetect_HoughLinesP_rho,
        tableRecognition_VerticalLineDetect_HoughLinesP_theta = tableRecognition_VerticalLineDetect_HoughLinesP_theta,
        tableRecognition_VerticalLineDetect_HoughLinesP_threshold = tableRecognition_VerticalLineDetect_HoughLinesP_threshold,
        tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength = tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength,
        tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap = tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap,
        tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope = tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept = tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        tableRecognition_Cell_Top_embedded = tableRecognition_Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        tableRecognition_Cell_Bottom_embedded = tableRecognition_Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        tableRecognition_Cell_Left_embedded = tableRecognition_Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        tableRecognition_Cell_Right_embedded = tableRecognition_Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        lineMeasuring_HorizontalLineDetect_Canny_threshold1 = lineMeasuring_HorizontalLineDetect_Canny_threshold1,
        lineMeasuring_HorizontalLineDetect_Canny_threshold2 = lineMeasuring_HorizontalLineDetect_Canny_threshold2,
        lineMeasuring_HorizontalLineDetect_Canny_apertureSize = lineMeasuring_HorizontalLineDetect_Canny_apertureSize,
        lineMeasuring_HorizontalLineDetect_Canny_L2gradient = lineMeasuring_HorizontalLineDetect_Canny_L2gradient,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_rho = lineMeasuring_HorizontalLineDetect_HoughLinesP_rho,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_theta = lineMeasuring_HorizontalLineDetect_HoughLinesP_theta,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold = lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength = lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap = lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap,
        lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope = lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept = lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        lineMeasuring_VerticalLineDetect_Canny_threshold1 = lineMeasuring_VerticalLineDetect_Canny_threshold1,
        lineMeasuring_VerticalLineDetect_Canny_threshold2 = lineMeasuring_VerticalLineDetect_Canny_threshold2,
        lineMeasuring_VerticalLineDetect_Canny_apertureSize = lineMeasuring_VerticalLineDetect_Canny_apertureSize,
        lineMeasuring_VerticalLineDetect_Canny_L2gradient = lineMeasuring_VerticalLineDetect_Canny_L2gradient,
        lineMeasuring_VerticalLineDetect_HoughLinesP_rho = lineMeasuring_VerticalLineDetect_HoughLinesP_rho,
        lineMeasuring_VerticalLineDetect_HoughLinesP_theta = lineMeasuring_VerticalLineDetect_HoughLinesP_theta,
        lineMeasuring_VerticalLineDetect_HoughLinesP_threshold = lineMeasuring_VerticalLineDetect_HoughLinesP_threshold,
        lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength = lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength,
        lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap = lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap,
        lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope = lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept = lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        lineMeasuring_Cell_Top_extension = lineMeasuring_Cell_Top_extension,  # int(-45)  # 截取圖片單元區域的上邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Left_extension = lineMeasuring_Cell_Left_extension,  # int(-90)  # 截取圖片單元區域的左邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Bottom_extension = lineMeasuring_Cell_Bottom_extension,  # int(0)  # 截取圖片單元區域的下邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Right_extension = lineMeasuring_Cell_Right_extension,  # int(90)  # 截取圖片單元區域的右邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Top_embedded = lineMeasuring_Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        lineMeasuring_Cell_Bottom_embedded = lineMeasuring_Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        lineMeasuring_Cell_Left_embedded = lineMeasuring_Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        lineMeasuring_Cell_Right_embedded = lineMeasuring_Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        CV_parameter = CV_parameter,
        save_image = save_image,  # False, True
        OCRmethod = OCRmethod,  # "teressact"
        tesseract_cmd = tesseract_cmd,  # str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
        tesseract_lang = tesseract_lang,  # 'chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選多語言混合識別，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
        tesseract_config = tesseract_config,  # '--psm 3 --oem 3'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        tesseract_output_type = tesseract_output_type,  # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
        tesseract_timeout = tesseract_timeout,  # int(0)  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
        tesseract_tessdata_dir = tesseract_tessdata_dir,  # "/usr/share/tessdata" # File PATH：用戶自定義指定本地訓練完畢的數據集文檔（tessdata）的儲存路徑位置，使用 Tesseract 識別，需要使用訓練好的數據集，如果不指定該參數，則預設使用系統預設的數據集文檔目錄 Specify the location of tessdata path.
        tesseract_user_words = tesseract_user_words,  # File PATH：用戶自定義指定的詞庫（字典）文檔的存儲位置，用戶字典可以包含一些特定的詞匯，以提高對特定詞匯的識別準確性，用戶字典文件應爲純文本文檔，每行一個詞匯 Specify the location of user words file.
        tesseract_user_patterns = tesseract_user_patterns,  # File PATH：用戶自定義指定的特定格式文本的文檔的存儲位置，即每行使用「某種正則表達式」，例如，正在掃描具有相同格式數據的多張頁面，即可使用此參數，特定格式文本的文檔應爲純文本文檔，每行一個正則表達式模式 Specify the location of user patterns file.
        OCR_parameter = OCR_parameter,
        # do_Function = do_Function,  # lambda x:x
        # is_Window = is_Window,  # 判斷是否有開啓圖形交互介面，可取值為：True、False;
        # is_Monitor_Concurrent = is_Monitor_Concurrent,  # "Multi-Threading"  # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程），可取值為：0、"0"、"Multi-Threading"、"Multi-Processes";
        # number_Worker_process = number_Worker_process,  # int(4)  # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
        # time_sleep = time_sleep  # float(0.02)  # 用於監聽程序的輪詢延遲參數，單位（秒）;
    )
    # OCR_Image_to_Characters = ComputerVision()

    # edges = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])
    # 其中參數：
    # image：待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）；
    # threshold1：第一次閾值；
    # threshold2：第二次閾值；
    # apertureSize：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
    # L2gradient：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
    # 函數返回值是一個輸出圖像，與輸入圖像大小及類型相同。
    # 函數「cv2.canny()」的實現原理主要基於以下幾個步驟：
    # Step 1：圖像灰度化。首先將輸入圖像轉換爲單通道的灰度圖像，可以通過函數「cv2.cvtColor」函數來完成。
    # Step 2：邊緣強度梯度計算。使用索伯爾運算元（Sobel）（算子）計算每個圖元（pixel）（像素）點在水平和垂直方向上的梯度值，並通過勾股定理（Pythagorean theorem）計算梯度幅值和方向。
    # Step 3：非極大值抑制。爲了減少邊緣（輪廓）圖元（pixel）（像素）數量，需要對梯度圖像中的強度值進行非極大值抑制，即只保留局部最大值點。
    # Step 4：滯後閾值處理。根據設定的閾值大小，將梯度幅值大於閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）。接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點也標記爲邊緣（輪廓）點。
    # Step 5：輸出邊緣（輪廓）圖像。最後將所有被標記爲邊緣（輪廓）的圖元（pixel）（像素）點輸出爲邊緣（輪廓）圖像。

    # 使用第三方庫「OpenCV」中的函數「cv2.Canny()」做圖形邊緣（輪廓）檢測，並將邊緣（輪廓）標記為白色圖元（pixel）（像素），黑色圖元（pixel）（像素）則表示非邊緣（輪廓）;
    Canny_threshold1 = int(30)  # cv2.Canny()：第一次閾值；
    Canny_threshold2 = int(240)  # cv2.Canny()：第二次閾值；
    Canny_apertureSize = int(3)  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
    Canny_L2gradient = bool(False)  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；

    edges = cv2.Canny(
        grayImageData,  # 待檢測的圖元（pixel）（像素）圖像，必須爲單通道8位或32位元浮點型圖元（pixel）（像素）;
        Canny_threshold1,  # 30,  # 第一次閾值，將梯度幅值大於第一次閾值的圖元（pixel）（像素）點劃分爲強邊緣（輪廓），小於閾值的圖元（pixel）（像素）點劃分爲弱邊緣（輪廓）或非邊緣（輪廓）;
        Canny_threshold2,  # 240,  # 第二次閾值，接著對弱邊緣（輪廓）進行處理，將與強邊緣（輪廓）相連的弱邊緣（輪廓）圖元（pixel）（像素）點，梯度幅值大於第二次閾值的，也標記爲邊緣（輪廓）點;
        apertureSize = Canny_apertureSize,  # 3,  # 用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3;
        L2gradient = Canny_L2gradient  # False  # 計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法;
    )

    # 第三方庫「OpenCV」中，有兩種算法檢測直缐或缐段，即「cv2.HoughLines()」標準霍夫缐變換「Hough Transform」和「cv2.HoughLinesP()」概率霍夫缐變換「Probabilistic Hough Transform」;
    # 標準霍夫缐變換「Hough Transform」函數「cv2.HoughLines()」返回值爲直綫的方程，即檢測結果爲「直綫」;
    # lines = cv2.HoughLines(image, rho, theta, threshold)
    # 概率霍夫缐變換「Probabilistic Hough Transform」函數「cv2.HoughLinesP()」返回值爲缐段起點與終點的座標值列表，即檢測結果爲「缐段」;
    # lines = cv2.HoughLinesP(image, rho, theta, threshold, minLineLength=None, maxLineGap=None)
    # 其中參數：
    # image：待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測；
    # rho：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
    # theta：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
    # threshold：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
    # minLineLength：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
    # maxLineGap：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
    # 函數返回值是一個三維陣列，其中每個元素表示一條直線，格式爲列表：(x1, y1, x2, y2），表示直線的兩個端點座標。

    # 使用第三方庫「OpenCV」中的函數「cv2.HoughLinesP()」概率霍夫變換「Probabilistic Hough Transform」演算法識別圖片（Image）表格（Table）中的橫向分隔缐段;
    HoughLinesP_rho = int(1)  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
    HoughLinesP_theta = float(np.pi/180)  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
    HoughLinesP_threshold = int(100)  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
    HoughLinesP_minLineLength = int(150)  # int(200)  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
    HoughLinesP_maxLineGap = int(15)  # int(15)  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。

    lines = cv2.HoughLinesP(
        edges,  # 待識別的二值化圖像，可以事先使用第三方庫「OpenCV」中的函數「cv2.Canny()」進行邊緣（輪廓）檢測;
        HoughLinesP_rho,  # 1,  # 距離解析度（分辨率），單位爲：圖元（pixel）（像素）;
        HoughLinesP_theta,  # np.pi/180,  # 角度解析度（分辨率），單位爲：弧度;
        HoughLinesP_threshold,  # 100,  # 閾值參數，只有累加器中的值高於閾值才會被認為是一條直線;
        minLineLength = HoughLinesP_minLineLength,  # 要求識別的缐段最小長度值（單位：圖元 pixel 也稱像素），比這個長度值小的缐段將會被忽略，自定義設定爲：500 個圖元;
        maxLineGap = HoughLinesP_maxLineGap  # 要求識別的線段之間的最大間隔上限值（單位：圖元 pixel 也稱像素），小於這個間隔上限值的缐段將被連接爲一條直綫，自定義設定爲：30 個圖元;
    ).tolist()
    # lines.append([[13, 102, 756, 102]])  # 可以追加畫出一條自定義位置的橫向缐段;
    sorted_lines = sorted(lines, key=lambda x: x[0])

    horizontal_lines = []  # 存儲在圖像表格（Table）中檢測到的橫向分隔缐段座標的列表;
    for line in sorted_lines:
        for x1, y1, x2, y2 in line:
            if y1 == y2:
                # print(line)
                horizontal_lines.append([x1, y1, x2, y2])  # 存儲在圖像表格（Table）中檢測到的橫向分隔缐段座標;
                # cv2.line(self.image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 在源圖像上繪製識別出的表格（Table）橫向分隔缐段;
    # print("Horizontal Lines:\n", horizontal_lines)
    # # 在源圖像上繪製所有識別出的表格（Table）橫向分隔缐段;
    # for line in horizontal_lines:
    #     for x1, y1, x2, y2 in line:
    #         if y1 == y2:
    #             # print(line)
    #             cv2.line(self.image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 在源圖像上繪製識別出的表格（Table）橫向分隔缐段;

    # 判斷是否一條都沒有識別出橫向分隔缐段;
    if len(horizontal_lines) == 0:
        print('horizontal lines not detected.')
        return response_data_String

    overlappingFilterThreshold_Slope = float(10)  # float(5)  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
    overlappingFilterThreshold_Intercept = float(10)  # float(5)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;

    # 刪除重複（圖片中的綫條比較寬，誤識別爲兩條較細的綫條）的橫向分隔缐段;
    horizontal_lines = OverlappingFilter(
        horizontal_lines,
        separationThresholdSlope = overlappingFilterThreshold_Slope,  # float(5)  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        separationThresholdIntercept = overlappingFilterThreshold_Intercept  # float(5)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
    )
    # print("Horizontal Lines:\n", horizontal_lines)

    # 篩選最長的橫向分隔缐段，用於分割圖片爲上下兩個區域;
    longest = float(0)
    longest_line = []
    for line in horizontal_lines:
        x1 = line[0]
        y1 = line[1]
        x2 = line[2]
        y2 = line[3]
        length_line = math.sqrt(math.pow(float(float(y2) - float(y1)), 2) + math.pow(float(float(x2) - float(x1)), 2))
        if float(length_line) > float(longest):
            longest = float(length_line)
            longest_line = line
    # print("Longest horizontal line:\n", longest_line)
    # print("Longest:", longest)

    # # 用於調試 #########################################################################
    # # 在源圖像上繪製識別出的最長的橫向分隔缐段;
    # x1 = int(0)  # longest_line[0]
    # y1 = longest_line[1]
    # x2 = int(int(img_width) - int(1))  # longest_line[2]
    # y2 = longest_line[3]
    # # print(x1, y1, x2, y2)
    # cv2.line(imageData, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 在源圖像上繪製識別出的表格（Table）橫向分隔缐段;
    # # 顯示圖片;
    # cv2.namedWindow("longestLineImage")  # 創建圖片展示窗口;
    # cv2.imshow("longestLineImage", imageData)  # 顯示圖片 display the image and wait for a keypress
    # # key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;
    # # if key == 27:
    # #     break
    # # # 回車鍵（Enter）的 ASCII 碼爲：ord('\n') == 13
    # # # 空格鍵的 ASCII 碼爲：ord(' ')
    # # # Tab 鍵的 ASCII 碼爲：ord('\t')
    # # # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
    # # # 換行鍵的 ASCII 碼爲：ord('\r')
    # # # Esc 鍵的 ASCII 碼爲：ord('\x1b') == 27
    # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
    # # cv2.destroyAllWindows()  # 關閉所有窗口 closing all open windows
    # cv2.destroyWindow("longestLineImage")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;
    # # 用於調試 #########################################################################

    Table_Top_embedded = int(0)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
    Table_Bottom_embedded = int(5)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
    Table_Left_embedded = int(0)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
    Table_Right_embedded = int(0)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
    # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
    X1 = int(int(0) + Table_Top_embedded)
    Y1 = int(int(0) + Table_Left_embedded)
    X2 = int(int(longest_line[3]) - Table_Bottom_embedded)
    Y2 = int(int(int(img_width) - int(1)) - Table_Right_embedded)
    imageData_Table = imageData[X1:X2, Y1:Y2]

    # # 用於調試 #########################################################################
    # # 在名稱爲 "TableImage" 的窗口中顯示截取出的表格（Table）圖片（Image）;
    # cv2.namedWindow("TableImage")  # 創建圖片展示窗口;
    # cv2.imshow("TableImage", imageData_Table)  # 顯示圖片 display the image and wait for a keypress
    # # key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;
    # # if key == 27:
    # #     break
    # # # 回車鍵（Enter）的 ASCII 碼爲：ord('\n') == 13
    # # # 空格鍵的 ASCII 碼爲：ord(' ')
    # # # Tab 鍵的 ASCII 碼爲：ord('\t')
    # # # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
    # # # 換行鍵的 ASCII 碼爲：ord('\r')
    # # # Esc 鍵的 ASCII 碼爲：ord('\x1b') == 27
    # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
    # # cv2.destroyAllWindows()  # 關閉所有窗口 closing all open windows
    # cv2.destroyWindow("TableImage")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;
    # # 用於調試 #########################################################################

    purpose = "tableRecognition"  # "tableRecognition", "lineMeasuring"
    # os.path.abspath(".")  # 獲取當前文檔所在的絕對路徑;
    # os.path.abspath("..")  # 獲取當前文檔所在目錄的上一層路徑;
    # input_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
    # input_dir = os.path.join(os.path.abspath(".."), "/inputTest/")  # "D:\\inputTest\\"，"../inputTest/" 需要注意目錄操作權限，用於輸入傳值的媒介目錄;
    # input_dir = pathlib.Path(os.path.abspath("..") + "/inputTest/")  # pathlib.Path("../inputTest/")
    # imageUrl = ""  # "http://www.tabel.jpg" 待識別檢測的圖片的 Web 請求網址 URL 字符串;
    # response = urllib_request.urlopen(imageUrl)  # 使用 Python 語言的原生模組「urllib」中的「request」中的「urlopen()」函數向服務器請求下載圖片數據;
    # img_array = np.array(bytearray(response.read()), dtype = np.uint8)  # 把從服務器下載的圖片數據轉換爲二進位 8 位字節數組的形式;
    # imageData = cv2.imdecode(img_array, -1)  # 使用 Python 語言的第三方擴展模組「opencv」中的「cv2.imdecode()」函數解析二進位 8 位字節數組形式的图片數據，RGB 模式;
    # imagePath = ""  # "C:/Criss/OCR-Measuring-Scale/src/inputTest/tabel.jpg"  # "./inputTest/tabel.jpg" 待識別檢測的圖片的硬盤保存位置路徑字符串;
    # imageData = imageData_Table  # cv2.imread(self.imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
    # img_height = int(0)
    # img_width = int(0)
    # if len(imageData) > 0:
    #     # 獲取圖像的高度和寬度：
    #     # print(imageData.shape)
    #     img_height, img_width, img_dimension = imageData.shape
    #     # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;
    #     # # 遍歷每個像素：
    #     # for i in range(img_height):
    #     #     for j in range(img_width):
    #     #         pixel_value = img[i, j]  # 在這個示例中：img[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
    #     #         print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))
    # print("Image height:", str(img_height))
    # print("Image width:", str(img_width))
    # grayImageData = []  # cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
    # binaryImageData = [],  # cv2.threshold(grayImageData, 127, 255, cv2.THRESH_BINARY_INV)  # 使用自定義閾值：「127」，過濾轉化爲二值化（非黑即白）的圖片;
    # binaryImageData = []  # cv2.threshold(grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
    # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
    # binaryImageData = cv2.ximgproc.thinning(binaryImageData, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;
    HorizontalLineDetect = "Hough"  # "PixelDifference"
    VerticalLineDetect = "Hough"  # "PixelDifference"
    tableRecognition_HorizontalLineDetect_Canny_threshold1 = int(30)
    tableRecognition_HorizontalLineDetect_Canny_threshold2 = int(240)
    tableRecognition_HorizontalLineDetect_Canny_apertureSize = int(3)
    tableRecognition_HorizontalLineDetect_Canny_L2gradient = bool(False)
    tableRecognition_HorizontalLineDetect_HoughLinesP_rho = int(1)
    tableRecognition_HorizontalLineDetect_HoughLinesP_theta = float(np.pi/180)
    tableRecognition_HorizontalLineDetect_HoughLinesP_threshold = int(100)
    tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength = int(150)
    tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap = int(15)
    tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope = float(10)  # float(5)  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
    tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept = float(10)  # float(5)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
    tableRecognition_VerticalLineDetect_Canny_threshold1 = int(30)
    tableRecognition_VerticalLineDetect_Canny_threshold2 = int(240)
    tableRecognition_VerticalLineDetect_Canny_apertureSize = int(3)
    tableRecognition_VerticalLineDetect_Canny_L2gradient = bool(False)
    tableRecognition_VerticalLineDetect_HoughLinesP_rho = int(1)
    tableRecognition_VerticalLineDetect_HoughLinesP_theta = float(np.pi/180)
    tableRecognition_VerticalLineDetect_HoughLinesP_threshold = int(100)
    tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength = int(150)
    tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap = int(15)
    tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope = float(10)  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
    tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept = float(10)  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
    tableRecognition_Cell_Top_embedded = int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
    tableRecognition_Cell_Bottom_embedded = int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
    tableRecognition_Cell_Left_embedded = int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
    tableRecognition_Cell_Right_embedded = int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
    global tabel_tesseract_config
    # tabel_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    # print("Input tabel tesseract config:", tabel_tesseract_config)

    result_Table = None
    # result_Table = OCR_Image_to_Characters.run()
    result_Table = OCR_Image_to_Characters.run(
        purpose = purpose,  # "tableRecognition", "lineMeasuring"
        # imageUrl = imageUrl,  # "http://www.tabel.jpg" 待識別檢測的圖片的 Web 請求網址 URL 字符串;
        # imagePath = imagePath,  # "./inputTest/tabel.jpg" 待識別檢測的圖片的硬盤保存位置路徑字符串;
        imageData = imageData_Table,  # [],  # cv2.imread(self.imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
        # img_height = img_height,
        # img_width = img_width,
        # grayImageData = grayImageData,  # [],  # cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
        # binaryImageData = binaryImageData,  # [],  # cv2.threshold(grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
        HorizontalLineDetect = HorizontalLineDetect,  # "Hough", "PixelDifference";
        VerticalLineDetect = VerticalLineDetect,  # "Hough", "PixelDifference";
        # Canny_threshold1 = Canny_threshold1,  # int(30)  # cv2.Canny()：第一次閾值；
        # Canny_threshold2 = Canny_threshold2,  # int(240)  # cv2.Canny()：第二次閾值；
        # Canny_apertureSize = Canny_apertureSize,  # int(3)  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        # Canny_L2gradient = Canny_L2gradient,  # bool(False)  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        # HoughLinesP_rho = HoughLinesP_rho,  # int(1)  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        # HoughLinesP_theta = HoughLinesP_theta,  # float(np.pi/180)  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        # HoughLinesP_threshold = HoughLinesP_threshold,  # int(100)  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        # HoughLinesP_minLineLength = HoughLinesP_minLineLength,  # int(50)  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        # HoughLinesP_maxLineGap = HoughLinesP_maxLineGap,  # int(10)  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        # CV_parameter = CV_parameter,
        tableRecognition_HorizontalLineDetect_Canny_threshold1 = tableRecognition_HorizontalLineDetect_Canny_threshold1,
        tableRecognition_HorizontalLineDetect_Canny_threshold2 = tableRecognition_HorizontalLineDetect_Canny_threshold2,
        tableRecognition_HorizontalLineDetect_Canny_apertureSize = tableRecognition_HorizontalLineDetect_Canny_apertureSize,
        tableRecognition_HorizontalLineDetect_Canny_L2gradient = tableRecognition_HorizontalLineDetect_Canny_L2gradient,
        tableRecognition_HorizontalLineDetect_HoughLinesP_rho = tableRecognition_HorizontalLineDetect_HoughLinesP_rho,
        tableRecognition_HorizontalLineDetect_HoughLinesP_theta = tableRecognition_HorizontalLineDetect_HoughLinesP_theta,
        tableRecognition_HorizontalLineDetect_HoughLinesP_threshold = tableRecognition_HorizontalLineDetect_HoughLinesP_threshold,
        tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength = tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength,
        tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap = tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap,
        tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope = tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5)  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept = tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        tableRecognition_VerticalLineDetect_Canny_threshold1 = tableRecognition_VerticalLineDetect_Canny_threshold1,
        tableRecognition_VerticalLineDetect_Canny_threshold2 = tableRecognition_VerticalLineDetect_Canny_threshold2,
        tableRecognition_VerticalLineDetect_Canny_apertureSize = tableRecognition_VerticalLineDetect_Canny_apertureSize,
        tableRecognition_VerticalLineDetect_Canny_L2gradient = tableRecognition_VerticalLineDetect_Canny_L2gradient,
        tableRecognition_VerticalLineDetect_HoughLinesP_rho = tableRecognition_VerticalLineDetect_HoughLinesP_rho,
        tableRecognition_VerticalLineDetect_HoughLinesP_theta = tableRecognition_VerticalLineDetect_HoughLinesP_theta,
        tableRecognition_VerticalLineDetect_HoughLinesP_threshold = tableRecognition_VerticalLineDetect_HoughLinesP_threshold,
        tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength = tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength,
        tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap = tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap,
        tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope = tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept = tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        tableRecognition_Cell_Top_embedded = tableRecognition_Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        tableRecognition_Cell_Bottom_embedded = tableRecognition_Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        tableRecognition_Cell_Left_embedded = tableRecognition_Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        tableRecognition_Cell_Right_embedded = tableRecognition_Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        # lineMeasuring_HorizontalLineDetect_Canny_threshold1 = lineMeasuring_HorizontalLineDetect_Canny_threshold1,
        # lineMeasuring_HorizontalLineDetect_Canny_threshold2 = lineMeasuring_HorizontalLineDetect_Canny_threshold2,
        # lineMeasuring_HorizontalLineDetect_Canny_apertureSize = lineMeasuring_HorizontalLineDetect_Canny_apertureSize,
        # lineMeasuring_HorizontalLineDetect_Canny_L2gradient = lineMeasuring_HorizontalLineDetect_Canny_L2gradient,
        # lineMeasuring_HorizontalLineDetect_HoughLinesP_rho = lineMeasuring_HorizontalLineDetect_HoughLinesP_rho,
        # lineMeasuring_HorizontalLineDetect_HoughLinesP_theta = lineMeasuring_HorizontalLineDetect_HoughLinesP_theta,
        # lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold = lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold,
        # lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength = lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength,
        # lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap = lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap,
        # lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope = lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        # lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept = lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        # lineMeasuring_VerticalLineDetect_Canny_threshold1 = lineMeasuring_VerticalLineDetect_Canny_threshold1,
        # lineMeasuring_VerticalLineDetect_Canny_threshold2 = lineMeasuring_VerticalLineDetect_Canny_threshold2,
        # lineMeasuring_VerticalLineDetect_Canny_apertureSize = lineMeasuring_VerticalLineDetect_Canny_apertureSize,
        # lineMeasuring_VerticalLineDetect_Canny_L2gradient = lineMeasuring_VerticalLineDetect_Canny_L2gradient,
        # lineMeasuring_VerticalLineDetect_HoughLinesP_rho = lineMeasuring_VerticalLineDetect_HoughLinesP_rho,
        # lineMeasuring_VerticalLineDetect_HoughLinesP_theta = lineMeasuring_VerticalLineDetect_HoughLinesP_theta,
        # lineMeasuring_VerticalLineDetect_HoughLinesP_threshold = lineMeasuring_VerticalLineDetect_HoughLinesP_threshold,
        # lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength = lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength,
        # lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap = lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap,
        # lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope = lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        # lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept = lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        # lineMeasuring_Cell_Top_extension = lineMeasuring_Cell_Top_extension,  # int(-45)  # 截取圖片單元區域的上邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        # lineMeasuring_Cell_Left_extension = lineMeasuring_Cell_Left_extension,  # int(-90)  # 截取圖片單元區域的左邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        # lineMeasuring_Cell_Bottom_extension = lineMeasuring_Cell_Bottom_extension,  # int(0)  # 截取圖片單元區域的下邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        # lineMeasuring_Cell_Right_extension = lineMeasuring_Cell_Right_extension,  # int(90)  # 截取圖片單元區域的右邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        # lineMeasuring_Cell_Top_embedded = lineMeasuring_Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        # lineMeasuring_Cell_Bottom_embedded = lineMeasuring_Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        # lineMeasuring_Cell_Left_embedded = lineMeasuring_Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        # lineMeasuring_Cell_Right_embedded = lineMeasuring_Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        # OCR_parameter = OCR_parameter,
        # OCRmethod = OCRmethod,  # "teressact"
        # tesseract_cmd = tesseract_cmd,  # str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
        # tesseract_lang = tesseract_lang,  # 'chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選多語言混合識別，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
        tesseract_config = tabel_tesseract_config,  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        # tesseract_timeout = tesseract_timeout,  # int(0)  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
        # tesseract_output_type = tesseract_output_type,  # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
    )

    # if not (not (result_Table is None)):
    #     print("The recognition result_Table is None.")
    # else:
    #     print(typeof(result_Table))
    #     print(result_Table)
    # response_data_JSON["table"] = result_Table

    response_data_JSON["key"] = [""] * 16
    # response_data_JSON["key"] = [""] * int(len(result_Table[0][1]) + len(result_Table[0][3]) + license(result_measuringRuler[0]))
    response_data_JSON["value"] = [""] * 16
    # response_data_JSON["value"] = [""] * int(len(result_Table[0][1]) + len(result_Table[0][3]) + license(result_measuringRuler[0]))

    for i in range(len(result_Table[0])):
        if isinstance(result_Table[0][i], list):
            # for item in result_Table[0][i]:
            for j in range(len(result_Table[0][i])):
                if i in [0, 2]:
                    response_data_JSON["key"][int(int(i / 2) * len(result_Table[0][0])) + j] = result_Table[0][i][j]
                    # response_data_JSON["key"].append(result_Table[0][i][j])
                if i in [1, 3]:
                    response_data_JSON["value"][int(int(int(i - 1) / 2) * len(result_Table[0][0])) + j] = result_Table[0][i][j]
                    # response_data_JSON["value"].append(result_Table[0][i][j])

    measuringRuler_Top_embedded = int(5)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
    measuringRuler_Bottom_embedded = int(0)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
    measuringRuler_Left_embedded = int(0)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
    measuringRuler_Right_embedded = int(0)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
    # 調整單元格（Cell）的上、下、左、右四條邊框的座標值，分別向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上、下、左、右四條邊框一起截取下來;
    X1 = int(int(longest_line[1]) + measuringRuler_Top_embedded)
    Y1 = int(int(0) + measuringRuler_Left_embedded)
    X2 = int(int(int(img_height) - int(1)) - measuringRuler_Bottom_embedded)
    Y2 = int(int(int(img_width) - int(1)) - measuringRuler_Right_embedded)
    imageData_Ruler = imageData[X1:X2, Y1:Y2]

    # # 用於調試 #########################################################################
    # # 在名稱爲 "measuringRulerImage" 的窗口中顯示截取出的量尺（measuringRuler）圖片（Image）;
    # cv2.namedWindow("measuringRulerImage")  # 創建圖片展示窗口;
    # cv2.imshow("measuringRulerImage", imageData_Ruler)  # 顯示圖片 display the image and wait for a keypress
    # # key = cv2.waitKey(50) & 0xFF  # 函數：cv2.waitKey(delay) 表示不斷刷新圖像，參數：delay 表示頻率間隔時長（單位：毫秒 ms），返回值爲當前鍵盤按鍵的 ASCII 值;
    # # if key == 27:
    # #     break
    # # # 回車鍵（Enter）的 ASCII 碼爲：ord('\n') == 13
    # # # 空格鍵的 ASCII 碼爲：ord(' ')
    # # # Tab 鍵的 ASCII 碼爲：ord('\t')
    # # # 退格鍵（backup ←）的 ASCII 碼爲：ord('\b')
    # # # 換行鍵的 ASCII 碼爲：ord('\r')
    # # # Esc 鍵的 ASCII 碼爲：ord('\x1b') == 27
    # cv2.waitKey(0)  # 函數：cv2.waitKey(0) 表示按任意鍵繼續;
    # # cv2.destroyAllWindows()  # 關閉所有窗口 closing all open windows
    # cv2.destroyWindow("measuringRulerImage")  # 關閉指定窗口，輸入參數爲窗口的名稱字符串;
    # # 用於調試 #########################################################################

    purpose = "lineMeasuring"  # "tableRecognition", "lineMeasuring"
    # os.path.abspath(".")  # 獲取當前文檔所在的絕對路徑;
    # os.path.abspath("..")  # 獲取當前文檔所在目錄的上一層路徑;
    # input_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
    # input_dir = os.path.join(os.path.abspath(".."), "/inputTest/")  # "D:\\inputTest\\"，"../inputTest/" 需要注意目錄操作權限，用於輸入傳值的媒介目錄;
    # input_dir = pathlib.Path(os.path.abspath("..") + "/inputTest/")  # pathlib.Path("../inputTest/")
    # imageUrl = ""  # "http://www.measuringRuler.jpg" 待識別檢測的圖片的 Web 請求網址 URL 字符串;
    # response = urllib_request.urlopen(imageUrl)  # 使用 Python 語言的原生模組「urllib」中的「request」中的「urlopen()」函數向服務器請求下載圖片數據;
    # img_array = np.array(bytearray(response.read()), dtype = np.uint8)  # 把從服務器下載的圖片數據轉換爲二進位 8 位字節數組的形式;
    # imageData = cv2.imdecode(img_array, -1)  # 使用 Python 語言的第三方擴展模組「opencv」中的「cv2.imdecode()」函數解析二進位 8 位字節數組形式的图片數據，RGB 模式;
    # imagePath = ""  # "C:/Criss/OCR-Measuring-Scale/src/inputTest/measuringRuler.jpg"  # "./inputTest/tabel.jpg" 待識別檢測的圖片的硬盤保存位置路徑字符串;
    # imageData = imageData_Ruler  # cv2.imread(self.imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
    # img_height = int(0)
    # img_width = int(0)
    # if len(imageData) > 0:
    #     # 獲取圖像的高度和寬度：
    #     # print(imageData.shape)
    #     img_height, img_width, img_dimension = imageData.shape
    #     # 三個結果分別爲：1、img_height 表示圖片的高度（單位：圖元（像素）數目），2、img_width 表示圖片的寬度（單位：圖元（像素）數目），3、img_dimension 表示圖片的輸出通道數，圖片若爲灰度（黑白）圖片，則不存在第三個通道輸出結果;
    #     # # 遍歷每個像素：
    #     # for i in range(img_height):
    #     #     for j in range(img_width):
    #     #         pixel_value = img[i, j]  # 在這個示例中：img[i,j] 表示圖片 img 的從上至下數（竪向）第 i 行、從左至右數（橫向）第 j 列處的像素值;
    #     #         print('Pixel at position (' + str(i) + ', ' + str(j) + '): ' + str(pixel_value))
    # print("Image height:", str(img_height))
    # print("Image width:", str(img_width))
    # grayImageData = []  # cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
    # binaryImageData = [],  # cv2.threshold(grayImageData, 127, 255, cv2.THRESH_BINARY_INV)  # 使用自定義閾值：「127」，過濾轉化爲二值化（非黑即白）的圖片;
    # binaryImageData = []  # cv2.threshold(grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
    # # 注意，函數：cv2.ximgproc.thinning() 只在庫「opencv-contrib-python」中有，在庫「opencv-python」中不存在，因此需要事先在控制臺安裝配置成功：root@localhost:~# pip install opencv-contrib-python -i https://mirrors.aliyun.com/pypi/simple/
    # binaryImageData = cv2.ximgproc.thinning(binaryImageData, cv2.ximgproc.THINNING_ZHANGSUEN)  # cv2.ximgproc.THINNING_GUOHALL  # 圖形骨架提取，將二值化後的圖像中的缐條細化爲單圖元（像素）寬度;
    HorizontalLineDetect = "Hough"  # "PixelDifference"
    VerticalLineDetect = "Hough"  # "PixelDifference"
    lineMeasuring_HorizontalLineDetect_Canny_threshold1 = int(30)
    lineMeasuring_HorizontalLineDetect_Canny_threshold2 = int(240)
    lineMeasuring_HorizontalLineDetect_Canny_apertureSize = int(3)
    lineMeasuring_HorizontalLineDetect_Canny_L2gradient = bool(False)
    lineMeasuring_HorizontalLineDetect_HoughLinesP_rho = int(1)
    lineMeasuring_HorizontalLineDetect_HoughLinesP_theta = float(np.pi/180)
    lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold = int(100)
    lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength = int(100)
    lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap = int(10)
    lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope = float(10)  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
    lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept = float(10)  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
    lineMeasuring_VerticalLineDetect_Canny_threshold1 = int(30)
    lineMeasuring_VerticalLineDetect_Canny_threshold2 = int(240)
    lineMeasuring_VerticalLineDetect_Canny_apertureSize = int(3)
    lineMeasuring_VerticalLineDetect_Canny_L2gradient = bool(False)
    lineMeasuring_VerticalLineDetect_HoughLinesP_rho = int(1)
    lineMeasuring_VerticalLineDetect_HoughLinesP_theta = float(np.pi/180)
    lineMeasuring_VerticalLineDetect_HoughLinesP_threshold = int(20)
    lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength = int(15)
    lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap = int(10)
    lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope = float(10)  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
    lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept = float(10)  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
    lineMeasuring_Cell_Top_extension = int(-45)  # 截取圖片單元區域的上邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
    lineMeasuring_Cell_Left_extension = int(-90)  # 截取圖片單元區域的左邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
    lineMeasuring_Cell_Bottom_extension = int(0)  # 截取圖片單元區域的下邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
    lineMeasuring_Cell_Right_extension = int(90)  # 截取圖片單元區域的右邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
    lineMeasuring_Cell_Top_embedded = int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
    lineMeasuring_Cell_Bottom_embedded = int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
    lineMeasuring_Cell_Left_embedded = int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
    lineMeasuring_Cell_Right_embedded = int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
    global measuringRuler_tesseract_config
    # measuringRuler_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    # print("Input measuring ruler tesseract config:", measuringRuler_tesseract_config)

    result_measuringRuler = None
    # result_measuringRuler = OCR_Image_to_Characters.run()
    result_measuringRuler = OCR_Image_to_Characters.run(
        purpose = purpose,  # "tableRecognition", "lineMeasuring"
        # imageUrl = imageUrl,  # "http://www.tabel.jpg" 待識別檢測的圖片的 Web 請求網址 URL 字符串;
        # imagePath = imagePath,  # "./inputTest/tabel.jpg" 待識別檢測的圖片的硬盤保存位置路徑字符串;
        imageData = imageData_Ruler,  # [],  # cv2.imread(self.imagePath, 1)  # 读取硬盤中的图片，RGB 模式;
        # img_height = img_height,
        # img_width = img_width,
        # grayImageData = grayImageData,  # [],  # cv2.cvtColor(self.imageData, cv2.COLOR_BGR2GRAY)  # 把 RGB 模式的圖片（Image）轉換爲灰度模式 GrayScale Conversion for the Canny Algorithm;
        # binaryImageData = binaryImageData,  # [],  # cv2.threshold(grayImageData, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  # 使用「Otsu」方法自適應閾值，過濾轉化爲二值化（非黑即白）的圖片;
        HorizontalLineDetect = HorizontalLineDetect,  # "Hough", "PixelDifference";
        VerticalLineDetect = VerticalLineDetect,  # "Hough", "PixelDifference";
        # Canny_threshold1 = Canny_threshold1,  # int(30)  # cv2.Canny()：第一次閾值；
        # Canny_threshold2 = Canny_threshold2,  # int(240)  # cv2.Canny()：第二次閾值；
        # Canny_apertureSize = Canny_apertureSize,  # int(3)  # cv2.Canny()：用於計算索伯爾運算元（Sobel）（算子）梯度的內核大小，預設值爲：3；
        # Canny_L2gradient = Canny_L2gradient,  # bool(False)  # cv2.Canny()：計算索伯爾運算元（Sobel）（算子）梯度的方法，預設值爲：False，表示使用「L1」範數方法；
        # HoughLinesP_rho = HoughLinesP_rho,  # int(1)  # cv2.HoughLinesP()：距離解析度（分辨率），單位爲：圖元（pixel）（像素），通常情況下，將距離解析度設為1即可；
        # HoughLinesP_theta = HoughLinesP_theta,  # float(np.pi/180)  # cv2.HoughLinesP()：角度解析度（分辨率），單位爲：弧度，通常情況下，將角度解析度設為「numpy.pi / 180」即可；
        # HoughLinesP_threshold = HoughLinesP_threshold,  # int(100)  # cv2.HoughLinesP()：閾值參數，只有累加器中的值高於閾值才會被認為是一條直線，閾值參數的選擇與圖像雜質訊息水準、直線密集程度等有關，需要通過實驗進行確定；
        # HoughLinesP_minLineLength = HoughLinesP_minLineLength,  # int(50)  # cv2.HoughLinesP()：設定一個線段長度的下限最小值，小於這個下限的線段將被忽略，一般根據具體需求設定，預設值爲：None；
        # HoughLinesP_maxLineGap = HoughLinesP_maxLineGap,  # int(10)  # cv2.HoughLinesP()：線段之間的最大間隔上限，如果兩條線段之間的距離超過了這個上限，這兩條線段將不會被連接成為一條直線，一般根據具體需求設定，預設值爲：None。
        # CV_parameter = CV_parameter,
        # tableRecognition_HorizontalLineDetect_Canny_threshold1 = tableRecognition_HorizontalLineDetect_Canny_threshold1,
        # tableRecognition_HorizontalLineDetect_Canny_threshold2 = tableRecognition_HorizontalLineDetect_Canny_threshold2,
        # tableRecognition_HorizontalLineDetect_Canny_apertureSize = tableRecognition_HorizontalLineDetect_Canny_apertureSize,
        # tableRecognition_HorizontalLineDetect_Canny_L2gradient = tableRecognition_HorizontalLineDetect_Canny_L2gradient,
        # tableRecognition_HorizontalLineDetect_HoughLinesP_rho = tableRecognition_HorizontalLineDetect_HoughLinesP_rho,
        # tableRecognition_HorizontalLineDetect_HoughLinesP_theta = tableRecognition_HorizontalLineDetect_HoughLinesP_theta,
        # tableRecognition_HorizontalLineDetect_HoughLinesP_threshold = tableRecognition_HorizontalLineDetect_HoughLinesP_threshold,
        # tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength = tableRecognition_HorizontalLineDetect_HoughLinesP_minLineLength,
        # tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap = tableRecognition_HorizontalLineDetect_HoughLinesP_maxLineGap,
        # tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope = tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5)  # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        # tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept = tableRecognition_HorizontalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        # tableRecognition_VerticalLineDetect_Canny_threshold1 = tableRecognition_VerticalLineDetect_Canny_threshold1,
        # tableRecognition_VerticalLineDetect_Canny_threshold2 = tableRecognition_VerticalLineDetect_Canny_threshold2,
        # tableRecognition_VerticalLineDetect_Canny_apertureSize = tableRecognition_VerticalLineDetect_Canny_apertureSize,
        # tableRecognition_VerticalLineDetect_Canny_L2gradient = tableRecognition_VerticalLineDetect_Canny_L2gradient,
        # tableRecognition_VerticalLineDetect_HoughLinesP_rho = tableRecognition_VerticalLineDetect_HoughLinesP_rho,
        # tableRecognition_VerticalLineDetect_HoughLinesP_theta = tableRecognition_VerticalLineDetect_HoughLinesP_theta,
        # tableRecognition_VerticalLineDetect_HoughLinesP_threshold = tableRecognition_VerticalLineDetect_HoughLinesP_threshold,
        # tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength = tableRecognition_VerticalLineDetect_HoughLinesP_minLineLength,
        # tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap = tableRecognition_VerticalLineDetect_HoughLinesP_maxLineGap,
        # tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope = tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        # tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept = tableRecognition_VerticalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        # tableRecognition_Cell_Top_embedded = tableRecognition_Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        # tableRecognition_Cell_Bottom_embedded = tableRecognition_Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        # tableRecognition_Cell_Left_embedded = tableRecognition_Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        # tableRecognition_Cell_Right_embedded = tableRecognition_Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        lineMeasuring_HorizontalLineDetect_Canny_threshold1 = lineMeasuring_HorizontalLineDetect_Canny_threshold1,
        lineMeasuring_HorizontalLineDetect_Canny_threshold2 = lineMeasuring_HorizontalLineDetect_Canny_threshold2,
        lineMeasuring_HorizontalLineDetect_Canny_apertureSize = lineMeasuring_HorizontalLineDetect_Canny_apertureSize,
        lineMeasuring_HorizontalLineDetect_Canny_L2gradient = lineMeasuring_HorizontalLineDetect_Canny_L2gradient,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_rho = lineMeasuring_HorizontalLineDetect_HoughLinesP_rho,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_theta = lineMeasuring_HorizontalLineDetect_HoughLinesP_theta,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold = lineMeasuring_HorizontalLineDetect_HoughLinesP_threshold,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength = lineMeasuring_HorizontalLineDetect_HoughLinesP_minLineLength,
        lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap = lineMeasuring_HorizontalLineDetect_HoughLinesP_maxLineGap,
        lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope = lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept = lineMeasuring_HorizontalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        lineMeasuring_VerticalLineDetect_Canny_threshold1 = lineMeasuring_VerticalLineDetect_Canny_threshold1,
        lineMeasuring_VerticalLineDetect_Canny_threshold2 = lineMeasuring_VerticalLineDetect_Canny_threshold2,
        lineMeasuring_VerticalLineDetect_Canny_apertureSize = lineMeasuring_VerticalLineDetect_Canny_apertureSize,
        lineMeasuring_VerticalLineDetect_Canny_L2gradient = lineMeasuring_VerticalLineDetect_Canny_L2gradient,
        lineMeasuring_VerticalLineDetect_HoughLinesP_rho = lineMeasuring_VerticalLineDetect_HoughLinesP_rho,
        lineMeasuring_VerticalLineDetect_HoughLinesP_theta = lineMeasuring_VerticalLineDetect_HoughLinesP_theta,
        lineMeasuring_VerticalLineDetect_HoughLinesP_threshold = lineMeasuring_VerticalLineDetect_HoughLinesP_threshold,
        lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength = lineMeasuring_VerticalLineDetect_HoughLinesP_minLineLength,
        lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap = lineMeasuring_VerticalLineDetect_HoughLinesP_maxLineGap,
        lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope = lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Slope,  # float(5) # 重叠缐過濾間距閾值：斜率（Slope），單位：圖元（像素）點個數;
        lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept = lineMeasuring_VerticalLineDetect_overlappingFilterThreshold_Intercept,  # float(5)  # # 重叠缐過濾間距閾值：截距（Intercept），單位：圖元（像素）點個數;
        lineMeasuring_Cell_Top_extension = lineMeasuring_Cell_Top_extension,  # int(-45)  # 截取圖片單元區域的上邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Left_extension = lineMeasuring_Cell_Left_extension,  # int(-90)  # 截取圖片單元區域的左邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Bottom_extension = lineMeasuring_Cell_Bottom_extension,  # int(0)  # 截取圖片單元區域的下邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Right_extension = lineMeasuring_Cell_Right_extension,  # int(90)  # 截取圖片單元區域的右邊框座標值增加量，識別出的量尺（Measuring Ruler）刻度「標識點」缐段（Line segment）圖片（Image）的上側的標識區域;
        lineMeasuring_Cell_Top_embedded = lineMeasuring_Cell_Top_embedded,  # int(3)  # 調整單元格（Cell）的上邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的上邊框一起截取下來;
        lineMeasuring_Cell_Bottom_embedded = lineMeasuring_Cell_Bottom_embedded,  # int(3)  # 調整單元格（Cell）的下邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的下邊框一起截取下來;
        lineMeasuring_Cell_Left_embedded = lineMeasuring_Cell_Left_embedded,  # int(3)  # 調整單元格（Cell）的左邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的左邊框一起截取下來;
        lineMeasuring_Cell_Right_embedded = lineMeasuring_Cell_Right_embedded,  # int(3)  # 調整單元格（Cell）的右邊框的座標值，向單元格（Cell）内部縮進 3 個圖元（像素）（Pixel）點的單位，目的是，在截取單元格（Cell）圖片（Image）時，防止將單元格（Cell）的右四條邊框一起截取下來;
        # OCR_parameter = OCR_parameter,
        # OCRmethod = OCRmethod,  # "teressact"
        # tesseract_cmd = tesseract_cmd,  # str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
        # tesseract_lang = tesseract_lang,  # 'chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 表示指定使用的語言模型，'eng' 表示英語，'chi_tra' 表示漢字橫板，'chi_tra_vert' 表示漢字竪版，'chi_tra+chi_tra_vert+eng' 表示多選多語言混合識別，'chi_sim' 表示殘體，'chi_sim_vert' 表示殘體竪版;
        tesseract_config = measuringRuler_tesseract_config,  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
        # tesseract_timeout = tesseract_timeout,  # int(0)  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
        # tesseract_output_type = tesseract_output_type,  # 預設值爲：pytesseract.Output.STRING，指定輸出的數據類型，pytesseract.Output.STRING 表示輸出字符串類型, pytesseract.Output.BYTES 表示輸出 8 位二進制字節數組，pytesseract.Output.DICT 表示輸出字典類型，pytesseract.Output.DATAFRAME 表示輸出第三方擴展：pandas 庫的數據框類型;
    )

    # if not (not (result_measuringRuler is None)):
    #     print("The recognition result_measuringRuler is None.")
    # else:
    #     print(typeof(result_measuringRuler))
    #     print(result_measuringRuler)
    # response_data_JSON["measuringRuler"] = result_measuringRuler

    # length_table = len(response_data_JSON["value"])
    for i in range(len(result_measuringRuler[0])):
        if isinstance(result_measuringRuler[0], dict):
            for key, value in result_measuringRuler[0].items():
                # print(key, ":", value)
                if isinstance(value, list):
                    if value[1] == "test-1":
                        response_data_JSON["key"][12] = "test-1"
                        # response_data_JSON["key"][length_table + 0] = "test-1"
                        response_data_JSON["value"][12] = value[2]
                        # response_data_JSON["value"][length_table + 0] = value[2]
                    if value[1] == "test-2":
                        response_data_JSON["key"][13] = "test-2"
                        # response_data_JSON["key"][length_table + 1] = "test-2"
                        response_data_JSON["value"][13] = value[2]
                        # response_data_JSON["value"][length_table + 1] = value[2]
                    if value[1] == "test-3":
                        response_data_JSON["key"][14] = "test-3"
                        # response_data_JSON["key"][length_table + 2] = "test-3"
                        response_data_JSON["value"][14] = value[2]
                        # response_data_JSON["value"][length_table + 2] = value[2]
                    if value[1] == "test-4":
                        response_data_JSON["key"][15] = "test-4"
                        # response_data_JSON["key"][length_table + 2] = "test-4"
                        response_data_JSON["value"][15] = value[2]
                        # response_data_JSON["value"][length_table + 2] = value[2]

    # now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    # response_data_JSON["time"] = str(now_date)

    response_data_String = ','.join([str(X) for X in response_data_JSON["value"]])

    # response_data_String = json.dumps([str(X) for X in response_data_JSON["value"]])  # 將JOSN對象轉換為JSON字符串;
    # # response_data_String = json.dumps(response_data_JSON["value"])  # 將JOSN對象轉換為JSON字符串;
    # # response_data_String = json.dumps(response_data_JSON)  # 將JOSN對象轉換為JSON字符串;
    # # response_data_JSON = json.loads(response_data_String)

    # response_data_String = "98765432101,悟空,1598-07-02,男,01-987654321,a@b.com,衛兵,2346-05-02,西使團,大學本科,28000,,-0.802710843373494,-0.20331325301204817,0.2966867469879517,0.6957831325301205"

    # response_data_String = str(rresponse_data_String, encoding="utf-8")  # str("", encoding="utf-8") 强制轉換為 "utf-8" 編碼的字符串類型數據;
    # .encode("utf-8")將字符串（str）對象轉換為 "utf-8" 編碼的二進制字節流（<bytes>）類型數據;
    response_data_bytes = response_data_String.encode("utf-8")
    # response_data_String_len = len(bytes(response_data_String, "utf-8"))

    return response_data_bytes  # response_data_String  # [str(X) for X in response_data_JSON["value"]]



def Input_and_Output(is_window, screenwidth, screenheight, is_Concurrent, is_storage_position, is_storage_type, input_Train_Path, input_Train_File_Array, input_Test_Path, input_Test_File_Array, do_Function, output_Test_Path, output_Test_File_Array, output_Test_URL, time_sleep, outqueue_from_task_to_host, outqueue_from_host_to_task):

    # if is_Concurrent == "0" or is_Concurrent == 0:
    #     global is_Runing
    #     if is_window:
    #         # global screenwidth
    #         # global screenheight
    #         global image_sample
    #     global input_dir
    #     global output_dir
    #     global file_Data
    #     global result_Data
    #     global complete_Number
    #     global Error_Log
    #     # global file_Data_bytes
    #     # global file_Data_len

    global is_Runing
    if is_Concurrent == "Multi-Threading":
        is_Runing = True
        if outqueue_from_host_to_task:
            # def Queue_update(outqueue_from_host_to_task):
            #     # outqueue_from_task_to_host = outqueue[0]
            #     # outqueue_from_host_to_task = outqueue[1]
            #     try:
            #         if outqueue_from_host_to_task.empty():
            #             window_root.after(250, Queue_update, outqueue_from_host_to_task)
            #             pass
            #         if not outqueue_from_host_to_task.empty():
            #             msg = outqueue_from_host_to_task.get(
            #                 block=False,
            #                 timeout=None
            #             )
            #             if msg[0] == "is_Runing_True":
            #                 is_Runing = True
            #                 window_root.after(250, Queue_update, outqueue_from_host_to_task)
            #                 # pass
            #                 # return return_value
            #             elif msg[0] == "is_Runing_False":
            #                 is_Runing = False
            #                 window_root.after(250, Queue_update, outqueue_from_host_to_task)
            #                 # pass
            #                 # return return_value
            #         # else:
            #         #     # By not calling window_root.after here, we allow update to
            #         #     # truly end
            #         #     window_root.after(250, Queue_update, outqueue_from_host_to_task)
            #         #     pass
            #     except queue.Empty:
            #         window_root.after(250, Queue_update, outqueue_from_host_to_task)
            # window_root.after(250, Queue_update, outqueue_from_host_to_task)
            if not outqueue_from_host_to_task.empty():
                msg = outqueue_from_host_to_task.get(
                    block=False,
                    timeout=None
                )
                if msg[0] == "is_Runing_True":
                    is_Runing = True
                    # window_root.after(250, Queue_update, outqueue_from_host_to_task)
                    # pass
                    # return return_value
                elif msg[0] == "is_Runing_False":
                    is_Runing = False
                    # window_root.after(250, Queue_update, outqueue_from_host_to_task)
                    # pass
                    # return return_value

    global file_Data
    # global file_Data_bytes
    # global file_Data_len
    file_Data = ""
    # file_Data_bytes = file_Data.encode("utf-8")
    # file_Data = file_Data_bytes.decode("utf-8")
    # file_Data = str(file_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
    # file_Data_len = len(bytes(file_Data, "utf-8"))

    global result_Data
    result_Data = ""
    # result_Data_bytes = result_Data.encode("utf-8")
    # result_Data = result_Data_bytes.decode("utf-8")
    # result_Data = str(result_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
    # result_Data_len = len(bytes(result_Data, "utf-8"))

    global image_sample
    image_sample = []

    # global complete_Number
    complete_Number = int(0)

    global Error_Log
    Error_Log = []

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
            if is_window:
                Label_State['text'] = "運行錯誤." + "\n" + "路徑: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_Path))).replace('\\', '/') + " ]" + "\n" + "找不到可處理檔."

        if is_Concurrent == "Multi-Threading":
            if outqueue_from_task_to_host:
                outqueue_from_task_to_host.put(
                    log_Wrong,
                    block=False,
                    timeout=None
                )

        Error_Log.append(str(os.path.normpath(str(input_Test_Path))).replace('\\', '/'))
        return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_Path))).replace('\\', '/')

    if is_window:
        if is_Concurrent == "0" or is_Concurrent == 0:
            # global image_sample
            image_sample = []
            Canvas_display_sample.delete("all")
            # Canvas_display_sample.create_image(
            #     0,
            #     0,
            #     anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
            #     image=image_sample,
            #     # fill="red",
            #     tag="one"
            # )
            # Canvas_display_sample.delete(tag="one")
            Label_display_sample['text'] = "Input file"

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

            output_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')

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
                            if is_window:
                                Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
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
                        Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'))
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
                        if is_window:
                            Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
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
                    Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'))
                    return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')

            if not (os.path.exists(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')).is_dir()):
                if is_Concurrent == "0" or is_Concurrent == 0:
                    sys.stdout.write("\n")  # 輸出換行;
                    sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
                    sys.stdout.write("\n")  # 輸出換行;
                    # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/')} : {error}')
                    # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                    if is_window:
                        Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
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
                Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(output_Test_Path)))))).replace('\\', '/'))
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
                #             window_root.after(250, Queue_update, outqueue_from_host_to_task)
                #             pass
                #         if not outqueue_from_host_to_task.empty():
                #             msg = outqueue_from_host_to_task.get(
                #                 block=False,
                #                 timeout=None
                #             )
                #             if msg[0] == "is_Runing_True":
                #                 is_Runing = True
                #                 window_root.after(250, Queue_update, outqueue_from_host_to_task)
                #                 # pass
                #                 # return return_value
                #             elif msg[0] == "is_Runing_False":
                #                 is_Runing = False
                #                 window_root.after(250, Queue_update, outqueue_from_host_to_task)
                #                 # pass
                #                 # return return_value
                #         # else:
                #         #     # By not calling window_root.after here, we allow update to
                #         #     # truly end
                #         #     window_root.after(250, Queue_update, outqueue_from_host_to_task)
                #         #     pass
                #     except queue.Empty:
                #         window_root.after(250, Queue_update, outqueue_from_host_to_task)
                # window_root.after(250, Queue_update, outqueue_from_host_to_task)
                if not outqueue_from_host_to_task.empty():
                    msg = outqueue_from_host_to_task.get(
                        block=False,
                        timeout=None
                    )
                    if msg[0] == "is_Runing_True":
                        is_Runing = True
                        # window_root.after(250, Queue_update, outqueue_from_host_to_task)
                        # pass
                        # return return_value
                    elif msg[0] == "is_Runing_False":
                        is_Runing = False
                        # window_root.after(250, Queue_update, outqueue_from_host_to_task)
                        # pass
                        # return return_value

        if not is_Runing:

            if is_Concurrent == "Multi-Threading":
                if outqueue_from_task_to_host:
                    if len(Error_Log) > 0:
                        outqueue_from_task_to_host.put(
                            [
                                "Discontinue",
                                "Error",
                                "[" + str(len(Error_Log)) + "]",
                                str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                str(','.join(Error_Log))
                            ],
                            block=False,
                            timeout=None
                        )
                    else:
                        outqueue_from_task_to_host.put(
                            [
                                "Discontinue",
                                "Complete",
                                "[" + str(complete_Number) + "]",
                                str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                                input_Test_Path,
                                output_Test_Path
                            ],
                            block=False,
                            timeout=None
                        )

            # continue
            # break
            if len(Error_Log) > 0:
                return "Error," + str(len(Error_Log)) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(','.join(Error_Log))
            else:
                return "Complete," + str(complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_Test_Path + "," + output_Test_Path  # None

        # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
        # print(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))

        if is_Concurrent == "0" or is_Concurrent == 0:
            if is_window:
                Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
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

        file_Data = ""
        result_Data = ""

        if is_window:
            if is_Concurrent == "0" or is_Concurrent == 0:
                image_sample = []
                # 清除自定義畫布組件中已經繪製的指定圖片;
                Canvas_display_sample.delete("all")
                # Canvas_display_sample.delete(tag="one")
                # Canvas_display_sample.create_image(
                #     0,
                #     0,
                #     anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
                #     image=image_sample,
                #     # fill="red",
                #     tag="one"
                # )
                Label_display_sample['text'] = "Input file"
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
                        if is_window:
                            Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
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
                    Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
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
                file_Data = fd.read()
                # file_Data = fd.read().decode("utf-8")
                # data_Bytes = file_Data.encode("utf-8")
                # file_Data = str(data_Bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
                # fd.write(data_Bytes)
            except FileNotFoundError:
                if is_Concurrent == "0" or is_Concurrent == 0:
                    sys.stdout.write("\n")
                    sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                    sys.stdout.write("\n")
                    # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在.")
                    if is_window:
                        Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在."
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
                Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                # break
                continue
            # except PersmissionError:
            #     if is_Concurrent == "0" or is_Concurrent == 0:
            #         sys.stdout.write("\n")
            #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
            #         sys.stdout.write("\n")
            #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無操作權限.")
            #         if is_window:
            #             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無操作權限."
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
            #     Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
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
                        if is_window:
                            Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據."
                        print("延時等待 " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ].")
                        if is_window:
                            # Label_State['text'] = "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
                            Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據." + "\n" + "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
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
                        file_Data = fd.read()
                        # file_Data = fd.read().decode("utf-8")
                        # data_Bytes = file_Data.encode("utf-8")
                        # fd.write(data_Bytes)
                    except OSError as error:
                        if is_Concurrent == "0" or is_Concurrent == 0:
                            sys.stdout.write("\n")
                            sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            sys.stdout.write("\n")
                            # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據.")
                            # print(error)
                            # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
                            if is_window:
                                Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據."
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
                        Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                        # break
                        continue
                else:
                    if is_Concurrent == "0" or is_Concurrent == 0:
                        sys.stdout.write("\n")
                        sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                        sys.stdout.write("\n")
                        # print(error)
                        # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
                        if is_window:
                            Label_State['text'] = "讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "發生錯誤." + "\n" + str(error)
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
                    Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                    # break
                    continue
            finally:
                fd.close()
            # 注：可以用try/finally語句來確保最後能關閉檔，不能把open語句放在try塊裡，因為當打開檔出現異常時，檔物件file_object無法執行close()方法;


            if is_window:
                # 讀取用於在畫布 canvas 組件中展示的樣本圖片;
                try:
                    # image_sample = tk.PhotoImage(file=str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))  # 使用 Python 原生的 tkinter 包中的 tkinter.PhotoImage() 函數讀取圖片檔;
                    imgFile = Image.open(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')).resize((int(int(screenwidth)*0.42), int(int(screenheight)*0.55)))  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.Image.open() 函數打開圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;
                    image_sample = ImageTk.PhotoImage(imgFile)  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.ImageTk.PhotoImage() 函數讀取圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;

                    if is_Concurrent == "0" or is_Concurrent == 0:
                        Label_display_sample['text'] = str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
                        # 在自定義畫布組件中展示讀入的圖片樣本;
                        # Canvas_display_sample.delete("all")
                        # Canvas_display_sample.delete(tag="one")
                        Canvas_display_sample.create_image(
                            0,
                            0,
                            anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
                            image=image_sample,
                            # fill="red",
                            tag="one"
                        )

                    if is_Concurrent == "Multi-Threading":
                        if outqueue_from_task_to_host:
                            outqueue_from_task_to_host.put(
                                [
                                    "image_sample",
                                    str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                    image_sample
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
                        Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在."
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
                    # Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                    # break
                    # continue
                # except PersmissionError:
                #     if is_Concurrent == "0" or is_Concurrent == 0:
                #         sys.stdout.write("\n")
                #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                #         sys.stdout.write("\n")
                #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無操作權限.")
                #         Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無操作權限."
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
                #     # Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
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
                            Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據."
                            print("延時等待 " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ].")
                            # Label_State['text'] = "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
                            Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據." + "\n" + "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
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
                            image_sample = ImageTk.PhotoImage(imgFile)  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.ImageTk.PhotoImage() 函數讀取圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;

                            if is_Concurrent == "0" or is_Concurrent == 0:
                                Label_display_sample['text'] = str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
                                # 在自定義畫布組件中展示讀入的圖片樣本;
                                Canvas_display_sample.delete("all")
                                # Canvas_display_sample.delete(tag="one")
                                Canvas_display_sample.create_image(
                                    0,
                                    0,
                                    anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
                                    image=image_sample,
                                    # fill="red",
                                    tag="one"
                                )

                            if is_Concurrent == "Multi-Threading":
                                if outqueue_from_task_to_host:
                                    outqueue_from_task_to_host.put(
                                        [
                                            "image_sample",
                                            str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                                            image_sample
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
                                Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法讀取數據."
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
                            # Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                            # break
                            # continue
                    else:
                        if is_Concurrent == "0" or is_Concurrent == 0:
                            sys.stdout.write("\n")
                            sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                            sys.stdout.write("\n")
                            # print(error)
                            # print(f'Error: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
                            Label_State['text'] = "讀取檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "發生錯誤." + "\n" + str(error)
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
                        # Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
                        # break
                        # continue
                finally:
                    imgFile.close()
                # 注：可以用try/finally語句來確保最後能關閉檔，不能把open語句放在try塊裡，因為當打開檔出現異常時，檔物件file_object無法執行close()方法;


            # # 使用 str("").encode("utf-8") 方法，將字符串（str）對象轉換為 "utf-8" 編碼的二進制字節流（<bytes>）類型數據;
            # file_Data_bytes = file_Data.encode("utf-8")
            # file_Data = file_Data_bytes.decode("utf-8")
            # file_Data_len = len(bytes(file_Data, "utf-8"))


            # # 讀取到輸入數據之後，刪除文檔;
            # try:
            #     os.remove(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))  # os.unlink(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')) 刪除文檔;
            #     # os.listdir(input_dir)  # 刷新目錄内容列表
            #     # print(os.listdir(input_dir))
            # except Exception as error:
            #     if is_Concurrent == "0" or is_Concurrent == 0:
            #         print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除.")
            #         print(f'Wrong: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
            #         if is_window:
            #             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除."
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
            #             if is_window:
            #                 # Label_State['text'] = "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試刪除檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
            #                 Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除." + "\n" + "延時等待: " + str(time_sleep) + " (秒)後." + "\n" + "重複嘗試刪除檔:" + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]."
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
            #                 if is_window:
            #                     Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除."
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
            #             Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
            #             # break
            #             continue
            #     # else:
            #     #     if is_Concurrent == "0" or is_Concurrent == 0:
            #     #         print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除.")
            #     #         print(error)
            #     #         # print(f'Wrong: {str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')} : {error}')
            #     #         if is_window:
            #     #             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "無法刪除."
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
            #     #     Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
            #     #     # break
            #     #     continue


            # 在這裏插入具體的數據處理算法;
            result_Data_JSON = do_Function(file_Data)
            result_Data = result_Data_JSON

            # print(type(file_Data))  # <class 'bytes'>
            # result_Data = str(file_Data)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
            # print(type(result_Data))  # <class 'str'>

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
            if is_window:

                if is_Concurrent == "0" or is_Concurrent == 0:

                    # Label_State['text'] = "Succeed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(input_Test_File_Array[i])
                    Label_State['text'] = "Succeed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')

                    # # 讀取多行文本輸入框中的内容;
                    # Text_display_result_value = Text_display_result.get(
                    #     "0.0",  # 表示讀取多行文本輸入框 .Text 控件中的全部值，如果設定參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始讀取;
                    #     "end"  # 表示讀取至多行文本輸入框 .Text 控件中全部值的最後一個字符爲止;
                    # )
                    # Text_display_result_value = str(Text_display_result_value)
                    # print(Text_display_result_value)

                    # # 刪除多行文本輸入框中的内容;
                    # Text_display_result.delete(
                    #     "1.0",  # 參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始刪除;
                    #     "end"  # 參數爲 "end" 表示刪除直至最後一個字符，即清空輸入框;
                    # )

                    # new_Text_display_result_value = Text_display_result_value + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Test_File_Array[i]) + "," + str(result_Data, encoding="utf-8")
                    new_Text_display_result_value = str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Test_File_Array[i]) + "," + str(result_Data, encoding="utf-8") + "\n"
                    # new_Text_display_result_value = str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n"
                    # print(new_Text_display_result_value)

                    # 將字符串寫入多行文本輸入框;
                    Text_display_result.insert(
                        "end",  # 參數 "1.0" 表示從第一行第一列開始插入，參數 "insert" 表示在當前光標位置處插入一個字符串，參數 "end" 表示在末尾位置處追加寫入一個字符串;
                        str(new_Text_display_result_value)
                    )

                    Text_display_result.see("end"),  # 表示將 .Text 組件中聚焦在文本末行，即顯示末尾;

            # 將運算結果寫入磁碟文檔;
            if is_storage_position == "Database_and_Disk" or is_storage_position == "Disk":

                for j in range(0, len(output_Test_File_Array)):

                    if len(str(output_Test_File_Array[j])) > 0:

                        # output_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')

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
                        #                 if is_window:
                        #                     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
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
                        #             Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'))
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
                        #             if is_window:
                        #                 Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
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
                        #         Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'))
                        #         # break
                        #         continue

                        # if not (os.path.exists(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')).is_dir()):
                        #     if is_Concurrent == "0" or is_Concurrent == 0:
                        #         sys.stdout.write("\n")  # 輸出換行;
                        #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')))  # 將字符串輸出寫到操作系統控制臺;
                        #         sys.stdout.write("\n")  # 輸出換行;
                        #         # print(f'Error: {str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/')} : {error}')
                        #         # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                        #         if is_window:
                        #             Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
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
                        #     Error_Log.append(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')))))).replace('\\', '/'))
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
                                        if is_window:
                                            Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在但無法修改為可讀可寫權限."
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
                                    Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
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
                            #         if is_window:
                            #             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在且無法刪除，以重新創建更新數據."
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
                            #     Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
                            #     # break
                            #     continue

                            # # 判斷用於接收傳值的媒介文檔，是否已經從硬盤刪除;
                            # if os.path.exists(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')) and os.path.isfile(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')):
                            #     if is_Concurrent == "0" or is_Concurrent == 0:
                            #         sys.stdout.write("\n")
                            #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
                            #         sys.stdout.write("\n")
                            #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在且無法刪除，以重新創建更新數據.")
                            #         if is_window:
                            #             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "已存在且無法刪除，以重新創建更新數據."
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
                            #     Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
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
                        #                 if is_window:
                        #                     Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
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
                        #             Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
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
                        #             if is_window:
                        #                 Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
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
                        #         Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
                        #         # break
                        #         continue

                        # if not (os.path.exists(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')) and pathlib.Path(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')).is_dir()):
                        #     if is_Concurrent == "0" or is_Concurrent == 0:
                        #         sys.stdout.write("\n")
                        #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
                        #         sys.stdout.write("\n")
                        #         # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
                        #         # print("運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                        #         if is_window:
                        #             Label_State['text'] = "運行錯誤." + "\n" + "目錄: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
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
                        #     Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
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
                            fd.write(result_Data)
                            # result_Data_bytes = result_Data.encode("utf-8")
                            # result_Data_len = len(bytes(result_Data, "utf-8"))
                            # fd.write(result_Data_bytes)
                        except FileNotFoundError:
                            if is_Concurrent == "0" or is_Concurrent == 0:
                                sys.stdout.write("\n")
                                sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                                sys.stdout.write("\n")
                                # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
                                # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "寫入失敗.")
                                if is_window:
                                    Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "寫入失敗."
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
                            Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
                            # break
                            continue
                        # except PersmissionError:
                        #     if is_Concurrent == "0" or is_Concurrent == 0:
                        #         sys.stdout.write("\n")
                        #         sys.stdout.write("Wrong," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                        #         sys.stdout.write("\n")
                        #         # print(f'Error: {str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/')} : {error}')
                        #         # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無操作權限.")
                        #         if is_window:
                        #             Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/') + " ]" + "\n" + "無操作權限."
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
                        #     Error_Log.append(str(os.path.normpath(str(output_Test_File_Array[j]))).replace('\\', '/'))
                        #     # break
                        #     continue
                        finally:
                            fd.close()
                        # 注：可以用try/finally語句來確保最後能關閉檔，不能把open語句放在try塊裡，因為當打開檔出現異常時，檔物件file_object無法執行close()方法;

            # if is_storage_position == "Database" or is_storage_position == "Database_and_Disk":

            complete_Number = complete_Number + int(1)  # 記錄處理成功的文檔個數;

            if is_Concurrent == "0" or is_Concurrent == 0:
                # sys.stdout.write("\n")  # 輸出換行;
                # sys.stdout.write("Succeed," + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "," + str(result_Data, encoding="utf-8"))  # 將字符串輸出寫到操作系統控制臺;
                # print("Succeed," + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "," + str(result_Data, encoding="utf-8"))  # 將字符串輸出寫到操作系統控制臺;
                print("Succeed," + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))

            if is_Concurrent == "Multi-Threading":
                if outqueue_from_task_to_host:
                    outqueue_from_task_to_host.put(
                        [
                            "Succeed",
                            str(int(i)+1),
                            str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                            str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'),
                            str(str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "," + str(result_Data, encoding="utf-8") + "\n"),
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
                if is_window:
                    Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + " ]" + "\n" + "不存在或不是檔."
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
            Error_Log.append(str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/'))
            # break
            continue


    # file_Data = ""
    # result_Data = ""
    # image_sample = []
    # 清除自定義畫布組件中已經繪製的指定圖片;
    # Canvas_display_sample.delete("all")
    # Canvas_display_sample.delete(tag="one")
    # Canvas_display_sample.create_image(
    #     0,
    #     0,
    #     anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
    #     image=image_sample,
    #     # fill="red",
    #     tag="one"
    # )
    # Label_display_sample['text'] = "input file"


    # if is_Concurrent == "0" or is_Concurrent == 0:
    #     # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
    #     if is_window:
    #         Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + input_Test_Path + " ]." + "\n" + "Output: [ " + output_Test_Path + " ]." + "\n" + "complete [ " + str(complete_Number) + " ]."
    #         # Label_State['text'] = "Stand by"

    if is_Concurrent == "Multi-Threading":
        if outqueue_from_task_to_host:
            if len(Error_Log) > 0:
                outqueue_from_task_to_host.put(
                    [
                        "Error",
                        "[" + str(len(Error_Log)) + "]",
                        str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")),
                        str(','.join(Error_Log))
                    ],
                    block=False,
                    timeout=None
                )
            else:
                outqueue_from_task_to_host.put(
                    [
                        "Complete",
                        "[" + str(complete_Number) + "]",
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
    #     message = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + input_Test_Path + " ]." + "\n" + "Output: [ " + output_Test_Path + " ]." + "\n" + "complete [ " + str(complete_Number) + " ]."
    # )

    if len(Error_Log) > 0:
        return "Error,[" + str(len(Error_Log)) + "]," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(','.join(Error_Log))
    else:
        return "Complete,[" + str(complete_Number) + "]," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_Test_Path + "," + output_Test_Path  # None


def Run(Path_Conversion, Input_and_Output, is_window, screenwidth, screenheight, is_Concurrent, is_storage_position, is_storage_type, inputTrain_path, inputTrain_File_Array, inputTest_path, inputTest_File_Array, do_Function, outputTest_path, outputTest_File_Array, outputTest_URL, time_sleep, outqueue_from_task_to_host, outqueue_from_host_to_task):

    try:

        # if not is_Runing:
        #     is_Runing = not is_Runing

        # complete_Number = int(0)
        # Error_Log = []
        # file_Data = ""
        # result_Data = ""
        # image_sample = []

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
            outqueue_from_host_to_task
        )
        # print(return_value)

        # inputTrain_File_Array = []
        # inputValidation_File_Array = []
        # inputTest_File_Array = []
        # outputTest_File_Array = []

        # if is_Runing:
        #     is_Runing = not is_Runing

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


default_inputTrain_path = ""
default_inputValidation_path = ""
default_inputTest_path = ""
default_outputTest_path = ""
# 判斷是否爲打包（.exe）後的環境;
if getattr(sys, 'frozen', False):
    default_inputTrain_path = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "inputTrain")).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTrain"))).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTrain"))).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTrain"))).replace('\\', '/')
    default_inputValidation_path = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "inputValidation")).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputValidation"))).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputValidation"))).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputValidation"))).replace('\\', '/')
    default_inputTest_path = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "inputTest")).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTest"))).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTest"))).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTest"))).replace('\\', '/')
    default_outputTest_path = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "outputTest", "test" + "." + str(is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
else:
    default_inputTrain_path = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "inputTrain")).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTrain"))).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTrain"))).replace('\\', '/')
    # default_inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTrain"))).replace('\\', '/')
    default_inputValidation_path = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "inputValidation")).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputValidation"))).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputValidation"))).replace('\\', '/')
    # default_inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputValidation"))).replace('\\', '/')
    default_inputTest_path = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "inputTest")).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTest"))).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTest"))).replace('\\', '/')
    # default_inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTest"))).replace('\\', '/')
    default_outputTest_path = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "outputTest", "test" + "." + str(is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
    # default_outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')


input_dir = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "inputTest")).replace('\\', '/')
# input_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
output_dir = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "outputTest")).replace('\\', '/')
# output_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')


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


# 使用 while True: 的方法設置死循環創建看守進程，監聽指定的硬盤目錄或文檔，響應創建事件，從而達到不同語言之間利用硬盤文檔傳輸數據交互的效果;
# 控制臺傳參，通過 sys.argv 數組獲取從控制臺傳入的參數
is_window = True  # bool(True), bool(False) 判斷只需要執行一次還是啓動監聽服務器功能;
is_Concurrent = "Multi-Threading"  # 選擇監聽動作的函數是否並發（多協程、多缐程、多進程），可取值：0、"0"、"Multi-Threading"、"Multi-Processes";
# is_storage_position = "Disk"  # 判斷存儲位置，可取值："Database", "Database_and_Disk", "Disk" ;
# is_storage_type = "csv"  # 判斷存儲類型，可取值："json", "csv", "txt", "xlsx";
# os.path.abspath(".")  # 獲取當前文檔所在的絕對路徑;
# os.path.abspath("..")  # 獲取當前文檔所在目錄的上一層路徑;
default_input_tabel_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
default_input_measuringRuler_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
input_tabel_tesseract_config = default_input_tabel_tesseract_config
input_measuringRuler_tesseract_config = default_input_measuringRuler_tesseract_config
tesseract_cmd = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tesseract")).replace('\\', '/')  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# tesseract_cmd = str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# tesseract_cmd = str(pathlib.Path(os.path.abspath("..") + "/Tesseract-OCR/" + "/tesseract/"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# print(tesseract_cmd)
# pytesseract.pytesseract.tesseract_cmd = tesseract_cmd  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
tesseract_tessdata_dir = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tessdata", "chi_tra.traineddata")).replace('\\', '/')  # "/usr/share/tessdata" # File PATH：用戶自定義指定本地訓練完畢的數據集文檔（tessdata）的儲存路徑位置，使用 Tesseract 識別，需要使用訓練好的數據集，如果不指定該參數，則預設使用系統預設的數據集文檔目錄 Specify the location of tessdata path.
# print(tesseract_tessdata_dir)
tesseract_user_words = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tesswords")).replace('\\', '/')  # File PATH：用戶自定義指定的詞庫（字典）文檔的存儲位置，用戶字典可以包含一些特定的詞匯，以提高對特定詞匯的識別準確性，用戶字典文件應爲純文本文檔，每行一個詞匯 Specify the location of user words file.
# print(tesseract_user_words)
tesseract_user_patterns = ""  # File PATH：用戶自定義指定的特定格式文本的文檔的存儲位置，即每行使用「某種正則表達式」，例如，正在掃描具有相同格式數據的多張頁面，即可使用此參數，特定格式文本的文檔應爲純文本文檔，每行一個正則表達式模式 Specify the location of user patterns file.
tesseract_timeout = float(0.0)  # 表示設置字符（Character）識別的超時時長，單位爲：毫秒 ms，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
tesseract_config = '--psm 3 --oem 3'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
tabel_tesseract_config = input_tabel_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
measuringRuler_tesseract_config = input_measuringRuler_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
# input_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
inputTrain_path = default_inputTrain_path  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
inputValidation_path = default_inputValidation_path  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
inputTest_path = default_inputTest_path  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
do_Function = do_data  # 用於接收執行功能的函數 "do_data";
# output_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')
outputTest_path = default_outputTest_path  # 用於輸出傳值的媒介文檔 "../temp/intermediary_write_Python.txt";
outputTest_URL = default_outputTest_URL
temp_cache_IO_data_dir = ""  # 用於暫存輸入輸出傳值文檔的媒介目錄 temp_cache_IO_data_dir = "../temp/";
number_Worker_process = int(0)  # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
time_sleep = float(0.01)  # float(0.05) 用於監聽程序的輪詢延遲參數，單位（秒）;
screenwidth = int(0)  # int(tk.Tk().winfo_screenwidth())  # 獲取顯示器屏幕寬度;
screenheight = int(0)  # int(tk.Tk().winfo_screenheight())  # 獲取顯示器屏幕高度;


# os.path.abspath(".")  # 獲取當前文檔所在的絕對路徑;
# os.path.abspath("..")  # 獲取當前文檔所在目錄的上一層路徑;
configFile = str(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.txt")).replace('\\', '/')  # "C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt" # "/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt"
# configFile = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config.txt"))  # "C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt" # "/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt"
# configFile = pathlib.Path(os.path.abspath("..") + "config.txt")  # pathlib.Path("../config.txt")
# print(configFile)
# 控制臺傳參，通過 sys.argv 數組獲取從控制臺傳入的配置文檔（config.txt）參數的保存路徑全名："C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt" "/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt" ;
# print(type(sys.argv))
# print(sys.argv)
if len(sys.argv) > 1:
    for i in range(len(sys.argv)):
        # print('arg '+ str(i), sys.argv[i])  # 通過 sys.argv 數組獲取從控制臺傳入的參數
        if i > 0:
            # 使用函數 isinstance(sys.argv[i], str) 判斷傳入的參數是否為 str 字符串類型 type(sys.argv[i]);
            if isinstance(sys.argv[i], str) and sys.argv[i] != "" and sys.argv[i].find("=", 0, int(len(sys.argv[i])-1)) != -1:
                if sys.argv[i].split("=", -1)[0] == "configFile":
                    configFile = sys.argv[i].split("=", -1)[1]  # 指定的配置文檔（config.txt）保存路徑全名："C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt" "/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt" ;
                    # print("Config file:", configFile)
                    break
                    # continue
                # 用於監聽程序的輪詢延遲參數，單位（秒） time_sleep = float(0.02);
                elif sys.argv[i].split("=", -1)[0] == "time_sleep":
                    time_sleep = float(sys.argv[i].split("=", -1)[1])  # 用於監聽程序的輪詢延遲參數，單位（秒） time_sleep = float(0.02);
                    # print("Operation document time sleep:", time_sleep)
                    continue
                else:
                    # print(sys.argv[i], "unrecognized.")
                    # sys.exit(1)  # 中止當前進程，退出當前程序;
                    continue


# 讀取配置文檔（config.txt）裏的參數;
# "/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt"
# "C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt"
if configFile != "":
    # 使用Python原生模組os判斷目錄或文檔是否存在以及是否為文檔;
    if os.path.exists(configFile) and os.path.isfile(configFile):
        # print(configFile, "is a file 是一個文檔.")

        # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
        # if not (os.access(configFile, os.R_OK) and os.access(configFile, os.W_OK)):
        if not (os.access(configFile, os.R_OK)):
            try:
                # 修改文檔權限 mode:777 任何人可讀寫;
                os.chmod(configFile, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                # os.chmod(configFile, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                # os.chmod(configFile, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                # os.chmod(configFile, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                # os.chmod(configFile, stat.S_IWOTH)  # 可被其它用戶寫入;
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
                print(f'Error: {configFile} : {error.strerror}')
                print("配置文檔 [ " + configFile + " ] 無法修改為可讀可寫權限.")
                # return configFile

        # if os.access(configFile, os.R_OK) and os.access(configFile, os.W_OK):
        if os.access(configFile, os.R_OK):

            fd = open(configFile, mode="r", buffering=-1, encoding="utf-8", errors=None, newline=None, closefd=True, opener=None)
            # fd = open(configFile, mode="rb+")
            try:
                print("Config file = " + str(configFile))
                # data_Str = fd.read()
                # data_Str = fd.read().decode("utf-8")
                # data_Bytes = data_Str.encode("utf-8")
                # fd.write(data_Bytes)
                lines = fd.readlines()
                line_I = int(0)
                for line in lines:
                    # print(line)

                    line_I = line_I + 1
                    line_Key = ""
                    line_Value = ""

                    # 使用函數 isinstance(line, str) 判斷傳入的參數是否為 str 字符串類型 type(line);
                    if isinstance(line, str) and line != "":

                        if line.find("\r\n", 0, int(len(line) + 1)) != -1:
                            line = line.replace('\r\n', '')  # 刪除行尾的換行符（\r\n）;
                        elif line.find("\r", 0, int(len(line))) != -1:
                            line = line.replace('\r', '')  # 刪除行尾的換行符（\r）;
                        elif line.find("\n", 0, int(len(line))) != -1:
                            line = line.replace('\n', '')  # 刪除行尾的換行符（\n）;
                        else:
                            line = line.strip(' ')  # 刪除行首尾的空格字符（' '）;

                        # 判斷字符串是否含有等號字符（=）連接符（Key=Value），若含有等號字符（=），則以等號字符（=）分割字符串;
                        if line.find("=", 0, int(len(line)-1)) != -1:
                            # line_split = line.split("=", -1)  # 分割字符串中含有的所有等號字符（=）;
                            line_split = line.split("=", 1)  # 祇分割字符串中含有的第一個等號字符（=）;
                            if len(line_split) == 1:
                                if str(line_split[0]) != "":
                                    line_Key = str(line_split[0]).strip(' ')  # 刪除字符串首尾的空格字符（' '）;
                            if len(line_split) > 1:
                                if str(line_split[0]) != "":
                                    line_Key = str(line_split[0]).strip(' ')  # 刪除字符串首尾的空格字符（' '）;
                                if str(line_split[1]) != "":
                                    line_Value = str(line_split[1]).strip(' ')  # 刪除字符串首尾的空格字符（' '）;
                        else:
                            line_Value = line

                        # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
                        if line_Key == "is_window":
                            # is_window = bool(line_Value)  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
                            if line_Value == "True":
                                is_window = True  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
                            elif line_Value == "False":
                                is_window = False  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
                            elif int(line_Value) >= int(1):
                                is_window = True  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
                            elif int(line_Value) == int(0):
                                is_window = False  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
                            # else:
                            # print("Is window:", is_window)
                            continue
                        # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程）可取值：is_Concurrent = 0 or "0" or "Multi-Threading" or "Multi-Processes";
                        elif line_Key == "is_Concurrent":
                            is_Concurrent = str(line_Value)  # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程），可取值：is_Concurrent = 0 or "0" or "Multi-Threading" or "Multi-Processes";
                            # print("Is Monitor Concurrent:", is_Concurrent)
                            continue
                        # 用於判斷存儲位置：is_storage_position = "Database", "Database_and_Disk", "Disk" ;
                        elif line_Key == "is_storage_position":
                            is_storage_position = line_Value  # 用於判斷存儲位置：is_storage_position = "Database", "Database_and_Disk", "Disk" ;
                            # print("storage position:", is_storage_position)
                            continue
                        # 用於判斷存儲類型：is_storage_type = "json", "csv", "txt", "xlsx" ;
                        elif line_Key == "is_storage_type":

                            is_storage_type = line_Value  # 用於判斷存儲類型：is_storage_type = "json", "csv", "txt", "xlsx" ;
                            # print("storage type:", is_storage_type)

                            if not (is_storage_type == "json" or is_storage_type == "csv" or is_storage_type == "txt" or is_storage_type == "xlsx"):
                                # sys.stdout.write("\n")  # 輸出換行;
                                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(is_storage_type))  # 將字符串輸出寫到操作系統控制臺;
                                # sys.stdout.write("\n")  # 輸出換行;
                                print("參數錯誤." + "\n" + "傳入的運算結果的輸出檔類型:" + "\n" + "[ " + is_storage_type + " ]" + "\n" + "不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                                # Error_Log.append(is_storage_type)
                                sys.exit(1)  # 中止當前進程，退出當前程序;

                            if len(is_storage_type) > 0:

                                if len(default_outputTest_path) > 0:
                                    if default_outputTest_path.find(".", 0, int(len(default_outputTest_path)-1)) != -1:
                                        # del default_outputTest_path.split('.')[len(default_outputTest_path.split('.'))-1]
                                        default_outputTest_path = str(''.join(default_outputTest_path.split('.')[0:len(default_outputTest_path.split('.'))-1])) + "." + is_storage_type
                                    else:
                                        default_outputTest_path = default_outputTest_path + "." + is_storage_type
                                # print("default output test path:", default_outputTest_path)

                                if len(outputTest_path) > 0:
                                    if outputTest_path.find(".", 0, int(len(outputTest_path)-1)) != -1:
                                        # del outputTest_path.split('.')[len(outputTest_path.split('.'))-1]
                                        outputTest_path = str(''.join(outputTest_path.split('.')[0:len(outputTest_path.split('.'))-1])) + "." + is_storage_type
                                    else:
                                        outputTest_path = outputTest_path + "." + is_storage_type
                                # print("output test path:", outputTest_path)

                                # if is_storage_type == "json":
                                #     Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                                #     Radiobutton_storage_type_txt.deselect()
                                #     Radiobutton_storage_type_Excel.deselect()
                                #     Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                                # elif is_storage_type == "csv":
                                #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                                #     Radiobutton_storage_type_txt.deselect()
                                #     Radiobutton_storage_type_Excel.deselect()
                                #     Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                                # elif is_storage_type == "txt":
                                #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                                #     Radiobutton_storage_type_csv.deselect()
                                #     Radiobutton_storage_type_Excel.deselect()
                                #     Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                                # elif is_storage_type == "xlsx":
                                #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                                #     Radiobutton_storage_type_csv.deselect()
                                #     Radiobutton_storage_type_txt.deselect()
                                #     Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                                # elif len(is_storage_type) == 0:
                                #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                                #     Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                                #     Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                                #     Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                                # else:
                                #     # sys.stdout.write("\n")  # 輸出換行;
                                #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(is_storage_type))  # 將字符串輸出寫到操作系統控制臺;
                                #     # sys.stdout.write("\n")  # 輸出換行;
                                #     print("參數錯誤." + "\n" + "傳入的運算結果的輸出檔類型:" + "\n" + "[ " + is_storage_type + " ]" + "\n" + "不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                                #     # Error_Log.append(is_storage_type)
                                #     sys.exit(1)  # 中止當前進程，退出當前程序;
                            else:
                                # sys.stdout.write("\n")  # 輸出換行;
                                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(is_storage_type))  # 將字符串輸出寫到操作系統控制臺;
                                # sys.stdout.write("\n")  # 輸出換行;
                                print("參數錯誤." + "\n" + "傳入的運算結果的輸出檔類型:" + "\n" + "[ " + is_storage_type + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                                # Error_Log.append(is_storage_type)
                                sys.exit(1)  # 中止當前進程，退出當前程序;

                            continue

                        # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置 tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe";
                        elif line_Key == "tesseract_cmd":
                            tesseract_cmd = line_Value  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置 "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe";
                            # print("Tesseract Cmd:", tesseract_cmd)
                            continue
                        # 指定第三方庫「Tesseract-OCR」的用戶自定義指定本地訓練完畢的數據集文檔（tessdata）的儲存路徑位置 tesseract_tessdata_dir = "/usr/share/tessdata";
                        elif line_Key == "tesseract_tessdata_dir":
                            tesseract_tessdata_dir = line_Value  # File PATH：用戶自定義指定本地訓練完畢的數據集文檔（tessdata）的儲存路徑位置，使用 Tesseract 識別，需要使用訓練好的數據集，如果不指定該參數，則預設使用系統預設的數據集文檔目錄 Specify the location of tessdata path.
                            # print("Tesseract tessdata directory:", tesseract_tessdata_dir)
                            continue
                        # 指定第三方庫「Tesseract-OCR」的用戶自定義指定的詞庫（字典）文檔的存儲位置 tesseract_user_words = "/usr/share/tessdata";
                        elif line_Key == "tesseract_user_words":
                            tesseract_user_words = line_Value  # File PATH：用戶自定義指定的詞庫（字典）文檔的存儲位置，用戶字典可以包含一些特定的詞匯，以提高對特定詞匯的識別準確性，用戶字典文件應爲純文本文檔，每行一個詞匯 Specify the location of user words file.
                            # print("Tesseract user words:", tesseract_user_words)
                            continue
                        # 指定第三方庫「Tesseract-OCR」的用戶自定義指定的特定格式文本的文檔的存儲位置 tesseract_user_patterns = "/usr/share/tessdata";
                        elif line_Key == "tesseract_user_patterns":
                            tesseract_user_patterns = line_Value  # File PATH：用戶自定義指定的特定格式文本的文檔的存儲位置，即每行使用「某種正則表達式」，例如，正在掃描具有相同格式數據的多張頁面，即可使用此參數，特定格式文本的文檔應爲純文本文檔，每行一個正則表達式模式 Specify the location of user patterns file.
                            # print("Tesseract user patterns:", tesseract_user_patterns)
                            continue
                        # 表示設置字符（Character）識別的超時時長，單位（秒） tesseract_timeout = float(0.02)，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
                        elif line_Key == "tesseract_timeout":
                            tesseract_timeout = float(line_Value)  # 表示設置字符（Character）識別的超時時長，單位（秒） tesseract_timeout = float(0.02)，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
                            # print("Tesseract timeout:", tesseract_timeout)
                            continue
                        # 用於輸入傳值的媒介目錄 input_dir = "../temp/";
                        elif line_Key == "input_dir":
                            input_dir = line_Value  # 用於輸入傳值的媒介目錄 "../temp/";
                            # print("input dir:", input_dir)
                            continue
                        # 用於配置 Google Tesseract 的參數（tesseract_config）：input_tabel_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";
                        # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                        elif line_Key == "input_tabel_tesseract_config":
                            input_tabel_tesseract_config = line_Value  # 用於配置 Google Tesseract 的參數（tesseract_config）：input_tabel_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";;
                            # print("input tabel tesseract config:", input_tabel_tesseract_config)
                            continue
                        # 用於配置 Google Tesseract 的參數（tesseract_config）：input_measuringRuler_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";
                        # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                        elif line_Key == "input_measuringRuler_tesseract_config":
                            input_measuringRuler_tesseract_config = line_Value  # 用於配置 Google Tesseract 的參數（tesseract_config）：input_measuringRuler_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";;
                            # print("input measuring ruler tesseract config:", input_measuringRuler_tesseract_config)
                            continue
                        # 用於接收傳值的媒介文檔 inputTrain_path = "../temp/intermediary_write_Node.txt";
                        elif line_Key == "inputTrain_path":
                            inputTrain_path = line_Value  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
                            # print("input train path:", inputTrain_path)
                            default_inputTrain_path = line_Value
                            # print("default input train path:", default_inputTrain_path)
                            continue
                        # 用於接收傳值的媒介文檔 inputValidation_path = "../temp/intermediary_write_Node.txt";
                        elif line_Key == "inputValidation_path":
                            inputValidation_path = line_Value  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
                            # print("input validation path:", inputValidation_path)
                            default_inputValidation_path = line_Value
                            # print("default input validation path:", default_inputValidation_path)
                            continue
                        # 用於接收傳值的媒介文檔 inputTest_path = "../temp/intermediary_write_Node.txt";
                        elif line_Key == "inputTest_path":
                            inputTest_path = line_Value  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
                            # print("input test path:", inputTest_path)
                            default_inputTest_path = line_Value
                            # print("default input test path:", default_inputTest_path)
                            continue
                        # 用於暫存輸入輸出傳值文檔的媒介目錄 temp_cache_IO_data_dir = "../temp/";
                        # elif line_Key == "temp_cache_IO_data_dir":
                        #     temp_cache_IO_data_dir = line_Value  # 用於輸入傳值的媒介目錄 "../temp/";
                        #     # print("temp cache IO data file dir:", temp_cache_IO_data_dir)
                        #     continue
                        # 用於操作硬盤文檔讀取或寫入的函數 Input_and_Output_Function = "Input_and_Output";
                        elif line_Key == "Input_and_Output_Function":
                            Input_and_Output_Function = line_Value  # 用於操作硬盤文檔讀取或寫入的函數 "Input_and_Output";
                            # print("Input and Output Function:", Input_and_Output_Function)
                            continue
                        # 用於接收執行功能的函數 do_Function = "do_data";
                        elif line_Key == "do_Function":
                            do_Function = line_Value  # 用於接收執行功能的函數 "do_data";
                            # print("do Function:", do_Function)
                            continue
                        # 用於輸出傳值的媒介目錄 input_dir = "../temp/";
                        elif line_Key == "output_dir":
                            output_dir = line_Value  # 用於輸出傳值的媒介目錄 "../temp/";
                            # print("output dir:", output_dir)
                            continue
                        # 用於輸出傳值的媒介文檔 outputTest_path = "../temp/intermediary_write_Python.txt";
                        elif line_Key == "outputTest_path":

                            outputTest_path = line_Value  # 用於輸出傳值的媒介文檔 "../temp/intermediary_write_Python.txt";
                            # print("output test path:", outputTest_path)
                            default_outputTest_path = line_Value
                            # print("default output test path:", default_outputTest_path)

                            if len(outputTest_path) > 0:
                                if outputTest_path.find(".", 0, int(len(outputTest_path)-1)) != -1:

                                    is_storage_type = str(outputTest_path.split('.')[len(outputTest_path.split('.'))-1])
                                    # print("storage type:", is_storage_type)

                                    if not (is_storage_type == "json" or is_storage_type == "csv" or is_storage_type == "txt" or is_storage_type == "xlsx"):
                                        # sys.stdout.write("\n")  # 輸出換行;
                                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                                        # sys.stdout.write("\n")  # 輸出換行;
                                        print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                                        # Error_Log.append(outputTest_path)
                                        sys.exit(1)  # 中止當前進程，退出當前程序;

                                    # if is_storage_type == "json":
                                    #     Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                                    #     Radiobutton_storage_type_txt.deselect()
                                    #     Radiobutton_storage_type_Excel.deselect()
                                    #     Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                                    # elif is_storage_type == "csv":
                                    #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                                    #     Radiobutton_storage_type_txt.deselect()
                                    #     Radiobutton_storage_type_Excel.deselect()
                                    #     Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                                    # elif is_storage_type == "txt":
                                    #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                                    #     Radiobutton_storage_type_csv.deselect()
                                    #     Radiobutton_storage_type_Excel.deselect()
                                    #     Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                                    # elif is_storage_type == "xlsx":
                                    #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                                    #     Radiobutton_storage_type_csv.deselect()
                                    #     Radiobutton_storage_type_txt.deselect()
                                    #     Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                                    # elif len(is_storage_type) == 0:
                                    #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                                    #     Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                                    #     Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                                    #     Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                                    # else:
                                    #     # sys.stdout.write("\n")  # 輸出換行;
                                    #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                                    #     # sys.stdout.write("\n")  # 輸出換行;
                                    #     print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                                    #     # Error_Log.append(outputTest_path)
                                    #     sys.exit(1)  # 中止當前進程，退出當前程序;
                                else:
                                    # sys.stdout.write("\n")  # 輸出換行;
                                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                                    # sys.stdout.write("\n")  # 輸出換行;
                                    print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + outputTest_path + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                                    # Error_Log.append(outputTest_path)
                                    sys.exit(1)  # 中止當前進程，退出當前程序;

                            continue

                        # 用於用於保存運算結果的數據庫服務器網址 outputTest_URL = "mongodb://username:password@127.0.0.1:27017/test-movie?authSource=admin&retryWrites=true&w=majority";
                        elif line_Key == "outputTest_URL":
                            outputTest_URL = line_Value  # 用於用於保存運算結果的數據庫服務器網址 outputTest_URL = "mongodb://username:password@127.0.0.1:27017/test-movie?authSource=admin&retryWrites=true&w=majority";
                            # print("output test url:", outputTest_URL)
                            default_outputTest_URL = line_Value
                            # print("default output test url:", default_outputTest_URL)
                            continue
                        # # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
                        # elif line_Key == "number_Worker_process":
                        #     number_Worker_process = int(line_Value)  # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
                        #     # print("number Worker processes:", number_Worker_process)
                        #     continue
                        # 用於監聽程序的輪詢延遲參數，單位（秒） time_sleep = float(0.02);
                        elif line_Key == "time_sleep":
                            time_sleep = float(line_Value)  # 用於監聽程序的輪詢延遲參數，單位（秒） time_sleep = float(0.02);
                            # print("Operation document time sleep:", time_sleep)
                            continue
                        # elif line_Key == "screenwidth":
                        #     screenwidth = int(line_Value)  # 顯示屏寬度，單位：像素;
                        #     # print("Screen width:", screenwidth)
                        #     continue
                        # elif line_Key == "screenheight":
                        #     screenheight = int(line_Value)  # 顯示屏高度，單位：像素;
                        #     # print("Screen height:", screenheight)
                        #     continue
                        else:
                            # print(line, "unrecognized.")
                            # sys.exit(1)  # 中止當前進程，退出當前程序;
                            continue

            except FileNotFoundError:
                print("配置文檔 [ " + configFile + " ] 不存在.")
            # except PersmissionError:
            #     print("配置文檔 [ " + configFile + " ] 沒有打開權限.")
            except Exception as error:
                if("[WinError 32]" in str(error)):
                    print("配置文檔 [ " + configFile + " ] 無法讀取數據.")
                    print(f'Error: {configFile} : {error.strerror}')
                    # print("延時等待 " + str(time_sleep) + " (秒)後, 重複嘗試讀取文檔 " + configFile)
                    # time.sleep(time_sleep)  # 用於讀取文檔時延遲參數，以防文檔被占用錯誤，單位（秒）;
                    # try:
                    #     data_Str = fd.read()
                    #     # data_Str = fd.read().decode("utf-8")
                    #     # data_Bytes = data_Str.encode("utf-8")
                    #     # fd.write(data_Bytes)
                    # except OSError as error:
                    #     print("配置文檔 [ " + configFile + " ] 無法讀取數據.")
                    #     print(f'Error: {configFile} : {error.strerror}')
                else:
                    print(f'Error: {configFile} : {error.strerror}')
            finally:
                fd.close()
            # 注：可以用try/finally語句來確保最後能關閉檔，不能把open語句放在try塊裡，因為當打開檔出現異常時，檔物件file_object無法執行close()方法;

    else:
        print("Config file: [ ", str(configFile), " ] unrecognized.")
        # sys.exit(1)  # 中止當前進程，退出當前程序;


# # 使用 while True: 的方法設置死循環創建看守進程，監聽指定的硬盤目錄或文檔，響應創建事件，從而達到不同語言之間利用硬盤文檔傳輸數據交互的效果;
# # 控制臺傳參，通過 sys.argv 數組獲取從控制臺傳入的參數
# is_window = True  # bool(True), bool(False) 判斷只需要執行一次還是啓動監聽服務器功能;
# is_Concurrent = "Multi-Threading"  # 選擇監聽動作的函數是否並發（多協程、多缐程、多進程），可取值：0、"0"、"Multi-Threading"、"Multi-Processes";
# # is_storage_position = "Disk"  # 判斷存儲位置，可取值："Database", "Database_and_Disk", "Disk" ;
# # is_storage_type = "csv"  # 判斷存儲類型，可取值："json", "csv", "txt", "xlsx";
# # os.path.abspath(".")  # 獲取當前文檔所在的絕對路徑;
# # os.path.abspath("..")  # 獲取當前文檔所在目錄的上一層路徑;
# default_input_tabel_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
# default_input_measuringRuler_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
# input_tabel_tesseract_config = default_input_tabel_tesseract_config
# input_measuringRuler_tesseract_config = default_input_measuringRuler_tesseract_config
# tesseract_cmd = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tesseract"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# # tesseract_cmd = str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# # tesseract_cmd = str(pathlib.Path(os.path.abspath("..") + "/Tesseract-OCR/" + "/tesseract/"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# # print(tesseract_cmd)
# # pytesseract.pytesseract.tesseract_cmd = tesseract_cmd  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# tesseract_tessdata_dir = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tessdata", "chi_tra.traineddata"))  # "/usr/share/tessdata" # File PATH：用戶自定義指定本地訓練完畢的數據集文檔（tessdata）的儲存路徑位置，使用 Tesseract 識別，需要使用訓練好的數據集，如果不指定該參數，則預設使用系統預設的數據集文檔目錄 Specify the location of tessdata path.
# # print(tesseract_tessdata_dir)
# tesseract_user_words = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tesswords"))  # File PATH：用戶自定義指定的詞庫（字典）文檔的存儲位置，用戶字典可以包含一些特定的詞匯，以提高對特定詞匯的識別準確性，用戶字典文件應爲純文本文檔，每行一個詞匯 Specify the location of user words file.
# # print(tesseract_user_words)
# tesseract_user_patterns = ""  # File PATH：用戶自定義指定的特定格式文本的文檔的存儲位置，即每行使用「某種正則表達式」，例如，正在掃描具有相同格式數據的多張頁面，即可使用此參數，特定格式文本的文檔應爲純文本文檔，每行一個正則表達式模式 Specify the location of user patterns file.
# tesseract_config = '--psm 3 --oem 3'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
# tabel_tesseract_config = input_tabel_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
# measuringRuler_tesseract_config = input_measuringRuler_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
# # input_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
# inputTrain_path = default_inputTrain_path  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
# inputValidation_path = default_inputValidation_path  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
# inputTest_path = default_inputTest_path  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
# do_Function = do_data  # 用於接收執行功能的函數 "do_data";
# # output_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')
# outputTest_path = default_outputTest_path  # 用於輸出傳值的媒介文檔 "../temp/intermediary_write_Python.txt";
# outputTest_URL = default_outputTest_URL
# temp_cache_IO_data_dir = ""  # 用於暫存輸入輸出傳值文檔的媒介目錄 temp_cache_IO_data_dir = "../temp/";
# number_Worker_process = int(0)  # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
# time_sleep = float(0.01)  # float(0.05) 用於監聽程序的輪詢延遲參數，單位（秒）;
# screenwidth = int(0)  # int(tk.Tk().winfo_screenwidth())  # 獲取顯示器屏幕寬度;
# screenheight = int(0)  # int(tk.Tk().winfo_screenheight())  # 獲取顯示器屏幕高度;
# 控制臺傳參，通過 sys.argv 數組獲取從控制臺傳入的參數
# print(type(sys.argv))
# print(sys.argv)
if len(sys.argv) > 1:
    for i in range(len(sys.argv)):
        # print('arg '+ str(i), sys.argv[i])  # 通過 sys.argv 數組獲取從控制臺傳入的參數
        if i > 0:
            # 使用函數 isinstance(sys.argv[i], str) 判斷傳入的參數是否為 str 字符串類型 type(sys.argv[i]);
            if isinstance(sys.argv[i], str) and sys.argv[i] != "" and sys.argv[i].find("=", 0, int(len(sys.argv[i])-1)) != -1:
                # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
                if sys.argv[i].split("=", -1)[0] == "is_window":
                    # is_window = bool(sys.argv[i].split("=", -1)[1])  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
                    if sys.argv[i].split("=", -1)[1] == "True":
                        is_window = True  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
                    elif sys.argv[i].split("=", -1)[1] == "False":
                        is_window = False  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
                    elif int(sys.argv[i].split("=", -1)[1]) >= int(1):
                        is_window = True  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
                    elif int(sys.argv[i].split("=", -1)[1]) == int(0):
                        is_window = False  # 判斷只需要執行一次還是啓動監聽服務器功能 is_window = True;
                    # else:
                    # print("Is window:", is_window)
                    continue
                # 選擇監聽動作的函數是否並發（多協程、多缐程、多進程）可取值：is_Concurrent = 0 or "0" or "Multi-Threading" or "Multi-Processes";
                elif sys.argv[i].split("=", -1)[0] == "is_Concurrent":
                    is_Concurrent = str(sys.argv[i].split("=", -1)[1])  # 選擇監聽動作的函數是否並發（多協程、多缐程、多進程），可取值：is_Concurrent = 0 or "0" or "Multi-Threading" or "Multi-Processes";
                    # print("Is Monitor Concurrent:", is_Concurrent)
                    continue
                # 用於判斷存儲位置：is_storage_position = "Database", "Database_and_Disk", "Disk" ;
                elif sys.argv[i].split("=", -1)[0] == "is_storage_position":
                    is_storage_position = sys.argv[i].split("=", -1)[1]  # 用於判斷存儲位置：is_storage_position = "Database", "Database_and_Disk", "Disk" ;
                    # print("storage position:", is_storage_position)
                    continue
                # 用於判斷存儲類型：is_storage_type = "json", "csv", "txt", "xlsx" ;
                elif sys.argv[i].split("=", -1)[0] == "is_storage_type":

                    is_storage_type = sys.argv[i].split("=", -1)[1]  # 用於判斷存儲類型：is_storage_type = "json", "csv", "txt", "xlsx" ;
                    # print("storage type:", is_storage_type)

                    if not (is_storage_type == "json" or is_storage_type == "csv" or is_storage_type == "txt" or is_storage_type == "xlsx"):
                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(is_storage_type))  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        print("參數錯誤." + "\n" + "傳入的運算結果的輸出檔類型:" + "\n" + "[ " + is_storage_type + " ]" + "\n" + "不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                        # Error_Log.append(is_storage_type)
                        sys.exit(1)  # 中止當前進程，退出當前程序;

                    if len(is_storage_type) > 0:

                        if len(default_outputTest_path) > 0:
                            if default_outputTest_path.find(".", 0, int(len(default_outputTest_path)-1)) != -1:
                                # del default_outputTest_path.split('.')[len(default_outputTest_path.split('.'))-1]
                                default_outputTest_path = str(''.join(default_outputTest_path.split('.')[0:len(default_outputTest_path.split('.'))-1])) + "." + is_storage_type
                            else:
                                default_outputTest_path = default_outputTest_path + "." + is_storage_type
                        # print("default output test path:", default_outputTest_path)

                        if len(outputTest_path) > 0:
                            if outputTest_path.find(".", 0, int(len(outputTest_path)-1)) != -1:
                                # del outputTest_path.split('.')[len(outputTest_path.split('.'))-1]
                                outputTest_path = str(''.join(outputTest_path.split('.')[0:len(outputTest_path.split('.'))-1])) + "." + is_storage_type
                            else:
                                outputTest_path = outputTest_path + "." + is_storage_type
                        # print("output test path:", outputTest_path)

                        # if is_storage_type == "json":
                        #     Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        #     Radiobutton_storage_type_txt.deselect()
                        #     Radiobutton_storage_type_Excel.deselect()
                        #     Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        # elif is_storage_type == "csv":
                        #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        #     Radiobutton_storage_type_txt.deselect()
                        #     Radiobutton_storage_type_Excel.deselect()
                        #     Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        # elif is_storage_type == "txt":
                        #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        #     Radiobutton_storage_type_csv.deselect()
                        #     Radiobutton_storage_type_Excel.deselect()
                        #     Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                        # elif is_storage_type == "xlsx":
                        #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        #     Radiobutton_storage_type_csv.deselect()
                        #     Radiobutton_storage_type_txt.deselect()
                        #     Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                        # elif len(is_storage_type) == 0:
                        #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                        #     Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                        #     Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                        #     Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                        # else:
                        #     # sys.stdout.write("\n")  # 輸出換行;
                        #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(is_storage_type))  # 將字符串輸出寫到操作系統控制臺;
                        #     # sys.stdout.write("\n")  # 輸出換行;
                        #     print("參數錯誤." + "\n" + "傳入的運算結果的輸出檔類型:" + "\n" + "[ " + is_storage_type + " ]" + "\n" + "不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                        #     # Error_Log.append(is_storage_type)
                        #     sys.exit(1)  # 中止當前進程，退出當前程序;
                    else:
                        # sys.stdout.write("\n")  # 輸出換行;
                        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(is_storage_type))  # 將字符串輸出寫到操作系統控制臺;
                        # sys.stdout.write("\n")  # 輸出換行;
                        print("參數錯誤." + "\n" + "傳入的運算結果的輸出檔類型:" + "\n" + "[ " + is_storage_type + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                        # Error_Log.append(is_storage_type)
                        sys.exit(1)  # 中止當前進程，退出當前程序;

                    continue

                # 用於配置 Google Tesseract 的參數（tesseract_config）：input_tabel_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";
                # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                elif sys.argv[i].split("=", -1)[0] == "input_tabel_tesseract_config":
                    input_tabel_tesseract_config = sys.argv[i].split("=", -1)[1]  # 用於配置 Google Tesseract 的參數（tesseract_config）：input_tabel_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";;
                    # print("input tabel tesseract config:", input_tabel_tesseract_config)
                    default_input_tabel_tesseract_config = sys.argv[i].split("=", -1)[1]
                    # print("default input tabel tesseract config:", default_input_tabel_tesseract_config)
                    tabel_tesseract_config = sys.argv[i].split("=", -1)[1]  # 指定第三方庫「Tesseract-OCR」的用戶自定義指定的識別圖片中的表格（tabel）内的文本的參數 tabel_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                    # print("Tesseract config (table):", tabel_tesseract_config)
                    continue
                # 用於配置 Google Tesseract 的參數（tesseract_config）：input_measuringRuler_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";
                # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                elif sys.argv[i].split("=", -1)[0] == "input_measuringRuler_tesseract_config":
                    input_measuringRuler_tesseract_config = sys.argv[i].split("=", -1)[1]  # 用於配置 Google Tesseract 的參數（tesseract_config）：input_measuringRuler_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";;
                    # print("input measuring ruler tesseract config:", input_measuringRuler_tesseract_config)
                    default_input_measuringRuler_tesseract_config = sys.argv[i].split("=", -1)[1]
                    # print("default input measuring ruler tesseract config:", default_input_measuringRuler_tesseract_config)
                    measuringRuler_tesseract_config = sys.argv[i].split("=", -1)[1]  # 指定第三方庫「Tesseract-OCR」的用戶自定義指定的識別圖片中的測量尺（Measuring Ruler）標識的文本的參數 measuringRuler_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                    # print("Tesseract config (Measuring Ruler):", measuringRuler_tesseract_config)
                    continue
                # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置 tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe";
                elif sys.argv[i].split("=", -1)[0] == "tesseract_cmd":
                    tesseract_cmd = sys.argv[i].split("=", -1)[1]  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置 "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe";
                    # print("Tesseract Cmd:", tesseract_cmd)
                    continue
                # 指定第三方庫「Tesseract-OCR」的用戶自定義指定的識別參數 tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                elif sys.argv[i].split("=", -1)[0] == "tesseract_config":
                    tesseract_config = sys.argv[i].split("=", -1)[1]  # 指定第三方庫「Tesseract-OCR」的用戶自定義指定的識別參數 tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                    # print("Tesseract config:", tesseract_config)
                    continue
                # 指定第三方庫「Tesseract-OCR」的用戶自定義指定的識別圖片中的表格（tabel）内的文本的參數 tabel_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                elif sys.argv[i].split("=", -1)[0] == "tabel_tesseract_config":
                    tabel_tesseract_config = sys.argv[i].split("=", -1)[1]  # 指定第三方庫「Tesseract-OCR」的用戶自定義指定的識別圖片中的表格（tabel）内的文本的參數 tabel_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                    # print("Tesseract config (table):", tabel_tesseract_config)
                    input_tabel_tesseract_config = sys.argv[i].split("=", -1)[1]  # 用於配置 Google Tesseract 的參數（tesseract_config）：input_tabel_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";;
                    # print("input tabel tesseract config:", input_tabel_tesseract_config)
                    default_input_tabel_tesseract_config = sys.argv[i].split("=", -1)[1]
                    # print("default input tabel tesseract config:", default_input_tabel_tesseract_config)
                    continue
                # 指定第三方庫「Tesseract-OCR」的用戶自定義指定的識別圖片中的測量尺（Measuring Ruler）標識的文本的參數 measuringRuler_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                elif sys.argv[i].split("=", -1)[0] == "measuringRuler_tesseract_config":
                    measuringRuler_tesseract_config = sys.argv[i].split("=", -1)[1]  # 指定第三方庫「Tesseract-OCR」的用戶自定義指定的識別圖片中的測量尺（Measuring Ruler）標識的文本的參數 measuringRuler_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                    # print("Tesseract config (Measuring Ruler):", measuringRuler_tesseract_config)
                    input_measuringRuler_tesseract_config = sys.argv[i].split("=", -1)[1]  # 用於配置 Google Tesseract 的參數（tesseract_config）：input_measuringRuler_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";;
                    # print("input measuring ruler tesseract config:", input_measuringRuler_tesseract_config)
                    default_input_measuringRuler_tesseract_config = sys.argv[i].split("=", -1)[1]
                    # print("default input measuring ruler tesseract config:", default_input_measuringRuler_tesseract_config)
                    continue
                # 指定第三方庫「Tesseract-OCR」的用戶自定義指定本地訓練完畢的數據集文檔（tessdata）的儲存路徑位置 tesseract_tessdata_dir = "/usr/share/tessdata";
                elif sys.argv[i].split("=", -1)[0] == "tesseract_tessdata_dir":
                    tesseract_tessdata_dir = sys.argv[i].split("=", -1)[1]  # File PATH：用戶自定義指定本地訓練完畢的數據集文檔（tessdata）的儲存路徑位置，使用 Tesseract 識別，需要使用訓練好的數據集，如果不指定該參數，則預設使用系統預設的數據集文檔目錄 Specify the location of tessdata path.
                    # print("Tesseract tessdata directory:", tesseract_tessdata_dir)
                    continue
                # 指定第三方庫「Tesseract-OCR」的用戶自定義指定的詞庫（字典）文檔的存儲位置 tesseract_user_words = "/usr/share/tessdata";
                elif sys.argv[i].split("=", -1)[0] == "tesseract_user_words":
                    tesseract_user_words = sys.argv[i].split("=", -1)[1]  # File PATH：用戶自定義指定的詞庫（字典）文檔的存儲位置，用戶字典可以包含一些特定的詞匯，以提高對特定詞匯的識別準確性，用戶字典文件應爲純文本文檔，每行一個詞匯 Specify the location of user words file.
                    # print("Tesseract user words:", tesseract_user_words)
                    continue
                # 指定第三方庫「Tesseract-OCR」的用戶自定義指定的特定格式文本的文檔的存儲位置 tesseract_user_patterns = "/usr/share/tessdata";
                elif sys.argv[i].split("=", -1)[0] == "tesseract_user_patterns":
                    tesseract_user_patterns = sys.argv[i].split("=", -1)[1]  # File PATH：用戶自定義指定的特定格式文本的文檔的存儲位置，即每行使用「某種正則表達式」，例如，正在掃描具有相同格式數據的多張頁面，即可使用此參數，特定格式文本的文檔應爲純文本文檔，每行一個正則表達式模式 Specify the location of user patterns file.
                    # print("Tesseract user patterns:", tesseract_user_patterns)
                    continue
                # 表示設置字符（Character）識別的超時時長，單位（秒） tesseract_timeout = float(0.02)，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
                elif sys.argv[i].split("=", -1)[0] == "tesseract_timeout":
                    tesseract_timeout = float(sys.argv[i].split("=", -1)[1])  # 表示設置字符（Character）識別的超時時長，單位（秒） tesseract_timeout = float(0.02)，如果字符（Character）識別耗時超過指定的時長，將引發「pytesseract.pytesseract.TesseractTimeoutError」錯誤;
                    # print("Tesseract timeout:", tesseract_timeout)
                    continue
                # 用於輸入傳值的媒介目錄 input_dir = "../temp/";
                elif sys.argv[i].split("=", -1)[0] == "input_dir":
                    input_dir = sys.argv[i].split("=", -1)[1]  # 用於輸入傳值的媒介目錄 "../temp/";
                    # print("input dir:", input_dir)
                    continue
                # 用於接收傳值的媒介文檔 inputTrain_path = "../temp/intermediary_write_Node.txt";
                elif sys.argv[i].split("=", -1)[0] == "inputTrain_path":
                    inputTrain_path = sys.argv[i].split("=", -1)[1]  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
                    # print("input train path:", inputTrain_path)
                    default_inputTrain_path = sys.argv[i].split("=", -1)[1]
                    # print("default input train path:", default_inputTrain_path)
                    continue
                # 用於接收傳值的媒介文檔 inputValidation_path = "../temp/intermediary_write_Node.txt";
                elif sys.argv[i].split("=", -1)[0] == "inputValidation_path":
                    inputValidation_path = sys.argv[i].split("=", -1)[1]  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
                    # print("input validation path:", inputValidation_path)
                    default_inputValidation_path = sys.argv[i].split("=", -1)[1]
                    # print("default input validation path:", default_inputValidation_path)
                    continue
                # 用於接收傳值的媒介文檔 inputTest_path = "../temp/intermediary_write_Node.txt";
                elif sys.argv[i].split("=", -1)[0] == "inputTest_path":
                    inputTest_path = sys.argv[i].split("=", -1)[1]  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
                    # print("input test path:", inputTest_path)
                    default_inputTest_path = sys.argv[i].split("=", -1)[1]
                    # print("default input test path:", default_inputTest_path)
                    continue
                # 用於暫存輸入輸出傳值文檔的媒介目錄 temp_cache_IO_data_dir = "../temp/";
                elif sys.argv[i].split("=", -1)[0] == "temp_cache_IO_data_dir":
                    temp_cache_IO_data_dir = sys.argv[i].split("=", -1)[1]  # 用於輸入傳值的媒介目錄 "../temp/";
                    # print("temp cache IO data file dir:", temp_cache_IO_data_dir)
                    continue
                # 用於接收執行功能的函數 do_Function = "do_data";
                elif sys.argv[i].split("=", -1)[0] == "do_Function":
                    do_Function = sys.argv[i].split("=", -1)[1]  # 用於接收執行功能的函數 "do_data";
                    # print("do Function:", do_Function)
                    continue
                # 用於輸出傳值的媒介目錄 input_dir = "../temp/";
                elif sys.argv[i].split("=", -1)[0] == "output_dir":
                    output_dir = sys.argv[i].split("=", -1)[1]  # 用於輸出傳值的媒介目錄 "../temp/";
                    # print("output dir:", output_dir)
                    continue
                # 用於輸出傳值的媒介文檔 outputTest_path = "../temp/intermediary_write_Python.txt";
                elif sys.argv[i].split("=", -1)[0] == "outputTest_path":

                    outputTest_path = sys.argv[i].split("=", -1)[1]  # 用於輸出傳值的媒介文檔 "../temp/intermediary_write_Python.txt";
                    # print("output test path:", outputTest_path)
                    default_outputTest_path = sys.argv[i].split("=", -1)[1]
                    # print("default output test path:", default_outputTest_path)

                    if len(outputTest_path) > 0:
                        if outputTest_path.find(".", 0, int(len(outputTest_path)-1)) != -1:

                            is_storage_type = str(outputTest_path.split('.')[len(outputTest_path.split('.'))-1])
                            # print("storage type:", is_storage_type)

                            if not (is_storage_type == "json" or is_storage_type == "csv" or is_storage_type == "txt" or is_storage_type == "xlsx"):
                                # sys.stdout.write("\n")  # 輸出換行;
                                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                                # sys.stdout.write("\n")  # 輸出換行;
                                print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                                # Error_Log.append(outputTest_path)
                                sys.exit(1)  # 中止當前進程，退出當前程序;

                            # if is_storage_type == "json":
                            #     Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                            #     Radiobutton_storage_type_txt.deselect()
                            #     Radiobutton_storage_type_Excel.deselect()
                            #     Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                            # elif is_storage_type == "csv":
                            #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                            #     Radiobutton_storage_type_txt.deselect()
                            #     Radiobutton_storage_type_Excel.deselect()
                            #     Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                            # elif is_storage_type == "txt":
                            #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                            #     Radiobutton_storage_type_csv.deselect()
                            #     Radiobutton_storage_type_Excel.deselect()
                            #     Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                            # elif is_storage_type == "xlsx":
                            #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                            #     Radiobutton_storage_type_csv.deselect()
                            #     Radiobutton_storage_type_txt.deselect()
                            #     Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                            # elif len(is_storage_type) == 0:
                            #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                            #     Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                            #     Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                            #     Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                            # else:
                            #     # sys.stdout.write("\n")  # 輸出換行;
                            #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                            #     # sys.stdout.write("\n")  # 輸出換行;
                            #     print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                            #     # Error_Log.append(outputTest_path)
                            #     sys.exit(1)  # 中止當前進程，退出當前程序;
                        else:
                            # sys.stdout.write("\n")  # 輸出換行;
                            # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                            # sys.stdout.write("\n")  # 輸出換行;
                            print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + outputTest_path + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                            # Error_Log.append(outputTest_path)
                            sys.exit(1)  # 中止當前進程，退出當前程序;

                    continue

                # 用於用於保存運算結果的數據庫服務器網址 outputTest_URL = "mongodb://username:password@127.0.0.1:27017/test-movie?authSource=admin&retryWrites=true&w=majority";
                elif sys.argv[i].split("=", -1)[0] == "outputTest_URL":
                    outputTest_URL = sys.argv[i].split("=", -1)[1]  # 用於用於保存運算結果的數據庫服務器網址 outputTest_URL = "mongodb://username:password@127.0.0.1:27017/test-movie?authSource=admin&retryWrites=true&w=majority";
                    # print("output test url:", outputTest_URL)
                    default_outputTest_URL = sys.argv[i].split("=", -1)[1]
                    # print("default output test url:", default_outputTest_URL)
                    continue
                # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
                elif sys.argv[i].split("=", -1)[0] == "number_Worker_process":
                    number_Worker_process = int(sys.argv[i].split("=", -1)[1])  # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
                    # print("number Worker processes:", number_Worker_process)
                    continue
                # 用於監聽程序的輪詢延遲參數，單位（秒） time_sleep = float(0.02);
                elif sys.argv[i].split("=", -1)[0] == "time_sleep":
                    time_sleep = float(sys.argv[i].split("=", -1)[1])  # 用於監聽程序的輪詢延遲參數，單位（秒） time_sleep = float(0.02);
                    # print("Operation document time sleep:", time_sleep)
                    continue
                # elif sys.argv[i].split("=", -1)[0] == "screenwidth":
                #     screenwidth = int(sys.argv[i].split("=", -1)[1])  # 顯示屏寬度，單位：像素;
                #     # print("Screen width:", screenwidth)
                #     continue
                # elif sys.argv[i].split("=", -1)[0] == "screenheight":
                #     screenheight = int(sys.argv[i].split("=", -1)[1])  # 顯示屏高度，單位：像素;
                #     # print("Screen height:", screenheight)
                #     continue
                else:
                    # print(sys.argv[i], "unrecognized.")
                    # sys.exit(1)  # 中止當前進程，退出當前程序;
                    continue


inputTrain_File_Array = []
inputValidation_File_Array = []
inputTest_File_Array = []
outputTest_File_Array = []

def Path_Conversion(input_Path_String, time_sleep):

    if is_Concurrent == "0" or is_Concurrent == 0:
        global Error_Log

    # global Error_Log
    Error_Log = []

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
                            if is_Concurrent == "0" or is_Concurrent == 0:
                                sys.stdout.write("\n")  # 輸出換行;
                                sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                                sys.stdout.write("\n")  # 輸出換行;
                                # print(error)
                                # print(f'Error: {str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/')} : {error}')
                                # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限.")
                                if is_window:
                                    Label_State['text'] = "運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + " ]" + "\n" + "無法修改為可讀可寫權限."
                            Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))
                            # break
                            continue

                    file_Array.append(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))
                
                else:
                    if is_Concurrent == "0" or is_Concurrent == 0:
                        sys.stdout.write("\n")  # 輸出換行;
                        sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))  # 將字符串輸出寫到操作系統控制臺;
                        sys.stdout.write("\n")  # 輸出換行;
                        # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + " ]" + "\n" + "不存在或者不是檔.")
                        if is_window:
                            Label_State['text'] = "運行錯誤." + "\n" + "檔:" + "\n" + "[ " + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/') + " ]" + "\n" + "不存在或者不是檔."
                    Error_Log.append(str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/'))
                    # break
                    continue

                if is_Concurrent == "0" or is_Concurrent == 0:
                    if is_window:
                        Label_State['text'] = "Parsed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(os.path.join(os.path.normpath(input_Path_String), items_1[i]))).replace('\\', '/')

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
                    if is_Concurrent == "0" or is_Concurrent == 0:
                        sys.stdout.write("\n")  # 輸出換行;
                        sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String) + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                        sys.stdout.write("\n")  # 輸出換行;
                        # print(f'Error: {input_Path_String} : {error}')
                        # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + input_Path_String + " ]" + "\n" + "無法修改為可讀可寫權限.")
                        if is_window:
                            Label_State['text'] = "運行錯誤." + "\n" + "檔:" + "\n" + "[ " + input_Path_String + " ]" + "\n" + "無法修改為可讀可寫權限."
                    Error_Log.append(input_Path_String)
                    return [file_Array, Error_Log, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))]  # None

            file_Array.append(input_Path_String)

            if is_Concurrent == "0" or is_Concurrent == 0:
                if is_window:
                    Label_State['text'] = "Parsed [ 1 ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(input_Path_String)

            # sys.stdout.write("\n")  # 輸出換行;
            # sys.stdout.write("Parsed,1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String))  # 將字符串輸出寫到操作系統控制臺;
            # print("Parsed,1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String))

        else:
            if is_Concurrent == "0" or is_Concurrent == 0:
                sys.stdout.write("\n")  # 輸出換行;
                sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String))  # 將字符串輸出寫到操作系統控制臺;
                sys.stdout.write("\n")  # 輸出換行;
                # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + input_Path_String + " ]" + "\n" + "類型無法識別.")
                if is_window:
                    Label_State['text'] = "運行錯誤." + "\n" + "檔:" + "\n" + "[ " + input_Path_String + " ]" + "\n" + "類型無法識別."
            Error_Log.append(input_Path_String)
            # return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_Path_String

    else:
        if is_Concurrent == "0" or is_Concurrent == 0:
            sys.stdout.write("\n")  # 輸出換行;
            sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Path_String))  # 將字符串輸出寫到操作系統控制臺;
            sys.stdout.write("\n")  # 輸出換行;
            # print("運行錯誤." + "\n" + "檔: " + "\n" + "[ " + input_Path_String + " ]" + "\n" + "不存在.")
            if is_window:
                Label_State['text'] = "運行錯誤." + "\n" + "檔:" + "\n" + "[ " + input_Path_String + " ]" + "\n" + "不存在."
        Error_Log.append(input_Path_String)
        # return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_Path_String

    # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
    if is_Concurrent == "0" or is_Concurrent == 0:
        if is_window:
            Label_State['text'] = "Path parse complete [ " + str(len(file_Array)) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + input_Path_String + " ]."
            # Label_State['text'] = "Stand by"

    # # 使用消息提示框控件給出溫馨提示;
    # tk_messagebox.showinfo(
    #     title = "溫馨提示",
    #     message = str("Path parse complete [ " + str(len(file_Array)) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + input_Path_String + " ].")
    # )

    return [file_Array, Error_Log, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))]  # None


outqueue_from_task_to_host = queue.Queue(maxsize=0)
outqueue_from_host_to_task = queue.Queue(maxsize=0)

def Queue_update(outqueue_from_task_to_host):

    # global inputTrain_File_Array
    # global inputValidation_File_Array
    global inputTest_File_Array
    global outputTest_File_Array
    global image_sample
    global is_Runing
    global is_window

    # outqueue_from_task_to_host = outqueue[0]
    # outqueue_from_host_to_task = outqueue[1]

    try:

        if outqueue_from_task_to_host.empty():
            window_root.after(5, Queue_update, outqueue_from_task_to_host)
            pass

        if not outqueue_from_task_to_host.empty():

            msg = outqueue_from_task_to_host.get(
                block=False,
                timeout=None
            )

            if msg[0] == "Complete":

                # inputTrain_File_Array = []
                # inputValidation_File_Array = []
                inputTest_File_Array = []
                outputTest_File_Array = []

                if is_Runing:
                    is_Runing = not is_Runing
                if is_Runing:
                    Button_start_and_stop_Test['text'] = "Stop Test"
                    Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                else:
                    Button_start_and_stop_Test['text'] = "Start Test"
                    Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

                return_value = str(','.join(msg))
                # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                print(return_value)
                # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                if is_window:
                    Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
                    # Label_State['text'] = "Stand by"

                    Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                    Canvas_display_sample.delete("all")

                # 使用消息提示框控件給出溫馨提示;
                tk_messagebox.showinfo(
                    title = "溫馨提示",
                    message = str('\n'.join(return_value.split(',')))
                )

                return return_value  # None

            elif msg[0] == "Error":

                # inputTrain_File_Array = []
                # inputValidation_File_Array = []
                inputTest_File_Array = []
                outputTest_File_Array = []

                if is_Runing:
                    is_Runing = not is_Runing
                if is_Runing:
                    Button_start_and_stop_Test['text'] = "Stop Test"
                    Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                else:
                    Button_start_and_stop_Test['text'] = "Start Test"
                    Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

                return_value = str(','.join(msg))
                # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                print(return_value)
                # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                if is_window:
                    Label_State['text'] = str('\n'.join(str(','.join(msg)).split(',')))
                    # Label_State['text'] = "Stand by"

                    Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                    Canvas_display_sample.delete("all")

                # 使用消息提示框控件給出溫馨提示;
                tk_messagebox.showinfo(
                    title = "溫馨提示",
                    message = str('\n'.join(return_value.split(',')))
                )

                return return_value  # None

            elif msg[0] == "Discontinue":

                # inputTrain_File_Array = []
                # inputValidation_File_Array = []
                inputTest_File_Array = []
                outputTest_File_Array = []

                if is_Runing:
                    is_Runing = not is_Runing
                if is_Runing:
                    Button_start_and_stop_Test['text'] = "Stop Test"
                    Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                else:
                    Button_start_and_stop_Test['text'] = "Start Test"
                    Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

                return_value = str(','.join(msg))
                # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                print(return_value)
                # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                if is_window:
                    Label_State['text'] = str('\n'.join(str(','.join(msg)).split(',')))
                    # Label_State['text'] = "Stand by"

                    Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                    Canvas_display_sample.delete("all")

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
                if is_window:
                    Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
                    # Label_State['text'] = "Stand by"

                    # Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                    # Canvas_display_sample.delete("all")

                window_root.after(5, Queue_update, outqueue_from_task_to_host)

            elif msg[0] == "image_sample_delete":

                # return_value = str(','.join(msg))
                # # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                # # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                # print(return_value)
                # # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                if is_window:
                    # Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
                    # Label_State['text'] = "Stand by"

                    Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                    Canvas_display_sample.delete("all")
                    image_sample = []

                window_root.after(5, Queue_update, outqueue_from_task_to_host)

            elif msg[0] == "image_sample":

                # return_value = str(','.join(msg))
                # # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                # # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                # print(return_value)
                # # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                if is_window:
                    # Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
                    # Label_State['text'] = "Stand by"

                    Label_display_sample['text'] = str(msg[1])  # "悟空，您好.",
                    image_sample = msg[2]
                    Canvas_display_sample.delete("all")
                    # Canvas_display_sample.delete(tag="one")
                    Canvas_display_sample.create_image(
                        0,
                        0,
                        anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
                        image=image_sample,
                        # fill="red",
                        tag="one"
                    )

                window_root.after(5, Queue_update, outqueue_from_task_to_host)

            elif msg[0] == "Succeed":

                return_value = str(','.join(str(msg[5]).split('\n')))
                print(return_value)

                # 將運算結果寫入用於展示結果的多行文本輸入框;
                if is_window:

                    # Label_State['text'] = "Succeed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(input_Test_File_Array[i])
                    # Label_State['text'] = "Succeed [ " + str(int(i)+1) + " ]." + "\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/')
                    Label_State['text'] = msg[5]

                    # # 讀取多行文本輸入框中的内容;
                    # Text_display_result_value = Text_display_result.get(
                    #     "0.0",  # 表示讀取多行文本輸入框 .Text 控件中的全部值，如果設定參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始讀取;
                    #     "end"  # 表示讀取至多行文本輸入框 .Text 控件中全部值的最後一個字符爲止;
                    # )
                    # Text_display_result_value = str(Text_display_result_value)
                    # print(Text_display_result_value)

                    # # 刪除多行文本輸入框中的内容;
                    # Text_display_result.delete(
                    #     "1.0",  # 參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始刪除;
                    #     "end"  # 參數爲 "end" 表示刪除直至最後一個字符，即清空輸入框;
                    # )

                    # new_Text_display_result_value = Text_display_result_value + str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Test_File_Array[i]) + "," + str(result_Data)

                    # new_Text_display_result_value = str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(input_Test_File_Array[i]) + "," + str(result_Data) + "\n"
                    # new_Text_display_result_value = str(int(i)+1) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(os.path.normpath(str(input_Test_File_Array[i]))).replace('\\', '/') + "\n"
                    # print(new_Text_display_result_value)

                    # 將字符串寫入多行文本輸入框;
                    Text_display_result.insert(
                        "end",  # 參數 "1.0" 表示從第一行第一列開始插入，參數 "insert" 表示在當前光標位置處插入一個字符串，參數 "end" 表示在末尾位置處追加寫入一個字符串;
                        str(msg[4])  # str(new_Text_display_result_value)
                    )

                    Text_display_result.see("end"),  # 表示將 .Text 組件中聚焦在文本末行，即顯示末尾;

                # return_value = str(','.join(msg))
                # # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                # # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                # print(return_value)
                # # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                # Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
                # # Label_State['text'] = "Stand by"

                # Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                # Canvas_display_sample.delete("all")

                window_root.after(5, Queue_update, outqueue_from_task_to_host)

            elif msg[0] == "Wrong":

                return_value = str(','.join(msg))
                # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                print(return_value)
                # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
                if is_window:
                    Label_State['text'] = str('\n'.join(msg))  # str('\n'.join(return_value.split(',')))
                    # Label_State['text'] = "Stand by"

                    # Label_display_sample['text'] = "Input file"  # "悟空，您好.",
                    # Canvas_display_sample.delete("all")

                window_root.after(5, Queue_update, outqueue_from_task_to_host)

        # else:
        #     # By not calling window_root.after here, we allow update to
        #     # truly end
        #     window_root.after(50, Queue_update, (outqueue_from_task_to_host, outqueue_from_host_to_task))
        #     pass
    except queue.Empty:
        window_root.after(5, Queue_update, outqueue_from_task_to_host)


# 函數使用示例;
# 控制臺命令行使用:
# C:\> C:\OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter\Scripts\python.exe C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/main.py configFile=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt is_window=False is_Concurrent=Multi-Threading is_storage_position=Disk is_storage_type=csv input_dir=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/inputTest/ outputTest_path=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/outputTest/test.csv tesseract_cmd=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/tesseract.exe tesseract_tessdata_dir=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tessdata tesseract_user_words=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tesswords input_tabel_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert" input_measuringRuler_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert"
# 啓動運行;
# 參數 C:\OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter\Scripts\python.exe 表示使用隔離環境 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 中的 python.exe 啓動運行;
# 使用示例，自定義類 File_Monitor 硬盤文檔監聽看守進程使用説明;
if __name__ == '__main__':

    # pid = multiprocessing.current_process().pid, threading.currentThread().ident;
    # os.chdir(input_dir)  # 可以先改變工作目錄到 static 路徑;

    if not is_window:

        try:

            if is_Concurrent == "0" or is_Concurrent == 0:

                screenwidth = int(0)
                screenheight = int(0)
                # outqueue_from_task_to_host = None
                # outqueue_from_host_to_task = None

                if not is_Runing:
                    is_Runing = not is_Runing

                complete_Number = int(0)
                Error_Log = []
                file_Data = ""
                result_Data = ""
                image_sample = []

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

                # print(inputTest_path)
                if len(inputTest_File_Array) == 0:
                    if len(inputTest_path) > 0:
                        # inputTest_File_Array = []
                        inputTest_File_Array = Path_Conversion(inputTest_path, time_sleep)[0]

                # print(outputTest_path)
                if len(outputTest_File_Array) == 0:
                    if len(outputTest_path) > 0:
                        # # outputTest_File_Array = []
                        # outputTest_File_Array = Path_Conversion(outputTest_path, time_sleep)[0]
                        outputTest_File_Array = [outputTest_path]

                return_value = ""
                return_value = Run(
                    Path_Conversion,
                    Input_and_Output,
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
                    outqueue_from_host_to_task
                )
                print(return_value)

                # inputTrain_File_Array = []
                # inputValidation_File_Array = []
                inputTest_File_Array = []
                outputTest_File_Array = []

                if is_Runing:
                    is_Runing = not is_Runing

            if is_Concurrent == "Multi-Threading":
                
                if not is_Runing:
                    is_Runing = not is_Runing

                if is_Runing:
                    if is_Concurrent == "Multi-Threading":
                        if outqueue_from_host_to_task:
                            outqueue_from_host_to_task.put(
                                [
                                    "is_Runing_True",
                                    ""
                                ],
                                block=False,
                                timeout=None
                            )
                else:
                    if is_Concurrent == "Multi-Threading":
                        if outqueue_from_host_to_task:
                            outqueue_from_host_to_task.put(
                                [
                                    "is_Runing_False",
                                    ""
                                ],
                                block=False,
                                timeout=None
                            )

                screenwidth = int(0)
                screenheight = int(0)
                complete_Number = int(0)
                Error_Log = []
                file_Data = ""
                result_Data = ""
                image_sample = []

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

                # print(inputTest_path)
                if len(inputTest_File_Array) == 0:
                    if len(inputTest_path) > 0:
                        # inputTest_File_Array = []
                        inputTest_File_Array = Path_Conversion(inputTest_path, time_sleep)[0]

                # print(outputTest_path)
                if len(outputTest_File_Array) == 0:
                    if len(outputTest_path) > 0:
                        # # outputTest_File_Array = []
                        # outputTest_File_Array = Path_Conversion(outputTest_path, time_sleep)[0]
                        outputTest_File_Array = [outputTest_path]

                thr = threading.Thread(
                    target = Run,
                    args = (
                        Path_Conversion,
                        Input_and_Output,
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
                        outqueue_from_host_to_task
                    ),
                    daemon = True  # 把創建的子缐程設爲守護缐程，當主缐程關閉時，子缐程同時關閉，這個標識必須在 .start() 方法調用之前設置;
                )
                thr.start()

                time.sleep(time_sleep)  # 用於讀取文檔時延遲參數，以防文檔被占用錯誤，單位（秒）;

                while not outqueue_from_task_to_host.empty():

                    try:
                        # if outqueue_from_task_to_host.empty():
                        #     window_root.after(5, Queue_update, outqueue_from_task_to_host)
                        #     pass

                        if not outqueue_from_task_to_host.empty():

                            msg = outqueue_from_task_to_host.get(
                                block=False,
                                timeout=None
                            )

                            if msg[0] == "Complete":

                                # inputTrain_File_Array = []
                                # inputValidation_File_Array = []
                                inputTest_File_Array = []
                                outputTest_File_Array = []

                                return_value = str(','.join(msg))
                                # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                                # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                                print(return_value)
                                # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");

                                break

                            if msg[0] == "Error":

                                # inputTrain_File_Array = []
                                # inputValidation_File_Array = []
                                inputTest_File_Array = []
                                outputTest_File_Array = []

                                return_value = str(','.join(msg))
                                # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                                # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                                print(return_value)
                                # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");

                                break

                            elif msg[0] == "Discontinue":

                                # inputTrain_File_Array = []
                                # inputValidation_File_Array = []
                                inputTest_File_Array = []
                                outputTest_File_Array = []

                                return_value = str(','.join(msg))
                                # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                                # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                                print(return_value)
                                # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");

                                break

                            elif msg[0] == "Runing":

                                return_value = str(','.join(msg))
                                # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                                # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                                # print(return_value)
                                # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");

                            # elif msg[0] == "image_sample_delete":

                            #     # return_value = str(','.join(msg))
                            #     # # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                            #     # # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                            #     # print(return_value)
                            #     # # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");

                            # elif msg[0] == "image_sample":

                            #     # return_value = str(','.join(msg))
                            #     # # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                            #     # # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                            #     # print(return_value)
                            #     # # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");

                            elif msg[0] == "Succeed":

                                return_value = str(','.join(str(msg[5]).split('\n')))
                                # # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                                # # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                                print(return_value)
                                # # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");

                            elif msg[0] == "Wrong":

                                return_value = str(','.join(msg))
                                # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
                                # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
                                print(return_value)
                                # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");

                        # else:
                        #     # By not calling window_root.after here, we allow update to
                        #     # truly end
                        #     window_root.after(50, Queue_update, (outqueue_from_task_to_host, outqueue_from_host_to_task))
                        #     break
                    except queue.Empty:
                        break

                    time.sleep(time_sleep)  # 用於讀取文檔時延遲參數，以防文檔被占用錯誤，單位（秒）;

        except Exception as error:
            print(error)
        finally:
            sys.exit(0)  # 中止當前進程，退出當前程序;
        # 注：可以用try/finally語句來確保最後能中止當前進程，退出當前程序;


# 實例化 object，創建窗口;
window_root = tk.Tk()

# 設置窗體標題;
window_root.title('悟空')  # 設置窗體標題;

# 設置窗口北京色爲：全黑色;
# window_root.configure(bg="#ffffff")  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色;

iconbitmap_path = ""
# 判斷是否爲打包（.exe）後的環境;
if getattr(sys, 'frozen', False):
    iconbitmap_path = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Icon", "iconbitmap.png")).replace('\\', '/')
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "Icon", "iconbitmap.png"))).replace('\\', '/')
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "Icon", "iconbitmap.png"))).replace('\\', '/')
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "Icon", "iconbitmap.png"))).replace('\\', '/')
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "Icon", "iconbitmap.png"))).replace('\\', '/')
else:
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "Icon", "iconbitmap.png"))).replace('\\', '/')
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "Icon", "iconbitmap.png"))).replace('\\', '/')
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "Icon", "iconbitmap.png"))).replace('\\', '/')
    # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "Icon", "iconbitmap.png"))).replace('\\', '/')
    iconbitmap_path = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Icon", "iconbitmap.png")).replace('\\', '/')
# print(iconbitmap_path)  # "C:/Criss/OCR/src/Icon/iconbitmap.png"
# 設置窗體徽標;
if os.path.exists(iconbitmap_path) and os.path.isfile(iconbitmap_path):
    window_root.iconbitmap(iconbitmap_path)  # 設置窗體徽標;
else:
    print("Error iconbitmap path: " + "\n" + iconbitmap_path)

# 獲取顯示器屏幕寬度;
screenwidth = int(window_root.winfo_screenwidth())  # 獲取顯示器屏幕寬度;
# print(screenwidth)
# 獲取顯示器屏幕高度;
screenheight = int(window_root.winfo_screenheight())  # 獲取顯示器屏幕高度;
# print(screenheight)

# 設定窗口的大小（寬 × 長），單位爲：像素（px）;
size_XY = '{}x{}+{}+{}'.format(str(int(int(screenwidth)*0.6)), str(int(int(screenheight)*0.6)), str(int(int(screenwidth)*0.2)), str(int(int(screenheight)*0.2)))
window_root.geometry(size_XY)  # 設定窗口的大小（寬 × 長），單位爲：像素（px），注意，這裏的乘號使用小寫字母「x」符號表示;

# 設置隱藏窗口上部的工具欄，注意因爲將不會顯示關閉按鈕，所以無法點擊關閉窗口;
# window_root.overrideredirect(True)  # 設置隱藏窗口上部的工具欄;

# 設置使窗口置頂（顯示爲當前活動窗口）;
# window_root.wm_attributes('-topmost', True)  # 第二個參數取：1 或 True 值，表示設置使窗口保持頂層（顯示爲當前活動窗口，覆蓋其它窗口），第二個參數若取：0 或 False 值，則表示爲正常窗口，允許其它窗口覆蓋;

# window_root.attributes("-toolwindow", True)  #第二個參數取：1 或 True 值，表示設置工具欄樣式窗口;

# 設置窗口的透明性;
window_root.attributes("-alpha", 1.0)
# 設置使窗口默認顔色透明;
# window_root.wm_attributes('-transparentcolor', window_root['bg'])  # 設置使窗口默認顔色透明;

# window_root.withdraw()  # 設置隱藏窗體，不需要事先執行：window_root.update()，因爲直接就不繪製窗體，但會裝在内存裏;
# window_root.state("zoomed")  # 使窗體最大化;
# window_root.state("iconic")  # 使窗體最小化，相當於隱藏窗口;
# window_root.state("normal")  # 使窗體爲：普通窗口;
# window_root.update()  # 刷新窗體介面;

# 設置橫向 x 軸（寬度，左右）方向、縱向 y 軸（高度，上下）方向，是否可以拖曳調整窗體大小，第一個參數表示橫向 x 軸（寬度，左右）方向的可調性，第二個參數表示縱向 y 軸（高度，上下）方向的可調性;
window_root.resizable(False, False)  # 設置橫向 x 軸（寬度，左右）方向、縱向 y 軸（高度，上下）方向，是否可以拖曳調整窗體大小，第一個參數表示橫向 x 軸（寬度，左右）方向的可調性，第二個參數表示縱向 y 軸（高度，上下）方向的可調性;
# window_root.transient(window_root, master=None)

# 創建用於判斷結果存儲位置的標簽框架（tkinter.LabelFrame）組件;
LabelFrame_storage_position = tk.LabelFrame(
    master=window_root,
    text="Result storage position",
    # bg="#ffffff",  # 參數：bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色;
    borderwidth=1.0
)
# 將標簽框架（tkinter.LabelFrame）組件插入窗體介面中;
# LabelFrame_storage_position.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="right",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     # fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     # expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
LabelFrame_storage_position.grid(
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

# 創建複選框（tkinter.Checkbutton）組件;
def select_Checkbutton_storage_position():

    global is_storage_position
    is_storage_position = ""
    if  Checkbutton_storage_position_Database_Var.get() and Checkbutton_storage_position_Disk_Var.get():
        is_storage_position = str(Checkbutton_storage_position_Database['text']) + "_and_" + str(Checkbutton_storage_position_Disk['text'])
    elif Checkbutton_storage_position_Database_Var.get() and not Checkbutton_storage_position_Disk_Var.get():
        is_storage_position = str(Checkbutton_storage_position_Database['text'])
    elif not Checkbutton_storage_position_Database_Var.get() and Checkbutton_storage_position_Disk_Var.get():
        is_storage_position = str(Checkbutton_storage_position_Disk['text'])
    elif not Checkbutton_storage_position_Database_Var.get() and not Checkbutton_storage_position_Disk_Var.get():
        is_storage_position = ""
    else:
        print("參數錯誤." + "\n" + "判斷運算結果存儲在數據庫的複選框值:" + "\n" + str(Checkbutton_storage_position_Database['text']) + "\n" + "無法識別." + "\n" + "判斷運算結果存儲在磁碟文檔的複選框值:" + "\n" + str(Checkbutton_storage_position_Disk['text']) + "\n" + "無法識別.")

        # 使用消息提示框控件給出溫馨提示;
        tk_messagebox.showinfo(
            title = "溫馨提示",
            message = str("參數錯誤." + "\n" + "判斷運算結果存儲在數據庫的複選框值:" + "\n" + str(Checkbutton_storage_position_Database['text']) + "\n" + "無法識別." + "\n" + "判斷運算結果存儲在磁碟文檔的複選框值:" + "\n" + str(Checkbutton_storage_position_Disk['text']) + "\n" + "無法識別.")
        )

    # print("storage position:", is_storage_position)

    global default_outputTest_path
    global outputTest_path
    global outputTestpath
    global default_outputTest_URL
    global outputTest_URL
    global outputTestURL

    if len(str(Entry_outputTest_path.get())) > 0:
        outputTest_path = str(Entry_outputTest_path.get())  # 讀取結果輸出位置文本框輸入的内容;

    if len(str(Entry_outputTest_URL.get())) > 0:
        outputTest_URL = str(Entry_outputTest_URL.get())  # 讀取結果輸出位置文本框輸入的内容;

    if  len(is_storage_position) == 0:

        outputTest_path = ""
        outputTestpath.set(outputTest_path)
        Entry_outputTest_path['textvariable'] = outputTestpath

        # outputTest_URL = ""
        # outputTestURL.set(outputTest_URL)
        # Entry_outputTest_URL['textvariable'] = outputTestURL

        if len(str(Entry_outputTest_path.get())) > 0:
            if str(Entry_outputTest_path.get()).find(".", 0, int(len(str(Entry_outputTest_path.get()))-1)) != -1:

                is_storage_type = str(str(Entry_outputTest_path.get()).split('.')[len(str(Entry_outputTest_path.get()).split('.'))-1])
                # print("storage type:", is_storage_type)

                if not (is_storage_type == "json" or is_storage_type == "csv" or is_storage_type == "txt" or is_storage_type == "xlsx"):
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get())  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                    # Error_Log.append(str(Entry_outputTest_path.get()))
                    return is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get())

                if is_storage_type == "json":
                    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()
                    Radiobutton_storage_type_Excel.deselect()
                    Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                elif is_storage_type == "csv":
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()
                    Radiobutton_storage_type_Excel.deselect()
                    Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                elif is_storage_type == "txt":
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()
                    Radiobutton_storage_type_Excel.deselect()
                    Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                elif is_storage_type == "xlsx":
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()
                    Radiobutton_storage_type_txt.deselect()
                    Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                elif len(is_storage_type) == 0:
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                else:
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(str(Entry_outputTest_path.get())))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                    # Error_Log.append(str(Entry_outputTest_path.get()))
                    return is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get())
            else:
                is_storage_type = ""
                Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                # sys.stdout.write("\n")  # 輸出換行;
                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                # sys.stdout.write("\n")  # 輸出換行;
                print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                # Error_Log.append(str(Entry_outputTest_path.get()))
                return is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get())
        else:
            is_storage_type = ""
            Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
            Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
            Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
            Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

            # # sys.stdout.write("\n")  # 輸出換行;
            # # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
            # # sys.stdout.write("\n")  # 輸出換行;
            # print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(Entry_outputTest_path.get()) + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
            # # Error_Log.append(str(Entry_outputTest_path.get()))
            # return is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get())

    elif is_storage_position == "Database_and_Disk":

        if  len(outputTest_path) == 0:
            outputTestpath.set(default_outputTest_path)
            Entry_outputTest_path['textvariable'] = outputTestpath
        else:
            outputTestpath.set(outputTest_path)
            Entry_outputTest_path['textvariable'] = outputTestpath

        # if  len(outputTest_URL) == 0:
        #     outputTestURL.set(default_outputTest_URL)
        #     Entry_outputTest_URL['textvariable'] = outputTestURL
        # else:
        #     outputTestURL.set(outputTest_URL)
        #     Entry_outputTest_URL['textvariable'] = outputTestURL

        if len(str(Entry_outputTest_path.get())) > 0:
            if str(Entry_outputTest_path.get()).find(".", 0, int(len(str(Entry_outputTest_path.get()))-1)) != -1:

                is_storage_type = str(str(Entry_outputTest_path.get()).split('.')[len(str(Entry_outputTest_path.get()).split('.'))-1])
                # print("storage type:", is_storage_type)

                if not (is_storage_type == "json" or is_storage_type == "csv" or is_storage_type == "txt" or is_storage_type == "xlsx"):
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                    # Error_Log.append(str(Entry_outputTest_path.get()))
                    return is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get())

                if is_storage_type == "json":
                    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()
                    Radiobutton_storage_type_Excel.deselect()
                    Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                elif is_storage_type == "csv":
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()
                    Radiobutton_storage_type_Excel.deselect()
                    Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                elif is_storage_type == "txt":
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()
                    Radiobutton_storage_type_Excel.deselect()
                    Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                elif is_storage_type == "xlsx":
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()
                    Radiobutton_storage_type_txt.deselect()
                    Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                elif len(is_storage_type) == 0:
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                else:
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(str(Entry_outputTest_path.get())))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                    # Error_Log.append(str(Entry_outputTest_path.get()))
                    return is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get())
            else:
                is_storage_type = ""
                Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                # sys.stdout.write("\n")  # 輸出換行;
                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                # sys.stdout.write("\n")  # 輸出換行;
                print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                # Error_Log.append(str(Entry_outputTest_path.get()))
                return is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get())
        else:
            is_storage_type = ""
            Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
            Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
            Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
            Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

            # # sys.stdout.write("\n")  # 輸出換行;
            # # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
            # # sys.stdout.write("\n")  # 輸出換行;
            # print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(Entry_outputTest_path.get()) + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
            # # Error_Log.append(str(Entry_outputTest_path.get()))
            # return is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get())

    elif is_storage_position == "Database":

        outputTest_path = ""
        outputTestpath.set(outputTest_path)
        Entry_outputTest_path['textvariable'] = outputTestpath

        # if  len(outputTest_URL) == 0:
        #     outputTestURL.set(default_outputTest_URL)
        #     Entry_outputTest_URL['textvariable'] = outputTestURL
        # else:
        #     outputTestURL.set(outputTest_URL)
        #     Entry_outputTest_URL['textvariable'] = outputTestURL

    elif is_storage_position == "Disk":

        if  len(outputTest_path) == 0:
            outputTestpath.set(default_outputTest_path)
            Entry_outputTest_path['textvariable'] = outputTestpath
        else:
            outputTestpath.set(outputTest_path)
            Entry_outputTest_path['textvariable'] = outputTestpath

        # outputTest_URL = ""
        # outputTestURL.set(outputTest_URL)
        # Entry_outputTest_URL['textvariable'] = outputTestURL

        if len(str(Entry_outputTest_path.get())) > 0:
            if str(Entry_outputTest_path.get()).find(".", 0, int(len(str(Entry_outputTest_path.get()))-1)) != -1:

                is_storage_type = str(str(Entry_outputTest_path.get()).split('.')[len(str(Entry_outputTest_path.get()).split('.'))-1])
                # print("storage type:", is_storage_type)

                if not (is_storage_type == "json" or is_storage_type == "csv" or is_storage_type == "txt" or is_storage_type == "xlsx"):
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                    # Error_Log.append(str(Entry_outputTest_path.get()))
                    return is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get())

                if is_storage_type == "json":
                    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()
                    Radiobutton_storage_type_Excel.deselect()
                    Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                elif is_storage_type == "csv":
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()
                    Radiobutton_storage_type_Excel.deselect()
                    Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                elif is_storage_type == "txt":
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()
                    Radiobutton_storage_type_Excel.deselect()
                    Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                elif is_storage_type == "xlsx":
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()
                    Radiobutton_storage_type_txt.deselect()
                    Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                elif len(is_storage_type) == 0:
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
                else:
                    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                    Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                    # sys.stdout.write("\n")  # 輸出換行;
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(str(Entry_outputTest_path.get())))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                    # Error_Log.append(str(Entry_outputTest_path.get()))
                    return is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get())
            else:
                is_storage_type = ""
                Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

                # sys.stdout.write("\n")  # 輸出換行;
                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
                # sys.stdout.write("\n")  # 輸出換行;
                print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(Entry_outputTest_path.get()) + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                # Error_Log.append(str(Entry_outputTest_path.get()))
                return is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get())
        else:
            is_storage_type = ""
            Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
            Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
            Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
            Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

            # # sys.stdout.write("\n")  # 輸出換行;
            # # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get()))  # 將字符串輸出寫到操作系統控制臺;
            # # sys.stdout.write("\n")  # 輸出換行;
            # print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + str(Entry_outputTest_path.get()) + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
            # # Error_Log.append(str(Entry_outputTest_path.get()))
            # return is_storage_position  # "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(Entry_outputTest_path.get())

    else:
        print("參數錯誤." + "\n" + "判斷運算結果存儲位置的複選框值:" + "\n" + str(is_storage_position) + "\n" + "無法識別.")

        # 使用消息提示框控件給出溫馨提示;
        tk_messagebox.showinfo(
            title = "溫馨提示",
            message = str("參數錯誤." + "\n" + "判斷運算結果存儲位置的複選框值:" + "\n" + str(is_storage_position) + "\n" + "無法識別.")
        )

    # print("Output test path: ", outputTest_path)
    # print("Output test url: ", outputTest_URL)

    return is_storage_position  # None

# 創建判斷結果存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
Checkbutton_storage_position_Database_Var = tk.BooleanVar(value=False)  # tk.IntVar(value=0)
Checkbutton_storage_position_Database = tk.Checkbutton(
    master=LabelFrame_storage_position,  # 將複選框組件放置在自定義的標簽框架組件内;
    text="Database",
    variable=Checkbutton_storage_position_Database_Var,
    onvalue=True,
    offvalue=False,
    # height=5,
    # width=20,
    state="disabled",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=select_Checkbutton_storage_position
)
# 將複選框（tkinter.Checkbutton）組件插入到標簽框架（tkinter.LabelFrame）組件中;
Checkbutton_storage_position_Database.grid(
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
Checkbutton_storage_position_Disk_Var = tk.BooleanVar(value=True)  # tk.IntVar(value=1)
Checkbutton_storage_position_Disk = tk.Checkbutton(
    master=LabelFrame_storage_position,  # 將複選框組件放置在自定義的標簽框架組件内;
    text="Disk",
    variable=Checkbutton_storage_position_Disk_Var,
    onvalue=True,
    offvalue=False,
    # height=5,
    # width=20,
    state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=select_Checkbutton_storage_position
)
# 將複選框（tkinter.Checkbutton）組件插入到標簽框架（tkinter.LabelFrame）組件中;
Checkbutton_storage_position_Disk.grid(
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
# Checkbutton_storage_position_Disk.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="left",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )

if is_storage_position == "Database":
    # Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
    # Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
elif is_storage_position == "Database_and_Disk":
    Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    # Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
    # Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
elif is_storage_position == "Disk":
    Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    # Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    # Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
    Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
elif len(is_storage_position) == 0:
    # Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    # Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
    Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
else:
    # sys.stdout.write("\n")  # 輸出換行;
    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + ",." + str(is_storage_position))  # 將字符串輸出寫到操作系統控制臺;
    # sys.stdout.write("\n")  # 輸出換行;
    print("參數錯誤." + "\n" + "用於輸出保存運算結果的位置:" + "\n" + "[ ." + str(is_storage_position) + " ]" + "\n" + "不合規，目前只支持:" + "\n" + "Database, Disk" + "\n" + "兩種方法.")
    # if is_window:
    #     Label_State['text'] = "參數錯誤." + "\n" + "用於輸出保存運算結果的位置:" + "\n" + "[ ." + str(is_storage_position) + " ]" + "\n" + "不合規，目前只支持:" + "\n" + "Database, Disk" + "\n" + "兩種方法."
    # Error_Log.append(str(is_storage_position))
    sys.exit(1)  # 中止當前進程，退出當前程序;


# 創建輸出運算結果路徑輸入框提示標簽（tkinter.Label）組件;
Label_outputTest_URL = tk.Label(
    master=window_root,
    text='Output url: ',
    # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
    # font=('Arial', 12),
    # width=30,
    # height=2
)  # 注意，標簽 width 和 height 的單位為「字符」個數;
# 將標簽（tkinter.Label）組件插入窗體介面中;
# Label_outputTest_URL.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Label_outputTest_URL.grid(
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

outputTestURL = tk.StringVar(value=default_outputTest_URL)
# outputTestURL.set(default_outputTest_URL)
# 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
# 創建輸出運算結果位置的單行文本輸入框（tkinter.Entry）組件;
Entry_outputTest_URL = tk.Entry(
    master=window_root,
    # font=("Arial", 14),
    textvariable=outputTestURL,
    state="disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
)
# 將單行文本框（tkinter.Entry）組件插入到窗體介面中;
# Entry_outputTest_URL.pack(
#     anchor="e",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="x",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Entry_outputTest_URL.grid(
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

def click_Button_outputTest_URL():

    global outputTest_URL

    outputTest_URL = str(Entry_outputTest_URL.get())  # 讀取結果輸出位置文本框輸入的内容;
    # outputTest_URL = str(outputTest_URL).replace('\\', '/')
    print(outputTest_URL)

    return outputTest_URL  # None

# 創建訓練集樣本加載按鈕（tkinter.Button）組件;
Button_outputTest_URL = tk.Button(
    master=window_root,
    text="Output url",
    # image=img_1,
    compound="center",
    cursor="hand2",
    state="disabled",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=click_Button_outputTest_URL  # 指定按鈕控件被單擊後執行的函數;
)
# 將按鈕（tkinter.Button）組件插入到窗體介面;
# Button_outputTest_URL.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="right",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     # fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     # expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Button_outputTest_URL.grid(
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
Label_outputTest_path = tk.Label(
    master=window_root,
    text='Output path: ',
    # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
    # font=('Arial', 12),
    # width=30,
    # height=2
)  # 注意，標簽 width 和 height 的單位為「字符」個數;
# 將標簽（tkinter.Label）組件插入窗體介面中;
# Label_outputTest_path.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Label_outputTest_path.grid(
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

outputTestpath = tk.StringVar(value=default_outputTest_path)
# outputTestpath.set(default_outputTest_path)
# 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
# 創建輸出運算結果位置的單行文本輸入框（tkinter.Entry）組件;
Entry_outputTest_path = tk.Entry(
    master=window_root,
    # font=("Arial", 14),
    textvariable=outputTestpath,
    state="normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
)
# 將單行文本框（tkinter.Entry）組件插入到窗體介面中;
# Entry_outputTest_path.pack(
#     anchor="e",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="x",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Entry_outputTest_path.grid(
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

# outputTest_path = Entry_outputTest_path.get()  # 讀取文本框輸入的内容;
# outputTest_path = str(outputTest_path).replace('\\', '/')
# # outputTest_path = outputTest_path.replace('/', r'\\')
# print(outputTest_path)
# tk_messagebox.showinfo(
#     title="溫馨提示 tkinter.Entry 2",
#     message=outputTest_path
# )

def click_Button_outputTest_path():

    global is_storage_position
    global is_storage_type
    # global window_root
    global output_dir
    global outputTestpath
    # outputTestpath = ""
    global outputTest_path
    # outputTest_path = ""
    global outputTest_File_Array
    outputTest_File_Array = []

    outputTest_path = str(Entry_outputTest_path.get())  # 讀取結果輸出位置文本框輸入的内容;
    outputTest_path = str(outputTest_path).replace('\\', '/')
    # outputTest_path = outputTest_path.replace('/', r'\\')

    # sysencode = sys.getfilesystemencoding()  # 包含有中文字符的文檔名編碼;

    output_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(outputTest_path))))).replace('\\', '/')
    # output_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(outputTest_path))))).replace('\\', '/')).encode(sysencode)

    # file_name_String = tk_filedialog.askopenfilename(title = '選定單檔')
    # directory_name_String = tk_filedialog.askdirectory(title = '選定資料夾')
    # files_name_Array = tk_filedialog.askopenfilenames(title = '選定多檔')

    outputTest_path = tk_filedialog.askopenfilename(
        title = '單選定運算結果輸出保存文檔',
        initialdir = output_dir,  # r'./test.csv', 默認打開路徑;
        defaultextension = ".csv",  # 預設文檔擴展名;
        initialfile = "test.csv",  # 對話框中初始化顯示的文檔名;
        # parent = window_root,  # 父對話框（由哪個窗口彈出就在哪個上端）;
        filetypes=[
            ("Result output documents", "*.csv *.txt *.json *.xlsx"),
            ("Comma-Separated Values files", "*.csv"),
            ("JavaScript Object Notation files", "*.json"),
            ("Plain text files", "*.txt"),
            ("Microsoft Office Excel files", "*.xlsx"),  # ("Microsoft Office Excel files", "*.xlsx .xls"),
            ("All files", ".*")
        ]
    )
    # print(outputTest_path)

    if len(outputTest_path) > 0:

        outputTest_path = str(os.path.normpath(os.path.abspath(os.path.normpath(outputTest_path)))).replace('\\', '/')
        # outputTest_path = str(str(os.path.normpath(os.path.abspath(os.path.normpath(outputTest_path)))).replace('\\', '/')).encode(sysencode)

        if outputTest_path.find(".", 0, int(len(outputTest_path)-1)) != -1:

            is_storage_type = str(outputTest_path.split('.')[len(outputTest_path.split('.'))-1])
            # print("storage type:", is_storage_type)

            if is_storage_type == "csv":
                Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_txt.deselect()
                Radiobutton_storage_type_Excel.deselect()
                Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
            elif is_storage_type == "json":
                Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_txt.deselect()
                Radiobutton_storage_type_Excel.deselect()
                Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
            elif is_storage_type == "txt":
                Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_csv.deselect()
                Radiobutton_storage_type_Excel.deselect()
                Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
            elif is_storage_type == "xlsx":
                Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_csv.deselect()
                Radiobutton_storage_type_txt.deselect()
                Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
            elif len(is_storage_type) == 0:
                Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
            else:
                # sys.stdout.write("\n")  # 輸出換行;
                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                # sys.stdout.write("\n")  # 輸出換行;
                print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                Label_State['text'] = str("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
                # Error_Log.append(outputTest_path)
                return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + outputTest_path  # None

            if is_storage_position == "":
                is_storage_position = "Disk"
            elif is_storage_position == "Database":
                is_storage_position = is_storage_position + "_and_" + "Disk"

            if is_storage_position == "Database":
                # Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                # Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            elif is_storage_position == "Database_and_Disk":
                Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                # Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                # Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            elif is_storage_position == "Disk":
                Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                # Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                # Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            elif len(is_storage_position) == 0:
                # Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
                # Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
                Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            else:
                # sys.stdout.write("\n")  # 輸出換行;
                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + ",." + str(is_storage_position))  # 將字符串輸出寫到操作系統控制臺;
                # sys.stdout.write("\n")  # 輸出換行;
                print("參數錯誤." + "\n" + "用於輸出保存運算結果的位置:" + "\n" + "[ ." + str(is_storage_position) + " ]" + "\n" + "不合規，目前只支持:" + "\n" + "Database, Disk" + "\n" + "兩種方法.")
                # Label_State['text'] = "參數錯誤." + "\n" + "用於輸出保存運算結果的位置:" + "\n" + "[ ." + str(is_storage_position) + " ]" + "\n" + "不合規，目前只支持:" + "\n" + "Database, Disk" + "\n" + "兩種方法."
                # Error_Log.append(str(is_storage_position))
                sys.exit(1)  # 中止當前進程，退出當前程序;

        else:
            # sys.stdout.write("\n")  # 輸出換行;
            # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
            # sys.stdout.write("\n")  # 輸出換行;
            print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + outputTest_path + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
            Label_State['text'] = str("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑:" + "\n" + "[ " + outputTest_path + " ]" + "\n" + "爲空，目前只支持：" + "\n" + ".json .csv .txt .xlsx" + "\n" + "四種類型.")
            # Error_Log.append(outputTest_path)
            return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + outputTest_path  # None

        outputTestpath.set(outputTest_path)
        Entry_outputTest_path['textvariable'] = outputTestpath

        outputTest_File_Array.append(outputTest_path)

        Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Output: [ " + str(outputTest_path) + " ] files."

    return outputTest_path  # None

# 創建訓練集樣本加載按鈕（tkinter.Button）組件;
Button_outputTest_path = tk.Button(
    master=window_root,
    text="Output Test",
    # image=img_1,
    compound="center",
    cursor="hand2",
    state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=click_Button_outputTest_path  # 指定按鈕控件被單擊後執行的函數;
)
# 將按鈕（tkinter.Button）組件插入到窗體介面;
# Button_outputTest_path.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="right",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     # fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     # expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Button_outputTest_path.grid(
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
LabelFrame_storage_type = tk.LabelFrame(
    master=window_root,
    text="Result storage type",
    # bg="#ffffff",  # 參數：bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色;
    borderwidth=1.0
)
# 將標簽框架（tkinter.LabelFrame）組件插入到窗體介面中;
# LabelFrame_storage_type.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="right",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     # fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     # expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
LabelFrame_storage_type.grid(
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

# 創建單選框（tkinter.Radiobutton）組件;
def select_Radiobutton_storage_type():

    global is_storage_type
    is_storage_type = str(Radiobutton_storage_type_Var.get())
    # print("storage type:", is_storage_type)

    global default_outputTest_path
    global outputTest_path
    global outputTestpath

    if len(str(Entry_outputTest_path.get())) > 0:
        outputTest_path = str(Entry_outputTest_path.get())  # 讀取結果輸出位置文本框輸入的内容;

    if len(outputTest_path) > 0:
        outputTest_path = str(outputTest_path).replace('\\', '/')
        if outputTest_path.find(".", 0, int(len(outputTest_path)-1)) != -1:
            # del default_outputTest_path.split('.')[len(default_outputTest_path.split('.'))-1]
            outputTest_path = str(''.join(outputTest_path.split('.')[0:len(outputTest_path.split('.'))-1])) + "." + is_storage_type
        else:
            outputTest_path = outputTest_path + "." + is_storage_type
        # print("output test path: ", outputTest_path)

        # outputTest_path = default_outputTest_path
        # print("output test path: ", outputTest_path)

    # print("storage position: ", is_storage_position)
    if is_storage_position == "Database_and_Disk" or is_storage_position == "Disk":
        outputTestpath.set(outputTest_path)
        Entry_outputTest_path['textvariable'] = outputTestpath

    return is_storage_type + "," + outputTest_path

Radiobutton_storage_type_Var = tk.StringVar(value="csv")  # tk.IntVar(value=0)

# 創建判斷結果存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
Radiobutton_storage_type_json = tk.Radiobutton(
    master=LabelFrame_storage_type,  # 將單選框組件放置在自定義的標簽框架組件内;
    text=".json",
    variable=Radiobutton_storage_type_Var,
    value="json",
    state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=select_Radiobutton_storage_type
)
# 將單選框（tkinter.Radiobutton）組件插入到標簽框架（tkinter.LabelFrame）組件中;
Radiobutton_storage_type_json.grid(
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
# Radiobutton_storage_type_json.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="left",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )

# 創建判斷結果存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
Radiobutton_storage_type_csv = tk.Radiobutton(
    master=LabelFrame_storage_type,  # 將單選框組件放置在自定義的標簽框架組件内;
    text=".csv",
    variable=Radiobutton_storage_type_Var,
    value="csv",
    state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=select_Radiobutton_storage_type
)
# 將單選框（tkinter.Radiobutton）組件插入到標簽框架（tkinter.LabelFrame）組件中;
Radiobutton_storage_type_csv.grid(
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
Radiobutton_storage_type_txt = tk.Radiobutton(
    master=LabelFrame_storage_type,  # 將單選框組件放置在自定義的標簽框架組件内;
    text=".txt",
    variable=Radiobutton_storage_type_Var,
    value="txt",
    state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=select_Radiobutton_storage_type
)
# 將單選框（tkinter.Radiobutton）組件插入到標簽框架（tkinter.LabelFrame）組件中;
Radiobutton_storage_type_txt.grid(
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
Radiobutton_storage_type_Excel = tk.Radiobutton(
    master=LabelFrame_storage_type,  # 將單選框組件放置在自定義的標簽框架組件内;
    text="Excel",
    variable=Radiobutton_storage_type_Var,
    value="xlsx",
    state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=select_Radiobutton_storage_type
)
# 將單選框（tkinter.Radiobutton）組件插入到標簽框架（tkinter.LabelFrame）組件中;
Radiobutton_storage_type_Excel.grid(
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

if is_storage_type == "json":
    Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
elif is_storage_type == "csv":
    # Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
elif is_storage_type == "txt":
    # Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
elif is_storage_type == "xlsx":
    # Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
elif len(is_storage_type) == 0:
    # Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    # Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
    Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
else:
    # sys.stdout.write("\n")  # 輸出換行;
    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + ",." + str(is_storage_type))  # 將字符串輸出寫到操作系統控制臺;
    # sys.stdout.write("\n")  # 輸出換行;
    print("參數錯誤." + "\n" + "用於輸出保存運算結果的檔的類型:" + "\n" + "[ ." + str(is_storage_type) + " ]" + "\n" + "不合規，目前只支持:" + "\n" + ".csv .txt .json .xlsx" + "\n" + "四種類型.")
    # if is_window:
    #     Label_State['text'] = "參數錯誤." + "\n" + "用於輸出保存運算結果的檔的類型:" + "\n" + "[ ." + str(is_storage_type) + " ]" + "\n" + "不合規，目前只支持:" + "\n" + ".csv .txt .json .xlsx" + "\n" + "四種類型."
    # Error_Log.append(str(is_storage_type))
    sys.exit(1)  # 中止當前進程，退出當前程序;

# 創建用於表格（tabel）中文本識別的 Google tesseract 參數（tesseract config）輸入框提示標簽（tkinter.Label）組件;
Label_tabel_tesseract_config = tk.Label(
    master=window_root,
    text='Tabel Config: ',
    # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
    # font=('Arial', 12),
    # width=30,  # 注意，標簽 width 的單位為「字符」個數;
    # height=2  # 注意，標簽 height 的單位為「字符」個數;
)
Label_tabel_tesseract_config.grid(
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
inputTabelTesseractConfig = tk.StringVar(value=default_input_tabel_tesseract_config)
# inputTabelTesseractConfig.set(default_input_tabel_tesseract_config)
# 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
# 在插入單行文本輸入框 Entry 控件的時候，使用參數 textvariable 指向變量 inputTabelTesseractConfig，即可指定單行文本輸入框 Entry 控件的預設值。
# 創建訓練集樣本輸入單行文本框（tkinter.Entry）組件;
Entry_tabel_tesseract_config = tk.Entry(
    master=window_root,
    # font=("Arial", 14),
    textvariable=inputTabelTesseractConfig,
    state="normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
)
# 將單行文本框（tkinter.Entry）組件插入到窗體介面;
Entry_tabel_tesseract_config.grid(
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
Label_measuringRuler_tesseract_config = tk.Label(
    master=window_root,
    text='Measuring Config: ',
    # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
    # font=('Arial', 12),
    # width=30,  # 注意，標簽 width 的單位為「字符」個數;
    # height=2  # 注意，標簽 height 的單位為「字符」個數;
)
Label_measuringRuler_tesseract_config.grid(
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
inputMeasuringRulerTesseractConfig = tk.StringVar(value=default_input_measuringRuler_tesseract_config)
# inputMeasuringRulerTesseractConfig.set(default_input_measuringRuler_tesseract_config)
# 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
# 在插入單行文本輸入框 Entry 控件的時候，使用參數 textvariable 指向變量 inputMeasuringRulerTesseractConfig，即可指定單行文本輸入框 Entry 控件的預設值。
# 創建驗證集樣本輸入單行文本框（tkinter.Entry）組件;
Entry_measuringRuler_tesseract_config = tk.Entry(
    master=window_root,
    # font=("Arial", 14),
    textvariable=inputMeasuringRulerTesseractConfig,
    state="normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
)
Entry_measuringRuler_tesseract_config.grid(
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

# 創建訓練集樣本輸入框提示標簽（tkinter.Label）組件;
Label_inputTrain_path = tk.Label(
    master=window_root,
    text='Input train: ',
    # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
    # font=('Arial', 12),
    # width=30,
    # height=2
)  # 注意，標簽 width 和 height 的單位為「字符」個數;
# 將標簽（tkinter.Label）組件插入窗體介面中;
# Label_inputTrain_path.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
# Label_inputTrain_path.grid(
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
inputTrainpath = tk.StringVar(value=default_inputTrain_path)
# inputTrainpath.set(default_inputTrain_path)
# 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
# 在插入單行文本輸入框 Entry 控件的時候，使用參數 textvariable 指向變量 inputTrainpath，即可指定單行文本輸入框 Entry 控件的預設值。
# 創建訓練集樣本輸入單行文本框（tkinter.Entry）組件;
Entry_inputTrain_path = tk.Entry(
    master=window_root,
    # font=("Arial", 14),
    textvariable=inputTrainpath,
    state="disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
)
# 將單行文本框（tkinter.Entry）組件插入到窗體介面;
# Entry_inputTrain_path.pack(
#     anchor="e",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="x",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
# Entry_inputTrain_path.grid(
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


def click_Button_inputTrain_path():

    # global window_root
    global input_dir
    global inputTrainpath
    # inputTrainpath = ""
    global inputTrain_path
    # inputTrain_path = ""
    global inputTrain_File_Array
    inputTrain_File_Array = []

    inputTrain_path = str(Entry_inputTrain_path.get())  # 讀取結果輸出位置文本框輸入的内容;
    inputTrain_path = str(inputTrain_path).replace('\\', '/')
    # inputTrain_path = inputTrain_path.replace('/', r'\\')

    # sysencode = sys.getfilesystemencoding()  # 包含有中文字符的文檔名編碼;

    if os.path.exists(inputTrain_path):
        if pathlib.Path(inputTrain_path).is_dir():
            input_dir = str(os.path.normpath(os.path.abspath(os.path.normpath(inputTrain_path)))).replace('\\', '/')
            # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
            if not (os.access(input_dir, os.R_OK) and os.access(input_dir, os.W_OK)):
                try:
                    # 修改文檔權限 mode:777 任何人可讀寫;
                    os.chmod(input_dir, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                    # os.chmod(input_dir, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                    # os.chmod(input_dir, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                    # os.chmod(input_dir, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                    # os.chmod(input_dir, stat.S_IWOTH)  # 可被其它用戶寫入;
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
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_dir + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    # print(error)
                    # print(f'Error: {input_dir} : {error}')
                    # print("參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + input_dir + " ]" + "\n" + "無法修改為可讀可寫權限.")
                    Label_State['text'] = "參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + input_dir + " ]" + "\n" + "無法修改為可讀可寫權限."
                    # Error_Log.append(input_dir)
                    # return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_dir  # None
        elif os.path.isfile(inputTrain_path):
            input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(inputTrain_path))))).replace('\\', '/')
            # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
            if not (os.access(input_dir, os.R_OK) and os.access(input_dir, os.W_OK)):
                try:
                    # 修改文檔權限 mode:777 任何人可讀寫;
                    os.chmod(input_dir, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                    # os.chmod(input_dir, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                    # os.chmod(input_dir, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                    # os.chmod(input_dir, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                    # os.chmod(input_dir, stat.S_IWOTH)  # 可被其它用戶寫入;
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
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_dir + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    # print(error)
                    # print(f'Error: {input_dir} : {error}')
                    # print("參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + input_dir + " ]" + "\n" + "無法修改為可讀可寫權限.")
                    Label_State['text'] = "參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + input_dir + " ]" + "\n" + "無法修改為可讀可寫權限."
                    # Error_Log.append(input_dir)
                    # return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_dir  # None
    #     else:
    #         # sys.stdout.write("\n")  # 輸出換行;
    #         # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(inputTrain_path))  # 將字符串輸出寫到操作系統控制臺;
    #         # sys.stdout.write("\n")  # 輸出換行;
    #         print("參數錯誤." + "\n" + "檔:" + "\n" + "[ " + inputTrain_path + " ]" + "\n" + "類型無法識別.")
    #         Label_State['text'] = "參數錯誤." + "\n" + "檔:" + "\n" + "[ " + inputTrain_path + " ]" + "\n" + "類型無法識別."
    #         # Error_Log.append(inputTrain_path)
    #         return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTrain_path  # None
    # else:
    #     # sys.stdout.write("\n")  # 輸出換行;
    #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(inputTrain_path))  # 將字符串輸出寫到操作系統控制臺;
    #     # sys.stdout.write("\n")  # 輸出換行;
    #     print("參數錯誤." + "\n" + "檔:" + "\n" + "[ " + inputTrain_path + " ]" + "\n" + "不存在.")
    #     Label_State['text'] = "參數錯誤." + "\n" + "檔:" + "\n" + "[ " + inputTrain_path + " ]" + "\n" + "不存在."
    #     # Error_Log.append(inputTrain_path)
    #     return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTrain_path  # None

    # file_name_String = tk_filedialog.askopenfilename(title = '選定單檔')
    # directory_name_String = tk_filedialog.askdirectory(title = '選定資料夾')
    # files_name_Array = tk_filedialog.askopenfilenames(title = '選定多檔')

    files_name_Array = tk_filedialog.askopenfilenames(
        title = '多選定待處理的圖片檔',
        initialdir = input_dir,  # r'./a/b/c', 默認打開路徑;
        initialfile = "",  # "test.bmp" 對話框中初始化顯示的文檔名;
        defaultextension = ".bmp",  # 預設文檔擴展名;
        # parent = window_root,  # 父對話框（由哪個窗口彈出就在哪個上端）;
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
            inputTrain_File_Array.append(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/'))
            # inputTrain_File_Array.append(str(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/')).encode(sysencode))

    # print(files_name_Array[0])
    if len(files_name_Array) == 1:
        if len(files_name_Array[0]) > 0:
            input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
            # input_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
            inputTrain_path = str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[0])))).replace('\\', '/')
            # inputTrain_path = str(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[0])))).replace('\\', '/')).encode(sysencode)
            inputTrainpath.set(inputTrain_path)
            Entry_inputTrain_path['textvariable'] = inputTrainpath
    elif len(files_name_Array) > 1:
        if len(files_name_Array[0]) > 0:
            input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
            # input_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
            inputTrain_path = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
            # inputTrain_path = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
            inputTrainpath.set(inputTrain_path)
            Entry_inputTrain_path['textvariable'] = inputTrainpath
    # elif len(files_name_Array) == 0:
    #     inputTrain_path = input_dir
    #     inputTrainpath.set(inputTrain_path)
    #     Entry_inputTrain_path['textvariable'] = inputTrainpath
    # else:

    if len(inputTrain_File_Array) > 0:
        Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "From: " + "[ " + inputTrain_path + " ]" + "\n" + "Input: [ " + str(len(inputTrain_File_Array)) + " ] files."

    return inputTrain_File_Array  # None

# 創建訓練集樣本加載按鈕（tkinter.Button）組件;
Button_inputTrain_path = tk.Button(
    master=window_root,
    text="Input Train",
    # image=img_1,
    compound="center",
    cursor="hand2",
    state="disabled",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=click_Button_inputTrain_path  # 指定按鈕控件被單擊後執行的函數;
)
# 將按鈕（tkinter.Button）組件插入到窗體介面;
# Button_inputTrain_path.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="right",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     # fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     # expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
# Button_inputTrain_path.grid(
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
Label_inputValidation_path = tk.Label(
    master=window_root,
    text='Input validation: ',
    # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
    # font=('Arial', 12),
    # width=30,
    # height=2
)  # 注意，標簽 width 和 height 的單位為「字符」個數;
# 將標簽（tkinter.Label）組件插入窗體介面中;
# Label_inputValidation_path.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
# Label_inputValidation_path.grid(
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
inputValidationpath = tk.StringVar(value=default_inputValidation_path)
# inputValidationpath.set(default_inputValidation_path)
# 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
# 在插入單行文本輸入框 Entry 控件的時候，使用參數 textvariable 指向變量 inputValidationpath，即可指定單行文本輸入框 Entry 控件的預設值。
# 創建驗證集樣本輸入單行文本框（tkinter.Entry）組件;
Entry_inputValidation_path = tk.Entry(
    master=window_root,
    # font=("Arial", 14),
    textvariable=inputValidationpath,
    state="disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
)
# 將單行文本框（tkinter.Entry）組件插入到窗體介面;
# Entry_inputValidation_path.pack(
#     anchor="e",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="x",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
# Entry_inputValidation_path.grid(
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


def click_Button_inputValidation_path():

    # global window_root
    global input_dir
    global inputValidationpath
    # inputValidationpath = ""
    global inputValidation_path
    # inputValidation_path = ""
    global inputValidation_File_Array
    inputValidation_File_Array = []

    inputValidation_path = str(Entry_inputValidation_path.get())  # 讀取結果輸出位置文本框輸入的内容;
    inputValidation_path = str(inputValidation_path).replace('\\', '/')
    # inputValidation_path = inputValidation_path.replace('/', r'\\')

    # sysencode = sys.getfilesystemencoding()  # 包含有中文字符的文檔名編碼;

    if os.path.exists(inputValidation_path):
        if pathlib.Path(inputValidation_path).is_dir():
            input_dir = str(os.path.normpath(os.path.abspath(os.path.normpath(inputValidation_path)))).replace('\\', '/')
            # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
            if not (os.access(input_dir, os.R_OK) and os.access(input_dir, os.W_OK)):
                try:
                    # 修改文檔權限 mode:777 任何人可讀寫;
                    os.chmod(input_dir, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                    # os.chmod(input_dir, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                    # os.chmod(input_dir, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                    # os.chmod(input_dir, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                    # os.chmod(input_dir, stat.S_IWOTH)  # 可被其它用戶寫入;
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
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_dir + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    # print(error)
                    # print(f'Error: {input_dir} : {error}')
                    # print("參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + input_dir + " ]" + "\n" + "無法修改為可讀可寫權限.")
                    Label_State['text'] = "參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + input_dir + " ]" + "\n" + "無法修改為可讀可寫權限."
                    # Error_Log.append(input_dir)
                    # return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_dir  # None
        elif os.path.isfile(inputValidation_path):
            input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(inputValidation_path))))).replace('\\', '/')
            # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
            if not (os.access(input_dir, os.R_OK) and os.access(input_dir, os.W_OK)):
                try:
                    # 修改文檔權限 mode:777 任何人可讀寫;
                    os.chmod(input_dir, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                    # os.chmod(input_dir, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                    # os.chmod(input_dir, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                    # os.chmod(input_dir, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                    # os.chmod(input_dir, stat.S_IWOTH)  # 可被其它用戶寫入;
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
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_dir + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    # print(error)
                    # print(f'Error: {input_dir} : {error}')
                    # print("參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + input_dir + " ]" + "\n" + "無法修改為可讀可寫權限.")
                    Label_State['text'] = "參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + input_dir + " ]" + "\n" + "無法修改為可讀可寫權限."
                    # Error_Log.append(input_dir)
                    # return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_dir  # None
    #     else:
    #         # sys.stdout.write("\n")  # 輸出換行;
    #         # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(inputValidation_path))  # 將字符串輸出寫到操作系統控制臺;
    #         # sys.stdout.write("\n")  # 輸出換行;
    #         print("參數錯誤." + "\n" + "檔:" + "\n" + "[ " + inputValidation_path + " ]" + "\n" + "類型無法識別.")
    #         Label_State['text'] = "參數錯誤." + "\n" + "檔:" + "\n" + "[ " + inputValidation_path + " ]" + "\n" + "類型無法識別."
    #         # Error_Log.append(inputValidation_path)
    #         return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputValidation_path  # None
    # else:
    #     # sys.stdout.write("\n")  # 輸出換行;
    #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(inputValidation_path))  # 將字符串輸出寫到操作系統控制臺;
    #     # sys.stdout.write("\n")  # 輸出換行;
    #     print("參數錯誤." + "\n" + "檔:" + "\n" + "[ " + inputValidation_path + " ]" + "\n" + "不存在.")
    #     Label_State['text'] = "參數錯誤." + "\n" + "檔:" + "\n" + "[ " + inputValidation_path + " ]" + "\n" + "不存在."
    #     # Error_Log.append(inputValidation_path)
    #     return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputValidation_path  # None

    # file_name_String = tk_filedialog.askopenfilename(title = '選定單檔')
    # directory_name_String = tk_filedialog.askdirectory(title = '選定資料夾')
    # files_name_Array = tk_filedialog.askopenfilenames(title = '選定多檔')

    files_name_Array = tk_filedialog.askopenfilenames(
        title = '多選定待處理的圖片檔',
        initialdir = input_dir,  # r'./a/b/c', 默認打開路徑;
        initialfile = "",  # "test.bmp" 對話框中初始化顯示的文檔名;
        defaultextension = ".bmp",  # 預設文檔擴展名;
        # parent = window_root,  # 父對話框（由哪個窗口彈出就在哪個上端）;
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
            inputValidation_File_Array.append(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/'))
            # inputValidation_File_Array.append(str(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/')).encode(sysencode))

    # print(files_name_Array[0])
    if len(files_name_Array) == 1:
        if len(files_name_Array[0]) > 0:
            input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
            # input_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
            inputValidation_path = str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[0])))).replace('\\', '/')
            # inputValidation_path = str(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[0])))).replace('\\', '/')).encode(sysencode)
            inputValidationpath.set(inputValidation_path)
            Entry_inputValidation_path['textvariable'] = inputValidationpath
    elif len(files_name_Array) > 1:
        if len(files_name_Array[0]) > 0:
            input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
            # input_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
            inputValidation_path = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
            # inputValidation_path = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
            inputValidationpath.set(inputValidation_path)
            Entry_inputValidation_path['textvariable'] = inputValidationpath
    # elif len(files_name_Array) == 0:
    #     inputValidation_path = input_dir
    #     inputValidationpath.set(inputValidation_path)
    #     Entry_inputValidation_path['textvariable'] = inputValidationpath
    # else:

    if len(inputValidation_File_Array) > 0:
        Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "From: " + "[ " + inputValidation_path + " ]" + "\n" + "Input: [ " + str(len(inputValidation_File_Array)) + " ] files."

    return inputValidation_File_Array  # None

# 創建訓練集樣本加載按鈕（tkinter.Button）組件;
Button_inputValidation_path = tk.Button(
    master=window_root,
    text="Input Validation",
    # image=img_1,
    compound="center",
    cursor="hand2",
    state="disabled",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=click_Button_inputValidation_path  # 指定按鈕控件被單擊後執行的函數;
)
# 將按鈕（tkinter.Button）組件插入到窗體介面;
# Button_inputValidation_path.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="right",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     # fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     # expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
# Button_inputValidation_path.grid(
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


# 創建測試集樣本輸入框提示標簽（tkinter.Label）組件;
Label_inputTest_path = tk.Label(
    master=window_root,
    text='Input test: ',
    # bg='#ffffff',  # bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
    # font=('Arial', 12),
    # width=30,
    # height=2
)  # 注意，標簽 width 和 height 的單位為「字符」個數;
# 將標簽（tkinter.Label）組件插入窗體介面中;
# Label_inputTest_path.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Label_inputTest_path.grid(
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
inputTestpath = tk.StringVar(value=default_inputTest_path)
# inputTestpath.set(default_inputTest_path)
# 定義一個單行輸入文本框，當輸入密碼不想顯示時，可以使用 show='*' 參數，星號表示輸入的任意字符都會以 * 的形式顯示;
# 在插入單行文本輸入框 Entry 控件的時候，使用參數 textvariable 指向變量 inputTestpath，即可指定單行文本輸入框 Entry 控件的預設值。
# 創建測試集樣本輸入單行文本框（tkinter.Entry）組件;
Entry_inputTest_path = tk.Entry(
    master=window_root,
    # font=("Arial", 14),
    textvariable=inputTestpath,
    state="normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，state="readonly" 表示只讀操作;
)
# 將單行文本框（tkinter.Entry）組件插入到窗體介面;
# Entry_inputTest_path.pack(
#     anchor="e",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="x",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Entry_inputTest_path.grid(
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
# Entry_inputTest_path.place(relx=0.405, rely=0.5, anchor="center")  # 設定輸入框位置;
# inputTest_path = Entry_inputTest_path.get()  # 讀取文本框輸入的内容;
# inputTest_path = str(inputTest_path).replace('\\', '/')
# print(inputTest_path)

def click_Button_inputTest_path():

    # global window_root
    global input_dir
    global inputTestpath
    # inputTestpath = ""
    global inputTest_path
    # inputTest_path = ""
    global inputTest_File_Array
    inputTest_File_Array = []

    inputTest_path = str(Entry_inputTest_path.get())  # 讀取結果輸出位置文本框輸入的内容;
    inputTest_path = str(inputTest_path).replace('\\', '/')
    # inputTest_path = inputTest_path.replace('/', r'\\')

    # sysencode = sys.getfilesystemencoding()  # 包含有中文字符的文檔名編碼;

    if os.path.exists(inputTest_path):
        if pathlib.Path(inputTest_path).is_dir():
            input_dir = str(os.path.normpath(os.path.abspath(os.path.normpath(inputTest_path)))).replace('\\', '/')
            # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
            if not (os.access(input_dir, os.R_OK) and os.access(input_dir, os.W_OK)):
                try:
                    # 修改文檔權限 mode:777 任何人可讀寫;
                    os.chmod(input_dir, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                    # os.chmod(input_dir, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                    # os.chmod(input_dir, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                    # os.chmod(input_dir, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                    # os.chmod(input_dir, stat.S_IWOTH)  # 可被其它用戶寫入;
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
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_dir + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    # print(error)
                    # print(f'Error: {input_dir} : {error}')
                    # print("參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + input_dir + " ]" + "\n" + "無法修改為可讀可寫權限.")
                    Label_State['text'] = "參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + input_dir + " ]" + "\n" + "無法修改為可讀可寫權限."
                    # Error_Log.append(input_dir)
                    # return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_dir  # None
        elif os.path.isfile(inputTest_path):
            input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(inputTest_path))))).replace('\\', '/')
            # 使用Python原生模組os判斷文檔或目錄是否可讀os.R_OK、可寫os.W_OK、可執行os.X_OK;
            if not (os.access(input_dir, os.R_OK) and os.access(input_dir, os.W_OK)):
                try:
                    # 修改文檔權限 mode:777 任何人可讀寫;
                    os.chmod(input_dir, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                    # os.chmod(input_dir, stat.S_ISVTX)  # 修改文檔權限 mode: 440 不可讀寫;
                    # os.chmod(input_dir, stat.S_IROTH)  # 修改文檔權限 mode: 644 只讀;
                    # os.chmod(input_dir, stat.S_IXOTH)  # 修改文檔權限 mode: 755 可執行文檔不可修改;
                    # os.chmod(input_dir, stat.S_IWOTH)  # 可被其它用戶寫入;
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
                    # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_dir + "\n" + str(error))  # 將字符串輸出寫到操作系統控制臺;
                    # sys.stdout.write("\n")  # 輸出換行;
                    # print(error)
                    # print(f'Error: {input_dir} : {error}')
                    # print("參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + input_dir + " ]" + "\n" + "無法修改為可讀可寫權限.")
                    Label_State['text'] = "參數錯誤." + "\n" + "目錄:" + "\n" + "[ " + input_dir + " ]" + "\n" + "無法修改為可讀可寫權限."
                    # Error_Log.append(input_dir)
                    # return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + input_dir  # None
    #     else:
    #         # sys.stdout.write("\n")  # 輸出換行;
    #         # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(inputTest_path))  # 將字符串輸出寫到操作系統控制臺;
    #         # sys.stdout.write("\n")  # 輸出換行;
    #         print("參數錯誤." + "\n" + "檔:" + "\n" + "[ " + inputTest_path + " ]" + "\n" + "類型無法識別.")
    #         Label_State['text'] = "參數錯誤." + "\n" + "檔:" + "\n" + "[ " + inputTest_path + " ]" + "\n" + "類型無法識別."
    #         # Error_Log.append(inputTest_path)
    #         return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTest_path  # None
    # else:
    #     # sys.stdout.write("\n")  # 輸出換行;
    #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(inputTest_path))  # 將字符串輸出寫到操作系統控制臺;
    #     # sys.stdout.write("\n")  # 輸出換行;
    #     print("參數錯誤." + "\n" + "檔:" + "\n" + "[ " + inputTest_path + " ]" + "\n" + "不存在.")
    #     Label_State['text'] = "參數錯誤." + "\n" + "檔:" + "\n" + "[ " + inputTest_path + " ]" + "\n" + "不存在."
    #     # Error_Log.append(inputTest_path)
    #     return "Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTest_path  # None

    # file_name_String = tk_filedialog.askopenfilename(title = '選定單檔')
    # directory_name_String = tk_filedialog.askdirectory(title = '選定資料夾')
    # files_name_Array = tk_filedialog.askopenfilenames(title = '選定多檔')

    files_name_Array = tk_filedialog.askopenfilenames(
        title = '多選定待處理的圖片檔',
        initialdir = input_dir,  # r'./a/b/c', 默認打開路徑;
        initialfile = "",  # "test.bmp" 對話框中初始化顯示的文檔名;
        defaultextension = ".bmp",  # 預設文檔擴展名;
        # parent = window_root,  # 父對話框（由哪個窗口彈出就在哪個上端）;
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
            inputTest_File_Array.append(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/'))
            # inputTest_File_Array.append(str(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[i])))).replace('\\', '/')).encode(sysencode))

    # print(files_name_Array[0])
    if len(files_name_Array) == 1:
        if len(files_name_Array[0]) > 0:
            input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
            # input_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
            inputTest_path = str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[0])))).replace('\\', '/')
            # inputTest_path = str(str(os.path.normpath(os.path.abspath(os.path.normpath(files_name_Array[0])))).replace('\\', '/')).encode(sysencode)
            inputTestpath.set(inputTest_path)
            Entry_inputTest_path['textvariable'] = inputTestpath
    elif len(files_name_Array) > 1:
        if len(files_name_Array[0]) > 0:
            input_dir = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
            # input_dir = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
            inputTest_path = str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')
            # inputTest_path = str(str(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(files_name_Array[0]))))).replace('\\', '/')).encode(sysencode)
            inputTestpath.set(inputTest_path)
            Entry_inputTest_path['textvariable'] = inputTestpath
    # elif len(files_name_Array) == 0:
    #     inputTest_path = input_dir
    #     inputTestpath.set(inputTest_path)
    #     Entry_inputTest_path['textvariable'] = inputTestpath
    # else:

    if len(inputTest_File_Array) > 0:
        Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "From: " + "[ " + inputTest_path + " ]" + "\n" + "Input: [ " + str(len(inputTest_File_Array)) + " ] files."

    return inputTest_File_Array  # None

# 創建訓練集樣本加載按鈕（tkinter.Button）組件;
Button_inputTest_path = tk.Button(
    master=window_root,
    text="Input Test",
    # image=img_1,
    compound="center",
    cursor="hand2",
    state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=click_Button_inputTest_path  # 指定按鈕控件被單擊後執行的函數;
)
# 將按鈕（tkinter.Button）組件插入到窗體介面;
# Button_inputTest_path.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="right",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     # fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     # expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Button_inputTest_path.grid(
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


def click_Button_start_and_stop_Train():

    global screenwidth
    global screenheight
    global is_storage_position
    global is_storage_type
    # global default_input_tabel_tesseract_config  # = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    # global input_tabel_tesseract_config
    # global default_input_measuringRuler_tesseract_config  # = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    # global input_measuringRuler_tesseract_config
    # global tabel_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    # global measuringRuler_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    global inputTrain_path
    global inputTrain_File_Array
    global inputValidation_path
    global inputValidation_File_Array
    # global inputTest_path
    # global inputTest_File_Array
    # global outputTest_path
    # global outputTest_File_Array
    # global outputTest_URL

    global complete_Number
    complete_Number = int(0)

    global is_Runing
    is_Runing = not is_Runing
    if is_Runing:

        if is_Concurrent == "Multi-Threading":
            if outqueue_from_host_to_task:
                outqueue_from_host_to_task.put(
                    [
                        "is_Runing_True",
                        ""
                    ],
                    block=False,
                    timeout=None
                )

        Button_start_and_stop_Train['text'] = "Stop Train"
        # Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        # Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        # Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    else:

        # print("程式被中止.")
        if is_Concurrent == "Multi-Threading":
            if outqueue_from_host_to_task:
                outqueue_from_host_to_task.put(
                    [
                        "is_Runing_False",
                        ""
                    ],
                    block=False,
                    timeout=None
                )

        if is_Concurrent == "0" or is_Concurrent == 0:
            # sys.stdout.write('\n')
            # sys.stdout.write("Discontinue," + str(complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTest_path + "," + outputTest_path)  # 將字符串輸出寫到操作系統控制臺;
            print("Discontinue," + str(complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTest_path + "," + outputTest_path)  # 將字符串輸出寫到操作系統控制臺;
            # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
            # Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + inputTest_path + " ]." + "\n" + "Output: [ " + outputTest_path + " ]." + "\n" + "discontinue [ " + str(complete_Number) + " ]."
            Label_State['text'] = "Stand by"

            Button_start_and_stop_Test['text'] = "Start Test"
            Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

            # 使用消息提示框控件給出溫馨提示;
            tk_messagebox.showinfo(
                title = "溫馨提示",
                message = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + inputTest_path + " ]." + "\n" + "Output: [ " + outputTest_path + " ]." + "\n" + "Discontinue [ " + str(complete_Number) + " ]."
            )

        return "Discontinue," + str(complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTrain_path + "," + inputValidation_path  # None

    global Error_Log
    Error_Log = []

    global input_tabel_tesseract_config
    input_tabel_tesseract_config = str(Entry_tabel_tesseract_config.get())  # 讀取表格（tabel）内的文本識別（Google tesseract）的參數（tesseract config）文本輸入框輸入的内容; # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    global tabel_tesseract_config
    tabel_tesseract_config = input_tabel_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    global input_measuringRuler_tesseract_config
    input_measuringRuler_tesseract_config = str(Entry_measuringRuler_tesseract_config.get())  # 讀取測量尺（Measuring Ruler）標識的文本識別（Google tesseract）的參數（tesseract config）文本框輸入的内容; # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    global measuringRuler_tesseract_config
    measuringRuler_tesseract_config = input_measuringRuler_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;

    inputTrain_path = str(Entry_inputTrain_path.get())  # 讀取訓練集樣本位置文本框輸入的内容;

    if len(inputTrain_path) == 0:

        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(inputTrain_path))  # 將字符串輸出寫到操作系統控制臺;
        print("參數錯誤." + "\n" + "訓練集樣本傳入路徑: " + "\n" + "[ " + inputTrain_path + " ]" + "\n" + "爲空.")
        # Label_State['text'] = "參數錯誤." + "\n" + "訓練集樣本傳入路徑: " + "\n" + "[ " + inputTrain_path + " ]" + "\n" + "爲空."
        Label_State['text'] = "Stand by"

        # Error_Log.append(inputTrain_path)

        if is_Runing:
            is_Runing = not is_Runing
        if is_Runing:
            Button_start_and_stop_Train['text'] = "Stop Train"
            # Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        else:
            Button_start_and_stop_Train['text'] = "Start Train"
            # Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Button_start_and_stop_Test['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

        # 使用消息提示框控件給出溫馨提示;
        tk_messagebox.showinfo(
            title = "溫馨提示",
            message = "參數錯誤." + "\n" + "訓練集樣本傳入路徑: " + "\n" + "[ " + inputTrain_path + " ]" + "\n" + "爲空."
        )

        return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTrain_path

    inputTrain_path = str(inputTrain_path).replace('\\', '/')
    # print("input train path:", inputTrain_path)

    inputValidation_path = str(Entry_inputValidation_path.get())  # 讀取驗證集樣本位置文本框輸入的内容;

    if len(inputValidation_path) == 0:

        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(inputValidation_path))  # 將字符串輸出寫到操作系統控制臺;
        print("參數錯誤." + "\n" + "驗證集樣本傳入路徑: " + "\n" + "[ " + inputValidation_path + " ]" + "\n" + "爲空.")
        # Label_State['text'] = "參數錯誤." + "\n" + "驗證集樣本傳入路徑: " + "\n" + "[ " + inputValidation_path + " ]" + "\n" + "爲空."
        Label_State['text'] = "Stand by"

        # Error_Log.append(inputValidation_path)

        if is_Runing:
            is_Runing = not is_Runing
        if is_Runing:
            Button_start_and_stop_Train['text'] = "Stop Train"
            # Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        else:
            Button_start_and_stop_Train['text'] = "Start Train"
            # Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Button_start_and_stop_Test['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

        # 使用消息提示框控件給出溫馨提示;
        tk_messagebox.showinfo(
            title = "溫馨提示",
            message = "參數錯誤." + "\n" + "驗證集樣本傳入路徑: " + "\n" + "[ " + inputValidation_path + " ]" + "\n" + "爲空."
        )

        return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputValidation_path

    inputValidation_path = str(inputValidation_path).replace('\\', '/')
    # print("input validation path:", inputValidation_path)

    # inputTest_path = str(Entry_inputTest_path.get())  # 讀取測試集樣本位置文本框輸入的内容;

    # if len(inputTest_path) == 0:

    #     # sys.stdout.write("Error," + + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," str(inputTest_path))  # 將字符串輸出寫到操作系統控制臺;
    #     print("參數錯誤." + "\n" + "測試集樣本傳入路徑: " + "\n" + "[ " + inputTest_path + " ]" + "\n" + "爲空.")
    #     # Label_State['text'] = "參數錯誤." + "\n" + "測試集樣本傳入路徑: " + "\n" + "[ " + inputTest_path + " ]" + "\n" + "爲空."
    #     Label_State['text'] = "Stand by"

    #     # Error_Log.append(inputTest_path)

    #     if is_Runing:
    #         is_Runing = not is_Runing
    #     if is_Runing:
    #         Button_start_and_stop_Train['text'] = "Stop Train"
    #         # Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         # Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         # Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     else:
    #         Button_start_and_stop_Train['text'] = "Start Train"
    #         # Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         # Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         # Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Button_start_and_stop_Test['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

    #     # 使用消息提示框控件給出溫馨提示;
    #     tk_messagebox.showinfo(
    #         title = "溫馨提示",
    #         message = "參數錯誤." + "\n" + "測試集樣本傳入路徑: " + "\n" + "[ " + inputTest_path + " ]" + "\n" + "爲空."
    #     )

    #     return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTest_path

    # inputTest_path = str(inputTest_path).replace('\\', '/')
    # # print("input test path:", inputTest_path)

    # global is_storage_type
    # is_storage_type = str(Radiobutton_storage_type_Var.get())
    # # print("storage type:", is_storage_type)

    # outputTest_path = str(Entry_outputTest_path.get())  # 讀取結果輸出位置文本框輸入的内容;

    # if len(outputTest_path) == 0:

    #     if len(is_storage_position) == 0:
    #         is_storage_position = ""
    #         # Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    #         Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    #         # Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
    #         Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
    #     elif is_storage_position == "Disk":
    #         is_storage_position = ""
    #         # Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    #         Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    #         # Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
    #         Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
    #     elif is_storage_position == "Database_and_Disk":
    #         is_storage_position = "Database"
    #         # Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    #         Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
    #         Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
    #         # Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;

    #     is_storage_type = ""
    #     # print("storage type:", is_storage_type)

    #     # Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    #     Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    #     # Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    #     Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    #     # Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    #     Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    #     # Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
    #     Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

    #     # # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
    #     # print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "爲空.")
    #     # # Label_State['text'] = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "爲空."
    #     # Label_State['text'] = "Stand by"

    #     # # Error_Log.append(outputTest_path)

    #     # if is_Runing:
    #     #     is_Runing = not is_Runing
    #     # if is_Runing:
    #     #     Button_start_and_stop_Train['text'] = "Stop Train"
    #     #     # Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     # Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     # Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     # else:
    #     #     Button_start_and_stop_Train['text'] = "Start Train"
    #     #     # Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     # Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     # Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     #     Button_start_and_stop_Test['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #     #     Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

    #     # # 使用消息提示框控件給出溫馨提示;
    #     # tk_messagebox.showinfo(
    #     #     title = "溫馨提示",
    #     #     message = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "爲空."
    #     # )

    #     # return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + outputTest_path

    # outputTest_path = str(outputTest_path).replace('\\', '/')
    # # print("output test path:", outputTest_path)

    # if len(outputTest_path) > 0:

    #     if outputTest_path.find(".", 0, int(len(outputTest_path)-1)) != -1:

    #         is_storage_type = str(outputTest_path.split('.')[len(outputTest_path.split('.'))-1])
    #         # print("storage type:", is_storage_type)
    #         if is_storage_type == "json":
    #             Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    #             Radiobutton_storage_type_txt.deselect()
    #             Radiobutton_storage_type_Excel.deselect()
    #             Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    #         elif is_storage_type == "csv":
    #             Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    #             Radiobutton_storage_type_txt.deselect()
    #             Radiobutton_storage_type_Excel.deselect()
    #             Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    #         elif is_storage_type == "txt":
    #             Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    #             Radiobutton_storage_type_csv.deselect()
    #             Radiobutton_storage_type_Excel.deselect()
    #             Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    #         elif is_storage_type == "xlsx":
    #             Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    #             Radiobutton_storage_type_csv.deselect()
    #             Radiobutton_storage_type_txt.deselect()
    #             Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
    #         elif len(is_storage_type) == 0:
    #             Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
    #             Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
    #             Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
    #             Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
    #         else:

    #             # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
    #             print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規.")
    #             # Label_State['text'] = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規."
    #             Label_State['text'] = "Stand by"

    #             # Error_Log.append(outputTest_path)

    #             if is_Runing:
    #                 is_Runing = not is_Runing
    #             if is_Runing:
    #                 Button_start_and_stop_Train['text'] = "Stop Train"
    #                 # Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 # Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 # Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             else:
    #                 Button_start_and_stop_Train['text'] = "Start Train"
    #                 # Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;    
    #                 Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 # Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 # Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #                 Button_start_and_stop_Test['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #                 Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

    #             # 使用消息提示框控件給出溫馨提示;
    #             tk_messagebox.showinfo(
    #                 title = "溫馨提示",
    #                 message = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規."
    #             )

    #             return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + outputTest_path

    #     else:

    #         # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
    #         print("參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規.")
    #         # Label_State['text'] = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規."
    #         Label_State['text'] = "Stand by"

    #         # Error_Log.append(outputTest_path)

    #         if is_Runing:
    #             is_Runing = not is_Runing
    #         if is_Runing:
    #             Button_start_and_stop_Train['text'] = "Stop Train"
    #             # Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             # Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             # Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             Button_start_and_stop_Test['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         else:
    #             Button_start_and_stop_Train['text'] = "Start Train"
    #             # Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             # Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             # Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #             Button_start_and_stop_Test['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #             Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

    #         # 使用消息提示框控件給出溫馨提示;
    #         tk_messagebox.showinfo(
    #             title = "溫馨提示",
    #             message = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規."
    #         )

    #         return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + outputTest_path

    global time_sleep
    global file_Data
    # global file_Data_bytes
    # global file_Data_len
    file_Data = ""
    # file_Data_bytes = file_Data.encode("utf-8")
    # file_Data = file_Data_bytes.decode("utf-8")
    # file_Data = str(file_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
    # file_Data_len = len(bytes(file_Data, "utf-8"))
    global result_Data
    result_Data = ""
    # result_Data_bytes = result_Data.encode("utf-8")
    # result_Data = result_Data_bytes.decode("utf-8")
    # result_Data = str(result_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
    # result_Data_len = len(bytes(result_Data, "utf-8"))
    global image_sample
    image_sample = []

    # print(inputTrain_path)
    if len(inputTrain_File_Array) == 0:
        if len(inputTrain_path) > 0:
            # inputTrain_File_Array = []
            inputTrain_File_Array = Path_Conversion(inputTrain_path, time_sleep)[0]

    # print(inputValidation_path)
    if len(inputValidation_File_Array) == 0:
        if len(inputValidation_path) > 0:
            # inputValidation_File_Array = []
            inputValidation_File_Array = Path_Conversion(inputValidation_path, time_sleep)[0]

    # print(inputTest_path)
    # if len(inputTest_File_Array) == 0:
    #     if len(inputTest_path) > 0:
    #         # inputTest_File_Array = []
    #         inputTest_File_Array = Path_Conversion(inputTest_path, time_sleep)[0]

    # print(outputTest_path)
    # if len(outputTest_File_Array) == 0:
    #     if len(outputTest_path) > 0:
    #         # # outputTest_File_Array = []
    #         # outputTest_File_Array = Path_Conversion(outputTest_path, time_sleep)[0]
    #         outputTest_File_Array = [outputTest_path]

    # 讀取多行文本輸入框中的内容;
    Text_display_result_value = Text_display_result.get(
        "0.0",  # 表示讀取多行文本輸入框 .Text 控件中的全部值，如果設定參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始讀取;
        "end"  # 表示讀取至多行文本輸入框 .Text 控件中全部值的最後一個字符爲止;
    )
    Text_display_result_value = str(Text_display_result_value)
    # print(Text_display_result_value)

    if len(Text_display_result_value) > 0:

        # 刪除多行文本輸入框中的内容;
        Text_display_result.delete(
            "1.0",  # 參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始刪除;
            "end"  # 參數爲 "end" 表示刪除直至最後一個字符，即清空輸入框;
        )

        Text_display_result.see("end"),  # 表示將 .Text 組件中聚焦在文本末行，即顯示末尾;

    # # 將字符串寫入多行文本輸入框;
    # Text_display_result.insert(
    #     "end",  # 參數 "1.0" 表示從第一行第一列開始插入，參數 "insert" 表示在當前光標位置處插入一個字符串，參數 "end" 表示在末尾位置處追加寫入一個字符串;
    #     str(new_Text_display_result_value)
    # )

    return_value = ""

    if is_Concurrent == "Multi-Threading":

        if not is_window:
            screenwidth = int(0)
            screenheight = int(0)
        # outqueue_from_task_to_host = queue.Queue(maxsize=0)
        # outqueue_from_host_to_task = queue.Queue(maxsize=0)

        # print("process-" + str(multiprocessing.current_process().pid) + " thread-" + str(threading.currentThread().ident) + " ( name: " + str(threading.currentThread().name) + " )")

        # # 使用 Python 原生的多執行緒（缐程）支持 threading 庫的 threading.Thread(target=do_Function, args=(args1, args2)) 創建一個子缐程，用於調用讀取指定文檔並處理數據函數;
        # # 第一個參數 target=do_Function 是子執行緒（缐程）函數變量，第二個參數 args=(args1, args2) 是一個數組變量參數，如果只傳遞一個參數就只需要 args1，如果要傳遞多個參數，可以使用元組，當元組中只包含一個元素時，需要在元素後面添加逗號，例如 args=(args1,) 形式;
        # t = threading.Thread(target=read_file_do_Function, args=(monitor_file,), daemon=True)
        # # 參數：daemon=True，表示把創建的子缐程設爲守護缐程，當主缐程關閉時，子缐程同時關閉，這個標識必須在 .start() 方法調用之前設置;
        # t.start()  # 啓動子缐程;
        # # threading.Condition()

        # # 使用 Python 原生的多進程支持 multiprocessing 庫的 multiprocessing.Process(target=do_Function, args=(args1, args2)) 創建一個子進程，用於調用讀取指定文檔並處理數據函數;
        # # 第一個參數 target=do_Function 是子進程函數變量，第二個參數 args=(args1, args2) 是一個數組變量參數，如果只傳遞一個參數就只需要 args1，如果要傳遞多個參數，可以使用元組，當元組中只包含一個元素時，需要在元素後面添加逗號，例如 args=(args1,) 形式;
        # p = multiprocessing.Process(target=read_file_do_Function, args=(monitor_file, monitor_dir, do_Function, output_dir, output_file, to_executable, to_script))
        # p.setDaemon(True)  # 把創建的子進程設爲守護進程，當主缐程關閉時，子進程同時關閉，這個標識必須在 .start() 方法調用之前設置;
        # p.start()  # 啓動子進程;
        # P.close()  # 關閉Process物件，並釋放與之關聯的所有資源，如果底層進程仍在運行，則會引發ValueError。而且，一旦close()方法成功返回，Process物件的大多數方法和屬性也可能會引發ValueError;
        # # P.terminate  # 强制終止進程子進程，如果調用此函數,進程P將被立即終止，同時不會進行任何清理動作，在Unix上使用的是SIGTERM信號，在Windows上使用的是TerminateProcess()。注意，進程的後代進程不會被終止（會變成“孤兒”進程）。另外，如果被終止的進程在使用Pipe或Queue時，它們有可能會被損害，並無法被其他進程使用；如果被終止的進程已獲得鎖或信號量等，則有可能導致其他進程鎖死。所以請謹慎使用此方法，如果p保存了一個鎖或參與了進程間通信，那麼終止它可能會導致鎖死或I/O損壞;
        # p.join()  # .join() 函數會使得主進程阻塞等待，直到該被調用的子進程運行結束或超時，才繼續執行主進程，要在 .close() 和 .terminate 方法之後使用;
        # # p.pid
        # # p.name
        # # p.ident
        # # p.sentinel

        window_root.after(5, Queue_update, outqueue_from_task_to_host)

        thr = threading.Thread(
            target = Run,
            args = (
                Path_Conversion,
                Input_and_Output,
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
                outqueue_from_host_to_task
            ),
            daemon = True  # 把創建的子缐程設爲守護缐程，當主缐程關閉時，子缐程同時關閉，這個標識必須在 .start() 方法調用之前設置;
        )
        thr.start()

    if is_Concurrent == "0" or is_Concurrent == 0:

        if not is_window:
            screenwidth = int(0)
            screenheight = int(0)
        # outqueue_from_task_to_host = None
        # outqueue_from_host_to_task = None

        return_value = Run(
            Path_Conversion,
            Input_and_Output,
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
            outqueue_from_host_to_task
        )
        # print(return_value)

        # inputTrain_File_Array = []
        # inputValidation_File_Array = []
        inputTest_File_Array = []
        outputTest_File_Array = []

        if is_Runing:
            is_Runing = not is_Runing
        if is_Runing:
            Button_start_and_stop_Test['text'] = "Stop Test"
            Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        else:
            Button_start_and_stop_Test['text'] = "Start Test"
            Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

        # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
        # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
        print(return_value)
        # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
        Label_State['text'] = str('\n'.join(return_value.split(',')))
        # Label_State['text'] = "Stand by"

        Label_display_sample['text'] = "Input file"  # "悟空，您好.",
        Canvas_display_sample.delete("all")

        # 使用消息提示框控件給出溫馨提示;
        tk_messagebox.showinfo(
            title = "溫馨提示",
            message = str('\n'.join(return_value.split(',')))
        )

        return return_value  # None

# 創建啓動訓練程式按鈕（tkinter.Button）組件;
Button_start_and_stop_Train = tk.Button(
    master=window_root,
    text="Start Train",
    # image=img_1,
    compound="center",
    cursor="hand2",
    state="disabled",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=click_Button_start_and_stop_Train  # 指定按鈕控件被單擊後執行的函數;
)
# 將按鈕（tkinter.Button）組件插入到窗體介面;
# Button_start_and_stop_Train.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="right",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     # fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     # expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Button_start_and_stop_Train.grid(
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


def click_Button_start_and_stop_Test():

    global screenwidth
    global screenheight
    global is_storage_position
    global is_storage_type
    # global default_input_tabel_tesseract_config  # = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    # global input_tabel_tesseract_config
    # global default_input_measuringRuler_tesseract_config  # = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    # global input_measuringRuler_tesseract_config
    # global tabel_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    # global measuringRuler_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    global inputTrain_path
    global inputTrain_File_Array
    # global inputValidation_path
    # global inputValidation_File_Array
    global inputTest_path
    global inputTest_File_Array
    global outputTest_path
    global outputTest_File_Array
    global outputTest_URL

    global complete_Number
    complete_Number = int(0)

    global is_Concurrent
    # if is_Concurrent == "Multi-Threading":
    #     if not outqueue_from_task_to_host:
    #         outqueue_from_task_to_host = queue.Queue(maxsize=0)
    #     if not outqueue_from_host_to_task:
    #         outqueue_from_host_to_task = queue.Queue(maxsize=0)

    global is_Runing
    is_Runing = not is_Runing
    if is_Runing:

        if is_Concurrent == "Multi-Threading":
            if outqueue_from_host_to_task:
                outqueue_from_host_to_task.put(
                    [
                        "is_Runing_True",
                        ""
                    ],
                    block=False,
                    timeout=None
                )

        Button_start_and_stop_Test['text'] = "Stop Test"
        Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

    else:
        # print("程式被中止.")
        if is_Concurrent == "Multi-Threading":
            if outqueue_from_host_to_task:
                outqueue_from_host_to_task.put(
                    [
                        "is_Runing_False",
                        ""
                    ],
                    block=False,
                    timeout=None
                )

        if is_Concurrent == "0" or is_Concurrent == 0:
            # sys.stdout.write('\n')
            # sys.stdout.write("Discontinue," + str(complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTest_path + "," + outputTest_path)  # 將字符串輸出寫到操作系統控制臺;
            print("Discontinue," + str(complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTest_path + "," + outputTest_path)  # 將字符串輸出寫到操作系統控制臺;
            # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
            # Label_State['text'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + inputTest_path + " ]." + "\n" + "Output: [ " + outputTest_path + " ]." + "\n" + "discontinue [ " + str(complete_Number) + " ]."
            Label_State['text'] = "Stand by"

            Button_start_and_stop_Test['text'] = "Start Test"
            Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

            # 使用消息提示框控件給出溫馨提示;
            tk_messagebox.showinfo(
                title = "溫馨提示",
                message = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "\n" + "Input: [ " + inputTest_path + " ]." + "\n" + "Output: [ " + outputTest_path + " ]." + "\n" + "Discontinue [ " + str(complete_Number) + " ]."
            )

        return "Discontinue," + str(complete_Number) + "," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTest_path + "," + outputTest_path  # None

    global Error_Log
    Error_Log = []

    global input_tabel_tesseract_config
    input_tabel_tesseract_config = str(Entry_tabel_tesseract_config.get())  # 讀取表格（tabel）内的文本識別（Google tesseract）的參數（tesseract config）文本輸入框輸入的内容; # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    global tabel_tesseract_config
    tabel_tesseract_config = input_tabel_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    global input_measuringRuler_tesseract_config
    input_measuringRuler_tesseract_config = str(Entry_measuringRuler_tesseract_config.get())  # 讀取測量尺（Measuring Ruler）標識的文本識別（Google tesseract）的參數（tesseract config）文本框輸入的内容; # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
    global measuringRuler_tesseract_config
    measuringRuler_tesseract_config = input_measuringRuler_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;

    inputTrain_path = str(Entry_inputTrain_path.get())  # 讀取訓練集樣本位置文本框輸入的内容;

    if len(inputTrain_path) == 0:

        # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(inputTrain_path))  # 將字符串輸出寫到操作系統控制臺;
        print("運行錯誤." + "\n" + "訓練集樣本傳入路徑: " + "\n" + "[ " + inputTrain_path + " ]" + "\n" + "爲空.")
        # Label_State['text'] = "參數錯誤." + "\n" + "訓練集樣本傳入路徑: " + "\n" + "[ " + inputTrain_path + " ]" + "\n" + "爲空."
        Label_State['text'] = "Stand by"

        # Error_Log.append(inputTrain_path)

        if is_Runing:
            is_Runing = not is_Runing
        if is_Runing:
            Button_start_and_stop_Test['text'] = "Stop Test"
            Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        else:
            Button_start_and_stop_Test['text'] = "Start Test"
            Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

        # 使用消息提示框控件給出溫馨提示;
        tk_messagebox.showinfo(
            title = "溫馨提示",
            message = "參數錯誤." + "\n" + "訓練集樣本傳入路徑: " + "\n" + "[ " + inputTrain_path + " ]" + "\n" + "爲空."
        )

        return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTrain_path

    inputTrain_path = str(inputTrain_path).replace('\\', '/')
    # print("input train path:", inputTrain_path)

    # inputValidation_path = str(Entry_inputValidation_path.get())  # 讀取驗證集樣本位置文本框輸入的内容;

    # if len(inputValidation_path) == 0:

    #     # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(inputValidation_path))  # 將字符串輸出寫到操作系統控制臺;
    #     print("運行錯誤." + "\n" + "驗證集樣本傳入路徑: " + "\n" + "[ " + inputValidation_path + " ]" + "\n" + "爲空.")
    #     # Label_State['text'] = "參數錯誤." + "\n" + "驗證集樣本傳入路徑: " + "\n" + "[ " + inputValidation_path + " ]" + "\n" + "爲空."
    #     Label_State['text'] = "Stand by"

    #     # Error_Log.append(inputValidation_path)

    #     if is_Runing:
    #         is_Runing = not is_Runing
    #     if is_Runing:
    #         Button_start_and_stop_Test['text'] = "Stop Test"
    #         Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;    
    #         Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #     else:
    #         Button_start_and_stop_Test['text'] = "Start Test"
    #         Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    #         # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
    #         Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

    #     # 使用消息提示框控件給出溫馨提示;
    #     tk_messagebox.showinfo(
    #         title = "溫馨提示",
    #         message = "參數錯誤." + "\n" + "驗證集樣本傳入路徑: " + "\n" + "[ " + inputValidation_path + " ]" + "\n" + "爲空."
    #     )

    #     return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputValidation_path

    # inputValidation_path = str(inputValidation_path).replace('\\', '/')
    # # print("input validation path:", inputValidation_path)

    inputTest_path = str(Entry_inputTest_path.get())  # 讀取測試集樣本位置文本框輸入的内容;

    if len(inputTest_path) == 0:

        # sys.stdout.write("Error," + + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," str(inputTest_path))  # 將字符串輸出寫到操作系統控制臺;
        print("運行錯誤." + "\n" + "測試集樣本傳入路徑: " + "\n" + "[ " + inputTest_path + " ]" + "\n" + "爲空.")
        # Label_State['text'] = "參數錯誤." + "\n" + "測試集樣本傳入路徑: " + "\n" + "[ " + inputTest_path + " ]" + "\n" + "爲空."
        Label_State['text'] = "Stand by"

        # Error_Log.append(inputTest_path)

        if is_Runing:
            is_Runing = not is_Runing
        if is_Runing:
            Button_start_and_stop_Test['text'] = "Stop Test"
            Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        else:
            Button_start_and_stop_Test['text'] = "Start Test"
            Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

        # 使用消息提示框控件給出溫馨提示;
        tk_messagebox.showinfo(
            title = "溫馨提示",
            message = "參數錯誤." + "\n" + "測試集樣本傳入路徑: " + "\n" + "[ " + inputTest_path + " ]" + "\n" + "爲空."
        )

        return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + inputTest_path

    inputTest_path = str(inputTest_path).replace('\\', '/')
    # print("input test path:", inputTest_path)

    global is_storage_type
    is_storage_type = str(Radiobutton_storage_type_Var.get())
    # print("storage type:", is_storage_type)

    outputTest_path = str(Entry_outputTest_path.get())  # 讀取結果輸出位置文本框輸入的内容;

    if len(outputTest_path) == 0:

        if len(is_storage_position) == 0:
            is_storage_position = ""
            # Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
            Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
            # Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
        elif is_storage_position == "Disk":
            is_storage_position = ""
            # Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
            Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
            # Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
        elif is_storage_position == "Database_and_Disk":
            is_storage_position = "Database"
            # Checkbutton_storage_position_Disk.select()  # 選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
            Checkbutton_storage_position_Disk.deselect()  # 取消選中存儲位置爲磁碟（Disk）的複選框（tkinter.Checkbutton）組件;
            Checkbutton_storage_position_Database.select()  # 選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;
            # Checkbutton_storage_position_Database.deselect()  # 取消選中存儲位置爲資料庫（Database）的複選框（tkinter.Checkbutton）組件;

        is_storage_type = ""
        # print("storage type:", is_storage_type)

        # Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
        Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
        # Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
        Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
        # Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
        Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
        # Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
        Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;

        # # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
        # print("運行錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "爲空.")
        # # Label_State['text'] = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "爲空."
        # Label_State['text'] = "Stand by"

        # # Error_Log.append(outputTest_path)

        # if is_Runing:
        #     is_Runing = not is_Runing
        # if is_Runing:
        #     Button_start_and_stop_Test['text'] = "Stop Test"
        #     Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        # else:
        #     Button_start_and_stop_Test['text'] = "Start Test"
        #     Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        #     # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
        #     Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

        # # 使用消息提示框控件給出溫馨提示;
        # tk_messagebox.showinfo(
        #     title = "溫馨提示",
        #     message = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "爲空."
        # )

        # return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + outputTest_path

    outputTest_path = str(outputTest_path).replace('\\', '/')
    # print("output test path:", outputTest_path)

    if len(outputTest_path) > 0:

        if outputTest_path.find(".", 0, int(len(outputTest_path)-1)) != -1:

            is_storage_type = str(outputTest_path.split('.')[len(outputTest_path.split('.'))-1])
            # print("storage type:", is_storage_type)
            if is_storage_type == "json":
                Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_txt.deselect()
                Radiobutton_storage_type_Excel.deselect()
                Radiobutton_storage_type_json.select()  # 選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
            elif is_storage_type == "csv":
                Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_txt.deselect()
                Radiobutton_storage_type_Excel.deselect()
                Radiobutton_storage_type_csv.select()  # 選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
            elif is_storage_type == "txt":
                Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_csv.deselect()
                Radiobutton_storage_type_Excel.deselect()
                Radiobutton_storage_type_txt.select()  # 選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
            elif is_storage_type == "xlsx":
                Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_csv.deselect()
                Radiobutton_storage_type_txt.deselect()
                Radiobutton_storage_type_Excel.select()  # 選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
            elif len(is_storage_type) == 0:
                Radiobutton_storage_type_json.deselect()  # 取消選中存儲類型爲 JSON 文本（.json）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_csv.deselect()  # 取消選中存儲類型爲 CSV 文本（.csv）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_txt.deselect()  # 取消選中存儲類型爲 TXT 文本（.txt）的單選框（tkinter.Radiobutton）組件;
                Radiobutton_storage_type_Excel.deselect()  # 取消選中存儲類型爲 Microsoft Excel 文檔（.xlsx）的單選框（tkinter.Radiobutton）組件;
            else:

                # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
                print("運行錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規.")
                # Label_State['text'] = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規."
                Label_State['text'] = "Stand by"

                # Error_Log.append(outputTest_path)

                if is_Runing:
                    is_Runing = not is_Runing
                if is_Runing:
                    Button_start_and_stop_Test['text'] = "Stop Test"
                    Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                else:
                    Button_start_and_stop_Test['text'] = "Start Test"
                    Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                    # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                    Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

                # 使用消息提示框控件給出溫馨提示;
                tk_messagebox.showinfo(
                    title = "溫馨提示",
                    message = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規."
                )

                return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + outputTest_path

        else:

            # sys.stdout.write("Error," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + str(outputTest_path))  # 將字符串輸出寫到操作系統控制臺;
            print("運行錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規.")
            # Label_State['text'] = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規."
            Label_State['text'] = "Stand by"

            # Error_Log.append(outputTest_path)

            if is_Runing:
                is_Runing = not is_Runing
            if is_Runing:
                Button_start_and_stop_Test['text'] = "Stop Test"
                Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            else:
                Button_start_and_stop_Test['text'] = "Start Test"
                Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
                # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
                Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

            # 使用消息提示框控件給出溫馨提示;
            tk_messagebox.showinfo(
                title = "溫馨提示",
                message = "參數錯誤." + "\n" + "傳入的運算結果的輸出路徑: " + "\n" + "[ " + outputTest_path + " ]" + "\n" + "類型不合規."
            )

            return "Error," + "1," + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + "," + outputTest_path

    global time_sleep
    global file_Data
    # global file_Data_bytes
    # global file_Data_len
    file_Data = ""
    # file_Data_bytes = file_Data.encode("utf-8")
    # file_Data = file_Data_bytes.decode("utf-8")
    # file_Data = str(file_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
    # file_Data_len = len(bytes(file_Data, "utf-8"))
    global result_Data
    result_Data = ""
    # result_Data_bytes = result_Data.encode("utf-8")
    # result_Data = result_Data_bytes.decode("utf-8")
    # result_Data = str(result_Data_bytes)  # 使用 str() 方法將二進制字節類型的變量轉換爲字符串類型的變量;
    # result_Data_len = len(bytes(result_Data, "utf-8"))
    global image_sample
    image_sample = []

    # print(inputTrain_path)
    if len(inputTrain_File_Array) == 0:
        if len(inputTrain_path) > 0:
            # inputTrain_File_Array = []
            inputTrain_File_Array = Path_Conversion(inputTrain_path, time_sleep)[0]

    # print(inputValidation_path)
    # if len(inputValidation_File_Array) == 0:
    #     if len(inputValidation_path) > 0:
    #         # inputValidation_File_Array = []
    #         inputValidation_File_Array = Path_Conversion(inputValidation_path, time_sleep)[0]

    # print(inputTest_path)
    if len(inputTest_File_Array) == 0:
        if len(inputTest_path) > 0:
            # inputTest_File_Array = []
            inputTest_File_Array = Path_Conversion(inputTest_path, time_sleep)[0]

    # print(outputTest_path)
    if len(outputTest_File_Array) == 0:
        if len(outputTest_path) > 0:
            # # outputTest_File_Array = []
            # outputTest_File_Array = Path_Conversion(outputTest_path, time_sleep)[0]
            outputTest_File_Array = [outputTest_path]

    # 讀取多行文本輸入框中的内容;
    Text_display_result_value = Text_display_result.get(
        "0.0",  # 表示讀取多行文本輸入框 .Text 控件中的全部值，如果設定參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始讀取;
        "end"  # 表示讀取至多行文本輸入框 .Text 控件中全部值的最後一個字符爲止;
    )
    Text_display_result_value = str(Text_display_result_value)
    # print(Text_display_result_value)

    if len(Text_display_result_value) > 0:

        # 刪除多行文本輸入框中的内容;
        Text_display_result.delete(
            "1.0",  # 參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始刪除;
            "end"  # 參數爲 "end" 表示刪除直至最後一個字符，即清空輸入框;
        )

        Text_display_result.see("end"),  # 表示將 .Text 組件中聚焦在文本末行，即顯示末尾;

    # # 將字符串寫入多行文本輸入框;
    # Text_display_result.insert(
    #     "end",  # 參數 "1.0" 表示從第一行第一列開始插入，參數 "insert" 表示在當前光標位置處插入一個字符串，參數 "end" 表示在末尾位置處追加寫入一個字符串;
    #     str(new_Text_display_result_value)
    # )

    return_value = ""

    if is_Concurrent == "Multi-Threading":

        if not is_window:
            screenwidth = int(0)
            screenheight = int(0)
        # outqueue_from_task_to_host = queue.Queue(maxsize=0)
        # outqueue_from_host_to_task = queue.Queue(maxsize=0)

        # print("process-" + str(multiprocessing.current_process().pid) + " thread-" + str(threading.currentThread().ident) + " ( name: " + str(threading.currentThread().name) + " )")

        # # 使用 Python 原生的多執行緒（缐程）支持 threading 庫的 threading.Thread(target=do_Function, args=(args1, args2)) 創建一個子缐程，用於調用讀取指定文檔並處理數據函數;
        # # 第一個參數 target=do_Function 是子執行緒（缐程）函數變量，第二個參數 args=(args1, args2) 是一個數組變量參數，如果只傳遞一個參數就只需要 args1，如果要傳遞多個參數，可以使用元組，當元組中只包含一個元素時，需要在元素後面添加逗號，例如 args=(args1,) 形式;
        # t = threading.Thread(target=read_file_do_Function, args=(monitor_file,), daemon=True)
        # # 參數：daemon=True，表示把創建的子缐程設爲守護缐程，當主缐程關閉時，子缐程同時關閉，這個標識必須在 .start() 方法調用之前設置;
        # t.start()  # 啓動子缐程;
        # # threading.Condition()

        # # 使用 Python 原生的多進程支持 multiprocessing 庫的 multiprocessing.Process(target=do_Function, args=(args1, args2)) 創建一個子進程，用於調用讀取指定文檔並處理數據函數;
        # # 第一個參數 target=do_Function 是子進程函數變量，第二個參數 args=(args1, args2) 是一個數組變量參數，如果只傳遞一個參數就只需要 args1，如果要傳遞多個參數，可以使用元組，當元組中只包含一個元素時，需要在元素後面添加逗號，例如 args=(args1,) 形式;
        # p = multiprocessing.Process(target=read_file_do_Function, args=(monitor_file, monitor_dir, do_Function, output_dir, output_file, to_executable, to_script))
        # p.setDaemon(True)  # 把創建的子進程設爲守護進程，當主缐程關閉時，子進程同時關閉，這個標識必須在 .start() 方法調用之前設置;
        # p.start()  # 啓動子進程;
        # P.close()  # 關閉Process物件，並釋放與之關聯的所有資源，如果底層進程仍在運行，則會引發ValueError。而且，一旦close()方法成功返回，Process物件的大多數方法和屬性也可能會引發ValueError;
        # # P.terminate  # 强制終止進程子進程，如果調用此函數,進程P將被立即終止，同時不會進行任何清理動作，在Unix上使用的是SIGTERM信號，在Windows上使用的是TerminateProcess()。注意，進程的後代進程不會被終止（會變成“孤兒”進程）。另外，如果被終止的進程在使用Pipe或Queue時，它們有可能會被損害，並無法被其他進程使用；如果被終止的進程已獲得鎖或信號量等，則有可能導致其他進程鎖死。所以請謹慎使用此方法，如果p保存了一個鎖或參與了進程間通信，那麼終止它可能會導致鎖死或I/O損壞;
        # p.join()  # .join() 函數會使得主進程阻塞等待，直到該被調用的子進程運行結束或超時，才繼續執行主進程，要在 .close() 和 .terminate 方法之後使用;
        # # p.pid
        # # p.name
        # # p.ident
        # # p.sentinel

        window_root.after(5, Queue_update, outqueue_from_task_to_host)

        thr = threading.Thread(
            target = Run,
            args = (
                Path_Conversion,
                Input_and_Output,
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
                outqueue_from_host_to_task
            ),
            daemon = True  # 把創建的子缐程設爲守護缐程，當主缐程關閉時，子缐程同時關閉，這個標識必須在 .start() 方法調用之前設置;
        )
        thr.start()

    if is_Concurrent == "0" or is_Concurrent == 0:

        if not is_window:
            screenwidth = int(0)
            screenheight = int(0)
        # outqueue_from_task_to_host = None
        # outqueue_from_host_to_task = None

        return_value = Run(
            Path_Conversion,
            Input_and_Output,
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
            outqueue_from_host_to_task
        )
        # print(return_value)

        # inputTrain_File_Array = []
        # inputValidation_File_Array = []
        inputTest_File_Array = []
        outputTest_File_Array = []

        if is_Runing:
            is_Runing = not is_Runing
        if is_Runing:
            Button_start_and_stop_Test['text'] = "Stop Test"
            Checkbutton_storage_position_Disk['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_json['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_csv['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_txt['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_Excel['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTrain_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputValidation_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_outputTest_path['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Button_start_and_stop_Train['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "disabled"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
        else:
            Button_start_and_stop_Test['text'] = "Start Test"
            Checkbutton_storage_position_Disk['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Checkbutton_storage_position_Database['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_json['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_csv['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_txt['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Radiobutton_storage_type_Excel['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_tabel_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Entry_measuringRuler_tesseract_config['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputTrain_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_inputValidation_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_inputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            Entry_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_outputTest_path['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Entry_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            # Button_outputTest_URL['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
            # Button_start_and_stop_Train['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal" 表示可讀可寫操作，, state="readonly" 表示只讀操作;
            Button_shut_down['state'] = "normal"  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;

        # sys.stdout.write('\n')  # 在輸出屏幕換行，重啓一行;
        # sys.stdout.write(return_value)  # 將字符串輸出寫到操作系統控制臺;
        print(return_value)
        # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))  # 打印當前日期時間 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())， after_30_Days = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S.%f");
        Label_State['text'] = str('\n'.join(return_value.split(',')))
        # Label_State['text'] = "Stand by"

        Label_display_sample['text'] = "Input file"  # "悟空，您好.",
        Canvas_display_sample.delete("all")

        # 使用消息提示框控件給出溫馨提示;
        tk_messagebox.showinfo(
            title = "溫馨提示",
            message = str('\n'.join(return_value.split(',')))
        )

        return return_value  # None

# 創建啓動或中止運行按鈕（tkinter.Button）組件;
Button_start_and_stop_Test = tk.Button(
    master=window_root,
    text="Start test",
    # image=img_1,
    compound="center",
    cursor="hand2",
    state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=click_Button_start_and_stop_Test  # 指定按鈕控件被單擊後執行的函數;
)
# 將按鈕（tkinter.Button）組件插入到窗體介面;
# Button_start_and_stop_Test.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     # fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     # expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Button_start_and_stop_Test.grid(
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


def click_Button_shut_down():

    window_root.quit()  # 關閉窗口，可以從窗口小部件取值;
    # window_root.destroy()  # 關閉窗口，不能再從窗口小部件取值;
    # window_root.iconify()  # 窗口最小化;
    # window_root.maxsize()  # 窗口最大化;

    return None

# 創建啓動或中止運行按鈕（tkinter.Button）組件;
Button_shut_down = tk.Button(
    master=window_root,
    text="Shut down",
    # image=img_1,
    compound="center",
    cursor="hand2",
    state="normal",  # state="disabled" 表示設置爲鎖定不可操作，state="normal", state="active" 表示可操作;
    command=click_Button_shut_down  # 指定按鈕控件被單擊後執行的函數;
)
# 將按鈕（tkinter.Button）組件插入到窗體介面;
# Button_shut_down.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     # fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     # expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Button_shut_down.grid(
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
Label_State = tk.Label(
    master=window_root,
    text='Stand by',  # 'Label: running state.', '悟空，您好.',
    # anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
    # justify='center'  # 定義對齊方式，可取值：'left', 'right', 'center'，預設值爲：'center' ;
    # bg='#ffffff',  # 背景色，bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
    # fg="#ffffff",  # 前景色;
    # font=('Arial', 12),
    # relief='flat',  # 邊框樣式，可取值：'flat', 'sunken', 'raised', 'groove', 'ridge'，預設值爲：'flat' ;
    # bd=1.0,  # 邊框寬度值;
    # wraplength=0,  # 設置標簽文本爲多少行顯示，預設值爲：0 ;
    # width=30,
    # height=2
)  # 注意，標簽 width 和 height 的單位為「字符」個數;
# 將標簽（tkinter.Label）組件插入窗體介面中;
# Label_State.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Label_State.grid(
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
Text_display_result = tk.Text(
    master=window_root,
    exportselection=True,  # 表示被選中的文本是否可以被複製到剪切板，預設值爲：True，若取：False 值，則表示不允許複製;
    undo=False,  # 表示 .Text 組件是否允許「撤銷」功能，預設值爲：False，若取：True 值，則表示允許「撤銷」功能;
    # autoseparators=True,  # 表示執行撤銷操作時是否自動插入一個「分隔符」（其作用是用於分隔操作記錄），預設值爲：True ;
    width=20,  # 標簽 width 的單位爲「字符」個數;，例如：width=13 表示設置爲 13 個字符的寬度，int(int(screenwidth)*0.4),
    height=4,  # 標簽 height 的單位爲「字符」個數;，例如：height=3 表示設置爲 3 個字符的高度，int(int(screenheight)*0.4),
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
# Text_display_result.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Text_display_result.grid(
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
# 將任何按鍵都綁定到 break 功能，以使多行輸入文本框（tkinter.Text）組件中的内容設置爲只讀，除了「Ctrl」+「c」和「Shift」+「↑」+「↓」+「←」+「→」鍵，從而不鎖定文本複製的功能;
def ctrlEvent(event):
    if (12==event.state and event.keysym=='c') or (event.keysym=='Up') or (event.keysym=='Down') or (event.keysym=='Left') or (event.keysym=='Right'):
        return
    else:
        return "break"
Text_display_result.bind("<Key>", lambda e: ctrlEvent(e))
# 刪除多行文本輸入框中的内容;
# Text_display_result.delete(
#     "1.0",  # 參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始刪除;
#     "end"  # 參數爲 "end" 表示刪除直至最後一個字符，即清空輸入框;
# )
# 設置多行文本輸入框 Text 控件的預設值;
# Text_display_result.insert(
#     "1.0",  # 參數 "1.0" 表示從第一行第一列開始插入，參數 "insert" 表示在當前光標位置處插入一個字符串，參數 "end" 表示在末尾位置處追加寫入一個字符串;
#     str("a1a2a3a4a5a6a7a8a9a10a11a12a13a14a15a16a17a18a19a20a21" + "\n" + "b1b2b3b4b5b6b7b8b9b10b11b12b13b14b15b16b17b18b19b20b21" + "\n" + "c1c2c3c4c5c6c7c8c9c10c11c12c13c14c15c16c17c18c19c20c21" + "\n" + "d1d2d3d4d5d6d7d8d9d10d11d12d13d14d15d16d17d18d19d20d21" + "\n" + "e1e2e3e4e5e6e7e8e9e10e11e12e13e14e15e16e17e18e19e20e21" + "\n" + "f1f2f3f4f5f6f7f8f9f10f11f12f13f14f15f16f17f18f19f20f21")
# )
# Text_display_result.see("end"),  # 表示將 .Text 組件中聚焦在文本末行，即顯示末尾;
# 讀取文本框輸入的内容;
# Text_display_result_value = Text_display_result.get(
#     "0.0",  # 表示讀取多行文本輸入框 .Text 控件中的全部值，如果設定參數爲 "1.0" 表示從多行文本輸入框 .Text 控件中的第一行第一列開始讀取;
#     "end"  # 表示讀取至多行文本輸入框 .Text 控件中全部值的最後一個字符爲止;
# )
# Text_display_result_value = str(Text_display_result_value)
# # Text_display_result_value = str(Text_display_result_value).replace('\\', '/').replace('\n', '')
# print(Text_display_result_value)


# # 創建滾動條（tkinter.Scrollbar）組件;
# Y_Scrollbar_Text_display_result = tk.Scrollbar(
#     master=Text_display_result,  # window_root,
#     orient='vertical'  # 'vertical' 表示設置滾動條垂直滾動，'horizontal' 表示設置滾動條橫向水平滾動;
# )
# # Y_Scrollbar_Text_display_result.grid(
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
# Y_Scrollbar_Text_display_result.pack(
#     anchor="e",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="right",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="y",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
# # 創建滾動條（tkinter.Scrollbar）組件;
# X_Scrollbar_Text_display_result = tk.Scrollbar(
#     master=Text_display_result,  # window_root,
#     orient='horizontal'  # 'vertical' 表示設置滾動條垂直滾動，'horizontal' 表示設置滾動條橫向水平滾動;
# )
# # X_Scrollbar_Text_display_result.grid(
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
# X_Scrollbar_Text_display_result.pack(
#     anchor="s",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="bottom",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="x",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
# # 關聯多行文本輸入框（tkinter.Text）組件和滾動條（tkinter.Scrollbar）組件;
# Y_Scrollbar_Text_display_result.config(command=Text_display_result.yview)
# Text_display_result.config(yscrollcommand=Y_Scrollbar_Text_display_result.set)
# X_Scrollbar_Text_display_result.config(command=Text_display_result.xview)
# Text_display_result.config(xscrollcommand=X_Scrollbar_Text_display_result.set)


# 創建窗體佈局隔離缐條標簽（tkinter.Label）組件;
Label_Isolation = tk.Label(
    master=window_root,
    text='|',
    # bg='#000000',  # 背景色，bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
    # fg="#ffffff",  # 前景色;
    # font=('Arial', 12),
    # relief='flat',  # 邊框樣式，可取值：'flat', 'sunken', 'raised', 'groove', 'ridge'，預設值爲：'flat' ;
    # bd=1.0,  # 邊框寬度值;
    # justify='center'  # 定義對齊方式，可取值：'left', 'right', 'center'，預設值爲：'center' ;
    # anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
    # wraplength=0,  # 設置標簽文本爲多少行顯示，預設值爲：0 ;
    # width=1,  # int(int(screenwidth)*0.4),
    # height=1  # int(int(screenheight)*0.4)
)  # 注意，標簽 width 和 height 的單位為「字符」個數;
# 將標簽（tkinter.Label）組件插入窗體介面中;
# Label_Isolation.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Label_Isolation.grid(
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


# 創建用於展示處理樣本的標簽框架（tkinter.LabelFrame）組件;
LabelFrame_display_sample = tk.LabelFrame(
    master=window_root,
    text="Sample display",
    # bg="#ffffff",  # 參數：bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色;
    borderwidth=1.0
)
# 將標簽框架（tkinter.LabelFrame）組件插入窗體介面中;
# LabelFrame_display_sample.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="right",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     # fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     # expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
LabelFrame_display_sample.grid(
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
Label_display_sample = tk.Label(
    master=LabelFrame_display_sample,  # master=window_root,
    text='Input file',  # '悟空，您好.',
    # bg='#ffffff',  # 背景色，bg="#ffffff" 表示全白色，bg="#000000" 表示全黑色，bg='green' 表示綠色;
    # fg="#ffffff",  # 前景色;
    # font=('Arial', 12),
    # relief='flat',  # 邊框樣式，可取值：'flat', 'sunken', 'raised', 'groove', 'ridge'，預設值爲：'flat' ;
    # bd=1.0,  # 邊框寬度值;
    # justify='center'  # 定義對齊方式，可取值：'left', 'right', 'center'，預設值爲：'center' ;
    # anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
    # wraplength=0,  # 設置標簽文本爲多少行顯示，預設值爲：0 ;
    # width=30,
    # height=2
)  # 注意，標簽 width 和 height 的單位為「字符」個數;
# 將標簽（tkinter.Label）組件插入窗體介面中;
# Label_display_sample.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Label_display_sample.grid(
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
# Label_display_sample['text'] = "./test.png"

# 創建處理樣本展示畫布（tkinter.Canvas）控件，並在畫布中插入自定義圖片;
Canvas_display_sample = tk.Canvas(
    master=LabelFrame_display_sample,  # master=window_root,
    width=int(int(screenwidth)*0.41),
    height=int(int(screenheight)*0.55),
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
# Canvas_display_sample.pack(
#     anchor="center",  # 設置控件中的内容西對齊，參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     # side="top",  # 設置控件在窗體中放置的位置左對齊，"top", "bottom", "left", "right";
#     fill="both",  # 設置控件填滿窗體中所在位置，參數："both" 橫向、縱向空間都填充，如取值 "x" 表示只填充橫向空間，如取 "y" 值表示只填充縱向空間;
#     expand=1  # 設置允許控件在橫向、縱向拉伸;
# )
Canvas_display_sample.grid(
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
# image_sample = []
# image_sample = tk.PhotoImage(file="./test.png")
# imgFile = Image.open("./test.png").resize((int(int(screenwidth)*0.42), int(int(screenheight)*0.55)))  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.Image.open() 函數打開圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;
# image_sample = ImageTk.PhotoImage(imgFile)  # 使用第三方擴展包 pillow 中的 PIL 模組中的 PIL.ImageTk.PhotoImage() 函數讀取圖片檔，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pillow -i https://mirrors.aliyun.com/pypi/simple/;
# imgFile.close()
# 清除自定義畫布組件中已經繪製的指定圖片;
# Canvas_display_sample.delete("all")
# Canvas_display_sample.delete(tag="one")
# Canvas_display_sample.create_image(
#     0,
#     0,
#     anchor="nw",  # 參數：anchor 表示組件定位，分別使用：「"e"」、「"w"」、「"s"」、「"n"」、「"center"」表示東西南北中;
#     image=image_sample,
#     # fill="red",
#     tag="one"
# )


def on_closing():

    # 使用消息提示框控件給出溫馨提示;
    # tk_messagebox.showinfo(
    #     title="溫馨提示",
    #     message="窗口關閉事件被觸發：WM_DELETE_WINDOW"
    # )

    # # 使用消息問詢框控件做確認動作;
    # if tk_messagebox.askokcancel("Quit", "Do you want to quit?"):
    #     window_root.quit()  # 關閉窗口，可以從窗口小部件取值;
    #     # window_root.destroy()  # 關閉窗口，不能再從窗口小部件取值;
    #     # window_root.iconify()  # 窗口最小化;
    #     # window_root.maxsize()  # 窗口最大化;

    window_root.quit()  # 關閉窗口，可以從窗口小部件取值;
    # window_root.destroy()  # 關閉窗口，不能再從窗口小部件取值;
    # window_root.iconify()  # 窗口最小化;
    # window_root.maxsize()  # 窗口最大化;

    return None

window_root.protocol("WM_DELETE_WINDOW", on_closing)  # 監聽捕捉窗口關閉事件，並綁定觸發執行的回調函數;

# 主窗口循環顯示;
window_root.mainloop()
# 注意，loop 是循環的意思，該行代碼會讓窗口（window）不斷地刷新，如果沒有 .mainloop() ，就會是一個靜態的窗口（window），所有的窗口對象 tk.TK() 都必須有 .mainloop() 函數;



# 通過命令列工具進入 app 目錄下，在該目錄下執行如下命令：
# root@localhost:~# pyinstaller -F -w ./test.py
# 上面命令中的「-F」選項指定生成單個的可執行程式，「-w」選項指定生成圖形化使用者介面程式（不需要命令列介面）。運行上面命令，該工具同樣在「app」目錄下生成了一個「dist」子目錄，並在該子目錄下生成了一個「app-window.exe」文件。
# 直接按兩下運行「app-window.exe」程式（該程式有圖形化使用者介面，因此可以按兩下運行），可查看運行結果。

# C:\Criss\OCR-Measuring-Scale\Scripts\python.exe C:\Criss\OCR-Measuring-Scale\src\py\OCR-Measuring-Scale.py is_window=False is_Concurrent=0
