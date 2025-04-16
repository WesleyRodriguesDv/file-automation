import os
import shutil
from pathlib import Path

# Caminhos base
pasta_downloads = Path.home() / 'Downloads'
pasta_documentos = Path.home() / 'Documentos'
pasta_imagens = Path.home() / 'Imagens'

# Extensões por categoria
ext_documentos = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.xlsm']
ext_imagens = ['.jpg', '.jpeg', '.png']

# Garante que as pastas existam
pasta_documentos.mkdir(parents=True, exist_ok=True)
pasta_imagens.mkdir(parents=True, exist_ok=True)

# Percorre os arquivos da pasta Downloads
for arquivo in pasta_downloads.iterdir():
    if arquivo.is_file():
        ext = arquivo.suffix.lower()

        # Mover para Documentos
        if ext in ext_documentos:
            destino = pasta_documentos / arquivo.name
        # Mover para Imagens
        elif ext in ext_imagens:
            destino = pasta_imagens / arquivo.name
        else:
            continue  # ignora arquivos que não se encaixam nas categorias

        try:
            shutil.move(str(arquivo), str(destino))
            print(f'Movido: {arquivo.name} → {destino.parent.name}')
        except Exception as e:
            print(f'Erro ao mover {arquivo.name}: {e}')
