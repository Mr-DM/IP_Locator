import socket
import geocoder
import IP2Location
import requests
from TXT_IP import save_in_txt

# Server setting #
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Server Port
port = 1020

#Get host IP
hostname = socket.gethostname()
# Resolve hostname to IP
local_ip = socket.gethostbyname(hostname)

server_socket.bind((local_ip, port ))

server_socket.listen(1)

Commands_List = ["HELLO", "LOCATE", "EXIT", "HELP"]
commands_info = """\n+-----------------------------------------------------+
|                  AVAILABLE COMMANDS                 |
+-----------------------------------------------------+
|  > HELLO   : To connect and start                   |
|  > LOCATE  : Locate place by IP (Send IP next)      |
|  > HELP    : Show this help menu                    |
|  > EXIT    : To stop the program                    |
+-----------------------------------------------------+
|  ℹ️  SYNTAX: Separate command and arguments with '|'|
+-----------------------------------------------------+"""

conn, address = server_socket.accept()

def Locate_IP_BY_GEOCODER(Ip_address):
    # Using 'me' fetches your own public IP location
    g = geocoder.ip(Ip_address)

    msg = f"""
    #######################################################
    #                 GEOLOCATION RESULTS                 #
    #######################################################
    #  [IP ADDRESS]  | {Ip_address:<34} #
    # ----------------------------------------------------#
    #  [COUNTRY]     | {g.country:<34} #
    #  [REGION]      | {g.state:<34} #
    #  [CITY]        | {g.city:<34} #
    #  [LAT / LONG]  | {f"{g.lat} , {g.lng}":<34} #
    #######################################################"""
    return msg
    # Or pass a specific IP address

def Locate_IP_BY_IP2Location(Ip_address):
    DB_PATH = "IP2LOCATION-LITE-DB3.BIN/IP2LOCATION-LITE-DB3.BIN"
    database = IP2Location.IP2Location()

    try:
        # 3. Open the file and look up the IP
        database.open(DB_PATH)
        rec = database.get_all(Ip_address)

        msg_return = f"""--- Results for {Ip_address} ---\nCountry: {rec.country_long} ({rec.country_short}) \nRegion/State: {rec.region} \nCity: {rec.city}"""

        return  msg_return
    except Exception as e:
        print(f"An error occurred: {e}")

def Locate_IP_BY_REQUESTS(Ip_address):
     if Ip_address is None:
        return None

     headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
     }
     url = f"https://ip-api.com/json/{Ip_address}"
     response = requests.get(url,headers=headers ,timeout=None).json()

     if response['status'] == 'success':
        return_msg = f"""--- Results for {Ip_address} ---
        \nCountry: {response['country']}
        \nRegion/State: {response['regionName']}
        \nCity: {response['city']}
        \nLat/Lng: ({response['lat']}, {response['lon']}) \n"""
        return return_msg
     list_info = [Ip_address,response['country'],response['regionName'],response['city'],response['lat'],response['lon'] ]
     api_message = response.get('message', 'Unknown API Error')
     return f"Failed to fetch location data. Reason: {api_message}"

def SAVE(Ip_address):
    g = geocoder.ip(Ip_address)
    return [Ip_address, g.country, g.city, g.state, g.lat, g.lng]

def HELLO():

    print("Connected to:", address)

    data = conn.recv(1024).decode()

    if data is None:
        conn.send("".encode())
    Command_split = data.split("|")
    while Command_split[0] != "HELLO":
        msg = ""
        print(Command_split)
        if Command_split[0] == "HELP":
            conn.send(commands_info.encode())
        if Command_split[0] not in Commands_List:
            msg += f"The Command {Command_split[0]} is not in the command list\n"
        if Command_split[0] is None:
            conn.send("".encode())
        conn.send(msg.encode())
        data = conn.recv(1024).decode()
        Command_split = data.split("|")
    else:
        conn.send(commands_info.encode())

def main_server_code():
    HELLO()
    data = conn.recv(1024).decode()
    Command_split = data.split("|")
    while Command_split[0] != "EXIT":
        if Command_split[0] not in Commands_List:
            msg = f"The Command {Command_split[0]} is not in the command list\n"
            conn.send(msg.encode())
        elif Command_split[0] == "HELP":
            conn.send(commands_info.encode())

        elif Command_split[0] == "LOCATE":
            save_in_txt(SAVE("me"))
            IP = Command_split[1]
            save_in_txt(SAVE(IP))
            print(IP)
            if IP == "":
                msg = f"There isn't an IP in command => write the IP after write LOCATE|IP"
                conn.send(msg.encode())
            else:
                #ret = str(Locate_IP_BY_IP2Location(IP))
                #ret = str(Locate_IP_BY_REQUESTS(IP))
                ret = str(Locate_IP_BY_GEOCODER(IP))
                conn.send(ret.encode())

        data = conn.recv(1024).decode()
        Command_split = data.split("|")
    else:
        msg = "Good bye"
        conn.send(msg.encode())
if __name__ == "__main__":
    main_server_code()
