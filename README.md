# kick-and-punch-object-detection

To execute the app, most of the commands are run from the root folder in your command line.

## Run the app locally

- Open your terminal and type:
``streamlit run streamlit_app.py``

## Docker image

- In case you want to run some experiments with the Docker container, you need to build your image being in the root folder:
``docker build -t kick-punch-detector:latest .``

- Then, run the kick and punch detector image:
``docker run -p 8501:8501 kick-punch-detector``

- If you want to visualize how many images, you can do: ``docker images``

- In order to remove the image, run the following command by addin the ID CONTAINER: ``docker rmi -f <ID CONTAINER>``

- Next, in order to clean some space: ``docker system prune``

### Test the app

In the */videos* folder are some videos if you want to try the app and you don't have any video locally.

## Dataset

Our dataset can be found at [Kick and Punch object detector dataset](https://universe.roboflow.com/georgebrown/kick-and-punch-object-detection)
