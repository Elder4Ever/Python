from distutils.version import Version
import os
import argparse
from pyclbr import Function
import time
import random
import socket
import ipaddress
import urllib.request
import http.client
import datetime
from datetime import datetime
import EYFUNC


if 'nt' in os.name:
    os.system('cls')
else:
    os.system('clear')

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='EXAMPLE #1: python3 ey-num.py 192.168.1.1 --P 22 --V --O')
gp = parser.add_mutually_exclusive_group(required=True)
gp.add_argument('target', action='store', nargs='?', const='', help="This will be the target ip. i.e: 192.168.0.1 or 192.168.0.1/24")

group1 = parser.add_argument_group(description='Optional:')
group1.add_argument('--D', '--delay', type=int, default=0, help="Delay time between each Ping. Can be used inconjunction with the --Jitter flag.")
group1.add_argument('--J', '--jitter', type=int, default=0, help="Random Jitter between pings. Can be used with or without the --Delay flag.")
group1.add_argument('--T', '--timeout', type=int, default=1, help="Set this flag to speed up the scan or slow it down")
group1.add_argument('--B', '--Banner', action='store_true', help="Banner grabbing to find versions of software.") #WORK ON THIS
group1.add_argument('--O', '--OS', action='store_true', help="Banner grabbing to find versions of software.") #WORK ON THIS
group1.add_argument('--C', '--common-ports', action='store_true', help="Scans all common ports") #WORK ON THIS
group1.add_argument('--P', '--port', type=int, nargs='*', help="Select ports that are not as common")
group1.add_argument('--A', '--all', action='store_true', help="Select ports that are not as common")
group1.add_argument('--V', '--Version', action='store_true', help="Grab the Build Version of EY-NUM") #WORK ON THIS

args = parser.parse_args()

##UNCOMMENT BELOW COMMAND TO DEBUG##
print('DEBUGGER: %s' % (parser.parse_args()))

if args.V:
    EYFUNC.Logo()
    EYFUNC.Version("0.1", 'June 20, 2022')

if args.O:
    def GetTTL(addr):
        result = os.popen("ping -c 1 "+addr).read()
        n = result.find("ttl=")
        if n >= 0:
            ttl = result[n+4:]
            n = ttl.find(" ")
            if n > 0:
                return int(ttl[:n])
        return -1
    
if args.target:
    octet = args.target
    octet0 = octet.split('.')
    octet1 = int(octet0[0])
    octet2 = int(octet0[1])
    octet3 = int(octet0[2])
    lastoctet = octet0[3].split('/')
    octet4 = int(lastoctet[0])
    delay = args.D
    jitter = args.J
    ComPorts = args.C
    Ports = args.P
    timeout = args.T
    now = datetime.now()
    dt_string = now.strftime('%m/%d/%Y %H:%M:%S')
    commonPorts = {
                    20:"FTP", 
                    21:"FTP",
                    22:"SSH", 
                    23:"Telnet",
                    25:"SMTP",
                    53:"DNS",
                    80:"HTTP",
                    110:"POP3",
                    135:"Microsoft-RPC",
                    139:"NETBIOS",
                    143:"IMAP",
                    369:"LDAP",
                    443:"HTTPS",
                    445:"Microsoft-DS",
                    465:"SMTP",
                    587:"SMTP",
                    636:"LDAPS",
                    993:"IMAPS",
                    995:"POP3",
                    1194:"",
                    1723:"PPTP",
                    3306:"MYSQL",
                    3389:"RDP",
                    5900:"VNC",
                    8080:"HTTP-PROXY",
                    32400:"PLEX"
                    }

    EYFUNC.Logo()                                                            
                                                                    
    print('Current Scan Started at %s' % (dt_string))



    try:
        cidr = int(lastoctet[1])
    except IndexError:
        cidr = 'null'
    
    if cidr == 'null':
        ip = "%s.%s.%s.%s" % (octet1, octet2, octet3, octet4)
        response = os.system("ping -c 1 " + ip + " > null")
        if response == 0:
            if args.O:
                ttl_result = GetTTL(ip)
                if ttl_result:
                    if ttl_result <= 64 and ttl_result > 32:
                        print('* * * * * (Possible OS: Linux/Unix) - TTL %s' % (ttl_result))
                    elif ttl_result <= 128 and ttl_result > 96:
                        print('* * * * * (Possible OS: Windows) - TTL %s' % (ttl_result))
                    elif ttl_result <= 255 and ttl_result > 223:
                        print('* * * * * (Possible OS: Solaris/AIX) - TTL %s' % (ttl_result))
                    else:
                        print('') 
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            try:
                hostname = socket.gethostbyaddr('%s' % (ip))
                hostname = hostname[0]
            except socket.herror:
                hostname = 'Unknown'
            print('IP ADDRESS: %s (%s) - ACTIVE' % (ip, hostname))
            print('')
            if args.C and args.target:
                portlist = []
                for c,n in commonPorts.items():
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    result = sock.connect_ex((str('%s' % (ip)), c))
                    sock.close()
                    print(c)
                    if result == 0:
                        portlist.append(result)
                        if n == "":
                            n = "UNKNOWN"
                        if args.B:
                            print("     %i[%s]: Open %s" % (c, n, EYFUNC.GetBanner(ip, c)))
                        else:    
                            print("     %i[%s]: Open " % (c, n))
                        if delay:
                            time.sleep(delay)  # Time Delay
                        if jitter:
                            time.sleep(random.randint(1, jitter))  # Time Jitter
                print(' ')
                if (len(portlist) < 1):
                    print('No Common Ports Are Open')
                    print(' ')

            if args.P and args.target:
                portlist = []
                for p in args.P:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    result = sock.connect_ex((str('%s' % (ip)), p))
                    sock.close()
                    if result == 0:
                        try:
                            x = commonPorts.get(p)
                        except NameError:
                            x = "Unknown"
                        portlist.append(result)
                        if args.V:
                            print("     %i[%s]: Open %s " % (p, x, EYFUNC.GetBanner(ip, p)))
                        else:    
                            print("     %i[%s]: Open " % (p, x))
                        if delay:
                            time.sleep(delay)  # Time Delay
                        if jitter:
                            time.sleep(random.randint(1, jitter))  # Time Jitter
                    else:
                        try:
                            x = commonPorts.get(p)
                        except NameError:
                            x = "Unknown"
                            #print("     %i[%s]: Closed " % (p, x))
                    print(' ')
                if (len(portlist) < 1):
                    print('     The Port(s) Selected Are Not Open')
                    print(' ')

            if args.A and args.target:
                portlist = []
                for i in range(1, 65535):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    result = sock.connect_ex((str('%s' % (ip)), int(i)))
                    sock.close()
                    #print (i)
                    if i%100==0:
                        print('     ------- Port %s%s' % (int(i),EYFUNC.PercentComplete(i, 65535)))
                    if result == 0:
                        #print('true')
                        x = commonPorts.get(i)
                        portlist.append(result)
                        if args.V:
                            print("     %i[%s]: Open %s " % (i, x, EYFUNC.GetBanner(ip, i)))
                        else:    
                            print("     %i[%s]: Open " % (i, x))
                        if delay:
                            time.sleep(delay)  # Time Delay
                        if jitter:
                            time.sleep(random.randint(1, jitter))  # Time Jitter
                        #try:
                        #    x = commonPorts.get(i)
                        #    print("     %i[%s]: Closed " % (i, x))
                        #except NameError:
                        #    x = "Unknown"
                        #    print("     %i[%s]: Closed " % (i, x))
                print(' ')
                if (len(portlist) < 1):
                            print('     The Port(s) Selected Are Not Open')
                            print(' ')
        else:
            print("Doesn't Seem Like %s is Online." % (ip))

    if cidr == 24:
        for a in range(1, 255):
            ip = "%i.%i.%i.%d" % (octet1, octet2, octet3, a)
            response = os.system("ping -c 1 " + ip + " > null")
            if response == 0:
                if args.O:
                    ttl_result = GetTTL(ip)
                    if ttl_result:
                        if ttl_result <= 64 and ttl_result > 32:
                            print('* * * * * (Possible OS: Linux/Unix) - TTL %s' % (ttl_result))
                        elif ttl_result <= 128 and ttl_result > 96:
                            print('* * * * * (Possible OS: Windows) - TTL %s' % (ttl_result))
                        elif ttl_result <= 255 and ttl_result > 223:
                            print('* * * * * (Possible OS: Solaris/AIX) - TTL %s' % (ttl_result))
                        else:
                            print('') 
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout)
                try:
                    hostname = socket.gethostbyaddr('%s' % (ip))
                    hostname = hostname[0]
                except socket.herror:
                    hostname = 'Unknown'
                print('IP ADDRESS: %s (%s) - ACTIVE' % (ip, hostname))
                print('')
                if args.C or args.target:
                    portlist = []
                    for c,n in commonPorts.items():
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(timeout)
                        result = sock.connect_ex((str('%s' % (ip)), c))
                        sock.close()
                        if result == 0:
                            portlist.append(result)
                            if n == "":
                                n = "UNKNOWN"
                            if args.B:
                                print("     %i[%s]: Open %s " % (c, n, GetBanner(ip, c)))
                            else:    
                                print("     %i[%s]: Open " % (c, n))
                            if delay:
                                time.sleep(delay)  # Time Delay
                            if jitter:
                                time.sleep(random.randint(1, jitter))  # Time Jitter
                    print(' ')
                    if (len(portlist) < 1):
                        print('No Common Ports Are Open')
                        print(' ')

                if args.P:
                    portlist = []
                    for p in args.P:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(timeout)
                        result = sock.connect_ex((str('%s' % (ip)), p))
                        sock.close()
                        if result == 0:
                            try:
                                x = commonPorts.get(p)
                            except NameError:
                                x = "Unknown"
                            portlist.append(result)
                            if args.V:
                                print("     %i[%s]: Open %s " % (p, x, GetBanner(ip, p)))
                            else:    
                                print("     %i[%s]: Open " % (p, x))
                            if delay:
                                time.sleep(delay)  # Time Delay
                            if jitter:
                                time.sleep(random.randint(1, jitter))  # Time Jitter
                        else:
                            try:
                                x = commonPorts.get(p)
                            except NameError:
                                x = "Unknown"
                                #print("     %i[%s]: Closed " % (p, x))
                        print(' ')
                    if (len(portlist) < 1):
                        print('     The Port(s) Selected Are Not Open')
                        print(' ')
            else:
                print("Doesn't Seem Like %s is Online." % (ip))

    if cidr == 16:
        for a in range(1,255):
            for b in range(1,255):
                ip = "%i.%i.%d.%d" % (octet1, octet2, a, b)
                response = os.system("ping -c 1 " + ip + " > null")
                if response == 0:
                    print('IP Address: %s is Online' % (ip))
                time.sleep(delay)  # Time Delay
                time.sleep(random.randint(1, jitter))  # Time Jitter

    if cidr == 8:
        for a in range(1,255):
            for b in range(1,255):
                for c in range(1,255):
                    ip = "%i.%d.%d.%d" % (octet1, a, b, c)
                    response = os.system("ping -c 1 " + ip + " > null")
                    if response == 0:
                        print('IP Address: %s is Online' % (ip))
                    time.sleep(delay)  # Time Delay
                    time.sleep(random.randint(1, jitter))  # Time Jitter
elif args.target is None and args.P:
    now = datetime.now()
    dt_string = now.strftime('%m/%d/%Y %H:%M:%S')
    
    EYFUNC.Logo()                                                           
    print('')                                                                
    print('Current Scan Started at %s' % (dt_string))
    print('')
    print('No Target Selected')
    print('')
elif args.target is None and args.C:
    now = datetime.now()
    dt_string = now.strftime('%m/%d/%Y %H:%M:%S')

    EYFUNC.Logo()                                                            
    print('')                                                                
    print('Current Scan Started at %s' % (dt_string))
    print('')
    print('No Target Selected')
    print('')
