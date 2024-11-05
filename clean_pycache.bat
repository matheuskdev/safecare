@echo off
echo Deleting all __pycache__ directories, excluding 'venv'...

REM Procura por todas as pastas __pycache__ e as remove, exceto dentro de 'venv'
for /d /r %%i in (__pycache__) do (
    echo %%i | findstr /i "\\venv\\" >nul
    if errorlevel 1 (
        echo Deleting %%i
        rmdir /s /q "%%i"
    ) else (
        echo Skipping %%i (inside venv)
    )
)

echo Done!
pause
