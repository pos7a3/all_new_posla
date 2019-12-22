# all_new_posla/Lamporghini

[![Lamporghini](http://img.youtube.com/vi/w62PZlp24T4/0.jpg)](https://www.youtube.com/watch?v=w62PZlp24T4 "Lamporghini")

라즈베리파이 기반의 교육용 RC카 키트에 lane detection(openCV), object detection(Yolo v3), 음성인식(Google STT API), 장애물 인식(Ultrasonic sensor) 기능을 추가하여 자율주행을 구현한 프로젝트 입니다. 


## Period
19.08.19 ~ 12.09.19 (약 5주)

## Environment
- Server PC
  - Ubuntu
  - intel Xeon
  - 64gb ddr4
  - gtx2080 sli
  
- Client PC
  - Raspberry Pi 3 B+ ( With Camera Module, usb mic, speaker)
  - raspbian
  
- RC Kit
  - [SunFounder PiCar-S kit]  [ [manual] ]
  
## How To Use
1. server 프로젝트는 server PC에, client 프로젝트는 client PC에 각각 다운받습니다.
1. 필요한 패키지를 설치합니다.
  - server
    - openCV
    - [pydarknet]
  - client
    - pygame
    - [picar]
    - [pycar-S]
    - google STT API
1. server pc에서 장애물 및 표지판 등 물체로 인식할 이미지들을 yolo로 학습시킨 후 생성된 .weights 파일과 .cfg, .data파일들을 yolo 디렉터리에 복사합니다.
1. server pc의 IP 주소를 server의 rc_driver_main의 코드와 client의 main의 코드에서 수정한 후 두 파일을 실행시킵니다.

[pydarknet]: https://github.com/gy20073/pydarknet
[SunFounder PiCar-S kit]: https://www.sunfounder.com/picar-s-kit.html
[manual]: https://www.sunfounder.com/learn/download/UGlDYXItU19Vc2VyX01hbnVhbC5wZGY=/dispi

[picar]: https://github.com/sunfounder/SunFounder_PiCar
[pycar-S]: https://github.com/sunfounder/SunFounder_PiCar-S

## 참고 사이트
- https://github.com/hamuchiwa/AutoRCCar
- https://towardsdatascience.com/deeppicar-part-4-lane-following-via-opencv-737dd9e47c96
