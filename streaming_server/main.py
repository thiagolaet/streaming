import tkinter as tk
from frames.insert_video_frame import InsertVideoFrame
from daos.video_dao import VideoDao

def list_videos():
    print('list_videos')

def add_videos():
    insert_window = tk.Toplevel(root)
    insert_window.title('Novo vídeo')
    InsertVideoFrame(insert_window)

def remove_videos():
    print('remove_videos')

VideoDao.create_table()
root = tk.Tk()
root.title('Streaming server')
frame = tk.LabelFrame(root, text="Gerenciamento de vídeos", padx=15, pady=15)
frame.pack(padx=10, pady=10)
list_videos_button = tk.Button(frame, text="Listar vídeos", width=30, height=2, command=list_videos)
list_videos_button.pack(pady=3)
add_videos_button = tk.Button(frame, text="Adicionar vídeo", width=30, height=2, command=add_videos)
add_videos_button.pack(pady=3)
remove_videos_button = tk.Button(frame, text="Remover vídeo", width=30, height=2, command=remove_videos)
remove_videos_button.pack(pady=3)
root.mainloop()
