@echo off
setlocal

:: === Configuración ===
set "VENV_DIR=.env"
set "APP_FILE=main.py"
set "LOCAL_PYTHON=Python\python-3.11.9-amd64.exe"

:: === Detectar Python global ===
where python >nul 2>&1
if %errorlevel%==0 (
    set "PYTHON_CMD=python"
    echo [INFO] Usando Python del sistema...
) else (
    if exist "%LOCAL_PYTHON%" (
        set "PYTHON_CMD=%LOCAL_PYTHON%"
        echo [INFO] Usando Python embebido en el proyecto: %LOCAL_PYTHON%
    ) else (
        echo [ERROR] No se encontró Python en el sistema ni en "%LOCAL_PYTHON%".
        echo Descarga Python desde https://www.python.org/downloads/ o incluye Python embebido en la carpeta "python".
        pause
        exit /b 1
    )
)

:: === Verificar entorno virtual ===
if not exist %VENV_DIR%\Scripts\activate (
    echo [INFO] No se encontró el entorno virtual, creando en "%VENV_DIR%"...
    "%PYTHON_CMD%" -m venv %VENV_DIR%
    if errorlevel 1 (
        echo [ERROR] No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
)

:: === Activar entorno virtual ===
call %VENV_DIR%\Scripts\activate
if errorlevel 1 (
    echo [ERROR] No se pudo activar el entorno virtual.
    pause
    exit /b 1
)

:: === Instalar dependencias ===
if exist requirements.txt (
    echo [INFO] Instalando dependencias desde requirements.txt...
    pip install -r requirements.txt
)

:: === Verificar archivo principal ===
if not exist %APP_FILE% (
    echo [ERROR] No se encontró el archivo %APP_FILE%.
    pause
    exit /b 1
)

:: === Ejecutar Streamlit ===
echo [INFO] Ejecutando Streamlit con %APP_FILE%...
streamlit run %APP_FILE%

endlocal
pause
