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
# C:\> C:\OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter\Scripts\python.exe C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/main.py configFile=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt is_window=False is_Concurrent=Multi-Threading is_storage_position=Disk is_storage_type=csv input_dir=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/inputTest/ outputTest_path=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/outputTest/test.csv tesseract_cmd=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/tesseract.exe tesseract_tessdata_dir=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tessdata tesseract_user_words=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tesswords input_tabel_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert" input_measuringRuler_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert"
# root@localhost:~# /usr/bin/python3 /home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/main.py configFile=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt is_window=False is_Concurrent=Multi-Threading is_storage_position=Disk is_storage_type=csv input_dir=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/inputTest/ outputTest_path=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/outputTest/test.csv tesseract_cmd=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/tesseract.exe tesseract_tessdata_dir=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tessdata tesseract_user_words=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tesswords input_tabel_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert" input_measuringRuler_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert"

#################################################################################


import os  # 加載 Python 原生的操作系統接口模組「os」;
import sys  # 加載 Python 原生的使用或維護的變量的接口模組「sys」;
import signal, stat  # 加載Python原生的「」;
import math  # 導入 Python 原生包「math」，用於數學計算;
# import random  # 導入 Python 原生包「random」，用於生成隨機數;
import json  # 導入 Python 原生模組「json」，用於解析 JSON 文檔;
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
import string  # 加載Python原生的字符串處理模組;
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
# from scipy import stats as scipy_stats  # 導入第三方擴展包「scipy」，用於實現 beta 分佈概率密度函數;
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
import pytesseract  # 導入第三方擴展包「pytesseract」，用於驅動 Tesseract-OCR 文字識別庫，需要事先在控制臺安裝配置成功：root@localhost:~# pip install pytesseract -i https://mirrors.aliyun.com/pypi/simple/ ，如果是 Ubuntu 系統需要事先安裝 Tesseract-OCR 應用成功：root@localhost:~# apt install tesseract-ocr libtesseract-dev tesseract-ocr-chi-tra tesseract-ocr-chi_tra_vert tesseract-ocr-chi-sim tesseract-ocr-chi_sim_vert ;
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
sys.path.append(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "src", "py"))).replace('\\', '/'))  # 將當前目錄中的子目錄「"./py/"」加入系統的搜索清單，當導入脚本時會增加搜索這個自定義添加的路徑;
# sys.path.append("C:/Criss/OCR-Measuring-Scale/src/py/")
# print(str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "py"))).replace('\\', '/'))
import window_tkinter as window_tkinter  # 導入當前運行代碼所在目錄的，自定義脚本文檔「./window_tkinter.py」;
# Window_Optical_Character_Recognition = window_tkinter.Window_Optical_Character_Recognition
from window_tkinter import Window_Optical_Character_Recognition as Window_Optical_Character_Recognition
# import Input_and_Output as Input_and_Output  # 導入當前運行代碼所在目錄的，自定義脚本文檔「./Input_and_Output.py」;
# Input_and_Output_Function = Input_and_Output.Input_and_Output
# Run_Input_and_Output = Input_and_Output.Run_Input_and_Output
# Path_Conversion = Input_and_Output.Path_Conversion
# Queue_update = Input_and_Output.Queue_update
# # check_json_format = Input_and_Output.check_json_format
# # win_file_is_Used = Input_and_Output.win_file_is_Used
# # clear_Directory = Input_and_Output.clear_Directory
# # formatByte = Input_and_Output.formatByte
from Input_and_Output import Input_and_Output as Input_and_Output_Function
from Input_and_Output import Run_Input_and_Output as Run_Input_and_Output
from Input_and_Output import Path_Conversion as Path_Conversion
from Input_and_Output import Queue_update as Queue_update
import optical_character_recognition as optical_character_recognition  # 導入當前運行代碼所在目錄的，自定義脚本文檔「./optical_character_recognition.py」;
# do_data = optical_character_recognition.do_data
from optical_character_recognition import do_data as do_data

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

inputTrain_File_Array = []
inputValidation_File_Array = []
inputTest_File_Array = []
outputTest_File_Array = []

outqueue_from_task_to_host = queue.Queue(maxsize=0)
outqueue_from_host_to_task = queue.Queue(maxsize=0)


# 使用 while True: 的方法設置死循環創建看守進程，監聽指定的硬盤目錄或文檔，響應創建事件，從而達到不同語言之間利用硬盤文檔傳輸數據交互的效果;
# 控制臺傳參，通過 sys.argv 數組獲取從控制臺傳入的參數
is_window = True  # bool(True), bool(False) 判斷只需要執行一次還是啓動監聽服務器功能;
is_Concurrent = "0"  # "Multi-Threading"  # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程），可取值：0、"0"、"Multi-Threading"、"Multi-Processes";
# is_storage_position = "Disk"  # 判斷存儲位置，可取值："Database", "Database_and_Disk", "Disk" ;
# is_storage_type = "csv"  # 判斷存儲類型，可取值："json", "csv", "txt", "xlsx";
# os.path.abspath(".")  # 獲取當前文檔所在的絕對路徑;
# os.path.abspath("..")  # 獲取當前文檔所在目錄的上一層路徑;
tesseract_cmd = str(os.path.join(os.path.dirname(os.path.realpath(__file__)), "Tesseract-OCR", "tesseract"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# tesseract_cmd = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tesseract"))
# tesseract_cmd = str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# tesseract_cmd = str(pathlib.Path(os.path.abspath("..") + "/Tesseract-OCR/" + "/tesseract/"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# pytesseract.pytesseract.tesseract_cmd = tesseract_cmd  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
tesseract_tessdata_dir = ""  # "/usr/share/tessdata" # File PATH：用戶自定義指定本地訓練完畢的數據集文檔（tessdata）的儲存路徑位置，使用 Tesseract 識別，需要使用訓練好的數據集，如果不指定該參數，則預設使用系統預設的數據集文檔目錄 Specify the location of tessdata path.
tesseract_user_words = ""  # File PATH：用戶自定義指定的詞庫（字典）文檔的存儲位置，用戶字典可以包含一些特定的詞匯，以提高對特定詞匯的識別準確性，用戶字典文件應爲純文本文檔，每行一個詞匯 Specify the location of user words file.
tesseract_user_patterns = ""  # File PATH：用戶自定義指定的特定格式文本的文檔的存儲位置，即每行使用「某種正則表達式」，例如，正在掃描具有相同格式數據的多張頁面，即可使用此參數，特定格式文本的文檔應爲純文本文檔，每行一個正則表達式模式 Specify the location of user patterns file.
# input_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
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
input_tabel_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
input_measuringRuler_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;


# os.path.abspath(".")  # 獲取當前文檔所在的絕對路徑;
# os.path.abspath("..")  # 獲取當前文檔所在目錄的上一層路徑;
configFile = str(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.txt"))  # "C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt" # "/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt"
# configFile = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config.txt"))  # "C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt" # "/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt"
# monitor_dir = pathlib.Path(os.path.abspath("..") + "config.txt")  # pathlib.Path("../config.txt")
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
        if not (os.access(configFile, os.R_OK) and os.access(configFile, os.W_OK)):
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

        fd = open(configFile, mode="r", buffering=-1, encoding="utf-8", errors=None, newline=None, closefd=True, opener=None)
        # fd = open(configFile, mode="rb+")
        try:
            # data_Str = fd.read()
            # data_Str = fd.read().decode("utf-8")
            # data_Bytes = data_Str.encode("utf-8")
            # fd.write(data_Bytes)
            line_I = int(0)
            lines = file.readlines()
            for line in lines:
                # print(line)

                line_I = line_I + 1
                line_Key = ""
                line_Value = ""

                # 使用函數 isinstance(line, str) 判斷傳入的參數是否為 str 字符串類型 type(line);
                if isinstance(line, str) and line != "":

                    # 判斷字符串是否含有等號字符（=）連接符（Key=Value），若含有等號字符（=），則以等號字符（=）分割字符串;
                    if line.find("=", 0, int(len(line)-1)) != -1:
                        # line_split = line.split("=", -1)  # 分割字符串中含有的所有等號字符（=）;
                        line_split = line.split("=", 1)  # 祇分割字符串中含有的第一個等號字符（=）;
                        line_Key = str(line_split[0])
                        line_Value = str(line_split[1])
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
                        print(line, "unrecognized.")
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
# is_Concurrent = "Multi-Threading"  # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程），可取值：0、"0"、"Multi-Threading"、"Multi-Processes";
# # is_storage_position = "Disk"  # 判斷存儲位置，可取值："Database", "Database_and_Disk", "Disk" ;
# # is_storage_type = "csv"  # 判斷存儲類型，可取值："json", "csv", "txt", "xlsx";
# # os.path.abspath(".")  # 獲取當前文檔所在的絕對路徑;
# # os.path.abspath("..")  # 獲取當前文檔所在目錄的上一層路徑;
# tesseract_cmd = str(os.path.join(os.path.dirname(os.path.realpath(__file__)), "Tesseract-OCR", "tesseract"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# # tesseract_cmd = str(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Tesseract-OCR", "tesseract"))
# # tesseract_cmd = str(os.path.join(os.path.abspath(".."), "Tesseract-OCR", "tesseract"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# # tesseract_cmd = str(pathlib.Path(os.path.abspath("..") + "/Tesseract-OCR/" + "/tesseract/"))  # r'C:/Tesseract-OCR/tesseract'  # 'C:/Tesseract-OCR/tesseract.exe'  # r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# # pytesseract.pytesseract.tesseract_cmd = tesseract_cmd  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置;
# tesseract_tessdata_dir = ""  # "/usr/share/tessdata" # File PATH：用戶自定義指定本地訓練完畢的數據集文檔（tessdata）的儲存路徑位置，使用 Tesseract 識別，需要使用訓練好的數據集，如果不指定該參數，則預設使用系統預設的數據集文檔目錄 Specify the location of tessdata path.
# tesseract_user_words = ""  # File PATH：用戶自定義指定的詞庫（字典）文檔的存儲位置，用戶字典可以包含一些特定的詞匯，以提高對特定詞匯的識別準確性，用戶字典文件應爲純文本文檔，每行一個詞匯 Specify the location of user words file.
# tesseract_user_patterns = ""  # File PATH：用戶自定義指定的特定格式文本的文檔的存儲位置，即每行使用「某種正則表達式」，例如，正在掃描具有相同格式數據的多張頁面，即可使用此參數，特定格式文本的文檔應爲純文本文檔，每行一個正則表達式模式 Specify the location of user patterns file.
# # input_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
# inputTrain_path = default_inputTrain_path  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
# inputValidation_path = default_inputValidation_path  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
# inputTest_path = default_inputTest_path  # 用於接收傳值的媒介文檔 "../temp/intermediary_write_Node.txt";
# Input_and_Output_Function = Input_and_Output_Function  # 操作硬盤文檔的函數讀取或寫入;
# do_Function = do_data  # 用於接收執行功能的函數 "do_data";
# # output_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')
# outputTest_path = default_outputTest_path  # 用於輸出傳值的媒介文檔 "../temp/intermediary_write_Python.txt";
# outputTest_URL = default_outputTest_URL
# # temp_cache_IO_data_dir = ""  # 用於暫存輸入輸出傳值文檔的媒介目錄 temp_cache_IO_data_dir = "../temp/";
# # number_Worker_process = int(0)  # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
# time_sleep = float(0.01)  # float(0.05) 用於監聽程序的輪詢延遲參數，單位（秒）;
# screenwidth = int(0)  # int(tk.Tk().winfo_screenwidth())  # 獲取顯示器屏幕寬度;
# screenheight = int(0)  # int(tk.Tk().winfo_screenheight())  # 獲取顯示器屏幕高度;
# input_tabel_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
# input_measuringRuler_tesseract_config = '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
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
                # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程）可取值：is_Concurrent = 0 or "0" or "Multi-Threading" or "Multi-Processes";
                elif sys.argv[i].split("=", -1)[0] == "is_Concurrent":
                    is_Concurrent = str(sys.argv[i].split("=", -1)[1])  # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程），可取值：is_Concurrent = 0 or "0" or "Multi-Threading" or "Multi-Processes";
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

                # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置 tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe";
                elif sys.argv[i].split("=", -1)[0] == "tesseract_cmd":
                    tesseract_cmd = sys.argv[i].split("=", -1)[1]  # 指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置 "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe";
                    # print("Tesseract Cmd:", tesseract_cmd)
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
                # 用於輸入傳值的媒介目錄 input_dir = "../temp/";
                elif sys.argv[i].split("=", -1)[0] == "input_dir":
                    input_dir = sys.argv[i].split("=", -1)[1]  # 用於輸入傳值的媒介目錄 "../temp/";
                    # print("input dir:", input_dir)
                    continue
                # 用於配置 Google Tesseract 的參數（tesseract_config）：input_tabel_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";
                # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                elif sys.argv[i].split("=", -1)[0] == "input_tabel_tesseract_config":
                    input_tabel_tesseract_config = sys.argv[i].split("=", -1)[1]  # 用於配置 Google Tesseract 的參數（tesseract_config）：input_tabel_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";;
                    # print("input tabel tesseract config:", input_tabel_tesseract_config)
                    continue
                # 用於配置 Google Tesseract 的參數（tesseract_config）：input_measuringRuler_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";
                # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                elif sys.argv[i].split("=", -1)[0] == "input_measuringRuler_tesseract_config":
                    input_measuringRuler_tesseract_config = sys.argv[i].split("=", -1)[1]  # 用於配置 Google Tesseract 的參數（tesseract_config）：input_measuringRuler_tesseract_config = "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert";;
                    # print("input measuring ruler tesseract config:", input_measuringRuler_tesseract_config)
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
                # elif sys.argv[i].split("=", -1)[0] == "temp_cache_IO_data_dir":
                #     temp_cache_IO_data_dir = sys.argv[i].split("=", -1)[1]  # 用於輸入傳值的媒介目錄 "../temp/";
                #     # print("temp cache IO data file dir:", temp_cache_IO_data_dir)
                #     continue
                # 用於操作硬盤文檔讀取或寫入的函數 Input_and_Output_Function = "Input_and_Output";
                elif sys.argv[i].split("=", -1)[0] == "Input_and_Output_Function":
                    Input_and_Output_Function = sys.argv[i].split("=", -1)[1]  # 用於操作硬盤文檔讀取或寫入的函數 "Input_and_Output";
                    # print("Input and Output Function:", Input_and_Output_Function)
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
                # # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
                # elif sys.argv[i].split("=", -1)[0] == "number_Worker_process":
                #     number_Worker_process = int(sys.argv[i].split("=", -1)[1])  # 用於判斷生成子進程數目的參數 number_Worker_process = int(0);
                #     # print("number Worker processes:", number_Worker_process)
                #     continue
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
                    print(sys.argv[i], "unrecognized.")
                    # sys.exit(1)  # 中止當前進程，退出當前程序;
                    continue


# # 設定窗口的大小（寬 × 長），單位爲：像素（px）;
# size_XY = '{}x{}+{}+{}'.format(str(int(int(screenwidth)*0.6)), str(int(int(screenheight)*0.6)), str(int(int(screenwidth)*0.2)), str(int(int(screenheight)*0.2)))

window_tkinter.default_input_tabel_tesseract_config = input_tabel_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
window_tkinter.input_tabel_tesseract_config = input_tabel_tesseract_config
window_tkinter.default_input_measuringRuler_tesseract_config = input_measuringRuler_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
window_tkinter.input_measuringRuler_tesseract_config = input_measuringRuler_tesseract_config
optical_character_recognition.tabel_tesseract_config = input_tabel_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
optical_character_recognition.measuringRuler_tesseract_config = input_measuringRuler_tesseract_config  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;

# 函數使用示例;
# 控制臺命令行使用:
# C:\> C:\OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter\Scripts\python.exe C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/main.py configFile=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt is_window=False is_Concurrent=Multi-Threading is_storage_position=Disk is_storage_type=csv input_dir=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/inputTest/ outputTest_path=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/outputTest/test.csv tesseract_cmd=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/tesseract.exe tesseract_tessdata_dir=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tessdata tesseract_user_words=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tesswords input_tabel_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert" input_measuringRuler_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert"
# 啓動運行;
# 參數 C:\OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter\Scripts\python.exe 表示使用隔離環境 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 中的 python.exe 啓動運行;
# 使用示例，自定義類 Window_Optical_Character_Recognition 圖形化用戶交互介面使用説明;
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
                return_value = Run_Input_and_Output(
                    Path_Conversion,
                    Input_and_Output_Function,
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
                    None,  # Label_State,
                    None,  # Text_display_result,
                    image_sample,
                    None,  # Canvas_display_sample,
                    None,  # Label_display_sample
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
                    target = Run_Input_and_Output,
                    args = (
                        Path_Conversion,
                        Input_and_Output_Function,
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
                        None,  # Label_State,
                        None,  # Text_display_result,
                        image_sample,
                        None,  # Canvas_display_sample,
                        None,  # Label_display_sample
                    ),
                    daemon = True  # 把創建的子綫程設爲守護綫程，當主綫程關閉時，子綫程同時關閉，這個標識必須在 .start() 方法調用之前設置;
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

    if is_window:

        # if not is_Runing:
        #     is_Runing = not is_Runing

        # screenwidth = int(0)
        # screenheight = int(0)
        # complete_Number = int(0)
        # Error_Log = []
        # file_Data = ""
        # result_Data = ""
        # image_sample = []

        # # # print(inputTrain_path)
        # # if len(inputTrain_File_Array) == 0:
        # #     if len(inputTrain_path) > 0:
        # #         # inputTrain_File_Array = []
        # #         inputTrain_File_Array = Path_Conversion(inputTrain_path, time_sleep)[0]

        # # # print(inputValidation_path)
        # # if len(inputValidation_File_Array) == 0:
        # #     if len(inputValidation_path) > 0:
        # #         # inputValidation_File_Array = []
        # #         inputValidation_File_Array = Path_Conversion(inputValidation_path, time_sleep)[0]

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

        # os.chdir(monitor_dir)  # 可以先改變工作目錄到 static 路徑;
        try:
            # Input_and_Output_Function = Input_and_Output_Function  # 操作硬盤文檔的函數讀取或寫入;
            # do_Function = do_data  # 用於接收執行功能的函數;
            # do_Function_obj = {
            #     "do_Function": do_Function  # 用於接收執行功能的函數;
            # }
            # time_sleep = float(0.01)  # 用於監聽程序的輪詢延遲參數，單位（秒）;
            # outqueue_from_task_to_host = queue.Queue(maxsize=0)
            # outqueue_from_host_to_task = queue.Queue(maxsize=0)
            # is_Concurrent = "Multi-Threading"  # 選擇監聽動作的函數是否並發（多協程、多綫程、多進程），可取值：0、"0"、"Multi-Threading"、"Multi-Processes";
            # is_storage_position = "Disk"  # "Database", "Database_and_Disk", "Disk" 判斷存儲位置;
            # is_storage_type = "csv"  # "json", "csv", "txt", "xlsx", 判斷存儲類型;
            # # is_window = True  # bool(True), bool(False) 判斷只需要執行一次還是啓動監聽服務器功能;
            # # screenwidth =  int(0)  # int(tk.Tk().winfo_screenwidth())  # 獲取顯示器屏幕寬度;
            # # screenheight =  int(0)  # int(tk.Tk().winfo_screenheight())  # 獲取顯示器屏幕高度;
            # # size_XY = '{}x{}+{}+{}'.format(str(int(int(screenwidth)*0.6)), str(int(int(screenheight)*0.6)), str(int(int(screenwidth)*0.2)), str(int(int(screenheight)*0.2)))
            # iconbitmap_path = ""
            # # 判斷是否爲打包（.exe）後的環境;
            # if getattr(sys, 'frozen', False):
            #     iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "Icon", "iconbitmap.png"))).replace('\\', '/')
            #     # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "Icon", "iconbitmap.png"))).replace('\\', '/')
            #     # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "Icon", "iconbitmap.png"))).replace('\\', '/')
            #     # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "Icon", "iconbitmap.png"))).replace('\\', '/')
            # else:
            #     # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "Icon", "iconbitmap.png"))).replace('\\', '/')
            #     # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "Icon", "iconbitmap.png"))).replace('\\', '/')
            #     # iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "Icon", "iconbitmap.png"))).replace('\\', '/')
            #     iconbitmap_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "Icon", "iconbitmap.png"))).replace('\\', '/')
            # # print(iconbitmap_path)  # "C:/Criss/OCR/src/Icon/iconbitmap.png"
            # inputTrain_path = ""
            # # 判斷是否爲打包（.exe）後的環境;
            # if getattr(sys, 'frozen', False):
            #     inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')
            #     # inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTrain"))).replace('\\', '/')
            #     # inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTrain"))).replace('\\', '/')
            #     # inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTrain"))).replace('\\', '/')
            # else:
            #     inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTrain"))).replace('\\', '/')
            #     # inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTrain"))).replace('\\', '/')
            #     # inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTrain"))).replace('\\', '/')
            #     # inputTrain_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTrain"))).replace('\\', '/')
            # # print(inputTrain_path)
            # inputTrain_File_Array = []
            # if len(inputTrain_File_Array) == 0:
            #     if len(inputTrain_path) > 0:
            #         # inputTrain_File_Array = []
            #         inputTrain_File_Array = Path_Conversion(inputTrain_path, time_sleep)[0]
            # inputValidation_path = ""
            # # 判斷是否爲打包（.exe）後的環境;
            # if getattr(sys, 'frozen', False):
            #     inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')
            #     # inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputValidation"))).replace('\\', '/')
            #     # inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputValidation"))).replace('\\', '/')
            #     # inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputValidation"))).replace('\\', '/')
            # else:
            #     inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputValidation"))).replace('\\', '/')
            #     # inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputValidation"))).replace('\\', '/')
            #     # inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputValidation"))).replace('\\', '/')
            #     # inputValidation_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputValidation"))).replace('\\', '/')
            # # print(inputValidation_path)
            # inputValidation_File_Array = []
            # if len(inputValidation_File_Array) == 0:
            #     if len(inputValidation_path) > 0:
            #         # inputValidation_File_Array = []
            #         inputValidation_File_Array = Path_Conversion(inputValidation_path, time_sleep)[0]
            # inputTest_path = ""
            # # 判斷是否爲打包（.exe）後的環境;
            # if getattr(sys, 'frozen', False):
            #     inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
            #     # inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTest"))).replace('\\', '/')
            #     # inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTest"))).replace('\\', '/')
            #     # inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTest"))).replace('\\', '/')
            # else:
            #     inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
            #     # inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "inputTest"))).replace('\\', '/')
            #     # inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "inputTest"))).replace('\\', '/')
            #     # inputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "inputTest"))).replace('\\', '/')
            # # print(inputTest_path)
            # inputTest_File_Array = []
            # if len(inputTest_File_Array) == 0:
            #     if len(inputTest_path) > 0:
            #         # inputTest_File_Array = []
            #         inputTest_File_Array = Path_Conversion(inputTest_path, time_sleep)[0]
            # # input_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "inputTest"))).replace('\\', '/')
            # outputTest_path = ""
            # # 判斷是否爲打包（.exe）後的環境;
            # if getattr(sys, 'frozen', False):
            #     outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
            #     # outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
            #     # outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
            #     # outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
            # else:
            #     outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
            #     # outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(str(sys.prefix)), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
            #     # outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(os.path.normpath(str(sys.executable))))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
            #     # outputTest_path = str(os.path.normpath(os.path.join(os.path.normpath(os.path.dirname(os.path.abspath(__file__))), "outputTest", "test" + "." + is_storage_type))).replace('\\', '/')
            # # print(outputTest_path)
            # outputTest_File_Array = []
            # if len(outputTest_File_Array) == 0:
            #     if len(outputTest_path) > 0:
            #         # # outputTest_File_Array = []
            #         # outputTest_File_Array = Path_Conversion(outputTest_path, time_sleep)[0]
            #         outputTest_File_Array = [outputTest_path]
            # # output_dir = str(os.path.normpath(os.path.join(os.path.normpath(str(os.getcwd())), "outputTest"))).replace('\\', '/')
            # outputTest_URL = "mongodb://username:password@127.0.0.1:27017/testDB"

            # pid = multiprocessing.current_process().pid, threading.currentThread().ident;

            init_window = tk.Tk()  # 創建 tkinter 的窗體介面;

            # # 獲取顯示器屏幕寬度;
            # screenwidth = int(init_window.winfo_screenwidth())  # int(0)  # int(tk.Tk().winfo_screenwidth())  # 獲取顯示器屏幕寬度;
            # # print(screenwidth)
            # # 獲取顯示器屏幕高度;
            # screenheight = int(init_window.winfo_screenheight())  # int(0)  # int(tk.Tk().winfo_screenheight())  # 獲取顯示器屏幕高度;
            # # print(screenheight)
            # size_XY = '{}x{}+{}+{}'.format(str(int(int(screenwidth)*0.6)), str(int(int(screenheight)*0.6)), str(int(int(screenwidth)*0.2)), str(int(int(screenheight)*0.2)))
            # # print(size_XY)

            # 創建自定義的人機交互介面窗口;
            OCR_GUI = Window_Optical_Character_Recognition(
                initializer_Window=init_window,
                # screenwidth=screenwidth,
                # screenheight=screenheight,
                # size_XY=size_XY,
                iconbitmap_path=iconbitmap_path,
                outqueue_from_task_to_host=outqueue_from_task_to_host,
                outqueue_from_host_to_task=outqueue_from_host_to_task,
                is_Concurrent=is_Concurrent,
                is_storage_position=is_storage_position,
                is_storage_type=is_storage_type,
                default_input_tabel_tesseract_config=input_tabel_tesseract_config,  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                input_tabel_tesseract_config=input_tabel_tesseract_config,
                default_input_measuringRuler_tesseract_config=input_measuringRuler_tesseract_config,  # '--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert'  # 取值爲字符類型，用於指定 Tesseract 的其他配置選項，預設值爲：'--psm 3 --oem 3'，其中 '--psm' 表示頁面分段模式（Page Segmentation Mode），'--psm 3' 爲預設值，表示完全自動分割圖片，'--psm 7' 表示强調圖像中爲單行文字，表示自動分段，'--psm 8' 表示將文本視爲單詞（Text），'--psm 10' 表示將文本視爲單個字符（Character），其中 '--oem' 表示 OCR 引擎模式（OCR Engine Mode），'--oem 3' 爲預設值，'--oem 0' 表示 Legacy Teesseract Engine，'--oem 1' 表示 Neural Nets LSTM Engine，'--oem 3' 表示 Default with fully initialized layout analysis，其中 '-c tessedit_char_whitelist=0123456789' 表示限制爲只需識別的字符白名單，例如只需要識別出阿拉伯數字：0 ~ 9，'-c tessedit_char_blacklist=0123456789' 表示限制忽略不需要識別的字符黑名單，例如不需要識別阿拉伯數字：0 ~ 9，'-c min_characters_to_try=5' 表示設置最小字符數目，預設值爲 50 個;
                input_measuringRuler_tesseract_config=input_measuringRuler_tesseract_config,
                inputTrain_path=inputTrain_path,
                # inputTrain_File_Array=inputTrain_File_Array,
                inputValidation_path=inputValidation_path,
                # inputValidation_File_Array=inputValidation_File_Array,
                inputTest_path=inputTest_path,
                # inputTest_File_Array=inputTest_File_Array,
                outputTest_path=outputTest_path,
                # outputTest_File_Array=outputTest_File_Array,
                outputTest_URL=outputTest_URL,
                Input_and_Output_Function=Input_and_Output_Function,
                do_Function=do_Function,
                # do_Function_obj=do_Function_obj,
                time_sleep=time_sleep
            )

            init_window.mainloop()  # 循環刷新 tkinter 窗體，實時顯示窗體變化;

        except Exception as error:
            print(error)




# 通過命令列工具進入 app 目錄下，在該目錄下執行如下命令：
# root@localhost:~# pyinstaller -F -w ./main.py
# 上面命令中的「-F」選項指定生成單個的可執行程式，「-w」選項指定生成圖形化使用者介面程式（不需要命令列介面）。運行上面命令，該工具同樣在「app」目錄下生成了一個「dist」子目錄，並在該子目錄下生成了一個「app-window.exe」文件。
# 直接按兩下運行「app-window.exe」程式（該程式有圖形化使用者介面，因此可以按兩下運行），可查看運行結果。
