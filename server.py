import socket
 
Ip = socket.gethostbyname(socket.gethostname())
Size = 1024
FORMAT = "utf-8"
Port = 8888
ADDR = (Ip, Port)


 
def main():
    print("[START] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Staring a TCP socket.
    server.bind(ADDR) # connecting the server socket to the Ip address and Port
    server.listen() # listening to the client (wait for the client to respond)
    print("[LISTEN] Server is listening.")
 
    while True:
        conn, addr = server.accept() #accepting the connection
        print(f"[NEW CONNECTION] {addr} connected.")

        filename = conn.recv(Size).decode(FORMAT) #getting the filename
        print(f"[RECVIVE] Receiving the filename.")
        file = open(filename, "w")
        conn.send("Filename received.".encode(FORMAT))
 
        data = conn.recv(Size).decode(FORMAT)# Receiving the data from the client
        print(f"[RECVIVE] Receiving the file data.")
        file.write(data)
        conn.send("File data received".encode(FORMAT))
 
        file.close() #close the file
 
        conn.close() #close the connection
        print(f"[DISCONNECTED] {addr} disconnected.")
 
if __name__ == "__main__":
    main()
