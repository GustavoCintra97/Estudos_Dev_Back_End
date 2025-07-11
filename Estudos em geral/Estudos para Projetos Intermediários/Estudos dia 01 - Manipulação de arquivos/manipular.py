import os
import shutil

caminhoOriginal = r'C:\Users\gusta\OneDrive\Documentos\Treino Jhow'
caminhoNovo = r'C:\Users\gusta\OneDrive\Documentos\Treino Jhow TESTE'

try:
    os.mkdir(caminhoNovo)
except FileExistsError as e:
    print(f'A pasta {caminhoNovo} já existe.')

for root, dirs, files in os.walk(caminhoNovo):
    for file in files:
        oldFilePath = os.path.join(root, file)
        newFilePath = os.path.join(caminhoNovo, file)
        
        if '.docx' in file:
            os.remove(newFilePath)