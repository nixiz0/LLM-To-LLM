@echo off
IF NOT EXIST .env (
    python -m venv .env
    cd .env\Scripts
    call activate.bat
    cd ../..
    pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
    pip install -r requirements.txt
) ELSE (
    cd .env\Scripts
    call activate.bat
    cd ../..
)

FOR /F "tokens=*" %%A IN ('powershell -Command "Get-Command ollama"') DO SET OLLAMA_COMMAND=%%A
IF "%OLLAMA_COMMAND%"=="" (
    echo Ollama is not installed on your system.
    echo Please download it from https://ollama.com/download/windows
    pause
    exit
) ELSE (
    start cmd /k ollama serve
)

python main.py