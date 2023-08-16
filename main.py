from ultralytics import YOLO

# Load a model yolov8n means nano and it's the lightest
# model = YOLO("yolov8s.yaml")  # Uncomment this if you want to build a new model from scratch
# model = YOLO("./runs/detect/train11-augmantated/weights/best.pt")  # load a pretrained model (recommended for training)
model = YOLO("./runs/detect/train22/weights/last.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="./data-fixed-augmentated/data.yaml", epochs=20)  # train the model
