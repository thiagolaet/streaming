import tkinter as tk
from tkinter import *
from frames import InsertVideoFrame, ListVideosFrame
from repositories.video_repository import VideoRepository

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        VideoRepository.create_table()
        self.title("Streaming Server")
        self.search_var = StringVar()
        self.create_widgets()

    def create_widgets(self):
        search_frame = Frame(self, padx=15, pady=15)
        search_frame.grid(row=0, column=1, padx=10, pady=10)
        ListVideosFrame(search_frame)

if __name__ == "__main__":
    app = App()
    app.mainloop()
