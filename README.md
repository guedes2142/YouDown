

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

