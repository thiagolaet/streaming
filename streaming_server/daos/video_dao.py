import sqlite3
import daos.constants as C

class VideoDao:

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
