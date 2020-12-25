'''
串口通信
'''
import sensor, image, time, ustruct
from pyb import USB_VCP

usb = USB_VCP()
sensor.reset()                      # 复位并初始化感光元件。
sensor.set_pixformat(sensor.RGB565) # 设置像素格式为RGB565(或GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # 将图像大小设置为QVGA (320x240)
sensor.skip_frames(time = 2000)     # 等待设置生效。

while(True):
    test='hi\r\n'
    usb.send(test)
    time.sleep(1000)