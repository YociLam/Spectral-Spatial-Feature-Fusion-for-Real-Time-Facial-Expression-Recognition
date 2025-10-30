from ultralytics import YOLO

if __name__ == '__main__':
    # 模型路径
    model_pt = r''
    model = YOLO(model_pt)
    # 数据集路径
    data_path = r'E:\Github\YoloV8\data\fer13'

    model.val(data=data_path,
              imgsz=640,
              batch=4,
              workers=0,                # 加载数据线程数
              conf=0.001,               # 设置检测的最小置信度阈值。置信度低于此阈值的检测将被丢弃。
              iou=0.6,                  # 设置非最大抑制 (NMS) 的交叉重叠 (IoU) 阈值。有助于减少重复检测。
              device='cuda',
              project='runs/val',
              name='exp',
              )
