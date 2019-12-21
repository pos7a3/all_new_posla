import logging
import picar
from picar import front_wheels
from picar import back_wheels

import playmusic
import time

DELAY = 0.01
DEFAULT_SPEED = 60


class Serial(object):
    def __init__(self):
        self.music = playmusic.MUSIC()
        
        self.steer_count = 0

        """ Init camera and wheels"""
        logging.info('Creating a DeepPiCar...')

        picar.setup()

        logging.debug('Set up back wheels')
        self.fw = front_wheels.Front_Wheels(db='config')
        self.bw = back_wheels.Back_Wheels(db='config')
        self.bw.speed = DEFAULT_SPEED

    def steer(self, data):
        if data.isdecimal():
            data = int(data) + 45
            print(data)
            if self.steer_count == 3:

                self.fw.turn(data)
                # if data < 60 or data > 120 :  # sharp turning left / right
                #    self.bw.speed = int(DEFAULT_SPEED * 0.7)
                # else:  # angle between 60~120
                #    self.bw.speed = DEFAULT_SPEED              
                # self.bw.speed = DEFAULT_SPEED
                self.steer_count = 0
                time.sleep(0.01)
            else:
                self.steer_count += 1
        
        if data == 'lo':
            self.music.play_music('./sounds/limit30.mp3')
            self.bw.speed = 40

        if data == 'lf':
            # self.bw.forward()
            # self.fw.turn(45)
            self.music.play_music('./sounds/turn_left.mp3')
            # time.sleep(DELAY)
            
        if (data == 'w') or (data == 'lw') or (data == 'ww'):
            logging.info('Starting to drive at speed %s...' % 50)
            self.bw.speed = DEFAULT_SPEED
            self.bw.forward()
            if data == 'lw':
                self.music.play_music('./sounds/go.mp3')
                
        elif data == 'x':
            self.bw.speed = DEFAULT_SPEED
            self.bw.backward()
            
        elif data == 'a':
            self.bw.forward()
            self.fw.turn(45)
            
        elif (data == 'd') or (data == 'td'):
            self.bw.forward()
            self.fw.turn(135)
            # for i in range(90, 136):
            #    self.fw.turn(i)
            #    time.sleep(DELAY)
            if data == 'td':
                self.music.play_music('./sounds/turn_right.mp3')
                
        elif data == 'z':
            self.bw.backward()
            self.fw.turn(45)
            
        elif data == 'c':
            self.bw.backward()
            self.fw.turn(135)
            
        elif (data == 's') or (data == 'us') or (data == 'ls') or (data == 'as') or (data == 'lass'):
            self.bw.stop()
            if data == 's':
                self.music.play_music('./sounds/stop.mp3')
            elif data == 'us':
                self.music.play_music('./sounds/obs_stop.mp3')
            elif data == 'ls':
                self.music.play_music('./sounds/light_stop.mp3')
            elif data == 'as':
                self.music.play_music('./sounds/lasso_stop.mp3')
