@ECHO OFF
TITLE �����

:PRESET
SET fname=%~n1
IF "%fname%" == "" GOTO :CHECK_ERROR_01
SET fpath=%~dp1
IF /i "%fname:~0,1%" NEQ "_" ( SET fname2=_%fname%) ELSE (
SET fname2=%fname%)
SET pyFile=%fname%.py
FOR /f "eol=[ tokens=1-2 delims==" %%i in (%pyFile%) do (if /i "%%i"=="VERSION " set ver=%%j)
SET ver=%ver: =%
SET ver=%ver:"=%
IF /i "%ver%" EQU " =" SET ver=v
ECHO %fname%.py  �汾��:%ver%
GOTO :DOIT

:DOIT
SET icon=%fpath%rc\%fname%.ico
IF EXIST %icon% ( GOTO :Case_12 ) ELSE ( GOTO :Case_22 )
GOTO :ENDCHECK

:CASE_11
::�նˣ���ͼ��
CALL pyinstaller -F %fname%.py -i %icon%
GOTO :CACHEDEL

:CASE_12
::GUI����ͼ��
CALL pyinstaller -F -w %fname%.py -i %icon%
GOTO :CACHEDEL

:CASE_21
::�նˣ���ͼ��
CALL pyinstaller -F %fname%.py
GOTO :CACHEDEL

:CASE_22
::GUI����ͼ��
CALL pyinstaller -F -w %fname%.py
GOTO :CACHEDEL

:CACHEDEL
IF EXIST .\%fname2%_%ver%.exe DEL /Q .\%fname2%_%ver%.exe
IF EXIST .\__pycache__ rd /s /q .\__pycache__
IF EXIST .\build RD /S /Q .\build
COPY .\dist\%fname%.exe .\%fname2%_%ver%.exe
IF EXIST .\dist RD /S /Q .\dist
IF EXIST %fname%.spec DEL /Q %fname%.spec
GOTO :ENDCHECK

:CHECK_ERROR_01
CLS
ECHO.
ECHO �������ܡ�
ECHO       �� *.py Դ������Ϊ *.exe
ECHO.
ECHO �������÷���
ECHO       ֱ���Ϸ� *.py Դ�ļ����������ϼ��ɣ�
ECHO.
ECHO ���������л�����
ECHO       1��������װ��python 3.6.5+��
ECHO       2��������װ��pyinstaller��
ECHO.
ECHO ��������������˳�������
PAUSE>NUL
GOTO :ENDCHECK

:ENDCHECK
EXIT
