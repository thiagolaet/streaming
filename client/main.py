import tkinter as tk

class client_app():
    def __init__(self):
        self.window = tk.Tk()
        self.username = ''
        self.status = ''
        self.lista_de_videos = []

    def login(self):
        logo = tk.Label(
            text="Streaming app",
            foreground="red",  # Set the text color to white
            background="black",  # Set the background color to black
            height=25,
            width=75
        )
        logo.pack(fill=tk.BOTH)
        self.nome = tk.Entry(width=30, bg="black", fg="#AAAAAA", relief=tk.RAISED, justify='center')
        self.nome.pack(fill=tk.BOTH)
        button = tk.Button(master=self.window,
                           text='Log in',
                           height=2,
                           bg="black",
                           fg="red", command=self.open_menu
                           )
        button.pack(fill=tk.BOTH)
        self.window.mainloop()

    def open_menu(self):
        if (self.nome.get() != ''):
            self.username = self.nome.get()
            # print('username')# envia sockets com nome, ip, flag_premium
            # espera "ENTRAR_NA_APP_ACK" para entrar
            self.window.destroy()
            self.window = tk.Tk()
            self.listar_videos()
            self.main_menu()

    def listar_videos(self):

        self.lista_de_videos = []
        # envia requisição de lista de videos atualizada
        # self.lista_de_videos = lista recebida

    def main_menu(self):
        frm_main_menu = tk.LabelFrame(master=self.window, text='Catálogo de filmes', height=50, borderwidth=3)
        for i in range(30):
            frm_videos = tk.Frame(master=frm_main_menu, height=50, width=400, relief=tk.RAISED)
            frm_videos.grid(column=i % 5, row=i // 5, sticky='w')
            label_video = tk.Button(master=frm_videos,
                                    text=f"O FILME {i}.",
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
                                bg='black',
                                fg='grey',
                                height=3)
        lbl_username.pack(fill=tk.X)
        lbl_group = tk.Label(master=frm_group,
                             text='Watch party',
                             width=25,
                             bg='blue',
                             height=3)
        lbl_group.pack(fill=tk.X, side='top')
        frm_group.pack(fill=tk.X, side="right", anchor='se', expand=True)
        lbl_atualiza = tk.Button(master=frm_group,
                                 text='Atualiza catalogo',
                                 width=25,
                                 bg='black',
                                 fg='red',
                                 height=3,
                                 relief=tk.GROOVE,
                                 command=self.listar_videos)
        lbl_atualiza.pack(fill=tk.X, side="top")

        lbl_sair = tk.Button(master=frm_group,
                             text='Sair da aplicação',
                             width=25,
                             bg='red',
                             fg='black',
                             height=3,
                             relief=tk.GROOVE,
                             command=self.sair_da_app)
        lbl_sair.pack(fill=tk.X, side="bottom")

        frm_main_menu.pack()

        self.window.mainloop()

    def sair_da_app(self):
        self.window.destroy()

    def seleciona_qualidade(self, i, frm_main_menu, frm_group):
        frm_main_menu.pack_forget()
        frm_group.pack_forget()

        filme = self.lista_de_videos[i]['text']

        frame = tk.LabelFrame(self.window, text=filme, padx=15, pady=5)
        frame.pack(padx=10, pady=10)
        cancel_frame = tk.LabelFrame(self.window, padx=15, relief='flat')
        cancel_frame.pack(padx=10)
        list_videos_button = tk.Button(frame, text="480p", width=30, height=2,
                                       command=lambda: self.assistir_video(frame, cancel_frame))
        list_videos_button.pack(pady=3)
        add_videos_button = tk.Button(frame, text="720p", width=30, height=2,
                                      command=lambda: self.assistir_video(frame, cancel_frame))
        add_videos_button.pack(pady=3)
        remove_videos_button = tk.Button(frame, text="1080p", width=30, height=2,
                                         command=lambda: self.assistir_video(frame, cancel_frame))
        remove_videos_button.pack(pady=3)
        btn_cancela = tk.Button(cancel_frame, text="Cancelar", width=30, height=2,
                                command=lambda: self.cancela_escolha_resolucao(frame, cancel_frame))
        btn_cancela.pack(pady=10)

        self.window.mainloop()

    def cancela_escolha_resolucao(self, frame, cancel_frame):
        frame.destroy()
        cancel_frame.destroy()
        self.main_menu()

    def assistir_video(self, frame, cancel_frame):
        frame.destroy()
        cancel_frame.destroy()
        # self.window = tk.Tk()
        self.window.title("Simple Text Editor")

        self.window.rowconfigure(0, minsize=600, weight=1)
        self.window.columnconfigure(1, minsize=600, weight=1)

        frm_video = tk.LabelFrame(self.window)
        frm_buttons = tk.Frame(self.window, bg='black')
        btn_open = tk.Button(frm_buttons, text="<", bg='black', fg='white', relief='flat',
                             command=lambda: self.volta_para_menu(frm_video, frm_buttons))
        btn_open.grid(row=0, column=0, sticky="ew", ipadx=15, ipady=10)
        btn_group = tk.Button(frm_buttons, text="Grupo", bg='black', fg='white', relief='flat')
        btn_group.grid(row=1, column=0, sticky="ew", ipadx=15, ipady=10)
        frm_buttons.grid(row=0, column=0, sticky="ns")
        frm_video.grid(row=0, column=1, sticky="nsew")
        self.window.mainloop()

    def volta_para_menu(self, frm_video, frm_buttons):
        frm_buttons.destroy()
        frm_video.destroy()
        self.main_menu()


client_app().login()