from datetime import date
from http.server import HTTPServer
from multiprocessing.pool import ApplyResult
import socket
from re import search
import time

def GetBanner(addr, port):
        bannergrab = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        try:
            bannergrab.connect((addr, port))
            data = 'WhoAreYou\r\n'
            bannergrab.send(data.encode())
            banner = bannergrab.recv(2048)
            try:
                output = banner.decode(encoding='unicode_escape')
                #print(output)
            except UnicodeDecodeError:
                return ''
            if 'Server:' in output:
                Web = output.split('\n')
                Web1 = Web[1]
                Web2 = Web[2]
                if "Server:" in Web1:
                    http = Web2.lstrip('Server:')
                    httpServerSplit = http.split(' ')
                    httpServer = httpServerSplit[1]
                    if '2.4.49' in httpServer:
                        return('- %s **VULNERABLE**' % (httpServer))
                    elif '2.4.50' in httpServer:
                        return('- %s **VULNERABLE**' % (httpServer))
                    else:
                        return('- %s' % (httpServer))
                elif "Server:" in Web2:
                    http = Web2.lstrip('Server:')
                    httpServerSplit = http.split(' ')
                    httpServer = httpServerSplit[1]
                    if '2.4.49' in httpServer:
                        return('- %s **VULNERABLE**' % (httpServer))
                    elif '2.4.50' in httpServer:
                        return('- %s **VULNERABLE**' % (httpServer))
                    else:
                        return('- %s' % (httpServer))
            if "SSH" in output:
                ssh = str(output.split('\n'))
                #sshVer = ssh.split(' ')
                ssh1 = ssh[0]
                SecShell = ssh1[2:]
                return('- %s' % (SecShell))
            if "220" in output:
                ftp = output.split('\n')
                set1 = ftp[0]
                FTP = set1.lstrip('220 ')
                return('- %s' % (FTP))
        except ConnectionRefusedError:
            return ''
        except ConnectionResetError:
            return ''
        except TimeoutError:
            return ''

#GetBanner('192.168.1.13', 80)

def Logo():
    print('*******************************************************************')
    print('**   ________ __       __        __    __ __    __ __       __   **')      
    print('**  |        \  \    /  \      |  \  |  \  \  |  \  \     /      **')
    print('**  | ▓▓▓▓▓▓▓▓\▓▓\  /  ▓▓      | ▓▓\ | ▓▓ ▓▓  | ▓▓ ▓▓\   /  ▓▓   **')     
    print('**  | ▓▓__     \▓▓\/  ▓▓ ______| ▓▓▓\| ▓▓ ▓▓  | ▓▓ ▓▓▓\ /  ▓▓▓   **')     
    print('**  | ▓▓  \     \▓▓  ▓▓ |      \ ▓▓▓▓\ ▓▓ ▓▓  | ▓▓ ▓▓▓▓\  ▓▓▓▓   **')     
    print('**  | ▓▓▓▓▓      \▓▓▓▓   \▓▓▓▓▓▓ ▓▓\▓▓ ▓▓ ▓▓  | ▓▓ ▓▓\▓▓ ▓▓ ▓▓   **')     
    print('**  | ▓▓_____    | ▓▓          | ▓▓ \▓▓▓▓ ▓▓__/ ▓▓ ▓▓ \▓▓▓| ▓▓   **')     
    print('**  | ▓▓     \   | ▓▓          | ▓▓  \▓▓▓\▓▓    ▓▓ ▓▓  \▓ | ▓▓   **')     
    print('**   \▓▓▓▓▓▓▓▓    \▓▓           \▓▓   \▓▓ \▓▓▓▓▓▓ \▓▓      \▓▓   **')     
    print('**                                                               **')
    print('**                                                               **')
    print('**                       BY CT CYBER TEAM                        **')
    print('**                                                               **')
    print('*******************************************************************') 

def Version(ProgVer, Date):
    print(' ')
    print('                        Version: ALPHA %s' % (ProgVer))
    print('                   Last Revised: %s' % (Date))
    print(' ')

def AllPorts():
    for i in range(1,65535):
        return(i)

def PercentComplete(port, portnum, integer = False):
    percent = port / portnum * 100

    if integer:
        return ' Progress Check: %s%i' % ('%',int(percent))
    return (' Progress Check: %s%.2f' % ('%',float(round(percent, 2))))
