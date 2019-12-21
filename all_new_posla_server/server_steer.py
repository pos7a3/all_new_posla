import server_socket


class Steer(object):

    def __init__(self, client):
        self.client = client
        self.ultrasonic = 9999
        self.microphone = 'NONE'
        self.line = 90
        self.obj_list = []
        self.state = 'NONE'
        self.speed = '0'
        self.light_signal = 'NONE'
        self.obs = 'NO'
        self.stoptime = 0
        
    def Set_UltraSonic(self, ultra):
        if int(ultra) > 500:
            return
        self.ultrasonic = int(ultra)

    def Set_Microphone(self, mic):
        self.microphone = mic

    def Set_Line(self, line):
        self.line = line

    def Set_ObjectDetection(self, obj):
        self.obj_list = obj

    def ultrasonic_process(self, ultra):
        if ultra < 7:
            return 's' 
        else:
            return 'w'

    def mic_process(self, speech):
        if (speech == '정지') or (speech == '멈춰') or (speech == '멈추라고'):
            return 's'  
        elif (speech == '가') or (speech == '가라고') or (speech == '출발'):
            return 'w'
        else:
            return ''

    def Control(self):
        mic_comm = self.mic_process(self.microphone)
        us_comm = self.ultrasonic_process(self.ultrasonic)

        # os.system('cls' if os.name == 'nt' else 'clear')
        # print('속도 : ', self.speed)
        # print('조향각 : ', str(self.line))
        # print('상태 : ', self.state)
        # print('전방 거리 : ', self.ultrasonic)
        # print('신호 명령 : ', self.light_signal)
        # print('음성 명령 : ', self.microphone)
        # print('정지 명령 : ', self.stopline)
        # print('장애물 : ', self.obs)

        # speed limit
        if 'slow' in self.obj_list:
            if self.speed != '30':
                self.client.send('slow'.encode())
                self.speed = '30'
                print('제한속도 : 30')

        if mic_comm == 'w':
            if self.state == 'STOP' and self.obs == 'NO':
                self.client.send('lw'.encode())
                self.state = 'DRIVE'
                print('MIC_GO')

        elif mic_comm == 's':
            if self.state == 'DRIVE':
                self.client.send('s'.encode())
                self.state = 'STOP'
                print('MIC_STOP')

        elif us_comm == 'w':
            if self.light_signal == 'DRIVE' and self.obs == 'YES':
                self.obs = 'NO'
                self.state = 'DRIVE'
                self.client.send('w'.encode())
                print('US_GO')

        elif us_comm == 's':
            if self.obs == 'NO':
                self.client.send('us'.encode())
                self.obs = 'YES'
                self.state = 'STOP'
                print('US_STOP')

        # if (self.light_signal == 'LIGHT_STOP') and ('greenlight' in self.obj_list):
        # if self.light_signal == 'LIGHT_STOP':
        #     self.light_signal = 'DRIVE'
        #     self.state = 'DRIVE'
        #     self.client.send('lw'.encode())
        #     print('GO')
            
        # driving                              
        if self.light_signal == 'DRIVE':
            if self.state == 'STOP':
                self.state = 'DRIVE'

                if self.line < 45:
                    self.client.send("0".encode())
                elif self.line < 135:
                    self.client.send(str(self.line - 45).encode())
                else:
                    self.client.send("90".encode())

        self.microphone = ''
