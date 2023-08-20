# Use an official Python runtime as the base image
FROM python:3.9-slim


# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libxcb-xinerama0 \
    libxkbcommon-x11-0 \
    libsm6 \
    && rm -rf /var/lib/apt/lists/* 

# Copy the current directory contents into the container at /app
COPY . /app

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run on container start
CMD ["streamlit", "run", "streamlit_app.py"]