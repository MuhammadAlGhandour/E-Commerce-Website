@echo off

echo creating the virtual environment
python -m venv venv

echo activating the virtual environment
call venv\Scripts\activate.bat

echo downloading the requirements
pip install -r requirements.txt