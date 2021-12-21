from socket import *
import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import pickle
from constants import *



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

        self.name = tk.Entry(width=30, bg="#F0F0F0", justify='center')
        self.name.grid(column=0, row=1, sticky='sew')

        btn_button = tk.Button(master=self.window, text='Log in', height=2, fg="blue", command=self.abre_menu)
        btn_button.grid(column=0, row=2, sticky='sew')
        self.window.mainloop()

    def abre_menu(self):
        if (self.name.get() != ''):
            self.username = self.name.get()
            self.window.destroy()
            self.window = tk.Tk()
            self.window.title('Streaming app')
            self.list_videos()
            self.main_menu()

    def list_videos(self):
        self.videos_list = []
        data = {
            'message': 'LISTAR_VIDEOS',
            'params': {}
        }
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

        self.window.mainloop()

    def update_catalog(self, frm_main_menu, frm_side):
        frm_main_menu.destroy()
        frm_side.destroy()
        self.list_videos()
        self.main_menu()

    def leave_app(self):
        data = {
            'message': 'leave_app',
            'params': {}
        }
        self.clientSocket.sendto(pickle.dumps(data), (server_ip , server_port))
        self.clientSocket.close()
        self.window.destroy()

    def choose_resolution(self, video, frm_main_menu, frm_side):
        frm_main_menu.pack_forget()
        frm_side.pack_forget()

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)


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

        self.window.mainloop()

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
            }
        self.clientSocket.sendto(pickle.dumps(data), (server_ip,server_port))
        frm_buttons.destroy()
        frm_video.destroy()
        self.main_menu()

if __name__ == "__main__":
    app = client_app()
