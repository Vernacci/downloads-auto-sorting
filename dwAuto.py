import os, shutil

EXT_AUDIO = [".wav", ".ogg", ".mp3", ".raw"]
EXT_IMAGES = [".jpg", ".jpeg", ".png", ".svg", ".gif"]
EXT_VIDEO = [".mp4", ".mov", ".wmv"]
EXT_DOCUMENTS = [".txt", ".pdf", ".docx", ".doc", ".pptx"]



print('ORGANIZANDO PASTA DE DOWNLOADS')


arquivos = os.listdir()

# cria os diretórios caso eles não existam
DIRS = ['Audio', 'Images', 'Video', 'Documents', 'Folders', 'Others']
if not os.path.isdir('./Audio'):
    for d in DIRS:
        os.mkdir('./{}'.format(d))
        print('diretórios criados com sucesso')


#programa principal 
for a in arquivos:
    name,extension = os.path.splitext(a)

    if extension in EXT_IMAGES:
        shutil.move(a, './Images/{}'.format(a))
    elif extension in EXT_AUDIO :
        shutil.move(a, './Audio/{}'.format(a))
    elif extension in EXT_VIDEO :
        shutil.move(a, './Video/{}'.format(a))
    elif extension in EXT_DOCUMENTS :
        shutil.move(a, './Documents/{}'.format(a))
    else:
        if os.path.isdir(name):
            if name not in DIRS:
                shutil.move(a, './folders/{}'.format(a))
        else:
            if a != 'dwAuto.py':
                shutil.move(a, './Others/{}'.format(a))
                
            
