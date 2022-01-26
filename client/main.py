from socket import *
import tkinter as tk
import cv2
import pickle
from constants import *

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes

class client_app():
    def __init__(self):
        self.managerSocket = socket(AF_INET, SOCK_STREAM)

        self.streamingSocket = socket(AF_INET, SOCK_DGRAM)
        self.window = tk.Tk()
        self.window.title('Streaming app - login')
        self.username = ''
        self.premium = tk.IntVar()
        self.group = 0
        self.group_view = 0
        self.login()

    def login(self):
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        logo = tk.Label(text="Streaming app", foreground="blue", height=8, width=40)
        logo.grid(column=0, row=0, columnspan=2, sticky='nsew')

<<<<<<< Updated upstream
        self.name = tk.Entry(width=30, bg="#F0F0F0", justify='center')
        self.name.grid(column=0, row=1, sticky='sew')

        btn_button = tk.Button(master=self.window, text='Log in', height=2, fg="blue", command=self.abre_menu)
        btn_button.grid(column=0, row=2, sticky='sew')
        self.window.mainloop()

    def abre_menu(self):
        if (self.name.get() != ''):
            self.username = self.name.get()
=======
        self.nome = tk.Entry(width=30, bg="#F0F0F0", justify='center')
        self.nome.grid(column=0, row=1, sticky='nsew')
        cb_premium_status = tk.Checkbutton(master=self.window, text='Premium', variable=self.premium, onvalue=True,
                                           offvalue=False)
        cb_premium_status.grid(column=1, row=1, sticky='se')
        button = tk.Button(master=self.window, text='Log in', height=2, fg="blue", command=self.conectar)
        button.grid(column=0, row=2, columnspan=2, sticky='sew')
        self.window.mainloop()

    def conectar(self):
        if self.nome.get() != '':
            self.username = self.nome.get()
>>>>>>> Stashed changes
            self.window.destroy()
            # self.managerSocket.connect((serverName, 'serverPort'))
            # data = {
            #     'message': 'ENTRAR_NA_APP',
            #     'params': {'Usuario':self.username, 'Status':self.premium , 'ip':'localhost'}
            # }
            # self.managerSocket.sendto(pickle.dumps(data), ('ip_servidor', 'porta_streaming'))
            # mensagem = self.streamingSocket.recv(1024)
            # mensagem = pickle.loads(mensagem)
            # if mensagem == 'ENTRAR_NA_APP_ACK':
            self.group = 0
            self.window = tk.Tk()
            self.window.title('Streaming app')
<<<<<<< Updated upstream
            self.list_videos()
            self.main_menu()

    def list_videos(self):
        self.videos_list = []
=======
            self.streamingSocket.setblocking(False)
            self.receber_lista_videos()
            self.menu_principal()

    def receber_lista_videos(self):
        self.lista_de_videos = []
>>>>>>> Stashed changes
        data = {
            'message': 'LISTAR_VIDEOS',
            'params': {}
        }
<<<<<<< Updated upstream
        self.clientSocket.sendto(pickle.dumps(data), (server_ip , server_port))
        list = self.clientSocket.recv(buffer_size)
        list = pickle.loads(list)
        self.videos_list = list['data']



    def main_menu(self):
        frm_main_menu = tk.LabelFrame(master=self.window, text='Catálogo de videos', height=50, borderwidth=3)
        frm_main_menu.pack(side='left')
        for i in range(len(self.videos_list)):
            frm_videos = tk.Frame(master=frm_main_menu, height=50, width=400, relief=tk.RAISED)
            frm_videos.grid(column=i % 5, row=i // 5, sticky='w')
            label_video = tk.Button(master=frm_videos, text=self.videos_list[i]['name'], font=('Lucida', 12), width=20, height=4,
                                    padx=5, pady=5, relief=tk.GROOVE,
                                    command=lambda i=i: self.choose_resolution(self.videos_list[i], frm_main_menu, frm_side))
            label_video.pack()

        frm_side = tk.LabelFrame(master=self.window)
        frm_side.columnconfigure(1, weight=1)
        frm_side.rowconfigure(1, weight=1)
        frm_side.pack(fill=tk.X, side="right", anchor='se', expand=True)

        lbl_username = tk.Label(master=frm_side, text=self.username, width=25, font=('Arial', 10), fg='blue', height=3)
        lbl_username.pack(fill=tk.X)

        lbl_update = tk.Button(master=frm_side, text='Atualiza catálogo', width=25, fg='blue', height=3,
                                 relief=tk.GROOVE, command=lambda: self.update_catalog(frm_main_menu, frm_side))
        lbl_update.pack(fill=tk.X, side="top")

        lbl_leave = tk.Button(master=frm_side, text='Sair da aplicação', width=25, fg='red', height=3, relief=tk.GROOVE,
                             command=self.leave_app)
        lbl_leave.pack(fill=tk.X, side="bottom")
=======
        self.streamingSocket.sendto(pickle.dumps(data), (ip_servidor, porta_streaming))
        lista = self.streamingSocket.recv(1024)
        lista = pickle.loads(lista)
        self.lista_de_videos = lista['data']

    def listar_videos(self, frm_menu_principal, frm_lateral, frm_grupo):
        for i in range(len(self.lista_de_videos)):
            frm_videos = tk.Frame(master=frm_menu_principal, height=50, width=400, relief=tk.RAISED)
            frm_videos.grid(column=i % 5, row=i // 5, sticky='w')
            label_video = tk.Button(master=frm_videos, text=self.lista_de_videos[i]['name'], font=('Lucida', 12),
                                    width=20, height=4,
                                    padx=5, pady=5, relief=tk.GROOVE,
                                    command=lambda i=i: self.seleciona_qualidade(self.lista_de_videos[i],
                                                                                 frm_menu_principal, frm_lateral,
                                                                                 frm_grupo))
            label_video.pack()

    def menu_principal(self):

        message = self.streamingSocket.recv(1024)

        frm_menu_principal = tk.LabelFrame(master=self.window, text='Catálogo de filmes', height=50, borderwidth=3)
        frm_menu_principal.pack(side='left')
        frm_lateral = tk.LabelFrame(master=self.window)
        frm_lateral.columnconfigure(1, weight=1)
        frm_lateral.rowconfigure(1, weight=1)
        frm_lateral.pack(fill=tk.X, side="left", anchor='se', expand=True)

        frm_grupo = tk.LabelFrame(master=self.window, relief='flat')
        frm_grupo.columnconfigure(2, weight=1)
        frm_grupo.rowconfigure(0, weight=1)
        frm_grupo.pack(side='right', anchor='n')

        self.listar_videos(frm_menu_principal, frm_lateral, frm_grupo)
        self.opcoes(frm_menu_principal, frm_lateral, frm_grupo)

        message = pickle.loads(message)

        if message == 'HOST_INICIOU_VIDEO':
            self.assistir_video('id_filme', 'resolucao', frm_menu_principal, frm_lateral, frm_grupo)
        else:
            self.window.mainloop()

    def opcoes(self, frm_menu_principal, frm_lateral, frm_grupo):
        lbl_username = tk.Label(master=frm_lateral, text=self.username, width=25, font=('Arial', 10), fg='blue',
                                height=3)
        lbl_username.pack(fill=tk.X)

        frm_user = tk.Frame(master=frm_grupo, relief='flat')
        frm_user.pack()

        if self.group_view == 1:
            if self.group == 2:
                label_input = tk.Entry(master=frm_user, bg="#F0F0F0", justify='center')

                lbl_adiciona_user = tk.Button(master=frm_user, text='+', width=3, height=1, bg='#33FF33',
                                              relief=tk.GROOVE,
                                              command=lambda: self.adiciona_usuario(label_input, frm_lateral, frm_grupo,
                                                                                    frm_user, frm_menu_principal))
                lbl_adiciona_user.pack(side='right', anchor='center')
                label_input.pack(fill=tk.BOTH)

                for i in range(5):
                    frm_user = tk.Frame(master=frm_grupo, relief='flat')
                    frm_user.pack(fill=tk.BOTH, anchor='e')
                    label_membro = tk.Label(master=frm_user, text='User {}'.format(i), height=2, bg='#dddddd',
                                            padx=1, pady=1)
                    lbl_remove_user = tk.Button(master=frm_user, text='x', width=3, height=1, bg='red', fg='white',
                                                relief=tk.GROOVE,
                                                command=lambda i=i: self.remove_usuario('usuario[i]', frm_lateral,
                                                                                        frm_grupo, lbl_mostrar_grupo,
                                                                                        frm_menu_principal))
                    lbl_remove_user.pack(side='right', anchor='e')

                    label_membro.pack(fill=tk.X, anchor='center')
            else:
                for i in range(5):
                    frm_user = tk.Frame(master=frm_grupo, relief='flat')
                    frm_user.pack(fill=tk.BOTH, anchor='e')
                    label_membro = tk.Label(master=frm_user, text='User {}'.format(i), height=2, bg='#dddddd',
                                            padx=1, pady=1)
                    label_membro.pack(fill=tk.X, anchor='center')

            lbl_mostrar_grupo = tk.Button(master=frm_lateral, text='Ocultar grupo', width=25, height=3,
                                          relief=tk.GROOVE,
                                          command=lambda: self.oculta_grupo(frm_lateral, frm_grupo, lbl_mostrar_grupo,
                                                                            frm_menu_principal))

            lbl_mostrar_grupo.pack(fill=tk.X, side='top')

            lbl_sair = tk.Button(master=frm_grupo, text='Sair do grupo', fg='red', height=3,
                                 relief=tk.GROOVE,
                                 command=self.sair_da_app)
            lbl_sair.pack(fill=tk.X, side="bottom")
        else:
            if self.group == 0 and self.premium.get() == 1:
                self.group = 2
                lbl_mostrar_grupo = tk.Button(master=frm_lateral, text='Criar grupo', width=25, height=3,
                                              relief=tk.GROOVE,
                                              command=lambda: self.criar_grupo(frm_lateral, frm_grupo,
                                                                               lbl_mostrar_grupo, frm_menu_principal))

                lbl_mostrar_grupo.pack(fill=tk.X, side='top')

            else:
                lbl_mostrar_grupo = tk.Button(master=frm_lateral, text='Mostrar grupo', width=25, height=3,
                                              relief=tk.GROOVE,
                                              command=lambda: self.ver_grupo(frm_lateral, frm_grupo, lbl_mostrar_grupo,
                                                                             frm_menu_principal))

                lbl_mostrar_grupo.pack(fill=tk.X, side='top')

        lbl_atualiza = tk.Button(master=frm_lateral, text='Atualiza catalogo', width=25, fg='blue', height=3,
                                 relief=tk.GROOVE,
                                 command=lambda: self.atualiza_catalogo(frm_menu_principal, frm_lateral, frm_grupo))
        lbl_atualiza.pack(fill=tk.X, side="top")

        lbl_sair = tk.Button(master=frm_lateral, text='Sair da aplicação', width=25, fg='red', height=3,
                             relief=tk.GROOVE,
                             command=self.sair_da_app)
        lbl_sair.pack(fill=tk.X, side="bottom")
>>>>>>> Stashed changes

        # lbl_exclui_grupo = tk.Button(master=frm_user, text='Desfazer grupo', width=3, height=1, bg='red',
        #                              fg='white',
        #                              relief=tk.GROOVE, command=lambda: self.desfaz_grupo(frm_grupo))
        # lbl_exclui_grupo.pack(side='bottom', fill=tk.BOTH)

    def ver_grupo(self, *args):
        self.group_view = 1
        for frame in args:
            frame.destroy()
        # data = {
        #     'message': 'VER_GRUPO',
        #     'params': {}
        # }
        # self.managerSocket.sendto(pickle.dumps(data), (ip_servidor, porta_streaming))
        # # espera ack
        # resposta = self.managerSocket.recv(1024)
        # resposta = pickle.loads(resposta)
        # membros = resposta['lista']
        self.menu_principal()

    def oculta_grupo(self, *args):
        self.group_view = 0
        for frame in args:
            frame.destroy()
        self.menu_principal()

    def adiciona_usuario(self, usuario, *args):
        for frame in args:
            frame.destroy()
        # data = {
        #     'message': 'ADD_USUARIO_GRUPO',
        #     'params': {'usuario': usuario}
        # }
        # self.managerSocket.sendto(pickle.dumps(data), ('ip_servidor', 'porta_streaming'))

        self.menu_principal()

    def criar_grupo(self, *args):
        self.group = 2
        self.group_view = 1
        # data = {
        #     'message': 'CRIAR_GRUPO',
        #     'params': {}
        #   }
        #   self.managerSocket.sendto(pickle.dumps(data), (ip_servidor, porta_streaming))
        for frame in args:
            frame.destroy()
        self.menu_principal()

    def remove_usuario(self, usuario, *args):
        # usuario = usuario.get()
        # data = {
        #     'message': 'REMOVE_USUARIO',
        #     'params': {'usuario': usuario}
        # }
        # self.managerSocket.sendto(pickle.dumps(data), ('ip_servidor', 'porta_streaming'))
        for frame in args:
            frame.destroy()
        self.menu_principal()

<<<<<<< Updated upstream
    def update_catalog(self, frm_main_menu, frm_side):
        frm_main_menu.destroy()
        frm_side.destroy()
        self.list_videos()
        self.main_menu()
=======
    # def desfaz_grupo(self, frm_grupo, lbl_mostrar_grupo, frm_lateral):
    #   # data = {
    #   #       'message': 'EXCLUI_GRUPO',
    #   #       'params': {}
    #   #   }
    #   # self.managerSocket.sendto(pickle.dumps(data), (ip_servidor, porta_streaming))
    #   # espera resposta
    #     frm_grupo.destroy()
    #     lbl_mostrar_grupo.destroy()
    #     lbl_mostrar_grupo = tk.Button(master=frm_lateral, text='Criar_grupo', width=25, height=3,
    #                                   relief=tk.GROOVE, command = self.criar_grupo)
    #     lbl_mostrar_grupo.pack(fill=tk.X, side='top')

    def atualiza_catalogo(self, *args):
        for frame in args:
            frame.destroy()
        self.receber_lista_videos()
        self.menu_principal()
>>>>>>> Stashed changes

    def leave_app(self):
        data = {
            'message': 'leave_app',
            'params': {}
        }
<<<<<<< Updated upstream
        self.clientSocket.sendto(pickle.dumps(data), (server_ip , server_port))
        self.clientSocket.close()
        self.window.destroy()

    def choose_resolution(self, video, frm_main_menu, frm_side):
        frm_main_menu.pack_forget()
        frm_side.pack_forget()
=======
        self.streamingSocket.sendto(pickle.dumps(data), (ip_servidor, porta_streaming))
        self.streamingSocket.close()
        self.window.destroy()

    def seleciona_qualidade(self, filme, *args):
        for frame in args:
            frame.destroy()
>>>>>>> Stashed changes

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)

<<<<<<< Updated upstream

        frm_description = tk.Frame(self.window, padx=15, pady=5)
        frm_description.grid(row=0, column=0)
        lbl_nome = tk.Label(frm_description, text="Título: "+video['name'], height=3, width=25, anchor='w')
        lbl_nome.pack()
        lbl_description = tk.Label(frm_description, text=str(video['views'])+" vizualizações", width=25, anchor='w')
        lbl_description.pack()

        frm_resolution = tk.LabelFrame(self.window, text='Resolução', padx=15, pady=5)
        frm_resolution.grid(row=0, column=1, padx=2, pady=5, sticky='s')
        frm_cancel = tk.LabelFrame(self.window, padx=15, relief='flat')
        frm_cancel.grid(row=1, column=1, padx=2, sticky='s')
        list_videos_button = tk.Button(frm_resolution, text="480p", width=12, height=1,
                                       command=lambda: self.watch_video(frm_description, frm_resolution, frm_cancel, video['id'], '640'))
        list_videos_button.pack(pady=3)
        btn_add_videos = tk.Button(frm_resolution, text="720p", width=12, height=1,
                                      command=lambda: self.watch_video(frm_description, frm_resolution, frm_cancel, video['id'], '1280'))
        btn_add_videos.pack(pady=3)
        btn_del_videos = tk.Button(frm_resolution, text="1080p", width=12, height=1,
                                         command=lambda: self.watch_video(frm_description, frm_resolution,frm_cancel, video['id'], '1920'))
        btn_del_videos.pack(pady=3)
        btn_cancel = tk.Button(frm_cancel, text="cancel", width=12, height=1,
                                command=lambda: self.close_res_window(frm_description, frm_resolution, frm_cancel))
        btn_cancel.pack(pady=10)
=======
        frm_descricao = tk.Frame(self.window, padx=15, pady=5)
        frm_descricao.grid(row=0, column=0)

        lbl_nome = tk.Label(frm_descricao, text="Título: " + filme['name'], height=3, width=25, anchor='w')
        lbl_nome.pack()
        lbl_descricao = tk.Label(frm_descricao, text=str(filme['views']) + " visualizações", width=25, anchor='w')
        lbl_descricao.pack()

        frm_cancelar = tk.LabelFrame(self.window, padx=15, relief='flat')
        frm_cancelar.grid(row=1, column=1, padx=2, sticky='s')
        btn_cancela = tk.Button(frm_cancelar, text="Cancelar", width=12, height=1,
                                command=lambda: self.cancela_escolha_resolucao(frm_descricao, frm_cancelar))
        btn_cancela.pack(pady=10)
>>>>>>> Stashed changes

        if self.premium.get() == 1:
            frm_qualidade = tk.LabelFrame(self.window, text='Resolução', padx=15, pady=5)
            frm_qualidade.grid(row=0, column=1, padx=2, pady=5, sticky='s')
            frm_cancelar = tk.LabelFrame(self.window, padx=15, relief='flat')
            frm_cancelar.grid(row=1, column=1, padx=2, sticky='s')
            low_quality_button = tk.Button(frm_qualidade, text="240p", width=12, height=1,
                                           command=lambda: self.assistir_video(filme['id'], 426, frm_descricao,
                                                                               frm_qualidade, frm_cancelar))
            low_quality_button.pack(pady=3)
            medium_quality_button = tk.Button(frm_qualidade, text="480p", width=12, height=1,
                                              command=lambda: self.assistir_video(filme['id'], 854, frm_descricao,
                                                                                  frm_qualidade, frm_cancelar))
            medium_quality_button.pack(pady=3)
            high_quality_button = tk.Button(frm_qualidade, text="720p", width=12, height=1,
                                            command=lambda: self.assistir_video(filme['id'], 1280, frm_descricao,
                                                                                frm_qualidade, frm_cancelar))
            high_quality_button.pack(pady=3)
            btn_cancela = tk.Button(frm_cancelar, text="Cancelar", width=12, height=1,
                                    command=lambda: self.cancela_escolha_resolucao(frm_descricao, frm_qualidade,
                                                                                           frm_cancelar))
            btn_cancela.pack(pady=10)

        self.window.mainloop()

<<<<<<< Updated upstream
    def close_res_window(self, frm_description, frm_resolution, frm_cancel):
        frm_description.destroy()
        frm_resolution.destroy()
        frm_cancel.destroy()
        self.main_menu()

    def watch_video(self, frm_description, frm_resolution, frm_cancel, id_video, resolution):
        frm_resolution.destroy()
        frm_description.destroy()
        frm_cancel.destroy()

        data = {
            'message': 'REPRODUZIR_VIDEO',
            'params': {
                'video_id': id_video,
                'video_resolution': resolution
            }
        }
        self.clientSocket.sendto(pickle.dumps(data), (server_ip, server_port))

        self.window.title('Streaming app')

        self.window.columnconfigure(0, weight=0)
        self.window.columnconfigure(1, weight=1)

        frm_video = tk.Label(self.window, relief='flat', bg='black')
        frm_buttons = tk.Frame(self.window, bg='black')
        btn_back = tk.Button(frm_buttons, text="<", bg='black', fg='white', relief='flat',
                             command=lambda: self.back_to_menu(frm_video, frm_buttons))
        btn_back.grid(row=0, column=0, sticky="ew", ipadx=15, ipady=10)
        btn_leave = tk.Button(frm_buttons, text="leave", bg='black', fg='red', relief='flat', command=lambda: self.leave_app())
        btn_leave.grid(row=1, column=0, sticky="ews", ipadx=15, ipady=10)
        frm_buttons.grid(row=0, column=0, sticky="ns")
        frm_video.grid(row=0, column=1, sticky="nsew")


        def show_frame():
=======
    def cancela_escolha_resolucao(self, *args):
        for frame in args:
            frame.destroy()
        self.menu_principal()

    def dump_buffer(self, sock):
        while True:
            seg, addr = sock.recvfrom(MAX_DGRAM)
            print(seg[0])
            if struct.unpack('B', seg[0:1])[0] == 1:
                break

    def assistir_video(self, id_filme, resolucao, *args):
        for frame in args:
            frame.destroy()

        # self.window.title('Streaming app')

        # self.window.columnconfigure(0, weight=0)
        # self.window.columnconfigure(1, weight=1)

        # frm_video = tk.Label(self.window, relief='flat', bg='black')
        # frm_buttons = tk.Frame(self.window, bg='black')
        # btn_voltar = tk.Button(frm_buttons, text="<", bg='black', fg='white', relief='flat',
        #                      command=lambda: self.volta_para_menu(frm_video, frm_buttons))
        # btn_voltar.grid(row=0, column=0, sticky="ew", ipadx=15, ipady=10)
        # btn_sair = tk.Button(frm_buttons, text="Sair", bg='black', fg='red', relief='flat', command=lambda: self.sair_da_app())
        # btn_sair.grid(row=1, column=0, sticky="ews", ipadx=15, ipady=10)
        # frm_buttons.grid(row=0, column=0, sticky="ns")
        # frm_video.grid(row=0, column=1, sticky="nsew")

        if self.group == 2:
            data = {
                'message': 'REPRODUZIR_VIDEO_GRUPO',
                'params': {
                    'video_id': id_filme,
                    'video_resolution': resolucao
                }
            }
        else:
            data = {
                'message': 'REPRODUZIR_VIDEO',
                'params': {
                    'video_id': id_filme,
                    'video_resolution': resolucao
                }
            }

        dat = b''
        self.streamingSocket.sendto(pickle.dumps(data), (ip_servidor, porta_streaming))
        self.dump_buffer(self.streamingSocket)

        while True:
            seg, addr = self.streamingSocket.recvfrom(MAX_DGRAM)
            if struct.unpack('B', seg[0:1])[0] > 1:
                dat += seg[1:]
            else:
                dat += seg[1:]
                img = cv2.imdecode(numpy.fromstring(dat, dtype=numpy.uint8), 1)
                cv2.imshow('frame', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                dat = b''
        cv2.destroyAllWindows()
        self.volta_para_menu()
>>>>>>> Stashed changes

            ret, frame = cap.read()

            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            frm_video.imgtk = imgtk
            frm_video.configure(image=imgtk)
            frm_video.after(4, show_frame)

        show_frame()

        frm_video.grid(row=0, column=1, sticky="nsew")


        self.window.mainloop()

    def back_to_menu(self, frm_video, frm_buttons):
        data = {
            'message': 'PARAR_STREAMING',
            'params': {}
<<<<<<< Updated upstream
            }
        self.clientSocket.sendto(pickle.dumps(data), (server_ip,server_port))
        frm_buttons.destroy()
        frm_video.destroy()
        self.main_menu()
=======
        }
        self.streamingSocket.sendto(pickle.dumps(data), (ip_servidor, porta_streaming))
        self.menu_principal()
>>>>>>> Stashed changes


if __name__ == "__main__":
    app = client_app()
