import telnetlib
import time
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def login (remote_conn,username,password):
 output = remote_conn.read_until ("sername:",TELNET_TIMEOUT)
 remote_conn.write (username + '\n')
 output = remote_conn.read_until ("ssword:",TELNET_TIMEOUT)
 remote_conn.write (password + '\n')
 return output

def main():
 ip_addr = "184.105.247.70"
 username = "pyclass"
 password = "88newclass"

 remote_conn = telnetlib.Telnet (ip_addr,TELNET_PORT,TELNET_TIMEOUT)

 output = login (remote_conn,username,password)

 time.sleep(1)
 remote_conn.write("show ip int brief" + '\n')
 time.sleep(1)
 output = remote_conn.read_very_eager()
 print output
 return output
 remote_conn.close()
if __name__ == "__main__":
 main()
