import sockets
import pickle


def espera_mensagem(self, resposta):
    response = self.streamingSocket.recv(1024)
    while (response['resposta'] != resposta):
        response = self.streamingSocket.recv(1024)
    return True

def envia_mensagem(self, mensagem, resposta):
    data = {
        'message': mensagem,
        'params': {}
    }
    self.managerSocket.sendto(pickle.dumps(data), ('ip_servidor', 'porta_streaming'))
    espera_mensagem(self, resposta)
    return True