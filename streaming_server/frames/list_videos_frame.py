import tkinter as tk
from tkinter import *
from repositories.video_repository import VideoRepository
from frames.videos_list_frame import VideosListFrame

class ListVideosFrame(tk.Frame):

    def __init__(self, master):
        self.padding = {'padx': 5, 'pady': 5}
        self.master = master
        self.frame = tk.Frame(self.master, **self.padding)
        self.name_var = tk.StringVar()
        self.videos_list_frame = VideosListFrame(self.frame)
        self.create_widgets()
        self.is_remove_button_binded = False

    def create_widgets(self):
        self.frame.pack()
        name_entry = Entry(self.frame, textvariable=self.name_var, width=60)
        name_entry.grid(column=0, row=0, **self.padding)
        name_entry.focus()
        search_video_button = Button(self.frame, text="Buscar", width=12, height=1, command=self.search_videos)
        search_video_button.grid(column=1, row=0, **self.padding)
        self.remove_video_button = Button(self.frame, text="Remover", width=12, height=1, command=self.remove_videos, state="disabled")
        self.remove_video_button.grid(column=2, row=0, **self.padding)

    def activate_remove_video_button(self, e):
        # Caso o clique não tenha sido em nenhuma linha da lista, retorna
        if not e.widget.selection():
            return
        self.remove_video_button['state'] = "normal"
        self.remove_video_button.grid(column=2, row=0, **self.padding)

    def search_videos(self):
        search_name = self.name_var.get()
        if (search_name):
            videos = VideoRepository.get_videos_by_name(search_name)
        else:
            videos = VideoRepository.get_all_videos()
        self.videos_list_frame.render_list(videos)
        if videos and not self.is_remove_button_binded:
            self.videos_list_frame.list.bind('<ButtonRelease-1>', self.activate_remove_video_button)
            self.is_remove_button_binded = True

    def remove_videos(self):
        self.videos_list_frame.remove_videos()
        # Após remover os videos, desativa o botão de remover novamente, uma vez que os objetos selecionados não existem mais
        self.remove_video_button['state'] = "disabled"

    def close(self):
        self.master.destroy()
