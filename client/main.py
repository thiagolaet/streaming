import tkinter as tk
from tkinter import *
from tkinter.ttk import *
# from tkinter.ttk import Frame
from PIL import Image
from PIL import ImageTk
# import Image, ImageTk
import globals
import cv2

class client_app():
    def __init__(self):
        # hostname = socket.gethostname()
        # self.ip_address = socket.gethostbyname(hostname)
        # self.socket_streaming = socket(AF_INET, SOCK_DGRAM)
        # self.socket_manager = socket(AF_INET, SOCK_STREAM)
        self.window = tk.Tk()
        self.window.title('Streaming app - login')
        self.username = ''
        self.status = ''
        self.lista_de_videos = []

    def login(self):
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        logo = tk.Label(
            text="Streaming app",
            foreground="blue",  # Set the background color to black
            height=8,
            width=25
        )
        logo.grid(column=0, row=0, sticky='nsew')
        self.nome = tk.Entry(width=30, bg="#F0F0F0", justify='center')
        self.nome.grid(column=0,row=1, sticky='sew')
        button = tk.Button(master=self.window,
                           text='Log in',
                           height=2,
                           fg="blue", command=self.open_menu
                           )
        button.grid(column=0,row=2, sticky='sew')
        self.window.mainloop()

    def open_menu(self):
        if (self.nome.get() != ''):
            self.username = self.nome.get()
            # message = ['ENTRAR_NA_APP', self.username, self.ip, 1]
            # self.socket_streaming.send(message.encode('UTF-8'))
            # if chegou_mensagem_streaming('ENTRAR_NA_APP_ACK'):
                # espera "ENTRAR_NA_APP_ACK" para entrar
            self.window.destroy()
            self.window = tk.Tk()
            self.window.title('Streaming app')
            self.listar_videos()
            self.main_menu()

    def listar_videos(self):
        self.lista_de_videos = []
        # message = 'LISTAR_VIDEOS'
        # self.socket_streaming.send(message.encode('UTF-8'))
        # if chegou_mensagem_streaming('LISTA_DE_VIDEOS'):
        # self.lista_de_videos.append() lista de videos

    def main_menu(self):
        frm_main_menu = tk.LabelFrame(master=self.window, text='Catálogo de filmes', height=50, borderwidth=3)
        # for i in range(len(self.lista_de_videos))
        for i in range(30):
            frm_videos = tk.Frame(master=frm_main_menu, height=50, width=400, relief=tk.RAISED)
            frm_videos.grid(column=i % 5, row=i // 5, sticky='w')
            label_video = tk.Button(master=frm_videos,
                                    text=f"O Filme {i}",
                                    font=('Lucida', 12),
                                    width=20,
                                    height=4,
                                    padx=5,
                                    pady=5,
                                    relief=tk.GROOVE,
                                    command=lambda i=i: self.seleciona_qualidade(i, frm_main_menu, frm_group))
            label_video.pack()
            self.lista_de_videos.append(label_video)
        frm_group = tk.LabelFrame(master=self.window)
        frm_group.columnconfigure(1, weight=1)
        frm_group.rowconfigure(1, weight=1)

        lbl_username = tk.Label(master=frm_group,
                                text=self.username,
                                width=25,
                                font=('Arial', 10),
                                fg='blue',
                                height=3)
        lbl_username.pack(fill=tk.X)
        # lbl_group = tk.Label(master=frm_group,
        #                       text='Watch party',
        #                      width=25,
        #                      bg='blue',
        #                      height=3)
        # lbl_group.pack(fill=tk.X, side='top')
        frm_group.pack(fill=tk.X, side="right", anchor='se', expand=True)
        lbl_atualiza = tk.Button(master=frm_group,
                                 text='Atualiza catalogo',
                                 width=25,
                                 fg='blue',
                                 height=3,
                                 relief=tk.GROOVE,
                                 command=self.listar_videos)
        lbl_atualiza.pack(fill=tk.X, side="top")

        lbl_sair = tk.Button(master=frm_group,
                             text='Sair da aplicação',
                             width=25,
                             fg='red',
                             height=3,
                             relief=tk.GROOVE,
                             command=self.sair_da_app)
        lbl_sair.pack(fill=tk.X, side="bottom")

        frm_main_menu.pack()

        self.window.mainloop()

    def sair_da_app(self):
        # message = 'SAIR_DA_APP'
        # self.socket_streaming.send(message.encode('UTF-8'))
        # if chegou_mensagem_streaming('SAIR_DA_APP_ACK'):
            ## message = 'PARAR_STREAMING'
            # self.socket_streaming.send(message.encode('UTF-8'))
            #if chegou_mensagem_streaming('PARAR_STREAMING'):
            #self.socket_streaming.close()
        self.window.destroy()

    def seleciona_qualidade(self, i, frm_main_menu, frm_group):
        frm_main_menu.pack_forget()
        frm_group.pack_forget()

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)



        filme = self.lista_de_videos[i]['text']

        frm_descricao = tk.Frame(self.window, padx=15, pady=5)
        frm_descricao.grid(row=0, column=0)
        lbl_nome = tk.Label(frm_descricao,
                            text=filme,  # Set the background color to black
                            height=3,
                            width=25,anchor='w')
        lbl_nome.pack()
        lbl_descricao = tk.Label(frm_descricao,
                            text='Filme top, assista com sua família!!',  # Set the background color to black
                            width=25, anchor='w')
        lbl_descricao.pack()

        frm_qualidade = tk.LabelFrame(self.window, text='Resolução', padx=15, pady=5)
        frm_qualidade.grid(row=0, column=1, padx=2, pady=5, sticky='s')
        cancel_frame = tk.LabelFrame(self.window, padx=15, relief='flat')
        cancel_frame.grid(row=1, column=1, padx=2, sticky='s')
        list_videos_button = tk.Button(frm_qualidade, text="480p", width=12, height=1,
                                       command=lambda: self.assistir_video(frm_descricao, frm_qualidade, cancel_frame))
        list_videos_button.pack(pady=3)
        add_videos_button = tk.Button(frm_qualidade, text="720p", width=12, height=1,
                                      command=lambda: self.assistir_video(frm_descricao, frm_qualidade, cancel_frame))
        add_videos_button.pack(pady=3)
        remove_videos_button = tk.Button(frm_qualidade, text="1080p", width=12, height=1,
                                         command=lambda: self.assistir_video(frm_descricao, frm_qualidade, cancel_frame))
        remove_videos_button.pack(pady=3)
        btn_cancela = tk.Button(cancel_frame, text="Cancelar", width=12, height=1,
                                command=lambda: self.cancela_escolha_resolucao(frm_descricao,  frm_qualidade, cancel_frame))
        btn_cancela.pack(pady=10)





        self.window.mainloop()

    def cancela_escolha_resolucao(self, frm_descricao, frm_qualidade, cancel_frame):
        frm_descricao.destroy()
        frm_qualidade.destroy()
        cancel_frame.destroy()
        self.main_menu()

    def assistir_video(self,frm_descricao, frm_qualidade, cancel_frame):
        frm_qualidade.destroy()
        frm_descricao.destroy()
        cancel_frame.destroy()
        # message = 'REPRODUZIR_VIDEO', 'video_x', 'resolucaoy'
        # self.socket_streaming.send(message.encode('UTF-8'))
        # if chegou_mensagem_streaming('REPRODUZINDO_VIDEO'):
            # espera data_video??
        # self.window = tk.Tk()
        self.window.title('Streaming app')

        self.window.columnconfigure(0, weight=0)
        self.window.columnconfigure(1, weight=1)

        frm_video = tk.Label(self.window, relief='flat', bg='black')
        frm_buttons = tk.Frame(self.window, bg='black')
        btn_open = tk.Button(frm_buttons, text="<", bg='black', fg='white', relief='flat',
                             command=lambda: self.volta_para_menu(frm_video, frm_buttons))
        btn_open.grid(row=0, column=0, sticky="ew", ipadx=15, ipady=10)
        btn_group = tk.Button(frm_buttons, text="Grupo", bg='black', fg='white', relief='flat')
        btn_group.grid(row=1, column=0, sticky="ew", ipadx=15, ipady=10)
        frm_buttons.grid(row=0, column=0, sticky="ns")
        frm_video.grid(row=0, column=1, sticky="nsew")


        cap = cv2.VideoCapture('video.mp4')

        def show_frame():
            ret, frame = cap.read()

            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

            img = Image.fromarray(cv2image)
                # .resize((760,400))
            imgtk = ImageTk.PhotoImage(image=img)
            frm_video.imgtk = imgtk
            frm_video.configure(image=imgtk)
            frm_video.after(4, show_frame)


        show_frame()
        frm_video.grid(row=0, column=1, sticky="nsew")

        # recebe data_video

        self.window.mainloop()

    def volta_para_menu(self, frm_video, frm_buttons):
        ## message = 'PARAR_STREAMING'
        # self.socket_streaming.send(message.encode('UTF-8'))
        # if chegou_mensagem_streaming('PARAR_STREAMING'):
        frm_buttons.destroy()
        frm_video.destroy()
        self.main_menu()


client_app().login()