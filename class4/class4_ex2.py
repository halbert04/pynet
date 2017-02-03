import paramiko
from getpass import getpass
import time

rtr2_ip = '184.105.247.71'
username = 'pyclass'
password = getpass()
port = 22

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(rtr2_ip, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)
remote_conn = remote_conn_pre.invoke_shell()

print "\nLogging buffer configuration BEFORE change is"
remote_conn.send("terminal length 0\n")
remote_conn.send("show run | i logging buffer\n")
time.sleep (1)
outp = remote_conn.recv(535)
print outp

remote_conn.send("conf t\n")
print "\nLogging buffer configuration AFTER change is"
remote_conn.send("logging buffer 19999\n")
remote_conn.send("end\n")
remote_conn.send("show run | i logging buffer\n")
time.sleep(1)
outp = remote_conn.recv(535)
print outp
