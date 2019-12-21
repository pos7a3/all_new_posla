import numpy as np
import cv2

# 차선 인식, 물체 인식 시 필요한 모듈 import
import object_detection
from lane_detection import Lane_Detection


class CollectTrainingData(object):
    def __init__(self, client, steer):
        self.client = client
        self.steer = steer
        
        self.dect = object_detection.Object_Detection(self.steer)
        self.lane_follower = Lane_Detection(steer)

    def collect(self):
        print("Start video stream")
        stream_bytes = b' '

        while True:
            stream_bytes += self.client.recv(1024)
            first = stream_bytes.find(b'\xff\xd8')
            last = stream_bytes.find(b'\xff\xd9')

            if first != -1 and last != -1:
                try:
                    jpg = stream_bytes[first:last + 2]
                    stream_bytes = stream_bytes[last + 2:]

                    # 수신한 이미지 프레임을 2장으로 복사하여 하나는 lane detection, 나머지 하나는 object detection에 사용
                    image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                    image_2 = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

                    image = self.lane_follower.follow_lane(image)
                    cv2.imshow('Lane Lines', image)

                    self.dect.detection(image_2)

                    self.steer.Control()
                except:
                    continue

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
