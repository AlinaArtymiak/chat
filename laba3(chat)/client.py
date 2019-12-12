import socket
import threading        #щоб користувач міг отримувати та відправляти повідомлення; користувач не отримував би повідомлення поки не відправив зворотнього повідомлення 
import time
import cesar
shutdown = False
join = False




def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                msg = data.decode("utf-8")
                
                print("[ You get a message! ]")
                choise = input("[ Do you want code a message? :: y/n] ")
                if choise == "y":
                    print(msg)
                elif choise == "n":
                    print(cesar.cesardecode(msg))
                
                time.sleep(0.2)
        except:
            pass

host = socket.gethostbyname(socket.gethostname())
port = 0


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))
sock.setblocking(0)     #щоб користувач уникнув помилок

ip = str(input("Enter IP: "))
print("[ Connected ]")
userName = input("Enter Your name: ")
server = (ip, 9090)        

rT = threading.Thread(target = receving, args = ("RecvThread", sock))      
rT.start()

while shutdown == False:
    if join == False:
        joinUser = ("[" + userName + "] => join chat ")
        joinUser = cesar.cesar(joinUser)
        sock.sendto(joinUser.encode("utf-8"), server)
        join = True
    else:
        try: 
            message = input()
            if message != "":
                message = str(cesar.cesar(message))
                sock.sendto(("[" + userName + "] :: " + message).encode("utf-8"), server)
                
            time.sleep(0.2)     
        except: #ctrl C
            sock.sendto(("[" + userName + "] <= left chat ").encode("utf-8"), server)
            shutdown = True
rT.join()       #щоб між користувачами не було розриву у часі
sock.close()

