@echo off
rem 命令列窗口，從本橫向列（row）開始，關閉回顯;
chcp 65001
rem 將命令列窗口顯示的字符編碼，改爲：UFT-8
cls

rem Title: Scale Computer Automated Measurement using Intel-OpenCV ( Open Source Computer Vision Library ) and HP-Google-Tesseract ( Optical Character Recognition )
rem Author: 弘毅
rem E-mail: 283640621@qq.com
rem Telephont number: +86 18604537694
rem Date: 歲在丙申
rem Operating system: Windows10 x86_64 Inter(R)-Core(TM)-m3-6Y30

rem 使用説明：在 Windows 系統的 cmd 控制臺命令列，使用如下指令，啓動執行;
rem C:\Scale_OCR> C:/Scale_OCR/startServer.bat C:/Scale_OCR/config.txt


set NoteVersion_1="Scale Computer Automated Measurement using Intel-OpenCV ( Open Source Computer Vision Library ) and HP-Google-Tesseract ( Optical Character Recognition )"
set NoteVersion_2="Windows10 x86_64 Inter(R)-Core(TM)-m3-6Y30"
set NoteVersion_3="283640621@qq.com"
set NoteVersion_4="+8618604537694"
set NoteVersion_5="弘毅"
set NoteVersion_6="歲在丙申"

set NoteHelp_1="--help -h --version -v"
set NoteHelp_2="configFile=C:/Scale_OCR/config.txt"
set NoteHelp_3="executableFile=C:/Scale_OCR/Scripts/python.exe"
set NoteHelp_4="executableFile=C:/Python/Python311/python.exe"
set NoteHelp_5="scriptFile=C:/Scale_OCR/src/main.py"
set NoteHelp_6="configInstructions=configFile=C:/Scale_OCR/src/config.txt,is_window=True,is_Concurrent=Multi-Threading,is_storage_position=Disk,is_storage_type=csv,tesseract_cmd=C:/Scale_OCR/Tesseract-OCR/tesseract,tesseract_tessdata_dir=C:/Scale_OCR/Tesseract-OCR/tessdata/chi_tra.traineddata,tesseract_user_words=C:/Scale_OCR/Tesseract-OCR/tesswords/,tesseract_user_patterns=,input_dir=C:/Scale_OCR/inputTest/,inputTest_path=C:/Scale_OCR/inputTest/,output_dir=C:/Scale_OCR/outputTest/,outputTest_path=C:/Scale_OCR/outputTest/test.csv,outputTest_URL=,time_sleep=0.01,input_tabel_tesseract_config=--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert,input_measuringRuler_tesseract_config=--psm 3 --oem 3 -l lang=chi_tra+chi_tra_vert+eng+chi_sim+chi_sim_vert"

rem 使用：enabledelayedexpansion 方法，來允許在：for 循環内部使用動態變量，即在循環過程中可以改變的變量;
setlocal enabledelayedexpansion

set configFileName=config.txt
set configFile=
rem set "configFile=C:/Scale_OCR/config.txt"

set CalculationTool=Python

rem 設置將傳入參數中的逗號字符(,)替換爲空格字符( );
set "search_string=,"
set "replace_string= "

set executableFileName=Scripts\python.exe
set executableFile=
rem set executableFile="C:/Scale_OCR/Scripts/python.exe"

set interpreterFileName=/
set interpreterFile=
rem set interpreterFile="--project=C:/Scale_OCR/"

set scriptFileName=src\main.py
set scriptFile=
rem set scriptFile="C:/Scale_OCR/src/main.py"

set configInstructions=
rem set configInstructions="configFile=C:/Scale_OCR/src/config.txt,is_window=True,is_Concurrent=Multi-Threading,is_storage_position=Disk,is_storage_type=csv,tesseract_cmd=C:/Scale_OCR/Tesseract-OCR/tesseract,tesseract_tessdata_dir=C:/Scale_OCR/Tesseract-OCR/tessdata/chi_tra.traineddata,tesseract_user_words=C:/Scale_OCR/Tesseract-OCR/tesswords/,tesseract_user_patterns=,input_dir=C:/Scale_OCR/inputTest/,inputTest_path=C:/Scale_OCR/inputTest/,output_dir=C:/Scale_OCR/outputTest/,outputTest_path=C:/Scale_OCR/outputTest/test.csv,outputTest_URL=,time_sleep=0.01"

set shellCodeScript=
rem set shellCodeScript="C:/Scale_OCR/Scripts/python.exe C:/Scale_OCR/src/main.py configFile=C:/Scale_OCR/src/config.txt is_window=True is_Concurrent=Multi-Threading is_storage_position=Disk is_storage_type=csv tesseract_cmd=C:/Scale_OCR/Tesseract-OCR/tesseract tesseract_tessdata_dir=C:/Scale_OCR/Tesseract-OCR/tessdata/chi_tra.traineddata tesseract_user_words=C:/Scale_OCR/Tesseract-OCR/tesswords/ tesseract_user_patterns= input_dir=C:/Scale_OCR/inputTest/ inputTest_path=C:/Scale_OCR/inputTest/ output_dir=C:/Scale_OCR/outputTest/ outputTest_path=C:/Scale_OCR/outputTest/test.csv outputTest_URL= time_sleep=0.01"

rem 獲取當前工作空間;
set "work_directory=%cd%"
rem echo Worker directory = %work_directory%
set "bat_file=%~f0"
rem echo File(.bat) = %bat_file%
set "bat_directory=%~dp0"
rem echo Directory(.bat) = %bat_directory%

rem 變量賦預設值;
set configFile=%bat_directory%%configFileName%
rem echo configFile = %configFile%

rem set executableFile=%bat_directory%%executableFileName%
rem rem echo executableFile = %executableFile%

rem set scriptFile=%bat_directory%%scriptFileName%
rem rem echo scriptFile = %scriptFile%

rem set interpreterFile=--project=%bat_directory%%interpreterFileName%
rem rem echo interpreterFile = %interpreterFile%

rem 讀取控制臺命令列傳入的參數;
rem echo %*
rem set "Argument=%*"
rem echo %Argument%

set /a index=0
for %%i in (%*) do (
    set /a index+=1
    rem echo !index!: %%i
    if not "%%i"=="" (
        if "%%i" equ "--version" (
            echo %NoteVersion_1%
            echo %NoteVersion_2%
            echo %NoteVersion_3%
            echo %NoteVersion_4%
            echo %NoteVersion_5%
            echo %NoteVersion_6%
            exit /b 0
        ) else if "%%i" equ "-v" (
            echo %NoteVersion_1%
            echo %NoteVersion_2%
            echo %NoteVersion_3%
            echo %NoteVersion_4%
            echo %NoteVersion_5%
            echo %NoteVersion_6%
            exit /b 0
        ) else if "%%i" equ "--help" (
            echo %NoteVersion_1%
            echo %NoteVersion_2%
            echo %NoteVersion_3%
            echo %NoteVersion_4%
            echo %NoteVersion_5%
            echo %NoteVersion_6%
            echo.
            echo %NoteHelp_1%
            echo %NoteHelp_2%
            echo %NoteHelp_3%
            echo %NoteHelp_4%
            echo %NoteHelp_5%
            echo %NoteHelp_6%
            exit /b 0
        ) else if "%%i" equ "-h" (
            echo %NoteVersion_1%
            echo %NoteVersion_2%
            echo %NoteVersion_3%
            echo %NoteVersion_4%
            echo %NoteVersion_5%
            echo %NoteVersion_6%
            echo.
            echo %NoteHelp_1%
            echo %NoteHelp_2%
            echo %NoteHelp_3%
            echo %NoteHelp_4%
            echo %NoteHelp_5%
            echo %NoteHelp_6%
            exit /b 0
        ) else if "%%i" equ "isJulia" (
            set CalculationTool=Julia
            rem echo CalculationTool = %CalculationTool%
        ) else if "%%i" equ "isPython" (
            set CalculationTool=Python
            rem echo CalculationTool = %CalculationTool%
        ) else (
            set "configFile=%%i"
            rem echo configFile = %configFile%
        )
    )
)
set /a index=0

rem 讀取控制文檔（config.txt）傳入的參數;
rem echo configFile = %configFile%
if "%configFile%"=="" (
    echo "Error ( configFile = "" )"
) else if not exist "%configFile%" (
    echo "Config file ( %configFile% ) unrecognized."
) else (
    echo configFile = %configFile%
    set /a index=0
    for /f "delims=" %%j in (%configFile%) do (
        set /a index+=1
        rem echo !index!: %%j
        if not "%%j"=="" (
            echo %%j|findstr "=" >nul
            if %errorlevel% equ 0 (
                rem set /a k=0
                for /f "tokens=1* delims==" %%a in ("%%j") do (
                    rem set /a k+=1
                    rem echo !k!: %%a
                    rem set "char[!k!]=%%a"
                    rem echo !k!: char[!k!]

                    set "char[1]=%%a"
                    rem echo char[1]: !char[1]!
                    set "char[2]=%%b"
                    rem echo char[2]: !char[2]!

                    rem set Argument_Key=%%a
                    rem rem echo Argument_Key = !Argument_Key!
                    rem if "%%b"=="" (
                    rem     set Argument_Value=
                    rem ) else (
                    rem     set Argument_Value=%%b
                    rem )
                    rem rem echo Argument_Value = !Argument_Value!
                )

                set Argument_Key=
                if "!char[1]!"=="" (
                    set Argument_Key=
                ) else (
                    set Argument_Key=!char[1]!
                )
                rem echo Argument_Key = !Argument_Key!

                rem 遍歷數組;
                set Argument_Value=
                for /l %%k in (2,1,2) do (
                    rem echo !char[%%k]!
                    if "!char[%%k]!"=="" (
                        rem set Argument_Value=!Argument_Value!
                    ) else (
                        set Argument_Value=!Argument_Value!!char[%%k]!
                    )
                )
                rem echo Argument_Value = !Argument_Value!

                if not "!Argument_Key!"=="" (

                    if "!Argument_Value!"=="" (

                        if "!Argument_Key!" equ "executableFile" (
                            set executableFile=
                            rem echo !Argument_Key! = !executableFile!
                        )
                        if "!Argument_Key!" equ "interpreterFile" (
                            set interpreterFile=
                            rem echo !Argument_Key! = !interpreterFile!
                        )
                        if "!Argument_Key!" equ "scriptFile" (
                            set scriptFile=
                            rem echo !Argument_Key! = !scriptFile!
                        )
                        if "!Argument_Key!" equ "configInstructions" (
                            set configInstructions=
                            rem echo !Argument_Key! = !configInstructions!
                        )

                    ) else (

                        set Argument_Value=!Argument_Value:%search_string%=%replace_string%!

                        if "!Argument_Key!" equ "executableFile" (
                            set executableFile=!Argument_Value!
                            rem echo !Argument_Key! = !executableFile!
                        )
                        if "!Argument_Key!" equ "interpreterFile" (
                            set interpreterFile=!Argument_Value!
                            rem echo !Argument_Key! = !interpreterFile!
                        )
                        if "!Argument_Key!" equ "scriptFile" (
                            set scriptFile=!Argument_Value!
                            rem echo !Argument_Key! = !scriptFile!
                        )
                        if "!Argument_Key!" equ "configInstructions" (
                            set configInstructions=!Argument_Value!
                            rem echo !Argument_Key! = !configInstructions!
                        )
                    )
                )

            ) else (

                echo "Unable to find equal sign(=) separator in the !index!: %%j"
            )
        )
    )
    set /a index=0
    rem echo executableFile = %executableFile%
    rem echo interpreterFile = %interpreterFile%
    rem echo scriptFile = %scriptFile%
    rem echo configInstructions = %configInstructions%
)

rem 拼接參數獲取 shell 啓動脚本;
if "%executableFile%"=="" (
    echo "Error, startup executable file path is empty ( executableFile = )."
    rem echo "Config file ( %configFile% ) import argument: [ executableFile ] is empty."
    exit /b 1
) else (
    if "%scriptFile%"=="" (
        if "%interpreterFile%"=="" (
            set shellCodeScript=%executableFile%
        ) else (
            set "shellCodeScript=%executableFile% %interpreterFile%"
        )
    ) else (
        if "%interpreterFile%"=="" (
            if "%configInstructions%"=="" (
                set "shellCodeScript=%executableFile% %scriptFile%"
            ) else (
                set "shellCodeScript=%executableFile% %scriptFile% %configInstructions%"
            )
        ) else (
            if "%configInstructions%"=="" (
                set "shellCodeScript=%executableFile% %interpreterFile% %scriptFile%"
            ) else (
                set "shellCodeScript=%executableFile% %interpreterFile% %scriptFile% %configInstructions%"
            )
        )
    )
    rem echo shellCodeScript = %shellCodeScript%
)

rem 啓動服務器二進制可執行檔（.exe）;
rem echo shellCodeScript = %shellCodeScript%
if "%shellCodeScript%"=="" (
    echo "Error, startup shell scrip is emptyt ( shellCodeScript = %shellCodeScript% )."
    exit /b 1
) else (

    C:\Windows\System32\cmd.exe /min /c "%shellCodeScript%"
    rem C:\Windows\System32\cmd.exe /b /min /c "%shellCodeScript%"
    rem C:\Windows\System32\cmd.exe /c "%shellCodeScript%"
    rem C:\Windows\System32\cmd.exe /c "cd /d %work_directory%&chcp 65001&cls&%shellCodeScript%"
    rem C:\Windows\System32\cmd.exe /c "cd /d %bat_directory%&chcp 65001&cls&%shellCodeScript%"

    rem 控制臺命令列窗口運行完畢，會自動關閉;
    rem start C:/Windows/System32/cmd.exe /c "cd /d %work_directory%&chcp 65001&cls&%shellCodeScript%"
    rem start C:/Windows/System32/cmd.exe /c "cd /d %bat_directory%&chcp 65001&cls&%shellCodeScript%"
    rem 控制臺命令列窗口運行完畢，不會自動關閉;
    rem start C:/Windows/System32/cmd.exe /k "cd /d %work_directory%&chcp 65001&cls&%shellCodeScript%"
    rem start C:/Windows/System32/cmd.exe /k "cd /d %bat_directory%&chcp 65001&cls&%shellCodeScript%"
    rem 最小化控制臺命令列窗口，運行完畢會自動關閉;
    rem start /min C:/Windows/System32/cmd.exe /c "cd /d %work_directory%&chcp 65001&cls&%shellCodeScript%"
    rem start /min C:/Windows/System32/cmd.exe /c "cd /d %bat_directory%&chcp 65001&cls&%shellCodeScript%"
    rem 在操作系統後臺隱藏啓動，控制臺命令列窗口運行完畢，會自動關閉;
    rem start /b C:/Windows/System32/cmd.exe /c "cd /d %work_directory%&chcp 65001&cls&%shellCodeScript%"
    rem start /b C:/Windows/System32/cmd.exe /c "cd /d %bat_directory%&chcp 65001&cls&%shellCodeScript%"
)

endlocal

rem 設定運行完畢窗口不要自動關閉;
rem pause

exit /b 0