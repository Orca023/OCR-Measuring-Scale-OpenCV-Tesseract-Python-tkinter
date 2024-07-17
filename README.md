## Computer Automated Measurement , Optical Character Recognition
#### Computer Automated Measurement using Intel-OpenCV ( Open Source Computer Vision Library ) and HP-Google-Tesseract ( Optical Character Recognition ).
#### Graphical User Interface using Python tkinter.
#### Intel OpenCV ( Open Source Computer Vision Library ) 4.8.1.78
#### HP Google Tesseract ( Optical Character Recognition ) 5.4.1
#### Python tkinter 3.12.4
#### 量表 ( Scale ) 數據識別, 使用 Intel OpenCV 和 HP Google Tesseract 和 Python tkinter 製作的, 計算機輔助測量 ( Computer Automated Measurement ) 的桌面工具.
---
<p word-wrap: break-word; word-break: break-all; overflow-x: hidden; overflow-x: hidden;>
使用計算機視覺 ( Optical Character Recognition ) 的方法, 識別量表 ( Scale ) 圖片裏顯示的資訊, 使用計算機輔助測量 ( Computer Automated Measurement ) 的方法, 識別計算量表 ( Scale ) 圖片裏顯示的測量值數據.

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

1. 項目 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 運行需要 Python 環境, 所以運行之前, 需對作業系統 ( Operating System ) 安裝配置 Python 環境成功方可.

   可在 Linux-Ubuntu 系統的控制臺命令列人機交互介面窗口 ( Ubuntu-bash ) 使用如下指令, 安裝配置 Python 環境 :

   root@localhost:~# sudo apt install python3

2. 首先需要下載安裝配置 HP Google Tesseract ( Optical Character Recognition ) 工具包, 或者, 也可以將其配置保存在項目空間 : ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/ 文件夾裏.

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

3. 手動創建配置計算機程式設計語言 Python 解釋器 ( Interpreter ) 項目 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 的隔離環境 :

   root@localhost:~# /usr/bin/python3 -m venv ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/

4. 激活計算機程式設計語言 Python 解釋器 ( Interpreter ) 的隔離環境 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 項目 :

   root@localhost:~# ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Scripts/activate

5. 手動配置計算機程式設計語言 Python 解釋器 ( Interpreter ) 的隔離環境 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 項目需要的第三方擴展包, 依照項目空間裏第三方擴展包的列表文檔 ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/packagelist.txt 安裝 :

   root@localhost:~# ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Scripts/pip.exe install --requirement ./OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/packagelist.txt

6. 以上全部配置完畢, 即可在作業系統 ( Operating System : Linux-Ubuntu , Windows ) 的控制臺命令列人機交互介面窗口 ( Ubuntu-bash , Windows-bat ) 使用如下指令, 啓動運行 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 項目 :

   root@localhost:~# /usr/bin/python3 /home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/main.py configFile=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt is_window=False is_Concurrent=Multi-Threading is_storage_position=Disk is_storage_type=csv input_dir=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/inputTest/ outputTest_path=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/outputTest/test.csv tesseract_cmd=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/tesseract.exe tesseract_tessdata_dir=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tessdata tesseract_user_words=/home/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tesswords input_tabel_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert" input_measuringRuler_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert"

   C:\> C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Scripts/python.exe C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/main.py configFile=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/config.txt is_window=False is_Concurrent=Multi-Threading is_storage_position=Disk is_storage_type=csv input_dir=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/inputTest/ outputTest_path=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/outputTest/test.csv tesseract_cmd=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/tesseract.exe tesseract_tessdata_dir=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tessdata tesseract_user_words=C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Tesseract-OCR/share/tesswords input_tabel_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert" input_measuringRuler_tesseract_config="--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert"

   其中 :

   參數 C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/Scripts/python.exe 表示使用計算機程式設計語言 Python 解釋器 ( Interpreter ) 的隔離環境 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 項目裏的 Python 解釋器 ( Interpreter ) 運行環境.

   參數 C:/OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter/main.py 表示項目 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 啓動入口文檔保存位置的路徑全名.

   參數 configFile 表示項目 OCR-Measuring-Scale-OpenCV-Tesseract-Python-tkinter 啓動時, 讀取啓動參數的配置文檔保存位置的路徑全名.

   參數 is_window 表示是否開啓人機交互介面 ( Graphical User Interface ) 的窗口, 祇能 [ True , False ] 取其一.

   參數 is_Concurrent 表示選擇圖形處理的函數 : Intel-OpenCV ( Open Source Computer Vision Library ) , HP-Google-Tesseract ( Optical Character Recognition ) 是否多綫程並發, 祇能 [ 0 , Multi-Threading ] 取其一.

   參數 is_storage_position 表示選擇識別結果的存儲位置, 祇能 [ Database , Database_and_Disk , Disk ] 取其一.

   參數 is_storage_type 表示選擇識別結果的存儲類型, 祇能 [ json , csv , txt , xlsx ] 取其一.

   參數 input_dir 表示自定義配置用於讀入待識別的量表 ( Scale ) 圖片 ( Image ) 檔的保存位置路徑全名, 多樣本應輸入樣本檔保存所在的文件夾路徑全名.

   參數 inputTest_path 表示自定義配置用於讀入待識別的量表 ( Scale ) 圖片 ( Image ) 檔的保存路徑名稱全名, 單樣本則應直接輸入樣本檔的保存路徑名稱全名.

   參數 outputTest_path 表示自定義配置用於輸出寫入識別結果的文檔保存路徑名稱全名, 可爲 .csv 或 .txt 類型.

   參數 output_dir 表示自定義配置用於輸出寫入識別結果的文檔的保存位置路徑全名, 即保存結果的文檔所在的文件夾路徑全名.

   參數 outputTest_URL 表示自定義配置用於保存識別結果的資料庫服務器地址 ( URL ) 全名, 取值應爲 URL 字符串.

   參數 time_sleep 表示自定義配置用於識別的量表 ( Scale ) 圖片 ( Image ) 檔等待休眠的間隔時長, 單位 ( Unit ) : 毫秒 ( Millisecond ).

   參數 tesseract_cmd 表示指定第三方庫「Tesseract-OCR」的二進位可執行檔「tesseract.exe」的安裝保存的位置路徑名稱全名.

   參數 tesseract_tessdata_dir 表示指定本地訓練完畢的數據集文檔（tessdata）的儲存路徑位置路徑名稱全名.

   參數 tesseract_user_words 表示指定的詞庫（字典）文檔的存儲位置路徑名稱全名, 用戶字典可以包含一些特定的詞匯, 以提高對特定詞匯的識別準確性.

   參數 tesseract_user_patterns 表示指定的特定格式文本的文檔的存儲位置路徑名稱全名, 即每行使用「某種正則表達式」.

   參數 input_tabel_tesseract_config 表示指定 Tesseract 的其他配置選項, 預設值爲 : "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert"

   參數 input_measuringRuler_tesseract_config 表示指定 Tesseract 的其他配置選項, 預設值爲 : "--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert"

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

[圖形處理工具包 Intel OpenCV ( Open Source Computer Vision Library ) 官方網站](https://opencv.org/): 
https://opencv.org/

HP Google Tesseract ( Optical Character Recognition ) - 5.4.1

[圖形識別工具包 HP Google Tesseract ( Optical Character Recognition ) 官方網站](https://code.google.com/p/tesseract-ocr/): 
https://code.google.com/p/tesseract-ocr/

---

解釋器 ( Interpreter ) : Python 和圖形處理工具 : Intel OpenCV ( Open Source Computer Vision Library ) , HP Google Tesseract ( Optical Character Recognition ) 預編譯二進制可執行檔 [百度網盤(pan.baidu.com)](https://pan.baidu.com/s/1IXjbZBRkurrNRs0GoURCaA?pwd=1dm7) 下載頁: 
https://pan.baidu.com/s/1IXjbZBRkurrNRs0GoURCaA?pwd=1dm7

提取碼：1dm7

---

![]()
