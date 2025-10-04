import cv2

cameraCapture = cv2.VideoCapture(0)
fps = 30  # an assumption

size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter("MyOutputVid.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
