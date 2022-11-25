import socket
 
Ip = socket.gethostbyname(socket.gethostname())
FORMAT = "utf-8"
Size = 1024
Port = 8888
Address = (Ip, Port)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #starting the socket
 
    client.connect(Address) #connecting to server

    file = open("thefile.txt", "r") # opening the file
    data = file.read()
 
    client.send("thefile.txt".encode(FORMAT)) #send the filename to server
    msg = client.recv(Size).decode(FORMAT)
    print(f"[SERVER]: {msg}")
 
    client.send(data.encode(FORMAT)) #receiving the data from the server
    msg = client.recv(Size).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    file.close() #closing the file
 
    client.close() #disconnecting
 
 
if __name__ == "__main__":
    main()
