import ssd1306
from machine import Pin , SoftSPI , TouchPad
import gc
from time import sleep

spi = SoftSPI(baudrate=500000, polarity=1, phase=0, sck=Pin(15), mosi=Pin(2), miso=Pin(0))

dc = Pin(16)
rst = Pin(4)
cs = Pin(17)


lcd = ssd1306.SSD1306_SPI(128,64,spi,dc,rst,cs)

#dis = [1,2,3,4,5,6,7,8,9]
#but = Pin(13, Pin.IN)
touchr = TouchPad(Pin(32))
touchl = TouchPad(Pin(12))
playerX = [1,2,3,4,5,6,7,8,9]
playerY = [1,2,3,4,5,6,7,8,9]



def garis():
    #garis vertical
    lcd.framebuf.line(53,0,53,65,1)
    lcd.framebuf.line(75,0,75,65,1)
    #garis horizontal
    lcd.framebuf.line(32,21,96,21,1)
    lcd.framebuf.line(32,42,96,42,1)
    lcd.show()

def cekresult():
    global playerX
    global playerY
    global sx
    global sy
    global kx
    global ky
    global posisi
    global total
    
    if (playerX[0] == "x" and playerX[1] == "x" and playerX[2] == "x"):
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.fill(0)
        lcd.text("PLAYER X WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerX[3] == "x" and playerX[4] == "x" and playerX[5] == "x"):
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.fill(0)
        lcd.text("PLAYER X WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerX[6] == "x" and playerX[7] == "x" and playerX[8] == "x"):
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.fill(0)
        lcd.text("PLAYER X WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerX[0] == "x" and playerX[4] == "x" and playerX[8] == "x"):
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.fill(0)
        lcd.text("PLAYER X WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerX[2] == "x" and playerX[4] == "x" and playerX[6] == "x"):
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.fill(0)
        lcd.text("PLAYER X WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir

    if (playerX[0] == "x" and playerX[3] == "x" and playerX[6] == "x"):
        lcd.fill(0)
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.text("PLAYER X WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerX[1] == "x" and playerX[4] == "x" and playerX[7] == "x"):
        lcd.fill(0)
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.text("PLAYER X WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerX[2] == "x" and playerX[5] == "x" and playerX[8] == "x"):
        lcd.fill(0)
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.text("PLAYER X WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerY[0] == "O" and playerY[1] == "O" and playerY[2] == "O"):
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.fill(0)
        lcd.text("PLAYER O WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerY[3] == "O" and playerY[4] == "O" and playerY[5] == "O"):
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.fill(0)
        lcd.text("PLAYER O WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerY[6] == "O" and playerY[7] == "O" and playerY[8] == "O"):
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.fill(0)
        lcd.text("PLAYER O WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerY[0] == "O" and playerY[3] == "O" and playerY[6] == "O"):
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.fill(0)
        lcd.text("PLAYER O WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerY[1] == "O" and playerY[4] == "O" and playerY[7] == "O"):
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.fill(0)
        lcd.text("PLAYER O WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerY[2] == "O" and playerY[5] == "O" and playerY[8] == "O"):
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.fill(0)
        lcd.text("PLAYER O WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerY[0] == "O" and playerY[4] == "O" and playerY[8] == "O"):
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.fill(0)
        lcd.text("PLAYER O WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
        
    if (playerY[2] == "O" and playerY[4] == "O" and playerY[6] == "O"):
        playerX = [1,2,3,4,5,6,7,8,9]
        playerY = [1,2,3,4,5,6,7,8,9]
        print("player x win")
        lcd.fill(0)
        lcd.text("PLAYER O WIN",15,30,1)
        lcd.show()
        sleep(0.3)
        while True:
            if (touchl.read() <400):
                sx = 19
                sy = 5
                kx = 34
                ky = 2
                posisi = 0
                total = 0
                lcd.fill(0)
                break
        sleep(0.2)
        akhir = menu1()
        return akhir
            


def cekX(index):
    if playerX[index] == "x":
        return False
    else :
        return True

def cekY(index):
    if playerY[index] == "O":
        return False
    else :
        return True

def tampilXY():
    tx = 40
    ty = 5
    for y in playerX:
        #print("_")
        #print(y)
        #print(tx)
        #print(ty)
        if y == "x":
            lcd.text("x",tx,ty,1)
            lcd.show()
        tx += 21
        if tx == 103:
            tx = 40
            ty += 21
    tx = 40
    ty = 5
    for y in playerY:
        #print("_")
        #print(y)
        #print(tx)
        #print(ty)
        if y == "O":
            lcd.text("O",tx,ty,1)
            lcd.show()
        tx += 21
        if tx == 103:
            tx = 40
            ty += 21

def menu1():
    
    xx = 20
    yy = 10
    c = True
    while True:
        if c:
            xx = 20
            yy = 10
        else :
            xx = 20
            yy = 35
        lcd.fill(0)
        lcd.text("play again",25,15,1)
        lcd.text("exit",48,40,1)
        lcd.framebuf.rect(xx,yy,90,18,1)
        lcd.show()
        sleep(0.3)
        if touchr.read() <400:
            c = not c
            sleep(0.3)
        if touchl.read() <400:
            if c:
                lcd.fill(0)
                lcd.show()
                print("satuuu!!")
                return 1
                
            else:
                lcd.fill(0)
                lcd.show()
                print("noolll!!")
                return 0
                


    
def start():
    sx = 19
    sy = 5
    kx = 34
    ky = 2
    posisi = 0
    total = 0
    haha = 1
    while haha == 1:       
#         gc.collect()
#         print("ram1" ,gc.mem_alloc())
#         print("free1" ,gc.mem_free())
        akhir = cekresult()
        if akhir == 0:
            print("akhir")
            haha = 0
            break
        elif akhir == 1:
            print("lanjut")
            sx = 19
            sy = 5
            kx = 34
            ky = 2
            posisi = 0
            total = 0
            haha = 1
        else:
            pass
            
        garis()
        #burn = touchr.read()
        #buln = touchl.read()
        #print(burn)
        #print(buln)
        sleep(0.2)
        if touchr.read() < 400:
            #print("pos : " , posisi)
            #print(but.value())
            lcd.fill(0)
            garis()
            tampilXY()
            #print("\n")
            lcd.framebuf.rect(kx,ky,18,18,1)
            #lcd.text("x",sx,sy,1)
            lcd.show()
            kx += 22
            sx += 21
            #print("sx,sy")
            #print(sx)
            #print(sy)
            #print("kx,ky")
            #print(kx)
            print(ky)
            if (kx == 100):
                kx = 34
                ky += 21
            if (ky == 65):
                kx = 34
                ky = 2
            if (sx==103):
                sx = 40
                sy += 21
            if (sy == 68):
                sx = 40
                sy = 5
                
            
            posisi += 1
            if (posisi == 10) :
                posisi = 1
                
            print(" P X : ", playerX)
            print(" P Y : ", playerY)
            sleep(0.5)
            
        if (touchl.read() < 400 and posisi > 0):         
            if (total % 2 == 0):
                print("poss :" ,posisi)
                statex = cekX(posisi - 1)
                statey = cekY(posisi - 1)
                if statex and statey:
                    lcd.text("x",sx,sy,1)
                    lcd.show()
                    print("insert")
                    playerX[posisi-1] = "x"
                    print(" P X : ", playerX)
                    print(" P Y : ", playerY)
                    total += 1
            else :
                print("poss :" ,posisi)
                statex = cekX(posisi - 1)
                statey = cekY(posisi - 1)
                if statex and statey:
                    lcd.text("O",sx,sy,1)
                    lcd.show()
                    print("insert")
                    playerY[posisi-1] = "O"
                    print(" P X : ", playerX)
                    print(" P Y : ", playerY)
                    total += 1
            
            
        sleep(0.1)
        
