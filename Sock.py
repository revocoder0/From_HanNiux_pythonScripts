import socket
print(socket.gethostname())
print(socket.gethostbyname("www.google.com"))

hostname=socket.gethostname()
try:
    ipAddress=socket.gethostbyname_ex(hostname)
    print(ipAddress)
except:
    print("error:....")

try:
    ipAddress=socket.gethostbyname(hostname)
    print(ipAddress)
except:
    print("error:....")