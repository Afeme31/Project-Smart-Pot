import network
import utime
import ntptime
from machine import Pin , SoftSPI , sleep, TouchPad, ADC,reset, PWM
import ssd1306
import writer
import digital7_35
import ufirebase as firebase
from time import sleep
import dht
import framebuf
import UniNeue25
import ufirebase as firebase
import _thread
import connectwifi
import animasi
import tictactoe
import ujson
import urequests

#deklarasi telegram
token = "5808295847:AAE_ElPOBjrBYc20TiexCuX_0hzBxHUY2iI"
massage1 = """ WARNING!!!! your plant is dry, please water it immediately"""
id1 = "865215885"
id2 = "904089865"
urlchat = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+id2+"&text="+massage1


#deklarasi ADC
adc = ADC(Pin(34))
ldr = ADC(Pin(35))
buzzer = PWM(Pin(22))
buzzer.duty(0)

#deklarasi untuk lcd
spi = SoftSPI(baudrate=500000, polarity=1, phase=0, sck=Pin(15), mosi=Pin(2), miso=Pin(0))
dc = Pin(16)
rst = Pin(4)
cs = Pin(17)
but = Pin(2, Pin.IN)
lcd = ssd1306.SSD1306_SPI(128,64,spi,dc,rst,cs)
clock = writer.Writer(lcd,digital7_35)
lcd21 = writer.Writer(lcd,UniNeue25)

#deklarasi gambar/icon
iconsuhu = framebuf.FrameBuffer(bytearray(b"\x03\xc0\x07`\xfe \x06 \x06 ~ \x06 \x06 \x06\xa0\xfe\xa0\x06\xa0\x06\xa0\x06\xa0~\xa0\x06\xb0\x1c\x9c9\xcc7\xe6'\xf6g\xf6'\xf63\xec\x18\x1c\x0fx\x07\xe0"), 15, 25, framebuf.MONO_HLSB)
iconlembab = framebuf.FrameBuffer(bytearray(b'\x00\xc0\x00\x00\xe0\x00\x01\xe0\x00\x03\xf0\x00\x07\xf8\x00\x07\xf8\x00\x0f\xfc\x00\x1f\xfe\x00\x1f\xfe\x00?\xff\x00x\x7f\x80{w\x80\xf8g\xc0\xfc\xcf\xc0\xff\x9f\xc0\xff?\xc0\xfe\x7f\xc0\xfc\xcf\xc0\xf9\x87\xc0{\xb7\x80\x7f\xc7\x80?\xef\x00\x1f\xfe\x00\x0f\xfc\x00\x03\xf0\x00'), 18, 25, framebuf.MONO_HLSB)
iconderajat = framebuf.FrameBuffer(bytearray(b'x\xcc\x84\x84\xccx'), 6, 6, framebuf.MONO_HLSB)
iconpersen = framebuf.FrameBuffer(bytearray(b'<\x06~\x0e\xe6\x1c\xe6\x1c\xe68~p<\xe0\x00\xe0\x01\xc0\x01\x80\x03\x80\x07\x00\x0e\x00\x0ex\x1c\xfc8\xcex\xc6p\xce\xe0\xfc\xc0x'),15,20,framebuf.MONO_HLSB)
iconbright = framebuf.FrameBuffer(bytearray(b'\x00\x08\x00\x00\x00\x08\x00\x00\x00\x08\x00\x00\x00\x08\x00\x00\x0c\x08\x18\x00\x0e\x008\x00\x06~0\x00\x00\xff\x80\x00\x01\xff\xc0\x00\x03\xff\xc0\x00\x03\xff\xe0\x00\x03\xff\xe0\x00\xfb\xff\xef\x80\x03\xff\xe0\x00\x03\xff\xe0\x00\x03\xff\xc0\x00\x01\xff\xc0\x00\x00\xff\x80\x00\x06\x7f0\x00\x0e\x008\x00\x0c\x08\x18\x00\x00\x08\x00\x00\x00\x08\x00\x00\x00\x08\x00\x00\x00\x08\x00\x00'),25,25,framebuf.MONO_HLSB)
icondim = framebuf.FrameBuffer(bytearray(b'\x00\x08\x00\x00\x00\x08\x00\x00\x00\x08\x00\x00\x00\x08\x00\x00\x0c\x08\x18\x00\x0e\x008\x00\x06~0\x00\x00\xf1\x80\x00\x01\xf0\xc0\x00\x03\xf0@\x00\x03\xf0 \x00\x03\xf0 \x00\xfb\xf0/\x80\x03\xf0 \x00\x03\xf0 \x00\x03\xf0@\x00\x01\xf0\xc0\x00\x00\xf1\x80\x00\x06\x7f0\x00\x0e\x008\x00\x0c\x08\x18\x00\x00\x08\x00\x00\x00\x08\x00\x00\x00\x08\x00\x00\x00\x08\x00\x00'),25,25,framebuf.MONO_HLSB)
icondark = framebuf.FrameBuffer(bytearray(b'\x00\x08\x00\x00\x00\x08\x00\x00\x00\x08\x00\x00\x00\x08\x00\x00\x0c\x08\x18\x00\x0e\x008\x00\x06~0\x00\x00\xc1\x80\x00\x01\x80\xc0\x00\x03\x00@\x00\x02\x00 \x00\x02\x00 \x00\xfa\x00/\x80\x02\x00 \x00\x02\x00 \x00\x03\x00@\x00\x01\x80\xc0\x00\x00\xc1\x80\x00\x06\x7f0\x00\x0e\x008\x00\x0c\x08\x18\x00\x00\x08\x00\x00\x00\x08\x00\x00\x00\x08\x00\x00\x00\x08\x00\x00'),25,25,framebuf.MONO_HLSB)
clearsky = framebuf.FrameBuffer(bytearray(b'\x00\x00\x00\xc0\x00\x00\x00\x00\x00\x01\xe0\x00\x00\x00\x00\x00\x01\xe0\x00\x00\x00\x00\x00\x01\xe0\x00\x00\x00\x00\x00\x01\xe0\x00\x00\x00\x00\x00\x01\xe0\x00\x00\x00\x00\x00\x01\xe0\x00\x00\x00\x01\xe0\x00\x00\x01\xe0\x00\x01\xf0\x00\x00\x03\xe0\x00\x01\xf0\x0f\xfc\x03\xe0\x00\x00\xd8?\xff\x87\xe0\x00\x00x\xff\xff\xc7\xc0\x00\x009\xff\xbb\xf7\x00\x00\x00\x07\xf7\xff\xf8\x00\x00\x00\x07\xff\xff\xfc\x00\x00\x00\x0f\xff\x7f\xfc\x00\x00\x00\x1f\xff\xff\xde\x00\x00\x00\x1f\xfb\xff\xfe\x00\x00\x00?\xff\xff\xff\x00\x00\x00?\xff\xff\xff\x00\x00\x00?\xff\xfb\xef\x80\x00\x00\x7f\xff\xf7\xff\x80\x00\x00\x7f\xff\xfe\xff\x80\x00~\x7f\x7f\xff\xff\x9f\x80\xff\x7f\xff\xef\xff\x9f\xc0\xfe\x7f\xff\xff\xfd\x9f\xc0~\x7f\xbe\xff\xfb\x9f\x80\x00w\xff\xff\xff\x80\x00\x00\x7f\xff\xff\xff\x80\x00\x00;\xff\xff\xff\x80\x00\x00?\xbf\xff\xff\x00\x00\x00?\xff\xff\xff\x00\x00\x00\x1f\xff\xff\xfe\x00\x00\x00\x1f\xff\xff\xfe\x00\x00\x00\x0f\xff\xfb\xfc\x00\x00\x00\x07\xff\xff\xf8\x00\x00\x00\x06\xff\xff\xf8\x00\x00\x009\xff\xff\xe7\x00\x00\x00\xf8\xff\xff\xc7\xc0\x00\x01\xf8?\xff\x07\xe0\x00\x01\xf0\x07\xf8\x03\xe0\x00\x01\xf0\x00\x00\x01\xe0\x00\x01\xe0\x00@\x00\xe0\x00\x00\x00\x01\xe0\x00\x00\x00\x00\x00\x01\xe0\x00\x00\x00\x00\x00\x01\xe0\x00\x00\x00\x00\x00\x01\xe0\x00\x00\x00\x00\x00\x01\xe0\x00\x00\x00\x00\x00\x01\xe0\x00\x00\x00\x00\x00\x00\xc0\x00\x00\x00'), 50, 50, framebuf.MONO_HLSB)
cloud = framebuf.FrameBuffer(bytearray(b'\x00\x00\x0f\xc0\x00\x00\x00\x00\x00\x7f\xf0\x00\x00\x00\x00\x00\xff\xf8\x00\x00\x00\x00\x01\xff\xfe\x00\x00\x00\x00\x03\xff\xff\x00\x00\x00\x00\x07\xff\xff\x00\x00\x00\x00\x07\xff\xff\x80\x00\x00\x00\x0f\xff\xff\x80\x00\x00\x00\x0f\xff\xff\xc0\x00\x00\x00\x0f\xff\xff\xc0\x00\x00\x00\x0f\xbf\xbf\xdf\x80\x00\x00\x0f\x7f\xff\xff\xe0\x00\x00\x0f\xff\xff\xff\xf0\x00\x00\x0f\xff\xff\xff\xf0\x00\x00\x0f\xff\xff\xff\xf8\x00\x01\xff\xff\xff\xff\xf8\x00\x0f\xff\xff\x7f\xff\xfc\x00\x1f\xff\xff\xff\xff\xfc\x00?\xff\xdf\xff\xff\xfc\x00?\xff\xf6\xff\xff\xff\xc0\x7f\xff\xff\xfd\xff\xff\xf0\x7f\xff\xff\x7f\xff\xff\xf8\xff\xff\xff\xff\xff\xff\xfc\xff\xff\xff\xff\xff\xff\xfc\xff\xff\xff\xff\xff\xff\xfc\xff\xf7\xff\xff\x7f\xff\xfe\xff\xff\xfb\xff\xff\xff\xfe\xff\xff\xff\xdf\xbf\xff\xfe\xff\xff\xff\xff\xff\xff\xfe\x7f\xff\xdf\xff\xff\xff\xfe\x7f\xff\xff\xff\xff\xff\xfc?\xff\xff\xdf\xff\xff\xfc?\xff\xff\xff\xff\xff\xf8\x1f\xff\xff\xff\xff\xff\xf8\x07\xff\xff\xff\xff\xff\xf0\x01\xbf\xff\xff\xff\xff\x80'), 55, 36, framebuf.MONO_HLSB)
lightcloud = framebuf.FrameBuffer(bytearray(b'\x00\x00\x00\x00\x07\xf0\x00\x00\x00\x00\x00?\xfe\x00\x00\x00\x00\x00\xff\xff\x80\x00\x00\x00\x01\xfe?\xc0\x00\x00\x1f\x87\xf0\x07\xe0\x00\x00\x7f\xe7\xc0\x01\xf0\x00\x01\xff\xff\x80\x00\xf8\x00\x03\xff\xff\x00\x00x\x00\x07\xef\xfe\x00\x00<\x00\x0f\xff\xfe\x00\x004\x00\x0f\xff\xdf\x00\x00\x1c\x00\x0f\xff\xfd\x00\x00\x1e\x00\x1f\xf7\xff\x00\x00\x1e\x00\x1f\xbf\xfb\xbe\x00\n\x00\x1f\xff\xff\xff\x80\x0e\x00\x1f\xff\xf7\xff\xc0\x0e\x00\x1f\xff\xff\xff\xe0\x1e\x00\xdf\xff\xdf\xff\xe0\x1e\x07\xff\xff\xff\xff\xf0\x1c\x1f\xff\xff\xff\xff\xf0\x1c?\xff\xff\xff\xff\xf0<?\xff\xff\xff\xef\xffx\x7f\xff\xff\xff\xff\xff\xf8\x7f\xff\xff\xff\xff\xff\xf0\xff\xff\xff\xff\xff\xff\xf0\xfe\xff\xff\xff\x7f\xbf\xf0\xff\xfe\xff\x7f\xff\xff\xf0\xff\xff\xff\xff\xbf\xff\xf8\xff\xff\xff\xff\xff\xff\xf8\xff\xff\xffm\xff\xbf\xf8\x7f\xff\xff\xff\xff\xff\xf0\x7f\xff\xef\xff\x7f\xff\xf0?_\xff\xff\xff\xdf\xf0\x1f\xff\xff\xfd\xff\xff\xe0\x0f\xff\xfb\xff\x7f\xff\x80\x01\xff\xdf\xff\xff\xfe\x00'), 55, 36, framebuf.MONO_HLSB)
rain = framebuf.FrameBuffer(bytearray(b'\x00\x00\x00>\x00\x00\x00\x00\x00\x01\xff\x80\x00\x00\x00\x00\x03\xff\xc0\x00\x00\x00\x00\x07\xc3\xf0\x00\x00\x00\x00\xff\x00\xf0\x00\x00\x00\x03\xff\x80x\x00\x00\x00\x07\xff\xc08\x00\x00\x00\x0f\xff\xe08\x00\x00\x00\x1f\xff\xe0?\xf0\x00\x00\x1f\xff\xf0?\xfc\x00\x00?\xff\xf0\x1f\xfc\x00\x00?\xff\xf1\x8e\x1e\x00\x00?\xff\xff\xe0\x0e\x00\x00?\xff\xff\xf8\x0e\x00\x00?\xff\xff\xf8\x0e\x00\x03\xff\xff\xbf\xfc\x0f\xf0\x0f\xff\xfe\xff\xfc\x07\xf8?\xff\xff\xff\xfc\x03\xfc?\xff\xff\xff\xfc\x00\x1c\x7f\xfe\xff\xdf\xff\xe0\x0e\x7f\xff\xff\xff\xff\xf0\x0e\xff\xdf\xff\xff\xff\xf8\x0e\xff\xff\xff\xff\xff\xfc\x0e\xfd\xff\xff\xff\xff\xfc\x1e\xff\xff\xff\xef\xfe\xfc<\xff\xff\xff\xbf\xbf\xff\xfc\x7f\xff\xff\xff\xff\xff\xf0\x7f\xfe\xff\xff\xf7\xff\xc0?\xff\xfb\xff\xff\xf8\x00\x1f\xff\xdf\x7f\xff\xf0\x00\x0f\xff\xff\xff\xff\xe0\x00\x01\x7f\xff\xff\xff\x80\x00\x00\x03\x80\x01\xc0\x00\x00\x00\x03\x81\x81\xc0\x00\x00\x00\x03\x03\x81\x80\x00\x00\x00\x03\x03\x81\x80\x00\x00\x00\x00\x03\x81\x80\x00\x00\x00\x00\x03\x01\x80\x00\x00\x00\x07\x03\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x06\x06\x02\x00\x00\x00\x00\x0e\x07\x07\x00\x00\x00\x00\x0e\x06\x07\x00\x00\x00\x00\x00\x06\x07\x00\x00\x00\x00\x00\x06\x07\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00'), 55, 47, framebuf.MONO_HLSB)
thunderstorm = framebuf.FrameBuffer(bytearray(b'\x00\x00\x00~\x00\x00\x00\x00\x00\x01\xff\x80\x00\x00\x00\x00\x03\xff\xe0\x00\x00\x00\x00\x07\xc3\xf0\x00\x00\x00\x01\xff\x00\xf0\x00\x00\x00\x03\xff\x80x\x00\x00\x00\x07\xff\xc08\x00\x00\x00\x0f\xff\xe08\x00\x00\x00\x1f\x7f\xf0;\xf0\x00\x00?\xff\xd0\x1f\xf8\x00\x00?\xff\xf0\x1f\xfc\x00\x00?\xff\xfb\xce\x1e\x00\x00?\xfe\xff\xf0\x0e\x00\x00?\xff\xff\xf8\x0e\x00\x00?\xff\xff\xf8\x0e\x00\x03\xff\xff\xff\xfc\x0f\xf0\x0f\xff\xff\xff\xfc\x07\xf8?\xff\xff\xff\xfc\x03\xfc?\xff\xdf\xff\xff\xc0\x1c\x7f\xff\xff\xff\xff\xe0\x1e\x7f\xff\xff\xff\xff\xf0\x0e\xff\xff\xff\xb7\xff\xf8\x0e\xff\xff\xff\xfd\xff\xfc\x0e\xff\xff\xff\xff\xff\xfc\x1c\xff\xff\xff\xff\xbf\xff\xfc_\xff\xff\xff\xff\xff\xf8\x7f\xff\xff\xff\xff\xff\xf0\x7f\xff\xff\xff\xff\xff\xc0?\xff\xf0?\xff\xf8\x00\x1f\xff\xe0\x7f\xff\xf0\x00\x03\xff\xe0\x7f\xf7\xe0\x00\x00\x00?\x00\x00\x00\x00\x00\x00\x7f\x00\x00\x00\x00\x00\x00\xff\xc0\x00\x00\x00\x00\x00\xff\x80\x00\x00\x00\x00\x01\xff\x00\x00\x00\x00\x00\x00>\x00\x00\x00\x00\x00\x00x\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x01\xc0\x00\x00\x00\x00\x00\x01\x80\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), 55, 45, framebuf.MONO_HLSB)
mist = framebuf.FrameBuffer(bytearray(b'\x00\x03\xff\xfe\x00\x00\x00\x00\x03\xff\xfe\x00\x00\x00\x00\x03\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xff\xff\xff\xe0\x00\x00\x1f\xff\xff\xff\xe0\x00\x00\x1f\xff\xff\xff\xe0\x00\x00\x1f\xff\xff\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xff\xff\xff\xff\xc0\x00\x03\xff\xff\xff\xff\xc0\x00\x03\xff\xff\xff\xff\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xfc\x00\x00\xff\xff\xff\xff\xfc\x00\x00\xff\xff\xff\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xf0\x00\x00\xff\xff\xff\xff\xf0\x00\x00\xff\xff\xff\xff\xf0\x00\x00\xff\xff\xff\xff\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xff\xff\xf0\x00\x00\x00\x03\xff\xff\xf0\x00\x00\x00\x03\xff\xff\xf0\x00\x00'), 55, 36, framebuf.MONO_HLSB)


#deklarasi wifi (hanya untuk prototype)
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()
# sta.connect("althaf","Althaf1234567")
# #print(sta.scan())
# while not sta.isconnected():
#      print(".",end="")
#      sleep(1)
#      
# if sta.isconnected():
#     print("connected")
#     print(sta.ifconfig())

#deklarasi firebase
firebase.setURL("https://buahahahah-68f02-default-rtdb.asia-southeast1.firebasedatabase.app/")
    
#test waktu
print(utime.localtime())

#deklarasi TouchPad
touchr = TouchPad(Pin(32))
touchl = TouchPad(Pin(12))

#menampilkan jam
def jam():
    lcd.fill(0)
    waktu=[]
    waktu = utime.localtime()
    jam = (str(waktu[3]) + ":" + str(waktu[4]) +":"+ str(waktu[5]))
    tanggal = (str(waktu[2]) + "/" + str(waktu[1]) +"/"+ str(waktu[0]))
    #tanggal = (str(waktu[2]) + "/" + str(waktu[1]) +"/"+ str(waktu[0]))
    lcd.text(tanggal,5,3,1)
    clock.set_textpos(0,15)
    clock.printstring(jam)
    lcd.show()
    sleep(0.2)
    #print("but jm = ",but.value())
    #print(stat)
    
#start screen
def mulai():
    global temp
    try:
        DHT.measure()
        temp = DHT.temperature()
        #print(temp)
        sleep(0.3)
    except:
        temp = temp
        #print("dht eror Mu")
    humid = int(100 - (adc.read() * (100/4095) ))
    chy = int(ldr.read() * (100/4095))
    lcd.fill(0)
    #lcd.text("mulai",20,20)
    #lcd.show()
    if (chy > 90):
        animasi.sunglass()
    elif (humid <5):
        animasi.dryy()
    elif (chy < 5):
        animasi.sleepp()
    elif (temp < 20):
        animasi.frozen() 
    else:
        animasi.normal()
    sleep(0.2)
    #print(stat)

def monitor():
    global temp
    #temp = t.temperature()
    #print(temp) 
    #print(adc.read())
    humid = int(100 - (adc.read() * (100/4095) ))
    chy = int(ldr.read() * (100/4095))
    #print(chy)
    #print(humid)
    
    try:
        DHT.measure()
        temp = DHT.temperature()
#         print(temp)
        
    except:
        temp = temp
        #print("dht eror Mo")
        #print("dht error")
    lcd.fill(0) # fill entire screen with colour=0
    lcd.framebuf.blit(iconsuhu,5,4) #display icon suhu
    lcd21.set_textpos(30,4) #set coordinat for text
    lcd21.printstring(str(temp)) #print text with writer module
    lcd.framebuf.blit(iconderajat,65,5) #display icon derajat
    lcd21.set_textpos(73,4) #set coordinat for text
    lcd21.printstring("C") #print text with writer module
    lcd.framebuf.blit(iconlembab,5,37) #display icon lembab
    lcd21.set_textpos(30,37) #set coordinat for text
    lcd21.printstring(str(humid)) #print text with writer module
    lcd.framebuf.blit(iconpersen,75,40) #display icon persen
    if (chy <= 25 and chy >= 0):
        lcd.framebuf.blit(icondark,100,19)
    elif (chy >= 25 and chy <= 75):
        lcd.framebuf.blit(icondim,100,19) #display icon brightness
    else:
        lcd.framebuf.blit(iconbright,100,19)
    #lcd.text("hai",0,0,1)
    lcd.show()
    sleep(0.7)

#display weather
def weather():
    try:
        lock.acquire()
        link = ("https://api.openweathermap.org/data/2.5/weather?id=1645524&appid=911219271f2f512e30f421ded47f44be")
        data = urequests.get(link)
        cuaca = ujson.loads(data.text)["weather"][0]["main"]
        icon = ujson.loads(data.text)["weather"][0]["icon"]
        description = ujson.loads(data.text)["weather"][0]["description"]
        print (cuaca)
        print (icon)
        print(description)
        lock.release()
        return icon,description
    except:
        return "error"
    
def displayweather(icon,desc):
    listt = desc.split(" ")
    #print(icon)
    
    if (icon == "01d" or icon == "01n"):
        lcd.fill(0)
        lcd.framebuf.blit(clearsky,5,7)
        y = 20
        for x in listt:
            lcd.text(x,70,y)
            y += 10
        lcd.show()
    if (icon == "02d" or icon == "02n"):
        lcd.fill(0)
        lcd.framebuf.blit(lightcloud,5,14)
        y = 20
        for x in listt:
            lcd.text(x,70,y)
            y += 10
        lcd.show()
    if (icon == "03d" or icon == "03n" or icon == "04d" or icon == "04n"):
        if (icon == "03d" or icon == "03n"):
            listt = ["scatter","clouds"]
        lcd.fill(0)
        lcd.framebuf.blit(cloud,5,14)
        y = 20
        for x in listt:
            lcd.text(x,70,y)
            y += 10
        lcd.show()
    if (icon == "09d" or icon == "09n" or icon == "10d" or icon == "10n"):
        lcd.fill(0)
        lcd.framebuf.blit(rain,5,8)
        y = 20
        for x in listt:
            lcd.text(x,70,y)
            y += 10
        lcd.show()
    if (icon == "11d" or icon == "11n"):
        lcd.fill(0)
        lcd.framebuf.blit(thunderstorm,5,10)
        y = 20
        listt = ["thunder","storm"]
        for x in listt:
            lcd.text(x,70,y)
            y += 10
        lcd.show()
    if (icon == "50d" or icon == "50n"):
        lcd.fill(0)
        lcd.framebuf.blit(mist,5,14)
        y = 20
        for x in listt:
            lcd.text(x,70,y)
            y += 10
        lcd.show()
        
#tictactoe game
# playerX = [1,2,3,4,5,6,7,8,9]
# playerY = [1,2,3,4,5,6,7,8,9]

#alarm
# def alarm():
#     lock.acquire()
#     while True:
#         humid = int(100 - (adc.read() * (100/4095) ))
#         if humid < 10:
#             
#             for x in range(5):
#                 buzzer.freq(1000)
#                 buzzer.duty(300)
#                 sleep(0.1)
#                 buzzer.duty(0)
#                 sleep(0.05)
#                 buzzer.freq(1600)
#                 buzzer.duty(300)
#                 sleep(0.2)
#                 buzzer.duty(0)
#                 sleep(0.65)
#         lock.release()      
#         sleep(30)
#     


#buzzer
def beep():
    buzzer.freq(1800)
    buzzer.duty(200)
    sleep(0.05)
    buzzer.duty(0)
    
def beeep():
    buzzer.freq(2000)
    buzzer.duty(200)
    sleep(0.05)
    buzzer.duty(0)
    
#get/send data to firebase
def getdata():
    sleep(2)
    menit1 = 0
    while True:
        waktu = utime.localtime()
        lock.acquire()
        menit = waktu[4]
        
        print(menit)
        print(menit1)
        if sta.isconnected():
            
            sleep(1)
            try:
                DHT.measure()
                temper = DHT.temperature()
                #print(temp)
                sleep(0.3)
            except:
                temper = temp
                #print("dht error Fi")
            try:
                humid = int(100 - (adc.read() * (100/4095) ))
                chy = int(ldr.read() * (100/4095))
                global suhu
                #suhu+= 1
                firebase.put("project/suhu", temper, bg=0)
                firebase.put("project/cahaya", chy, bg=0)
                firebase.put("project/kelembaban", humid, bg=0)
                print("sent")
                gc.collect()
                print("ram1" ,gc.mem_alloc())
                print("free1" ,gc.mem_free())
                #sleep(5)
                if menit > menit1:
                    if humid < 5:
                        urequests.get(urlchat)
                        sleep(0.2)
                        for x in range(10):
                            buzzer.freq(1000)
                            buzzer.duty(300)
                            sleep(0.1)
                            buzzer.duty(0)
                            sleep(0.05)
                            buzzer.freq(1600)
                            buzzer.duty(300)
                            sleep(0.2)
                            buzzer.duty(0)
                            sleep(0.65)
                    
                    menit1 = menit + 5
                    if menit1 > 60:
                        menit1 -= 60
                    #print(menit1)
            except:
                print("firebase error")
                #reset()
        else:
            print("no connection")
            sleep(1)
        lock.release()

#deklarasi variabel pendukung
stat = 1 
DHT = dht.DHT11(Pin(5))
suhu = 0
adc = ADC(Pin(34))
temp = 0
lock = _thread.allocate_lock()
#lock1 = _thread.allocate_lock()
        

kirim =_thread.start_new_thread(getdata,())
#_thread.start_new_thread(alarm,())
#mulai program
while True:
    try:
        buzzer.duty(0)
        while not sta.isconnected():
            connectwifi.start(lcd)
        if stat == 1:
            #print("stat m = ",stat)
            while stat==1:
                mulai()
                #print(touchr.read())
                if touchr.read() < 400:
                    stat = 2
                    sleep(0.2)
                    beep()
                    break
                sleep(0.1)
                
        elif stat == 2:
            #print("stat j = ",stat)
            while stat == 2:
                jam()
                #print(touchr.read())
                if touchr.read() < 400:
                    stat = 3
                    sleep(0.2)
                    beep()
                    break
                sleep(0.1)
                
        elif stat == 3:
            #print("stat j = ",stat)
            while stat == 3:
                monitor()
                #print(touchr.read())
                if touchr.read() < 400:
                    stat = 4
                    sleep(0.2)
                    beep()
                    break
                sleep(0.1)
        elif stat == 4:
            
            lcd.fill(0)
            lcd21.set_textpos(12,17)
            lcd21.printstring("Weather")
            lcd.show()
            if (touchl.read() <400):
                beeep()
                lcd.fill(0)
                lcd.text("loading..",25,25,1)
                lcd.show()
                icon,desc = weather()
                #print("stat j = ",stat)
                while stat == 4:
                    displayweather(icon,desc)
                    sleep(0.1)
                    #print(touchr.read())
                    if touchr.read() < 400:
                        stat = 5
                        sleep(0.2)
                        beep()
                        break
            if touchr.read() < 400:            
                stat = 5
                sleep(0.2)
                beep()
            sleep(0.05)
                
            sleep(0.2)
        elif stat == 5:
            #print("stat j = ",stat)
            while stat == 5:
                lcd.fill(0)
                lcd21.set_textpos(30,17)
                lcd21.printstring("Game")
                lcd.show()
                sleep(0.1)
                #print(touchr.read())
                if touchl.read() <400:
                    beeep()
                    tictactoe.start()
                if touchr.read() < 400:
                    stat = 1
                    sleep(0.2)
                    beep()
                    break
                sleep(0.2)
                
        else:
            stat=1
    except:
        print("system erorr")
        pass
        


