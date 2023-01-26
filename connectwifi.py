import network
import socket
from time import sleep
import machine

filename = "pw.txt"

#activated Access Point
ap = network.WLAN(network.AP_IF)


#Activated Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
adde = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
print(adde)

try:
    s.bind(adde)
    s.listen(1)
    print("socket active")
except:
    machine.reset()

#activated station
sta = network.WLAN(network.STA_IF)
sta.active(True)

constatus = 0

def wifiscan():
    wifi = sta.scan()
    print(wifi)
    ssids= []
    for ssid, dua, tiga, empat, auth, enam in wifi:
        print(ssid.decode(), end="/")
        ssids.append(ssid.decode())
        print(auth)
    return ssids    

def writefile(name,isi):
    print("write file" , "\n")
    index = searcht(isi,"=",2)
    index2 = isi.find("&")
    ssid = isi[index[0]+1:index2]
    passw = isi[index[1]+1:]
    print(ssid)
    print(passw)
    f = open(name,"w")
    f.write(ssid+","+passw)
    f.close
    return ssid,passw
    
    
def readfile(name):
    try:
        f = open(name, "r")
        isi = f.read()
        wifi = isi.split(",")
        f.close()
    except:
        wifi = ""
    return wifi

def searcht(isi,text,repeat):
    print("search" , "\n")
    x=0
    li = []
    for i in range(repeat):
        x = isi.index(text,x+1)
        li.append(x)
        print(li)
    return li
    
def connect(ssid1,passw1,lcd):
    global constatus
    print("connect")
    print("ssid=",ssid1)
    print("pass=",passw1)
    sta.disconnect()
    
    try:
        for i in range(10):
            sta.connect(ssid1,passw1)        
            print(".",end="")
            sleep(5)
            if sta.isconnected():
                print("connect to : ", ssid1)
                print(sta.ifconfig())
                constatus = 1
                break
    except OSError:
        print("FAIL TO CONNECT")
        constatus = 2
        sendhtml(lcd)
    
    stt = sta.isconnected()
    print(stt)
    if (sta.isconnected()):
        print(2)
        print("Wifi Connected")
        print(sta.ifconfig())
        if sta.isconnected():
            #sendsukses(ssid1)
            s.close()
            ap.active(False)
        

def start(lcd):
    
    ap.active(True)
    ap.config(essid='Smart Pot',password='12345678')
    print(ap.ifconfig())
    global con
    credential = readfile(filename)
    #print(credential)
    if (not sta.isconnected()):
        if (len(credential) > 1):
        
            try:
                print(1)
                sta.disconnect()
                for i in range(10):
                    
                    sta.connect(credential[0],credential[1])
                    print(".",end="")
                    sleep(3)
                    print(credential[0])
                    print(credential[1])
                    if (sta.isconnected()):
                        #print(3)
                        ap.active(False)
                        s.close()
                        #print("finish")
                        break
                        
                if (not sta.isconnected()):
                        sta.disconnect()
                        print("fail")
                        sendhtml(lcd)
            
            except OSError:
                print("eror start")
                sendhtml(lcd)
    if (sta.isconnected()):
        print(2)
        print("Wifi Connected")
        print(sta.ifconfig())
        #sendsukses(credential[0])
        ap.active(False)
        s.close()
                        
    else:
        print("not connect start")
        sendhtml(lcd)
    
        
        
def sendhtml(lcd):
    lcd.text("connect to wifi",0,0,1)
    lcd.text("ssid = Smart Pot",0,10,1)
    lcd.text("pass = 12345678",0,20,1)
    lcd.text("go to link below",0,40,1)
    lcd.text("192.168.4.1",0,50,1)
    lcd.show()
    ap.active(True)
    global con
    ssids = wifiscan()
    print ("available = ", ssids)
    print("status" , constatus)
    con,addr = s.accept()
    print(con)
    print(addr)
    print("status" , constatus)
    con.sendall("HTTP/1.0 {} OK\r\n".format(200))
    con.sendall("Content-Type: text/html\r\n")
    con.sendall("\r\n")
    con.sendall("""
    <html>
    <head>
        <title> Smart Pot Wifi </title>
        <style>
            label{
                margin-right: 10px;
            }
            .buton{
                margin-top: 2vh;
                background-color: #93d6fb;
                width: 10vw;
                border-radius: 5px;
                border: 1px solid gray;
                padding-top: 5px;
                padding-bottom: 5px;
            }

            table{
                
                border-collapse: separate;
                border-spacing: 0 10px;
            }

            select{
                border: 1px solid gray;
                width: 20vw;
                height: 25px;
                border-radius: 5px;
            }

            input{
                border: 1px solid gray;
                width: 20vw;
                height: 25px;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <center>
            <h1> Smart Pot </h1>
            <br>
            <h1>Connect to Wifi</h1> """)
    if (constatus==2):
        con.sendall("""
            <div>
                <h2 style="color:red;" class="warning">Failed to Connect!!</h2>
            </div>
        """)
    con.sendall("""
            <form method="post">
                <table>
                    <tr>
                        <td><label> Wifi Name  </label></td>                          
    """)
    #con.sendall("<option value="{0}>{0}</option>")
#    if (len(ssids) > 0):
#         con.sendall(""" <td><select class="ssid" name="ssid">""")
#         for i in ssids:
#             print( "wifi =" , i)
#             con.sendall("""
#             <option value={0}>{0}</option>
#             """.format(i))
#         con.sendall("</select> </td>")
        
#    else:
    con.sendall("""
            <td>
                <input type="text" class="pass" name="ssid">
            </td>
        """)
        
    con.sendall("""
                                   
                        </tr>
                        <tr>
                            <td>
                                <label>Password  </label>
                            </td>
                            <td>
                                <input type="password" class="pass" name="paswd">
                            </td>
                        </tr>
                    </table>                                               
                    <input type="submit" value="Click" class="buton">
                </form>
            </center>
        </body>
    </html>

    """)
    request = con.recv(1024)    
    print(type(request))
    
    while "\r\n\r\n" not in request:
        request += con.recv(512)
    isi = request.decode()
    print(isi)
    
    method = isi.split("\n")[0]
    if "POST" in method:
        file = isi.split("\n")[-1]
        print(file)
        
        ssid,pw = writefile(filename,file)
        
        print(ssid,pw)
        filee = readfile(filename)
        print("credential = " ,filee)
        status = connect(ssid,pw,lcd)
    else:
        print("method = get")

# def sendsukses(ssid):
#     
#     con.sendall("HTTP/1.0 {} OK\r\n".format(200))
#     con.sendall("Content-Type: text/html\r\n")
#     con.sendall("\r\n")
#     con.sendall("""
#     <html>
#         <head>
#         </head>
#         <body>
#             <center>
#             <div>
#                 <div>
#                     <h1 style="color:lightgreen; margin-top:5%">Success Connect to {0}</h1>
#                 </div>
#             </div>
#             </center>
#         </body>
#     </html>
#     """.format(ssid))
    
# while True:
#     start()