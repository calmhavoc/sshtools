import paramiko
import sys
import os

def uploadExecute(ssh, filename):
    # need to check for write access before attempting write action
    sftpClient = ssh.open_sftp()
    sftpClient.put(filename, "/tmp/" + filename)
    ssh.exec_command("chmod a+x /tmp/" + filename)
    ssh.exec_command("nohup /tmp/{} &".format(filename))
    
   
if __name__ == "__main__":
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(sys.argv[1], username=sys.argv[2], password=sys.argv[3])
    uploadExecute(ssh, sys.argv[4])
    ssh.close()
