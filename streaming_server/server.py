import socketserver, threading, time, pickle
import constants as C
from helpers import get_videos_as_dict_list


class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = pickle.loads(self.request[0].strip())
        socket = self.request[1]
        current_thread = threading.current_thread()
        response = {}
        if data.get('message'):
            if data['message'] == C.LIST_VIDEOS:
                response['message'] = C.LIST_VIDEOS_RESPONSE
                response['data'] = get_videos_as_dict_list(data.get('params').get('name'))
                socket.sendto(pickle.dumps(response), self.client_address)
            # elif data['message'] == C.START_STREAMING:
            #     play_video(socket, self.client_address, data.get('params').get('video_id'), data.get('params').get('video_resolution'))
            # elif data['message'] == C.STOP_STREAMING:
            #     socket.close()
        return


class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 6000
    server = ThreadedUDPServer((C.HOST, C.PORT), ThreadedUDPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True

    try:
        server_thread.start()
        print("Server started at {} port {}".format(C.HOST, C.PORT))
        while True: time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        print("Server stopped")
