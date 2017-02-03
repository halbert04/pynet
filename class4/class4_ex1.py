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

remote_conn.send("terminal len 0\n")
remote_conn.send("show ver\n")
time.sleep(2)
outp = remote_conn.recv(65535)

print outp
