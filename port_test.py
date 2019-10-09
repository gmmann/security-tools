import socket
port_test = '22'
ip_test = '192.168.69.9'
def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        http_open = 'True'
        print(http_open)
        return True
   except:
        http_open = 'False'
        return False
        print(http_open)

isOpen(ip_test, port_test)
