import os
import shutil
from pathlib import Path
import mimetypes

# Caminhos base
pasta_downloads = Path.home() / 'Downloads'
pasta_documentos = Path.home() / 'Documentos'
pasta_imagens = Path.home() / 'Imagens'
pasta_videos = Path.home() / 'Vídeos'
pasta_musicas = Path.home() / 'Músicas'
pasta_instalacoes = pasta_downloads / 'Instalações'

# Extensões conhecidas
ext_documentos = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.xlsm']
ext_imagens = ['.jpg', '.jpeg', '.png', '.webp']

# Cria todas as pastas se não existirem
for pasta in [pasta_documentos, pasta_imagens, pasta_videos, pasta_musicas, pasta_instalacoes]:
    pasta.mkdir(parents=True, exist_ok=True)

# Função para identificar tipo MIME
def tipo_arquivo(caminho: Path):
    tipo, _ = mimetypes.guess_type(caminho)
    return tipo or ''

# Percorre os arquivos da pasta Downloads
for arquivo in pasta_downloads.iterdir():
    if arquivo.is_file():
        ext = arquivo.suffix.lower()
        tipo = tipo_arquivo(arquivo)

        # Verifica categorias
        if ext in ext_documentos:
            destino = pasta_documentos / arquivo.name
        elif ext in ext_imagens:
            destino = pasta_imagens / arquivo.name
        elif tipo.startswith('video'):
            destino = pasta_videos / arquivo.name
        elif tipo.startswith('audio'):
            destino = pasta_musicas / arquivo.name
        else:
            destino = pasta_instalacoes / arquivo.name

        # Move o arquivo
        try:
            shutil.move(str(arquivo), str(destino))
            print(f'Movido: {arquivo.name} → {destino.parent.name}')
        except Exception as e:
            print(f'Erro ao mover {arquivo.name}: {e}')
