import geocoder

import TXT_IP
from TXT_IP import save_in_txt

Ip_address = "2.2.2.2"
g = geocoder.ip(Ip_address)
msg =  f"""--- Results for {Ip_address} ---\nCountry: {g.country} \nRegion/State: {g.state} \nCity: {g.city} \nLat: {g.lat}"""
list_info = [Ip_address,g.country,g.city,g.state,g.lat, g.lng]
print(save_in_txt(list_info))

def Locate_IP(Ip_address):
    # Using 'me' fetches your own public IP location

    pass


    # Or pass a specific IP address
    #DB_PATH = "IP2LOCATION-LITE-DB3.BIN/IP2LOCATION-LITE-DB3.BIN"
    #database = IP2Location.IP2Location()

    #try:
    #    # 3. Open the file and look up the IP
    #    database.open(DB_PATH)
    #    rec = database.get_all(Ip_address)

    #    msg_return = f"""--- Results for {Ip_address} ---\nCountry: {rec.country_long} ({rec.country_short}) \nRegion/State: {rec.region} \nCity: {rec.city}"""

    #    return  msg_return
    #except Exception as e:
    #    print(f"An error occurred: {e}")

     #if Ip_address is None:
        #    return None

        #headers = {
        #    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        #}
        #url = f"https://ip-api.com/json/{Ip_address}"
        #response = requests.get(url,headers=headers ,timeout=None).json()

        #if response['status'] == 'success':
        #    return_msg = f"""--- Results for {Ip_address} ---
        #    \nCountry: {response['country']}
        #    \nRegion/State: {response['regionName']}
        #    \nCity: {response['city']}
        #    \nLat/Lng: ({response['lat']}, {response['lon']}) \n"""
        #    return return_msg

        #api_message = response.get('message', 'Unknown API Error')
        #return f"Failed to fetch location data. Reason: {api_message}"
