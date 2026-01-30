@echo off
REM start_project.bat - Instala dependencias y levanta el servidor (CMD)
SETLOCAL
SET "ROOT=%~dp0"

IF EXIST "%ROOT%project\Scripts\python.exe" (
  SET "PY=%ROOT%project\Scripts\python.exe"
) ELSE (
  WHERE python >nul 2>&1 && SET "PY=python" || (ECHO Python no encontrado & EXIT /B 1)
)

IF NOT EXIST "%ROOT%requirements.txt" (
  ECHO fastapi> "%ROOT%requirements.txt"
  ECHO uvicorn[standard]>> "%ROOT%requirements.txt"
  ECHO Se creo requirements.txt con dependencias basicas.
) ELSE (
  ECHO Usando requirements.txt existente.
)

"%PY%" -m pip install --upgrade pip
"%PY%" -m pip install -r "%ROOT%requirements.txt"

ECHO Iniciando Uvicorn en http://127.0.0.1:8000
"%PY%" -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
ENDLOCAL