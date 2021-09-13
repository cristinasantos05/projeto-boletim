# inicialization
python -m pip install --upgrade pip
python -m venv .venv

##### ativar ambiente venv
.venv\Scripts\Activate.ps1

# formas de inicializar o ambiente venv
POSIX
    bash/zsh
        $ source <venv>/bin/activate
    fish
        $ source <venv>/bin/activate.fish
    csh/tcsh
        $ source <venv>/bin/activate.csh
    PowerShell Core
        $ <venv>/bin/Activate.ps1
Windows
    cmd.exe
        C:\> <venv>\Scripts\activate.bat
    PowerShell
        PS C:\> <venv>\Scripts\Activate.ps1

# dentro do ambiente
python -m pip install --upgrade pip
pip install flask

PowerShell
    $env:FLASK_ENV = "development"
    $env:FLASK_APP = "app"

# rodar o Flask
Flask run
