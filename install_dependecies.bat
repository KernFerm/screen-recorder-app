@echo off
echo Installing dependencies...

:: Ensure pip is available and valid
pip --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Pip is not installed or not available in PATH. Please install pip first.
    pause
    exit /b
)

:: Install the dependencies from requirements.txt
pip install -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo Failed to install some dependencies. Please check for errors.
    pause
    exit /b
)

echo Dependencies installed successfully.
pause
