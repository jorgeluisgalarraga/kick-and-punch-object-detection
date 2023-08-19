import cv2
from ultralytics import YOLO
#from helpers.rep_inference_video import reproduce_video


# # Load a pretrained YOLOv8n model
model = YOLO('./model_data/best.pt')
# cut_video(download_path)
# # Run inference on 'bus.jpg' with arguments
model.predict('./videos/clipped_video.mp4', save=True ,conf=0.65)

# print(results.plot())
# reproduce_video('./runs/detect/train22/weights/best.pt', './videos/short_video.mp4')
# --------------------------------------------------



# import streamlit as st
# from PIL import Image
# import base64

# from ultralytics import YOLO

# # Load the Yolo Model
# model = YOLO('./runs/classify/train7/weights/best.pt')  # load a custom model

# def set_background(image_file):
#     """
#     This function sets the background of a Streamlit app to an image specified by the given image file.

#     Parameters:
#         image_file (str): The path to the image file to be used as the background.

#     Returns:
#         None
#     """
#     with open(image_file, "rb") as f:
#         img_data = f.read()
#     b64_encoded = base64.b64encode(img_data).decode()
#     style = f"""
#         <style>
#         .stApp {{
#             background-image: url(data:image/png;base64,{b64_encoded});
#             background-size: cover;
#             background-transparency: 0.1;
#         }}
#         </style>
#     """
#     st.markdown(style, unsafe_allow_html=True)


# def predict(image):
#     image = Image.open(image)
#     results = model(image)
#     probs = results[0].probs.data.tolist()
#     names = results[0].names

#     # Create a dictionary mapping class labels to probabilities
#     prob_dict = {names[i]: prob for i, prob in enumerate(probs)}

#     # Find the class with the highest probability
#     max_class = max(prob_dict, key=prob_dict.get)
#     max_prob = prob_dict[max_class]

#     # st.subheader('Predicted class:')
#     # st.write(f'**{(max_class).capitalize()}** with a probability of {max_prob: .3f}')
#     return max_class, max_prob

# set_background('./images/bg.jpg')


# st.title(":red[Kick and Punch Classifier with YoloV8]")

# col1, col2 = st.columns(2)

# uploaded_file = st.file_uploader(":red[Choose an image...]", type=["jpg", "jpeg", "png"])


# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     max_class, max_prob = predict(uploaded_file)
#     new_image = image.resize((300, 300))
#     with col1:
#         st.write("")
#         st.image(new_image, use_column_width=False)
#         st.write(f':red[This a {(max_class).capitalize()}!]')
#     with col2:
#         # predict(uploaded_file)
#         st.subheader(':red[Predicted class:]')
#         st.write(f':red[**{(max_class).capitalize()}** with a probability of {max_prob: .3f}]')
    