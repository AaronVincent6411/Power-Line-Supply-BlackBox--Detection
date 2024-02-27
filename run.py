from ultralytics import YOLO

model = YOLO('best.pt')

results = model.track(source="/home/lionex/Videos/DJI_0103.MOV", show=True)