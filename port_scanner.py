import socket #This module lets your program talk to networks and open connections to other computers.
import threading 
services = {
    21:"FTP",
    22:"SSH",
    23:"TELNET",
    25:"SMTP",
    53:"DNS",
    80:"HTTP",
    110:"POP3",
    139:"NetBIOS",
    143:"IMAP",
    443:"HTTPS",
    445:"SMB",
    3389:"RDP"
}
high_risk = [21,23,445,3389]

target = input("Enter target IP: ") #Asks user to enter an IP address
start = int(input("Start port: "))
end = int(input("End port: "))

print(f"\nScanning target {target} from {start} to {end}...\n") #Prints a message to the user that the scan is starting.
log = open("scan_log.txt","a")
def scan(port):
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            service = services.get(port, "Unknown")
            if port in high_risk:
                risk="High Risk"
            else:
                risk="LOW Risk"
            print(f"Port {port} OPEN - {service} - {risk}")
            try:
                s.send(b"HEllo\rn")
                banner = s.recv(1024).decode().strip()
                print(f"Banner: {banner}")
            except:
                pass
            log.write(f"{target}:{port} OPEN {service} Risk:{risk}n")
            s.close()
    except:
         pass
for port in range(start, end+1): #This is a loop that scans ports.
     t=threading.Thread(target=scan, args=(port,))
     t.start()
log.close()
print("\nScan Complete.")
   