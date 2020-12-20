from serial.serialutil import Timeout
import serial
try:
    portx="COM2"
    bps=115200
    timex=1
    ser=serial.Serial(portx,bps)

    print("串口信息: "+"\n已连接串口: "+str(ser.port)+" 波特率: "+str(ser.baudrate))
    text="hello world"
    result=ser.write(text.encode("utf-8"))
    result+=ser.write("\r\n".encode("utf-8"))
    print("写总字节数: ",result)
    result=ser.readline().decode("utf-8")
    print("\n已收到:"+result)
        
    ser.close()

except Exception as e:
    print("error: ",e)