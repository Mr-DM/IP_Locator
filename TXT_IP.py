
def save_in_txt(info):
    if chech_in_txt(info[0]):
        return "IP IN txt"
    with open("IPS_table.txt", "a") as f:
        msg = ""
        for value in info:
            msg += f"{value},"
        f.write(msg + "\n")

    return "IP Saved"


def chech_in_txt(IP):
    dict_IP_info = {}
    with open("IPS_table.txt", "r") as f:
        Slite_line = f.read().split("\n")
        #print(Slite_line)
        for line in Slite_line:
            info = line.split(",")
            dict_IP_info[info[0]] = info[1:]
    if IP in dict_IP_info.keys():
        return True
    return False
