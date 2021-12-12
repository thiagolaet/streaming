import tkinter as tk
from tkinter import *
from frames import InsertVideoFrame, ListVideosFrame
from repositories.video_repository import VideoRepository

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Streaming Server")
        self.search_var = StringVar()
        self.create_widgets()
        self.showing_videos_list = False

    def create_widgets(self):
        frame = tk.LabelFrame(self, text="Gerenciamento de vídeos", padx=15, pady=15)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        list_videos_button = tk.Button(frame, text="Listar vídeos", width=30, height=2, command=self.open_search_video_frame)
        list_videos_button.pack(pady=3)
        add_videos_button = tk.Button(frame, text="Adicionar vídeo", width=30, height=2, command=self.open_add_video_window)
        add_videos_button.pack(pady=3)
        # remove_videos_button = tk.Button(frame, text="Remover vídeo", width=30, height=2, command=remove_videos)
        # remove_videos_button.pack(pady=3)

    def open_add_video_window(self):
        insert_window = Toplevel(self)
        insert_window.title('Novo vídeo')
        InsertVideoFrame(insert_window)

    def open_search_video_frame(self):
        if not self.showing_videos_list:
            search_frame = Frame(self, padx=15, pady=15)
            search_frame.grid(row=0, column=1, padx=10, pady=10)
            ListVideosFrame(search_frame)
            self.showing_videos_list = True

if __name__ == "__main__":
    VideoRepository.create_table()
    app = App()
    app.mainloop()
