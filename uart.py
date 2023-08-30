import serial,time,codecs

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.flush()


class Autriger():
    
    def initialization(self):
        self.com('1\n','Initialization')
    
    def extend(self):
        result = self.com('2\n','Extend')
        return(result)

    def align(self):
        self.com('3\n','Align')
    
    def revert(self):
        result = self.com('4\n','Revert')
        return(result)
        
    def returned(self,line) :
        if line == "1":
            return (' OK')
        elif line != '1':
            return (' ERROR')
    
    def com (self, point, com_name) :
        ser.write(point.encode ('utf-8'))
        flag = False
        while(flag != True) :
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                flag = True
            return (com_name + self.returned(line))


robot = Autriger()
time.sleep(2)# не забыть

robot.revert()