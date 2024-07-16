## Computer Automated Measurement , Optical Character Recognition
#### Computer Automated Measurement using Intel-OpenCV ( Open Source Computer Vision Library ) and HP-Google-Tesseract ( Optical Character Recognition ).
#### Graphical User Interface using Python tkinter.
#### Intel OpenCV ( Open Source Computer Vision Library ) 4.8.1.78
#### HP Google Tesseract ( Optical Character Recognition ) 5.4.1
#### Python tkinter 3.12.4
#### 量表 ( Scale ) 數據識別, 使用 Intel OpenCV 和 HP Google Tesseract 和 Python tkinter 製作的, 計算機輔助測量 ( Computer Automated Measurement ) 的圖形化工具.
---
<p word-wrap: break-word; word-break: break-all; overflow-x: hidden; overflow-x: hidden;>
使用計算機視覺 ( Optical Character Recognition ) 的方法, 識別量表 ( Scale ) 資訊, 使用計算機輔助測量 ( Computer Automated Measurement ) 的方法, 識別計算量表 ( Scale ) 測量值數據.

其中, 量表 ( Scale ) 圖片 ( Image ) 降噪分割使用第三方 Intel OpenCV ( Open Source Computer Vision Library ) 工具包.

[圖形處理工具包 Intel OpenCV ( Open Source Computer Vision Library ) 官方網站](https://opencv.org/): 
https://opencv.org/

其中, 量表 ( Scale ) 圖片 ( Image ) 識別使用第三方 HP Google Tesseract ( Optical Character Recognition ) 工具包.

[圖形識別工具包 HP Google Tesseract ( Optical Character Recognition ) 官方網站](https://code.google.com/p/tesseract-ocr/): 
https://code.google.com/p/tesseract-ocr/

圖形化人機交互介面 ( Graphical User Interface ) 使用 Python tkinter 工具包.

[計算機程式設計語言 Python 解釋器 ( Interpreter ) 官方網站](https://www.python.org/): 
https://www.python.org/
</p>

---

使用 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 説明 :

一. 項目 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 運行需要 Python 環境, 所以運行之前, 需對作業系統 ( Operating System ) 安裝配置 Python 環境成功方可.

    可在 Linux-Ubuntu 系統的控制臺命令列人機交互介面窗口 ( Ubuntu-bash ) 使用如下指令, 安裝配置 Python 環境 :

    root@localhost:~# sudo apt install python3

二. 首先需要下載安裝配置 HP Google Tesseract ( Optical Character Recognition ) 工具包, 或者, 也可以將其配置保存在項目空間 : ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/ 文件夾裏.

    可在 Linux-Ubuntu 系統的控制臺命令列人機交互介面窗口 ( Ubuntu-bash ) 使用如下指令, 安裝配置 HP Google Tesseract ( Optical Character Recognition ) 工具包 :

    root@localhost:~# sudo apt install tesseract-ocr

    或者, 首先, 在 Linux-Ubuntu 系統的控制臺命令列人機交互介面窗口 ( Ubuntu-bash ) 使用如下指令, 下載 HP Google Tesseract ( Optical Character Recognition ) 工具包 :

    root@localhost:~# wget https://notesalexp.org/tesseract-ocr5/bionic/pool/main/t/tesseract/tesseract-ocr_5.3.0-1_amd64.deb

    然後, 在 Linux-Ubuntu 系統的控制臺命令列人機交互介面窗口 ( Ubuntu-bash ) 使用如下指令, 安裝配置 HP Google Tesseract ( Optical Character Recognition ) 工具包, 將其配置保存在項目空間 : ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/ 文件夾裏 :

    root@localhost:~# sudo dpkg-deb -R --unpack ./tesseract-ocr_5.3.0-1_amd64.deb ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/

    可在 Window10 系統的控制臺命令列人機交互介面窗口 ( Windows-bat ) 使用如下指令, 下載 HP Google Tesseract ( Optical Character Recognition ) 工具包 :

    C:\> wget https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.3.0.20221214.exe

    然後, 在 Window10 系統的控制臺命令列人機交互介面窗口 ( Windows-bat ) 使用如下指令, 安裝配置 HP Google Tesseract ( Optical Character Recognition ) 工具包 :

    C:\> C:\tesseract-ocr-w64-setup-v5.3.0.20221214.exe

    若想調整保存路徑, 選擇將其安裝配置在項目空間 : ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/ 文件夾裏即可.

三. 手動創建配置計算機程式設計語言 Python 解釋器 ( Interpreter ) 項目 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 的隔離環境 :

    root@localhost:~# /usr/bin/python3 -m venv ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/

四. 激活計算機程式設計語言 Python 解釋器 ( Interpreter ) 的隔離環境 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 項目 :

    root@localhost:~# ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Scripts/activate

五. 手動配置計算機程式設計語言 Python 解釋器 ( Interpreter ) 的隔離環境 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 項目需要的第三方擴展包, 依照項目空間裏第三方擴展包的列表文檔 ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/packagelist.txt 安裝 :

    root@localhost:~# ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Scripts/pip.exe install --requirement ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/packagelist.txt

六. 以上全部配置完畢, 即可在作業系統 ( Operating System : Linux-Ubuntu , Windows ) 的控制臺命令列人機交互介面窗口 ( Ubuntu-bash , Windows-bat ) 使用如下指令, 啓動運行 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 項目 :

    root@localhost:~# ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Scripts/python3.exe ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/main.py

![]()

---

Operating System :

Acer-NEO-2023 Windows10 x86_64 Inter(R)-Core(TM)-m3-6Y30

Acer-NEO-2023 Linux-Ubuntu-22.04 x86_64 Inter(R)-Core(TM)-m3-6Y30

Google-Pixel-6 Android-11 Termux-0.118 Linux-Ubuntu-22.04-LTS-rootfs Arm64-aarch64 MSM8998-Snapdragon835-Qualcomm®-Kryo™-280

---

Interpreter : python - 3.12.4

[程式設計 Python 語言解釋器 ( Interpreter ) 官方網站](https://www.python.org/): 
https://www.python.org/

[程式設計 Python 語言解釋器 ( Interpreter ) 官方下載頁](https://www.python.org/downloads/): 
https://www.python.org/downloads/

[程式設計 Python 語言解釋器 ( Interpreter ) 官方 GitHub 網站賬戶](https://github.com/python): 
https://github.com/python

[程式設計 Python 語言解釋器 ( Interpreter ) 官方 GitHub 網站倉庫](https://github.com/python/cpython): 
https://github.com/python/cpython.git

Intel OpenCV ( Open Source Computer Vision Library ) - 4.8.1.78

[作業系統 ( Operating system ) 之 Microsoft Windows 官方網站](https://www.microsoft.com/zh-tw/windows): 
https://www.microsoft.com/zh-tw/windows

HP Google Tesseract ( Optical Character Recognition ) - 5.4.1

[作業系統 ( Operating system ) 之 Microsoft Windows 官方網站](https://www.microsoft.com/zh-tw/windows): 
https://www.microsoft.com/zh-tw/windows

---

瀏覽器 ( Browser : Microsoft Internet Explorer , Microsoft Edge , Google Chrome , Mozilla Firefox ) 和解釋器 ( Interpreter : Node.js ) 預編譯二進制可執行檔 [百度網盤(pan.baidu.com)](https://pan.baidu.com/s/1IXjbZBRkurrNRs0GoURCaA?pwd=1dm7) 下載頁: 
https://pan.baidu.com/s/1IXjbZBRkurrNRs0GoURCaA?pwd=1dm7

提取碼：1dm7

---

![]()
