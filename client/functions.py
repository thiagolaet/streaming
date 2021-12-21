import sockets


def espera_mensagem(self, resposta):
    response = self.streamingSocket.recv(1024)
    while (response.decode('UTF-8')[0] != resposta):
        response = self.streamingSocket.recv(1024)
    return True

def envia_mensagem(self, mensagem, resposta):
    self.streamingSocket.send(mensagem.encode('UTF-8'))
    espera_mensagem(self, resposta)
    return True



