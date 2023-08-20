from pytube import YouTube

# Download a video from YouTube
def download_yt_video():
    video_url = input("Enter the video URL: ")
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()  # Gets the first mp4 stream available
    # Download the video in the specific folder, that if it's not already there, it will be create
    download_path = stream.download(output_path='videos')  
    print(f"Video downloaded at {download_path}")
    return download_path

download_yt_video()