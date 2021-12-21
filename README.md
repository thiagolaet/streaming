##### Trabalho de Redes de computadores 2 - UFF - Etapa 1

## Funcionamento

### Como usar:
* Instale as dependências listadas no arquivo requirements.txt.
* O servidor (__server.py__) deve ser executado antes do cliente.
* O servidor não precisa ser executado junto com sua interface gráfica (__app.py__).
* Na interface gráfica do servidor, o usuário pode gerenciar os vídeos salvos no banco de dados.
* No cliente, o usuário deve primeiro inserir um nome para se conectar a plataforma.
* No menu principal, será apresentada uma lista de filmes, o nome do usuário, um botão que possibilita a atualização do catálogo de filmes e um botão para sair da aplicação.
* Quando o usuário seleciona um dos filmes do catálogo ele é redirecionado para uma tela com os botões que o possibilitam escolher a resolução desejada para assistir ao vídeo, e um botão de cancelar, caso ele queira voltar ao menu principal.
* Ao escolher o vídeo, o usuário começará a assistir o vídeo e terá acesso a um botão que o possibilita voltar ao menu inicial, assim como um botão para realizar a saída do aplicativo.

### Recursos:
* As interfaces gráficas estão sendo geradas com a biblioteca __tkinter__.
* A transmissão de dados está sendo feita com o uso de __sockets__ e da biblioteca __pickle__.
* A biblioteca __OpenCV__ é utilizada para o processamento do vídeo no servidor e para a exibição do vídeo no cliente.
* O __sqlite3__ é utilizado para o armazenamento dos metadados dos vídeos no servidor de streaming.
