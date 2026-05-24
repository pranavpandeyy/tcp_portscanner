import socket
import threading
from datetime import datetime

target = input("Enter IP or hostname: ")
startport = int(input("Enter start port: "))
endport = int(input("Enter end port: "))

print(f"\n{'='*50}")
print(f"Scanning: {target}")
print(f"Ports: {startport} - {endport}")
print(f"Started: {datetime.now()}")
print(f"{'='*50}\n")

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        try:
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = sock.recv(1024).decode().strip()
            print(f"[OPEN] Port {port} | {banner[:50]}")
        except:
            print(f"[OPEN] Port {port} | No banner")
    sock.close()

threads = []
for port in range(startport, endport + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\n{'='*50}")
print(f"Scan complete! | {datetime.now()}")
print(f"{'='*50}")
