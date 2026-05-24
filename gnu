import socket
target=input("Enter the id or hostname: ")
startport=int(input("Enter the start port number: "))
endport=int(input("Enter the end port number: "))

printf(f"\Searching {target} from {searchport} to {endport}")

for port in range(startport, endport+1):
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(0.5)
result=sock.connect_ex((target,port))
if result==0:
	printf(f"Port {port} is OPEN")
else
	printf(f"Port {port} is CLOSED")
scan.close()
