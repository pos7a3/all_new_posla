import ultrasonic_avoidance
import time

UA = altrasonic_avoidance.Ultrasonic_Avoidance(20)


class UltraSonic(object):
    def run(self, server):
        while True:
            distance = UA.get_distance()
            if distance != -1:
                # print('distance', distance, 'cm')
                server.Send_Data(str(distance).encode())
                time.sleep(0.1)
            else:
                print(False)
