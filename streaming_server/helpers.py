
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_videos_as_dict_list(name):
    from repositories.video_repository import VideoRepository
    if name:
        videos = VideoRepository.get_videos_by_name(name)
    else:
        videos = VideoRepository.get_all_videos()
    return [video.__dict__ for video in videos]

# def play_video(video_id):
#     from repositories.video_repository import VideoRepository
#     video = VideoRepository.get_video_by_id(video_id)
#     import ipdb; ipdb.set_trace()
