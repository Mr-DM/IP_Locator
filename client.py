import socket
import TXT_IP
from TXT_IP import save_in_txt

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

my_socket.connect((local_ip,1020))
print("Hello welcome to locator IP To start enter HELLO|name of your device or HELP")
input_user = ""
while input_user != "EXIT":
    input_user = input("Enter command: ")
    my_socket.send(input_user.encode())
    response = my_socket.recv(1024).decode()
    print("Server says:", response)

my_socket.close()
