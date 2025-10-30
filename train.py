import os
from ultralytics import YOLO

if __name__ == '__main__':

    model_orin = r'E:\Github\yolo\\ultralytics\cfg\models\\v8\yolov8s-cls.yaml'
    model_SPAM = r'C:\Users\44724\Desktop\SPAYOLO\ultralytics\cfg\models\v8\yolov8s-cls-spam.yaml'


    fer13 = r'E:\Github\YoloV8\data\fer13'
    affectnet = r'E:\Github\YoloV8\data\affectnet'

    model_yaml = model_SPAM
    model = YOLO(model_yaml)
    data_path = affectnet

    name = os.path.basename(model_yaml).split('.')[0]

    model.train(data=data_path,
                imgsz=224,
                epochs=200,
                batch=128,
                workers=4,        # 加载数据线程数
                device='cuda',
                optimizer='Adan',  # 'SGD', 'AdaBoB'
                project='runs/train',
                name=name,
                )
