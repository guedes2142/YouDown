

<img src="https://raw.githubusercontent.com/guedes2142/YouDown/main/Screenshot%20from%202023-05-17%2001-11-02.png" alt="">

# YouTube Video Downloader

Este script permite baixar vídeos do YouTube usando a biblioteca pytube. Ele fornece uma interface de linha de comando para selecionar a resolução do vídeo e fazer o download do mesmo.

## Requisitos

- Biblioteca pytube (instale usando o comando pip: `pip install pytube`)
- Biblioteca colorama (instale usando o comando pip: `pip install colorama`)

## Como usar

1. Execute o script.
2. Escolha uma opção:
    - 1: Baixar um vídeo do YouTube.
    - 2: Sair do programa.
3. Se a opção 1 for escolhida:
    - Insira um link válido de um vídeo do YouTube.
    - Escolha uma resolução (1: 1080p, 2: 720p, 3: 360p).
    - O vídeo será baixado e salvo no diretório atual.

Observações:
- Este script requer uma conexão ativa com a internet.
- O vídeo baixado será salvo no diretório atual.
- Certifique-se de instalar as bibliotecas necessárias antes de executar o script.

## Solução para o erro no pytube 15

Atualmente, no pytube 15, há um erro que pode ocorrer durante o processo de download. Para corrigir esse erro, siga as instruções abaixo:

1. Abra o arquivo `cypher.py`, que está localizado em `Python311\Lib\site-packages\pytube\cypher.py` (certifique-se de substituir `Python311` pelo diretório correto da sua instalação do Python).
2. Substitua o script atual pelo seguinte código:

```python
linhas 264 - 274
function_patterns = [
    # https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377
    # https://github.com/yt-dlp/yt-dlp/commit/48416bc4a8f1d5ff07d5977659cb8ece7640dcd8
    # var Bpa = [iha];
    # ...
    # a.C && (b = a.get("n")) && (b = Bpa[0](b), a.set("n", b),
    # Bpa.length || iha("")) }};
    # In the above case, `iha` is the relevant function name
    r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
    r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
]


Lembre-se de substituir `Python311` pelo diretório correto da sua instalação do Python. Essa solução deve resolver o erro relacionado ao pytube 15.
```


# English version

This script allows you to download YouTube videos using the pytube library. It provides a command-line interface to select the video resolution and download it.

## Requirements

- pytube library (install using the command: `pip install pytube`)
- colorama library (install using the command: `pip install colorama`)

## How to Use

1. Run the script.
2. Choose an option:
    - 1: Download a YouTube video.
    - 2: Exit the program.
3. If option 1 is chosen:
    - Enter a valid link to a YouTube video.
    - Choose a resolution (1: 1080p, 2: 720p, 3: 360p).
    - The video will be downloaded and saved in the current directory.

Notes:
- This script requires an active internet connection.
- The downloaded video will be saved in the current directory.
- Make sure to install the necessary libraries before running the script.

## Solution for pytube 15 Error

Currently, in pytube 15, there is an error that may occur during the download process. To fix this error, follow the instructions below:

1. Open the `cypher.py` file, located at `Python311\Lib\site-packages\pytube\cypher.py` (make sure to replace `Python311` with the correct directory of your Python installation).
2. Replace the current script with the following code:

```python
lines 264 - 274
function_patterns = [
    # https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377
    # https://github.com/yt-dlp/yt-dlp/commit/48416bc4a8f1d5ff07d5977659cb8ece7640dcd8
    # var Bpa = [iha];
    # ...
    # a.C && (b = a.get("n")) && (b = Bpa[0](b), a.set("n", b),
    # Bpa.length || iha("")) }};
    # In the above case, `iha` is the relevant function name
    r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
    r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
]```


Remember to replace `Python311` with the correct directory of your Python installation. This solution should resolve the error related to pytube 15.
