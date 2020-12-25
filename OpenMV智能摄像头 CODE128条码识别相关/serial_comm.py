#-*- coding : utf-8-*-
from serial.serialutil import Timeout
import serial
try:
    portx="COM5"
    bps=115200
    timex=1
    ser=serial.Serial(portx,bps)

    print("串口信息: "+"\n已连接串口: "+str(ser.port)+" 波特率: "+str(ser.baudrate))
    while(1):
        result=ser.readline().decode("utf-8")
        print("\n已收到:"+result)
        
    ser.close()

except Exception as e:
    pass
