#!/bin/env python3

# [code]Box | Andrei A.Abd 2022.
# Source : https://github.com/codeBOX-projects

import termcolor, subprocess , socket, argparse
from geoip import geolite2

#Setup Program Function
def geo_ip_location(host_ip):
    #Introduction & presents
    subprocess.run("clear")
    info_1="""
    █▀▀ █▀▀ █▀█
    █▄█ ██▄ █▄█ vol 0.1\n
    [*] [code]Box | Andrei A.Abd 2022.
    [*] Geolocation & information tool for any available network IP adress.\n
    [*] Source : https://github.com/codeBOX-projects
    [?] Usage:
        Help > python3 geo.py --help
        Exit > ctl+c 
    """
    info_2 = termcolor.colored("[important notice]:",'red')
    info_2_1 = """
    \tOnly use host public name as numbers ex(8.8.8.8), Don't use any privet or string domain name of any website.
    \tFor some resons the result will be not found from some host names, because firewall blocked program from search.
    """     
    #Check if User input Argparser values OR not...
    if host_ip == None:
        print(info_1 + "\n" + info_2 + "\n" + info_2_1)
        #Input user the target public ip
        host_ip = str(input("\n> Enter Host IP number: "))
        while True:
            if host_ip == "":
                host_ip = str(input("\n> Enter Host IP number: "))               
            else:
                #Cashed veriable:
                locate_host_ip = geolite2.lookup(host_ip)
                #Summary information:
                print("\n[*] Searching for target IP address [", locate_host_ip.ip, "]:")
                #Get host by name:
                print("\n[+] Target Host name: ", termcolor.colored(socket.gethostbyaddr(locate_host_ip.ip)[0], 'green'))
                #find Country:
                print("[+] Target Country: ", termcolor.colored(locate_host_ip.country, 'green'))
                #find Subdivisions:
                print("[+] Target Sub Divisions: ", termcolor.colored(locate_host_ip.subdivisions, 'green'))
                #find correct Timezone:
                print("[+] Target Timezone: ", termcolor.colored(locate_host_ip.timezone, 'green'))
                #find target geolocation:
                print("[+] Target Location: " + "[latitude = ", termcolor.colored(locate_host_ip.location[0], 'green') + "]" + "[longitude = ", termcolor.colored(locate_host_ip.location[1], 'green') + "]")
                break
    
    else:
        print(info_1 + "\n" + info_2 + "\n" + info_2_1)
        #Input args value - target public ip
        host_ip = args.host_ip
        #Cashed veriable:
        locate_host_ip = geolite2.lookup(host_ip)
        #Summary information:
        print("\n[*] Searching for target IP address [", locate_host_ip.ip, "]:")
        #Get host by name:
        print("\n[+] Target Host name: ", termcolor.colored(socket.gethostbyaddr(locate_host_ip.ip)[0], 'green'))
        #find Country:
        print("[+] Target Country: ", termcolor.colored(locate_host_ip.country, 'green'))
        #find Subdivisions:
        print("[+] Target Sub Divisions: ", termcolor.colored(locate_host_ip.subdivisions, 'green'))
        #find correct Timezone:
        print("[+] Target Timezone: ", termcolor.colored(locate_host_ip.timezone, 'green'))
        #find target geolocation:
        print("[+] Target Location: " + "[latitude = ", termcolor.colored(locate_host_ip.location[0], 'green') + "]" + "[longitude = ", termcolor.colored(locate_host_ip.location[1], 'green') + "]")

#start program....
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=termcolor.colored("[important notice]: Only use host public name as numbers ex(8.8.8.8), " 
                                                "Don't use any privet or string domain name of any website.\n\tFor some " 
                                                "resons the result will be not found from some host names, because firewall "
                                                "blocked program from search.", 'white'))
    parser.add_argument("-H", "--host-ip",type=str, help="type target ip ex: 8.8.8.8")
    # parse arguments
    args = parser.parse_args()
    host_ip = args.host_ip
    try:
        while True:
            geo_ip_location(host_ip)
            ask_user = str(input(termcolor.colored("\n> Do you want to search again? y/n: " ,'green')))
            if ask_user == 'y' or ask_user == 'yes' or ask_user == 'Y':
                host_ip = None
                geo_ip_location(host_ip)
                continue
            elif ask_user == 'n' or ask_user == 'no' or ask_user == 'N':
                break
            elif ask_user == "":
                ask_user = str(input(termcolor.colored("\n> Do you want to search again? y/n: " ,'green')))

    except:
        #Echo errors and exit:
        print(termcolor.colored("\n[!] Exception has occurred: no result found.", 'red'))