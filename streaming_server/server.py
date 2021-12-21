import socketserver, threading, time, pickle
import constants as C
from helpers import get_videos_list


class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = pickle.loads(self.request[0].strip())
        socket = self.request[1]
        current_thread = threading.current_thread()
        response = {}
        if data.get('message'):
            if data['message'] == C.LIST_VIDEOS:
                response['message'] = C.LIST_VIDEOS_RESPONSE
                response['data'] = get_videos_list(data.get('params').get('name'))
            # elif data['message'] == C.START_STREAMING:
            #     response['message'] = 'RESPOSTA'
            #     response['data'] = get_video()
            # elif data['message'] = C.STOP_STREAMING:
            #     response['message'] = 'RESPOSTA'

        socket.sendto(pickle.dumps(response), self.client_address)
        return


class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 6000
    server = ThreadedUDPServer((HOST, PORT), ThreadedUDPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True

    try:
        server_thread.start()
        print("Server started at {} port {}".format(HOST, PORT))
        while True: time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        print("Server stopped")
