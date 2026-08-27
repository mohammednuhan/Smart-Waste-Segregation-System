@echo off
echo ====================================
echo Smart Waste Segregation System
echo Conservation of Natural Resources
echo ====================================
echo.

echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo.
echo Installing required packages...
pip install -r requirements.txt

echo.
echo Starting the application...
echo Please open your browser and go to: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py
