from pydarknet import Detector, Image
import cv2

import server_steer


class Object_Detection(object):
    def __init__(self, steer):

        self.steer = steer

        # Detection 및 Classification에 사용할 모델 구조(cfg), 학습한 가중치 결과(weights), label 분류 파일(data) 파일을
        # Detector의 매개변수로 지정한다.
        self.net = Detector(bytes("./yolo/cfg/yolo-obj.cfg", encoding="utf-8"),
                            bytes("./yolo/cfg/yolo-obj_400.weights", encoding="utf-8"),
                            0,
                            bytes("./yolo/obj.data", encoding="utf-8"))

    def detection(self, img):
        results = self.net.detect(Image(img))       
       
        detect_list = []

        for cat, score, bounds in results:
            x, y, w, h = bounds
            cv2.rectangle(img, 
                          (int(x - w / 2), int(y - h / 2)), 
                          (int(x + w / 2), int(y + h / 2)), 
                          (255, 0, 0), 
                          thickness=2)
            cv2.putText(img, 
                        str(cat.decode("utf-8")), 
                        (int(x - w / 2), int(y + h / 4)), 
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
            detect_list.append(cat.decode())

        cv2.imshow('dect', img)

        self.steer.Set_ObjectDetection(detect_list)
