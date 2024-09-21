# Organizador_Downloads
Um projeto que contem um script e um executável feito em Python para organizar arquivos da pasta downloads para suas pastas correta, apenas foi testado no windows, mas em teoria deveria funcionar corretamente em Linux e Mac por causa das biblioteca pathlib que procuraria se o caminho a partir da sua pasta home existiria e se não existe ele criaria a pasta e então após isso moveria os arquivos com o com o shutil.

Para esse script e executavel funcionarem é necessario que o Python esteja instalado:
https://www.python.org/downloads/

Para usar ele temos duas opções a primeira sendo usar o executavel que fica na pasta dist e a segunda roda o script no CMD, para usar a segunda opção é preciso usar o comando **cd** para a pasta onde esta o script e usar esse comando em seguida:

```
python organizador_downloads.py
```

Caminhos que o programa vai realizar

```
C:\Users\usario\Downloads --> C:\Users\usario\Pictures

C:\Users\usario\Downloads --> C:\Users\usario\Music

C:\Users\usario\Downloads --> C:\Users\usario\Videos

C:\Users\usario\Downloads --> C:\Users\usario\Documents\Docs organizer\Texts

C:\Users\usario\Downloads --> C:\Users\usario\Documents\Docs organizer\Sheets

C:\Users\usario\Downloads --> C:\Users\usario\Documents\Docs organizer\Powerpoints
```

Os tipo de arquivos o que ele lida

```
Imagens: {'.jpg','.jpeg','.png','gif','.bmp','.svg','.tiff','.tif'}

Musica: {'.mp3','.wav','.aac','.flac'}

Videos: {'.mp4','.mkv','.mov','.wmv','.avi','.srt'}

Documentos de Texto: {'.doc','.docx','.pdf','.rtf','.odt','.txt'}

Planilhas: {'.xls','.csv','.ods'}

Powerpoints: {'.ppt','.pptx','.odp'}
```

Link das bibliotecas usadas:

[shutil](https://docs.python.org/pt-br/3/library/shutil.html)

[pathlib](https://docs.python.org/pt-br/3.12/library/pathlib.html)

Usado para construir o executavel

[pyinstaller](https://pyinstaller.org/en/stable/)
