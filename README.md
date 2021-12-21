##### Trabalho de Redes de computadores 2 - UFF - Etapa 1

## Funcionamento

### Como usar:

* O servidor (__server.py__) deve ser executado antes do cliente.
* O servidor não precisa ser executado junto com sua interface gráfica (__app.py__).
* Na interface gráfica do servidor, o usuário tem acesso a uma lista com os vídeos disponíveis, um mecanismo de busca, além de adição e remoção de vídeos.
* No cliente, o usuário deve primeiro inserir um nome para se conectar a plataforma.
* No menu principal, será apresentada uma lista de filmes, o nome do usuário, um botão que possibilita a atualização do catálogo de filmes e um botão para sair da aplicação.
* Quando o usuário seleciona um dos filmes do catálogo, até uma tela com o botões para escolher a resolução desejada para assistir ao filme, e um botão de cancelar, caso ele queira voltar ao menu principal.
* Ao escolher o filme, o usuário começará a assistir o filme e terá acesso a um botão que o possibilita voltar ao menu inicial, assim como um botão para realizar a saída do aplicativo.


### Recursos:
* As interfaces gráficas estão sendo geradas com a biblioteca __tkinter__.
* A transmissão de dados está sendo feita com o uso de __sockets__ e da biblioteca __pickle__.
* A biblioteca __OpenCV__ é a utilizada para o processamento do vídeo no servidor.
* A biblioteca __OpenCV__ e a __PIL__ são utilizadas no cliente para a exibiçao do vídeo.
* As bibliotecas ~~ ~~ e __sqlite3__ são utilizadas no servidos para o gerenciamento interno dos arquivos de vídeo.
	
  
### Implementação
* No cliente, um objeto aplicação é instanciado na execução do aplicativo, e cada tela, além de alguns procedimentos que são chamados, são métodos dessa classe.
* Os botões que representam os filmes da lista são gerados dinamicamente baseados na lista de vídeos.
* A biblioteca pickle está sendo usada para enviar e receber os dados de forma conveniente pelo sockets, mantendo as estuturas de dados.
* A biblioteca pillow (PIL) está sendo utilizada para realizar a reprodução de imagens do OpenCV num label da tkinter, tornando possível a execução do vídeo e a disposição de botões na lateral

* No servidor a biblioteca pickle tem o mesmo intuito de simplificar a transmissão e recepção de dados.
* A biblioteca sys e a ~~ são utilizadas na app.py para tornar simplificada a adição de videos no servidor.
