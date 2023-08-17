from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from download_from_youtube import download_yt_video

def cut_video(video_path, start_time: int = 20, end_time: int = 35, save_path='./videos/clipped_video.mp4'):
    """
    This function cuts a video from a start time to an end time and saves it in the specified path
    start_time: int
    end_time: int
    save_path: str
    """
    ffmpeg_extract_subclip(video_path, start_time, end_time, targetname=save_path)

#TODO: Add an if to ask if the video is already downloaded or you want to download it from YouTube
# Uncomment the following line to download a video from YouTube and cut it
# download_video = download_yt_video()
cut_video('videos/clipped_video_out.mp4', 0, 20)
