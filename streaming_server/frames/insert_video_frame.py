import tkinter as tk
from tkinter import filedialog, Label, Button, Entry
from repositories.video_repository import VideoRepository
from services.video_file_manager_service import VideoFileManagerService

class InsertVideoFrame:

    def __init__(self, master):
        self.padding = {'padx': 5, 'pady': 5}
        self.master = master
        self.frame = tk.Frame(self.master, padx=5, pady=5)
        self.name_var = tk.StringVar()
        self.video_path = 'Nenhum vídeo selecionado'
        self.create_widgets()

    def create_widgets(self):
        Label(self.frame, text='Vídeo:').grid(column=0, row=0, **self.padding)
        self.video_name_output_label = Label(self.frame, text=self.video_path)
        self.video_name_output_label.grid(column=1, row=0, **self.padding)
        search_video_button = Button(self.frame, text="Buscar vídeo", width=16, height=1, command=self.select_videos)
        search_video_button.grid(column=1, row=1, **self.padding)
        Label(self.frame, text='Nome:').grid(column=0, row=2, **self.padding)
        name_entry = Entry(self.frame, textvariable=self.name_var)
        name_entry.grid(column=1, row=2, **self.padding)
        name_entry.focus()
        cancel_button = Button(self.frame, text="Cancelar", width=14, height=1, command=self.close)
        cancel_button.grid(column=0, row=3, **self.padding)
        confirm_button = Button(self.frame, text="Confirmar", width=14, height=1, command=self.submit)
        confirm_button.grid(column=1, row=3, **self.padding)
        self.frame.grid(**self.padding)

    def close(self):
        self.master.destroy()

    def select_videos(self):
         self.video_path = filedialog.askopenfilename(initialdir="/", title="Selecione os vídeos")
         self.frame.focus()
         self.video_name_output_label.config(text=self.video_path.split('/')[-1])

    def submit(self):
        video_name = self.name_var.get()
        video_format = self.video_path.split('.')[-1]
        video_id = VideoRepository.insert(video_name, video_format)
        filename = f"{video_id}_{video_name.replace(' ', '_')}.{video_format}".lower()
        VideoFileManagerService.copy_file(self.video_path, filename)
        self.close()
