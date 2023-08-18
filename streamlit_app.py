import streamlit as st
from helpers.rep_inference_video import reproduce_video
from helpers.download_streamlit_video import get_video_download_link
import base64

# Set the background of the app
def set_background(image_file):
    """
    This function sets the background of a Streamlit app to an image specified by the given image file.

    Parameters:
        image_file (str): The path to the image file to be used as the background.

    Returns:
        None
    """
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
            background-transparency: 0.1;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def main():
    st.title(":red[Kick and Punch detector with YoloV8]")
    
    # Upload the video
    video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
    
    if video_file is not None:
        st.video(video_file)

        # Call the reproduce_video function on button click
        if st.button("Process Video"):
            path_model = './model_data/best.pt'
            processed_video_path = reproduce_video(path_model, video_file)
            st.video(processed_video_path)  # Play the processed video

            # Download the processed video
            st.markdown(get_video_download_link(processed_video_path, 'processed_video.mp4'), unsafe_allow_html=True)


if __name__ == "__main__":
    set_background('./images/bg.jpg')
    main()