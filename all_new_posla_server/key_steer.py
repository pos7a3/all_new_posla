import server_socket
import threading

import pygame
from pygame.locals import *

import time


class KeySteer(object):

    def __init__(self, host, port):
        self.socket = server_socket.Server(host, port)
        self.client = self.socket.Get_Client()
        self.send_inst = True

        pygame.init()
        pygame.display.set_mode((250, 250))
        pygame.key.set_repeat(True)

    def Steer(self):
        while self.send_inst:
            # get input from human driver
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    key_input = pygame.key.get_pressed()
                    # complex orders
                    if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
                        print("Forward Right")
                        self.client.send('d'.encode())
                        time.sleep(0.1)

                    elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
                        print("Forward Left")
                        self.client.send('a'.encode())
                        time.sleep(0.1)

                    elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
                        print("Reverse Right")
                        self.client.send('c'.encode())
                        time.sleep(0.1)

                    elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
                        print("Reverse Left")
                        self.client.send('z'.encode())
                        time.sleep(0.1)

                    # simple orders
                    if key_input[pygame.K_UP]:
                        print("Forward")
                        self.client.send('w'.encode())
                        time.sleep(0.1)

                    elif key_input[pygame.K_DOWN]:
                        print("Reverse")
                        self.client.send('x'.encode())
                        time.sleep(0.1)

                    elif key_input[pygame.K_RIGHT]:
                        print("Right")
                        self.client.send('d'.encode())
                        time.sleep(0.1)

                    elif key_input[pygame.K_LEFT]:
                        print("Left")
                        self.client.send('a'.encode())
                        time.sleep(0.1)

                    elif key_input[pygame.K_q]:
                        print("exit")
                        self.send_inst = False
                        self.client.send('q'.encode())
                        self.client.close()
                        break

                else:  # key up
                    self.client.send('s'.encode())
                    time.sleep(0.1)

    def Run(self):
        mic_thread = threading.Thread(target=self.Steer, args=())
        mic_thread.start()
