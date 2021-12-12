class Video:

    def __init__(self, video):
        self.id = video.get('id')
        self.name = video.get('name')
        self.video_format = video.get('video_format')
        self.views = video.get('views')
        self.uploaded_at = video.get('uploaded_at')
