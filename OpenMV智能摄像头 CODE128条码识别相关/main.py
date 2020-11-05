import sensor, image, time, math,pyb
from pyb import LED
blue_led  = LED(3)
green_led = LED(2)

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.VGA)
sensor.set_windowing((640, 80))
sensor.skip_frames(30)
sensor.set_auto_gain(True)
sensor.set_auto_whitebal(True)
sensor.set_auto_exposure(True)
sensor.set_vflip(True)
sensor.set_hmirror(True)
clock = time.clock()
temp=''
result=[]
def barcode_name(code):
    if(code.type() == image.EAN2):
        return "EAN2"
    if(code.type() == image.EAN5):
        return "EAN5"
    if(code.type() == image.EAN8):
        return "EAN8"
    if(code.type() == image.UPCE):
        return "UPCE"
    if(code.type() == image.ISBN10):
        return "ISBN10"
    if(code.type() == image.UPCA):
        return "UPCA"
    if(code.type() == image.EAN13):
        return "EAN13"
    if(code.type() == image.ISBN13):
        return "ISBN13"
    if(code.type() == image.I25):
        return "I25"
    if(code.type() == image.DATABAR):
        return "DATABAR"
    if(code.type() == image.DATABAR_EXP):
        return "DATABAR_EXP"
    if(code.type() == image.CODABAR):
        return "CODABAR"
    if(code.type() == image.CODE39):
        return "CODE39"
    if(code.type() == image.PDF417):
        return "PDF417"
    if(code.type() == image.CODE93):
        return "CODE93"
    if(code.type() == image.CODE128):
        return "CODE128"
while(True):
    clock.tick()
    blue_led.on()
    img = sensor.snapshot()
    codes = img.find_barcodes()
    for code in codes:
        img.draw_rectangle(code.rect())
        print(result)
        if temp!=code.payload():
            temp=code.payload()
            result.append(code.payload())
            green_led.on()
            time.sleep(100)
            green_led.off()
            with open('result.txt','w') as f:
                f.write(temp)
            time.sleep(150)
            pyb.hard_reset()
    if not codes:
        pass
