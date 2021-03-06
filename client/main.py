from socket import *
import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import pickle
from constants import *
import struct
import numpy

MAX_DGRAM = 2**16

class client_app():
    def __init__(self):
        self.clientSocket = socket(AF_INET, SOCK_DGRAM)
        self.window = tk.Tk()
        self.window.title('Streaming app - login')
        self.username = ''
        self.login()

    def login(self):
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        logo = tk.Label(text="Streaming app", foreground="blue", height=8, width=25)
        logo.grid(column=0, row=0, sticky='nsew')

        self.nome = tk.Entry(width=30, bg="#F0F0F0", justify='center')
        self.nome.grid(column=0, row=1, sticky='sew')

        button = tk.Button(master=self.window, text='Log in', height=2, fg="blue", command=self.abre_menu)
        button.grid(column=0, row=2, sticky='sew')
        self.window.mainloop()

    def abre_menu(self):
        if (self.nome.get() != ''):
            self.username = self.nome.get()
            self.window.destroy()
            self.window = tk.Tk()
            self.window.title('Streaming app')
            self.listar_videos()
            self.menu_principal()

    def listar_videos(self):
        self.lista_de_videos = []
        data = {
            'message': 'LISTAR_VIDEOS',
            'params': {}
        }
        self.clientSocket.sendto(pickle.dumps(data), (ip_servidor, porta_servidor))
        lista = self.clientSocket.recv(1024)
        lista = pickle.loads(lista)
        self.lista_de_videos = lista['data']



    def menu_principal(self):
        frm_menu_principal = tk.LabelFrame(master=self.window, text='Catálogo de filmes', height=50, borderwidth=3)
        frm_menu_principal.pack(side='left')
        for i in range(len(self.lista_de_videos)):
            frm_videos = tk.Frame(master=frm_menu_principal, height=50, width=400, relief=tk.RAISED)
            frm_videos.grid(column=i % 5, row=i // 5, sticky='w')
            label_video = tk.Button(master=frm_videos, text=self.lista_de_videos[i]['name'], font=('Lucida', 12), width=20, height=4,
                                    padx=5, pady=5, relief=tk.GROOVE,
                                    command=lambda i=i: self.seleciona_qualidade(self.lista_de_videos[i], frm_menu_principal, frm_lateral))
            label_video.pack()

        frm_lateral = tk.LabelFrame(master=self.window)
        frm_lateral.columnconfigure(1, weight=1)
        frm_lateral.rowconfigure(1, weight=1)
        frm_lateral.pack(fill=tk.X, side="right", anchor='se', expand=True)

        lbl_username = tk.Label(master=frm_lateral, text=self.username, width=25, font=('Arial', 10), fg='blue', height=3)
        lbl_username.pack(fill=tk.X)

        lbl_atualiza = tk.Button(master=frm_lateral, text='Atualiza catalogo', width=25, fg='blue', height=3,
                                 relief=tk.GROOVE, command=lambda: self.atualiza_catalogo(frm_menu_principal, frm_lateral))
        lbl_atualiza.pack(fill=tk.X, side="top")

        lbl_sair = tk.Button(master=frm_lateral, text='Sair da aplicação', width=25, fg='red', height=3, relief=tk.GROOVE,
                             command=self.sair_da_app)
        lbl_sair.pack(fill=tk.X, side="bottom")

        self.window.mainloop()

    def atualiza_catalogo(self, frm_menu_principal, frm_lateral):
        frm_menu_principal.destroy()
        frm_lateral.destroy()
        self.listar_videos()
        self.menu_principal()

    def sair_da_app(self):
        data = {
            'message': 'SAIR_DA_APP',
            'params': {}
        }
        self.clientSocket.sendto(pickle.dumps(data), (ip_servidor, porta_servidor))
        self.clientSocket.close()
        self.window.destroy()

    def seleciona_qualidade(self, filme, frm_menu_principal, frm_lateral):
        frm_menu_principal.pack_forget()
        frm_lateral.pack_forget()

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)


        frm_descricao = tk.Frame(self.window, padx=15, pady=5)
        frm_descricao.grid(row=0, column=0)
        lbl_nome = tk.Label(frm_descricao, text="Título: "+filme['name'], height=3, width=25, anchor='w')
        lbl_nome.pack()
        lbl_descricao = tk.Label(frm_descricao, text=str(filme['views'])+" visualizações", width=25, anchor='w')
        lbl_descricao.pack()

        frm_qualidade = tk.LabelFrame(self.window, text='Resolução', padx=15, pady=5)
        frm_qualidade.grid(row=0, column=1, padx=2, pady=5, sticky='s')
        frm_cancelar = tk.LabelFrame(self.window, padx=15, relief='flat')
        frm_cancelar.grid(row=1, column=1, padx=2, sticky='s')
        remove_videos_button = tk.Button(frm_qualidade, text="240p", width=12, height=1,
                                         command=lambda: self.assistir_video(frm_descricao, frm_qualidade,frm_cancelar, filme['id'], 426))
        remove_videos_button.pack(pady=3)
        list_videos_button = tk.Button(frm_qualidade, text="480p", width=12, height=1,
                                       command=lambda: self.assistir_video(frm_descricao, frm_qualidade, frm_cancelar, filme['id'], 854))
        list_videos_button.pack(pady=3)
        add_videos_button = tk.Button(frm_qualidade, text="720p", width=12, height=1,
                                      command=lambda: self.assistir_video(frm_descricao, frm_qualidade, frm_cancelar, filme['id'], 1280))
        add_videos_button.pack(pady=3)
        btn_cancela = tk.Button(frm_cancelar, text="Cancelar", width=12, height=1,
                                command=lambda: self.cancela_escolha_resolucao(frm_descricao, frm_qualidade, frm_cancelar))
        btn_cancela.pack(pady=10)

        self.window.mainloop()

    def cancela_escolha_resolucao(self, frm_descricao, frm_qualidade, frm_cancelar):
        frm_descricao.destroy()
        frm_qualidade.destroy()
        frm_cancelar.destroy()
        self.menu_principal()

    def dump_buffer(self, sock):
        while True:
            seg, addr = sock.recvfrom(MAX_DGRAM)
            if struct.unpack('B', seg[0:1])[0] == 1:
                break

    def assistir_video(self, frm_descricao, frm_qualidade, frm_cancelar, id_filme, resolucao):
        frm_qualidade.destroy()
        frm_descricao.destroy()
        frm_cancelar.destroy()

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

        data = {
            'message': 'REPRODUZIR_VIDEO',
            'params': {
                'video_id': id_filme,
                'video_resolution': resolucao
            }
        }
        dat = b''
        self.clientSocket.sendto(pickle.dumps(data), (ip_servidor, porta_servidor))
        self.dump_buffer(self.clientSocket)

        while True:
            seg, addr = self.clientSocket.recvfrom(MAX_DGRAM)
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

        # def show_frame():

        #     ret, frame = cap.read()

        #     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

        #     img = Image.fromarray(cv2image)
        #     imgtk = ImageTk.PhotoImage(image=img)
        #     frm_video.imgtk = imgtk
        #     frm_video.configure(image=imgtk)
        #     frm_video.after(4, show_frame)

        # show_frame()
        # frm_video.grid(row=0, column=1, sticky="nsew")

        # recebe data_video

        self.window.mainloop()

    def volta_para_menu(self):
        data = {
            'message': 'PARAR_STREAMING',
            'params': {}
            }
        self.clientSocket.sendto(pickle.dumps(data), (ip_servidor,porta_servidor))
        self.menu_principal()

if __name__ == "__main__":
    app = client_app()
