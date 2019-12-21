import server_video
import server_ultra
import server_microphone
import server_steer
import server_socket

# 트랙 학습 시 차량 수동 조작 시 import
# import key_steer

if __name__ == '__main__':
    # host, port
    # 호스트 서버 PC의 ip 주소와 임의의 포트 번호를 지정한다.
    host, port = "192.168.0.40", 1971

    client = server_socket.Server(host, port)

    steer = server_steer.Steer(client.Get_Client())

    # 멀티 스레드를 통해 초음파 및 STT 데이터 병렬 수신 및 차량 제어
    ultrasonic_object = server_ultra.UltraSonic(host, port + 1, steer)
    ultrasonic_object.Run()

    microphone_object = server_microphone.Microphone(host, port + 2, steer)
    microphone_object.Run()

    # 필요 시 차량 수동 조작
    # key_steer = key_steer.KeySteer(host, port + 3)
    # key_steer.Run()

    # loop를 통해 Client에서 이미지 프레임 수신 및 차량 제어
    video_object = server_video.CollectTrainingData(client.Get_Client(), steer)
    video_object.collect()
