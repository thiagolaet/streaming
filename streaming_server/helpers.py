import socket, cv2, pickle,struct, math, imutils
import constants as C


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

class FrameSegment(object):
  MAX_DGRAM = 2**16
  MAX_IMAGE_DGRAM = MAX_DGRAM - 64 # minus 64 bytes in case UDP frame overflown
  def __init__(self, sock, client_address):
    self.s = sock
    self.client_address = client_address
  def udp_frame(self, img):
    compress_img = cv2.imencode('.jpg', img)[1]
    dat = compress_img.tostring()
    size = len(dat)
    num_of_segments = math.ceil(size/(self.MAX_IMAGE_DGRAM))
    array_pos_start = 0

    while num_of_segments:
        array_pos_end = min(size, array_pos_start + self.MAX_IMAGE_DGRAM)
        self.s.sendto(
            struct.pack('B', num_of_segments) +
            dat[array_pos_start:array_pos_end],
            self.client_address
        )
        array_pos_start = array_pos_end
        num_of_segments -= 1

def play_video(socket, client_address, video_id, video_resolution):
    from repositories.video_repository import VideoRepository
    fs = FrameSegment(socket, client_address)
    video = VideoRepository.get_video_by_id(video_id)
    video_capture_data = cv2.VideoCapture(C.VIDEOS_PATH + f'/{video.id}_{video.name.replace(" ", "_")}.{video.video_format}')
    while (video_capture_data.isOpened()):
        __, frame = video_capture_data.read()
        frame = imutils.resize(frame, width=video_resolution)
        fs.udp_frame(frame)
    video_capture_data.release()
