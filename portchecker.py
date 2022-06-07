import socket
import threading
import concurrent.futures
from colorama import Fore, init

print_lock = threading.Lock()

init()
cgreen = Fore.GREEN
reset = Fore.RESET
cred = Fore.RED
cdef = Fore.WHITE
chost = Fore.LIGHTBLUE_EX

def singlechekport(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True

def checkport(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.close()
        with print_lock:
            print(f"{cgreen}{host}:{port} is open {reset}")
    except:
        pass

host = input("Enter a host:")
while True:
    print(f"\nHost is: {chost}{host} {reset}")    
    chs = input(f"1. Definite Port\n2. Port in range\n3. Change host\n4. Exit\n")
    match chs:
        case '1':
            tport = input("Enter a port:")
            for port in range(int(tport), int(tport) + 1):
                if(singlechekport(host, port)):
                    print(f"{cgreen}{host}:{port} is open {reset}")
                else:
                    print(f"{cred}{host}:{port} is closed {reset}")
        case '2':
            r1 = input("From (1-65535):")
            r2 = input("To (1-65535):")
            if(int(r1) < 0 or int(r2) > 65535 or (r1 > r2)):
                print("Incorrent value!")
            else:
                with concurrent.futures.ThreadPoolExecutor(max_workers=777) as executor:
                    for port in range(int(r1), int(r2)):
                        executor.submit(checkport, host, port)  
        case '3':
            host = input("Enter a host:")
        case '4':
            break