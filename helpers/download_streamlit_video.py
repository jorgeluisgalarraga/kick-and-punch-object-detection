import base64


def get_video_download_link(video_path, download_name):
    with open(video_path, 'rb') as f:
        video_binary = f.read()
    b64 = base64.b64encode(video_binary).decode()
    href = f'<a href="data:video/mp4;base64,{b64}" download="{download_name}">Download Processed Video</a>'
    return href