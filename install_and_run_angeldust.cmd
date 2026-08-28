@echo off
setlocal
title ANGELDUST Multi-Tool Installer

echo ==========================================
echo      ANGELDUST MULTI-TOOL INSTALLER
echo ==========================================
echo.

where py >nul 2>&1
if %errorlevel%==0 (
    set "PY=py"
) else (
    where python >nul 2>&1
    if %errorlevel%==0 (
        set "PY=python"
    ) else (
        echo [ERROR] Python is not installed or not in PATH.
        echo Install Python 3 from https://www.python.org/downloads/
        echo Make sure "Add Python to PATH" is enabled.
        pause
        exit /b 1
    )
)

echo [1/3] Checking pip...
%PY% -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not available.
    pause
    exit /b 1
)

echo [2/3] Installing required Python packages...
%PY% -m pip install --upgrade requests psutil pystyle rich
if errorlevel 1 (
    echo.
    echo [ERROR] Package installation failed.
    pause
    exit /b 1
)

echo.
echo [3/3] Starting ANGELDUST...
echo.
%PY% "%~dp0angeldust.py"

echo.
echo ==========================================
echo ANGELDUST has exited.
echo ==========================================
pause
