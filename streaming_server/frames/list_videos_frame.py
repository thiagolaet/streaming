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
        self.create_widgets()
        self.videos_list_frame = VideosListFrame(self.frame)

    def create_widgets(self):
        self.frame.pack()
        name_entry = Entry(self.frame, textvariable=self.name_var, width=60)
        name_entry.grid(column=0, row=0, **self.padding)
        name_entry.focus()
        search_video_button = Button(self.frame, text="Buscar", width=12, height=1, command=self.search_videos)
        search_video_button.grid(column=1, row=0, **self.padding)

    def search_videos(self):
        search_name = self.name_var.get()
        if (search_name):
            videos = VideoRepository.get_videos_by_name(search_name)
        else:
            videos = VideoRepository.get_all_videos()
        self.videos_list_frame.render_list(videos)

    def close(self):
        self.master.destroy()
