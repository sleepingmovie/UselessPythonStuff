import socket
from colorama import Fore, init

init()
cgreen = Fore.GREEN
reset = Fore.RESET
cred = Fore.RED
cdef = Fore.WHITE
chost = Fore.LIGHTBLUE_EX

def checkport(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True

host = input("Enter a host:")
while True:
    print(f"\nHost is: {chost}{host} {reset}")    
    chs = input(f"1. Definite Port\n2. Port in range\n3. Change host\n4. Exit\n")
    match chs:
        case '1':
            tport = input("Enter a port:")
            for port in range(int(tport), int(tport) + 1):
                if(checkport(host, port)):
                    print(f"{cgreen}{host}:{port} is open {reset}")
                else:
                    print(f"{cred}{host}:{port} is closed{reset}")
        case '2':
            r1 = input("From:")
            r2 = input("To:")
            if(int(r1) < 0 or int(r2) > 65535):
                print("Incorrent value!")
            else:  
                for port in range(int(r1), int(r2) + 1):
                    if(checkport(host, port)):
                        print(f"{cgreen}{host}:{port} is open {reset}")
                    else:
                        print(f"{cred}{host}:{port} is closed{reset}")
        case '3':
            host = input("Enter a host:")
        case '4':
            break