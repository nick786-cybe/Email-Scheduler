import socket
import smtplib,ssl
import time
import datetime

smtp_server = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(smtp_server,port)
server.starttls()


def login(email,password):
    try:
        server.login(email,password)
        print("login sucess")
    except Exception as e:
        print(e)


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ("https://www.pythonanywhere.com")

port = 1255
s.bind((host,port))
s.listen(5)






#server.sendmail(sender_email, receiver_email, message)


def start_server():
    print("server Started")
    run = True
    count = 0
    socketclient, address = s.accept()
    print("connected to ",address)
    try:
        while run:
            msg = socketclient.recv(1024)
            msg = msg.decode("utf-8")
            print(msg)
            
            if msg ==  "":
                count = count+1
                if count == 5:
                    run = False
                    start_server()
                
            if msg == "login":
                email = socketclient.recv(1024)
                email = email.decode("utf-8")   
                print(email)
                password = socketclient.recv(1024)
                password = password.decode("utf-8")
                print(password)
                login(email,password)
                socketclient.send(("login sucess").encode("utf-8"))

                    
                    
            elif msg ==  "send message":
                client_email = socketclient.recv(1024)
                client_email = client_email.decode("utf-8")
                print("client email is: ",client_email)
                title = socketclient.recv(1024)
                title = title.decode("utf-8")
                print("Title is : ",title)
                message = socketclient.recv(1024)
                message = message.decode("utf-8")

                print("message is: ",message)
                server.sendmail(email, client_email, f"subject:{title}\n\n{message}")
                socketclient.send(("message sent sucessfuly").encode("utf-8"))
                
            elif msg ==  "schedule":
                client_email = socketclient.recv(1024)
                client_email = client_email.decode("utf-8")
                print("client email is: ",client_email)
                
                title = socketclient.recv(1024)
                title = title.decode("utf-8")
                print("Title is : ",title)
                
                message = socketclient.recv(1024)
                message = message.decode("utf-8")
                print("message is: ",message)
                
                date = socketclient.recv(1024)
                date = date.decode("utf-8")
                print("date is: ",date)

                times = socketclient.recv(1024)
                times = times.decode("utf-8")
                print("date is: ",times)
                while True:
                    today = time.strftime("%m/%d/%Y")
                    now = time.strftime("%I:%M %p")
                    if (date == today):
                        print(date,' is today')
                        if (now == times):
                            print(now,' is now')
                            server.sendmail(email, client_email, f"subject:{title}\n\n{message}")
                            print("Message sent sucessfully")
                            break
                        else:
                            print(now,"!=",times)   
                    else:
                        print(date,"!=",today)    
                        
    except Exception as e:
        print(e)
        start_server()
        
start_server()




