import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime

class VideosListFrame(tk.Frame):
    def __init__(self, master):
        self.padding = {'padx': 5, 'pady': 5}
        self.master = master
        self.frame = tk.LabelFrame(self.master, text='Vídeos', **self.padding)

    def render_list(self, data):
        self.clear_frame()
        if not data:
            label = tk.Label(self.frame, text='Nenhum vídeo encontrado.', **self.padding)
            label.pack()
        else:
            # scrollbar
            y_scrollbar = Scrollbar(self.frame)
            y_scrollbar.pack(side=RIGHT, fill=Y)

            # table
            list = ttk.Treeview(self.frame)
            list['columns'] = ('id', 'title', 'video_format', 'views', 'uploaded_at')

            list.column("#0", width=0,  stretch=NO)
            list.column("id",anchor=CENTER, width=30)
            list.column("title",anchor=CENTER, width=220)
            list.column("video_format",anchor=CENTER,width=70)
            list.column("views",anchor=CENTER,width=84)
            list.column("uploaded_at",anchor=CENTER,width=124)

            list.heading("#0",text="",anchor=CENTER)
            list.heading("id",text="Id",anchor=CENTER)
            list.heading("title",text="Título",anchor=CENTER)
            list.heading("video_format",text="Formato",anchor=CENTER)
            list.heading("views",text="Visualizações",anchor=CENTER)
            list.heading("uploaded_at",text="Data de upload",anchor=CENTER)
            list.pack()

            label = tk.Label(self.frame, text='* os horários mostrados na tabela estão no fuso horário UTC', **self.padding)
            label.pack()

            for video in data:
                list.insert(parent='',index='end',iid=video.id,text='',
                values=(video.id, video.name, video.video_format, video.views, datetime.strptime(video.uploaded_at, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')))

        self.frame.grid(row=1, column=0, columnspan=2)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
