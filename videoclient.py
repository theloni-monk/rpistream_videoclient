from clientDependency.streamclient import Client
import socket
import sys
import cv2


SERVER_IP = "YOURIPHERE"
SERVER_PORT = 5000
#NOTE: if you change the resolution in the server, you have to change it in the client
try:
    client = Client(serverIp=SERVER_IP, port = SERVER_PORT, promoteErrors = True, writeFile = False, verbose = False) # Connects to the server
    client.s.settimeout(15)
except socket.error:
    print ("Error connecting to duckybot, make sure that your raspberry pi is running your program and you have editted this file to contain the IP address of your duckybot")
    sys.exit(0)
client.initializeStream()
try:
    try:
        client.startStream()
    except Exception as e:
        print(e)
except KeyboardInterrupt as e:
    print("exiting")
    cv2.destroyAllWindows()
