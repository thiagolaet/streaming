from domain.video import Video

class VideoFactory:

    @classmethod
    def build_from_dict(cls, data):
        return Video(data)
