import serial

class PongBot:
    def __init__(self):
        connected = False
        port = 0
        while not connected:
            if port > 10:
                raise RuntimeError("serial connection to Arduino failed")
            try:
                self.serialConnection = serial.Serial('/dev/ttyACM{}'.format(port), 9600, timeout=0)
                connected = True
            except Exception as e:
                connected = False
                port += 1
        print('Arduino connected to port {}'.format(port))

    def _stringtobinary(self, s):
        return bytes(s, "ascii")

    def shoot(self):
        self.serialConnection.write(self._stringtobinary('1'))

    def left(self):
        self.serialConnection.write(self._stringtobinary('2'))

    def right(self):
        self.serialConnection.write(self._stringtobinary('3'))

