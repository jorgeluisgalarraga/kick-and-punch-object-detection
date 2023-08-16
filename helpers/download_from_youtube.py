from pytube import YouTube

video_url = 'https://www.youtube.com/shorts/qLRq6AwFImA'
yt = YouTube(video_url)
stream = yt.streams.get_highest_resolution()  # Gets the first mp4 stream available
# Download the video in the specific folder, that if it's not already there, it will be create
download_path = stream.download(output_path='./extracted_f')  
print(f"Video downloaded at {download_path}")