import socket
ip = input("Enter IP address: ")
start_port = int(input("Enter starting port number: "))
end_port  = int(input("Enter ending port number: "))

def port_scan(ip, start_port, end_port):
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port+1):
         s = socket.socket()
         s.settimeout(0.5)
         result = s.connect_ex((ip, port))
         if result == 0:
            print(f"Port {port} is open")
         s.close()

port_scan(ip,start_port,end_port)