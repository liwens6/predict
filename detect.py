from ultralytics import YOLO
 
if __name__=="__main__":
    
    pth_path=r"2024年校赛数据集\predict\chip.pt"
 
    test_path=r"2024年校赛数据集\predict\image\031.jpg"
    # Load a model
    #model = YOLO('yolov8n.pt')  # load an official model
    model = YOLO(pth_path)  # load a custom model
 
    # Predict with the model
    results = model.predict(test_path,save=True,conf=0.5)  # predict on an image

    pth_path=r"2024年校赛数据集\predict\cola.pt"
 
    test_path=r"runs\detect\predict\031.jpg"
    # Load a model
    #model = YOLO('yolov8n.pt')  # load an official model
    model = YOLO(pth_path)  # load a custom model
 
    # Predict with the model
    results = model.predict(test_path,save=True,conf=0.5)  # predict on an image

    pth_path=r"2024年校赛数据集\predict\cookie.pt"
 
    test_path=r"runs\detect\predict2\031.jpg"
    # Load a model
    #model = YOLO('yolov8n.pt')  # load an official model
    model = YOLO(pth_path)  # load a custom model
 
    # Predict with the model
    results = model.predict(test_path,save=True,conf=0.5)  # predict on an image

    pth_path=r"2024年校赛数据集\predict\fan.pt"
 
    test_path=r"runs\detect\predict3\031.jpg"
    # Load a model
    #model = YOLO('yolov8n.pt')  # load an official model
    model = YOLO(pth_path)  # load a custom model
 
    # Predict with the model
    results = model.predict(test_path,save=True,conf=0.5)  # predict on an image

    pth_path=r"2024年校赛数据集\predict\lays.pt"
 
    test_path=r"runs\detect\predict4\031.jpg"
    # Load a model
    #model = YOLO('yolov8n.pt')  # load an official model
    model = YOLO(pth_path)  # load a custom model
 
    # Predict with the model
    results = model.predict(test_path,save=True,conf=0.5)  # predict on an image

    pth_path=r"2024年校赛数据集\predict\Nescafe.pt"
 
    test_path=r"runs\detect\predict5\031.jpg"
    # Load a model
    #model = YOLO('yolov8n.pt')  # load an official model
    model = YOLO(pth_path)  # load a custom model
 
    # Predict with the model
    results = model.predict(test_path,save=True,conf=0.5)  # predict on an image

    pth_path=r"2024年校赛数据集\predict\orange juice.pt"
 
    test_path=r"runs\detect\predict6\031.jpg"
    # Load a model
    #model = YOLO('yolov8n.pt')  # load an official model
    model = YOLO(pth_path)  # load a custom model
 
    # Predict with the model
    results = model.predict(test_path,save=True,conf=0.5)  # predict on an image

    pth_path=r"2024年校赛数据集\predict\sprite.pt"
 
    test_path=r"runs\detect\predict7\031.jpg"
    # Load a model
    #model = YOLO('yolov8n.pt')  # load an official model
    model = YOLO(pth_path)  # load a custom model
 
    # Predict with the model
    results = model.predict(test_path,save=True,conf=0.5)  # predict on an image

    pth_path=r"2024年校赛数据集\predict\water.pt"
 
    test_path=r"runs\detect\predict8\031.jpg"
    # Load a model
    #model = YOLO('yolov8n.pt')  # load an official model
    model = YOLO(pth_path)  # load a custom model
 
    # Predict with the model
    results = model.predict(test_path,save=True,conf=0.5)  # predict on an image

    pth_path=r"2024年校赛数据集\predict\Xiaoxiaosu.pt"
 
    test_path=r"runs\detect\predict9\031.jpg"
    # Load a model
    #model = YOLO('yolov8n.pt')  # load an official model
    model = YOLO(pth_path)  # load a custom model
 
    # Predict with the model
    results = model.predict(test_path,save=True,conf=0.5)  # predict on an image