# 📁 Organizador de Downloads

Script em Python para organizar automaticamente os arquivos da pasta **Downloads** em categorias como Documentos, Imagens, Vídeos, Músicas e Instalações, com base na extensão do arquivo e no tipo MIME.

## ✅ Funcionalidades

- Move documentos para a pasta **Documentos**
- Move imagens para a pasta **Imagens**
- Move vídeos para a pasta **Vídeos**
- Move áudios para a pasta **Músicas**
- Move arquivos diversos para a subpasta **Instalações** dentro de Downloads
- Cria as pastas automaticamente caso não existam

## 🧠 Lógica de Classificação

- **Documentos**: `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.xlsm`
- **Imagens**: `.jpg`, `.jpeg`, `.png`, `.webp`
- **Vídeos**: arquivos com MIME `video/*`
- **Músicas**: arquivos com MIME `audio/*`
- **Instalações**: todos os outros arquivos

## 🛠️ Como usar

1. Instale o Python (versão 3.6+ recomendada)
2. Salve o script como `organizador_downloads.py`
3. Execute no terminal:

```bash
python organizador_downloads.py
