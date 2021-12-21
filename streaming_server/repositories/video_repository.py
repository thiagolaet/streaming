import sqlite3
import repositories.constants as C
from helpers import dict_factory
from factories.video_factory import VideoFactory

class VideoRepository:

    @classmethod
    def create_table(cls):
        db = sqlite3.connect(C.DB_NAME)
        cursor = db.cursor()
        cursor.executescript(C.CREATE_TABLE_QUERY)
        db.close()

    @classmethod
    def insert(cls, video_name, video_format):
        db = sqlite3.connect(C.DB_NAME)
        cursor = db.cursor()
        cursor.execute(C.INSERT_QUERY, (video_name, video_format))
        id = cursor.lastrowid
        db.commit()
        db.close()
        return id

    @classmethod
    def delete(cls, video_id):
        db = sqlite3.connect(C.DB_NAME)
        cursor = db.cursor()
        cursor.execute(C.DELETE_QUERY, video_id)
        db.commit()
        db.close()

    @classmethod
    def get_all_videos(cls):
        db = sqlite3.connect(C.DB_NAME)
        db.row_factory = dict_factory
        cursor = db.cursor()
        cursor.execute(C.SELECT_ALL_QUERY)
        result = cursor.fetchall()
        videos = []
        for video in result:
            videos.append(VideoFactory.build_from_dict(video))
        db.close()
        return videos

    @classmethod
    def get_videos_by_name(cls, name):
        db = sqlite3.connect(C.DB_NAME)
        db.row_factory = dict_factory
        cursor = db.cursor()
        result = cursor.execute(C.SELECT_BY_NAME_QUERY, (f'%{name}%',))
        videos = []
        for video in result:
            videos.append(VideoFactory.build_from_dict(video))
        db.close()
        return videos

    @classmethod
    def get_video_by_id(cls, id):
        db = sqlite3.connect(C.DB_NAME)
        db.row_factory = dict_factory
        cursor = db.cursor()
        result = cursor.execute(C.SELECT_BY_ID_QUERY, (id,))
        videos = []
        for video in result:
            videos.append(VideoFactory.build_from_dict(video))
        db.close()
        return videos[0]
