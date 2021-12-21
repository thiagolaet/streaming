
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_videos_list(name):
    from repositories.video_repository import VideoRepository
    if name:
        return VideoRepository.get_videos_by_name(name)
    return VideoRepository.get_all_videos()
