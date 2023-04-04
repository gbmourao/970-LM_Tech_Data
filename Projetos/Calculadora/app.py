import sys
from pathlib import Path

# Importanto a função do arquivo calculadora/__init__.py
projeto_970_dir = str(Path(__file__).resolve().parent.parent.parent)
if projeto_970_dir not in sys.path:
    sys.path.append(projeto_970_dir)

from Projetos.Calculadora import calcule

# Executando a aplicação
print(calcule())