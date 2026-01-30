# start_project.ps1
# Instala dependencias (si faltan) y levanta el servidor Uvicorn para la app FastAPI.
# Uso: Ejecutar en PowerShell desde la carpeta del proyecto:
#   .\start_project.ps1

Set-StrictMode -Version Latest
$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Buscar Python en venv local 'project' si existe, si no usar el Python del sistema
$venvPython = Join-Path $projectRoot 'project\Scripts\python.exe'
if (Test-Path $venvPython) {
    $python = $venvPython
    Write-Host "Usando Python del entorno virtual: $python"
} else {
    $python = 'python'
    Write-Host "No se encontró 'project' venv. Usando 'python' del sistema." 
}

# Crear requirements.txt si no existe (con las dependencias necesarias)
$reqFile = Join-Path $projectRoot 'requirements.txt'
if (!(Test-Path $reqFile)) {
    @"
fastapi
uvicorn[standard]
"@ | Out-File -FilePath $reqFile -Encoding UTF8
    Write-Host "Se creó 'requirements.txt' con dependencias básicas."
} else {
    Write-Host "Se usará el archivo existente: $reqFile"
}

# Instalar dependencias
Write-Host "Instalando dependencias desde $reqFile..."
& $python -m pip install --upgrade pip
& $python -m pip install -r $reqFile

# Levantar el servidor
Write-Host "Iniciando servidor Uvicorn en http://127.0.0.1:8000 (CTRL+C para detener)"
& $python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
