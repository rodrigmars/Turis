@echo off

START /high /wait cmd /c "py F:\Laboratorio\Turis\vars.py"

if %ERRORLEVEL% EQU 0 (
   echo Success ERRORLEVEL: %ERRORLEVEL%
) else (
   echo Failure Reason Given is %ERRORLEVEL%
   exit /b %ERRORLEVEL%
)
::EXIT