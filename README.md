Programa de download de vídeos do YouTube

Este programa é capaz de baixar vídeos do YouTube em diferentes resoluções, a partir de um link válido fornecido pelo usuário. Ele usa a biblioteca Pytube para realizar o download.
Requisitos

Para executar este programa, você precisa ter a biblioteca Pytube instalada. Você pode instalá-la usando o pip:
pip install pytube
Ou instale os requerimentos com o seguinte comando no terminal
pip install -r requirements.txt
Lembrando que o requerimentos esta na mesma pasta do arquivo main.py

Uso

Para executar o programa, execute o arquivo download_youtube.py. Ele irá solicitar que você insira o link do vídeo que deseja baixar. Se o link for inválido, uma mensagem de erro será exibida e o programa será encerrado.

Depois de inserir um link válido, o programa irá exibir uma lista de opções de resolução disponíveis para download. Insira o número correspondente à opção que deseja baixar. Se a opção não for válida, uma mensagem de erro será exibida e o programa solicitará uma nova entrada.

Depois de selecionar a opção de resolução desejada, o programa iniciará o download do vídeo. Se o download for bem-sucedido, uma mensagem de sucesso será exibida. Caso contrário, uma mensagem de erro será exibida.

Limitações

Este programa é capaz de baixar apenas vídeos públicos do YouTube. Ele não pode baixar vídeos que requerem autenticação ou que foram marcados como privados. Além disso, o programa pode enfrentar problemas ao baixar vídeos muito grandes ou com resoluções muito altas, devido a limitações de memória do sistema.
