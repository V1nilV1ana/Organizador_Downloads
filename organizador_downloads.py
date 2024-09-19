#Encontra o caminho de download
#Ler o tipo do arquivo como mp3, pdf, mkv, zip...
#Ir para o caminho correto
#Verificar se a pasta existe e se não existe criar ela
#Mover os arquivo

from pathlib import Path # usar caminhos 
import shutil # mover arquivos

# Caminho para a pasta downloads, o Path.home() puxa o caminho e nome do usuario atual e o / 'downloads' faz uma ligação para trazer o caminho para pasta downloads
downloads = Path.home() / 'Downloads'

# Dicionario dos caminhos
destinations = {
    'images': Path.home() / 'Pictures',
    'music': Path.home() / 'Music',
    'videos': Path.home() / 'Videos',
    'docsT': Path.home() / 'Documents' / 'Docs organizer' / 'Texts',
    'docsS': Path.home() / 'Documents' / 'Docs organizer' / 'Sheets',
    'docsP': Path.home() / 'Documents' / 'Docs organizer' / 'Powerpoints',
}

# Dicionario para a leitura das extensões 
extensions ={
    'images':{'.jpg','.jpeg','.png','gif','.bmp','.svg','.tiff','.tif'},
    'music':{'.mp3','.wav','.aac','.flac'},
    'videos':{'.mp4','.mkv','.mov','.wmv','.avi','.srt'},
    'docsT':{'.doc','.docx','.pdf','.rtf','.odt','.txt'},
    'docsS':{'.xls','.csv','.ods'},
    'docsP':{'.ppt','.pptx','.odp'},
}

def organize_files():
    for file in downloads.iterdir(): # traz uma lista com o caminho e o nome dos arquivos suas extensões
        if file.is_file(): # verificar se o file é realmente um arquivo
            for category, exts in extensions.items(): # vai puxar todos os itens de extensions e vai separar eles como em category = images e vai ser igual a ext = {'.jpg','.jpeg','.png','gif','.bmp','.svg','.tiff','.tif'}... 
                if file.suffix.lower() in exts: # le o nome das extensões em caixa baixa
                    destination = destinations[category] # da caminho para guarda os itens usando o que esta no dicionario de extensions
                    destination.mkdir(parents=True, exist_ok=True) #verifica se a pasta existe e se não exister ele cria ela
                    shutil.move(str(file), destination / file.name) # move o arquivo para o seu novo destino usando o shutil
                    print(f'{file} --> {destination}')
                    
                    break


organize_files()
input('Processo terminado, aperte uma tecla para fechar')