import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

to_dir = "C:/Users/tamir/Downloads"
from_dir = "C:/Users/tamir/OneDrive/Área de Trabalho/Vitor/Byju's Codigos/Python/imagens_baixadas/Arquivos_Imagem"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.pdf, .txt, .doc, .docx']:

        path1 = from_dir + '/' + file_name                              
        path2 = to_dir + '/' + "Arquivos_Imagem"                      
        path3 = to_dir + '/' + "Arquivos_Imagem" + '/' + file_name 

        if os.path.exists(path2):
          print("Movendo " + file_name + ".....")

          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
