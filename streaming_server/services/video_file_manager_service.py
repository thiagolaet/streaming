from constants import VIDEOS_PATH
from shutil import copyfile

class VideoFileManagerService:

    @classmethod
    def copy_file(cls, path, filename):
        copyfile(path, f'{VIDEOS_PATH}/{filename}')
