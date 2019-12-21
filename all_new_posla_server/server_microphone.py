import server_socket
import threading
import time


class Microphone(object):

    def __init__(self, host, port, steer):
        self.steer = steer
        self.socket = server_socket.Server(host, port)
        self.client = self.socket.Get_Client()

    def Recv(self):
        while True:
            speech = self.client.recv(128).decode()
            print('speech', speech)
            self.steer.Set_Microphone(speech)
            time.sleep(0.1)

            if 0xFF == ord('q'):
                break
    
    def Run(self) :
        mic_thread = threading.Thread(target=self.Recv, args=())
        mic_thread.start()
