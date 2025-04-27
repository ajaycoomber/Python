#import socket library
import socket

#cancel connection after one second of no response for socket objects in script
socket.setdefaulttimeout(0.1)

def grab_banner(ip, port):

        s = socket.socket()
        s.connect_ex((ip, port))
        s.send(b'HEAD / HTTP/1.0\r\n\r\n')
        banner = s.recv(1024)
        s.close()
        return banner


#def identify_service():

def main():

     #Ask user for domain name
        addr = input("Please enter a domain or ip address: ")
        #port = int(input ("Please enter a port: "))

     #Convert domain to ip if necessary
        ip = socket.gethostbyname(addr)

     #Allows for modification of port range
        for port in range(1,1024):

            try:
                #create socket object for each port using IPv4 and TCP protocol
                target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                #attempt to connect to ip/port using target object
                if target.connect_ex((addr, port)) == 0:
                    #print("Open Port: " + str(port))

                    banner = grab_banner(addr, port)

                    print("Website: " + addr)
                    print("Port: " + str(port))
                    for line in banner.decode().splitlines():
                        if line.startswith("Server"):
                            print("Server: " + line[8:])

            #handle connect_ex errors
            except (socket.gaierror, socket.timeout, socket.error, OSError) as e:
                print(e)

        print("Scan finished")

if __name__ == "__main__":
    main()

