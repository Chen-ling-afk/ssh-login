#ssh登录
import paramiko
def ssh_command():
    command = input("请输入需要执行的ssh终端命令：")
    return command

def ssh_login(host,username,password,port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while True:
        ssh.connect(host,port,username,password)
        command = ssh_command()
        print(command)
        if command=='exit':
            ssh.close()
            exit()
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode('utf-8'))

if __name__ == '__main__':
    host = input("请输入主机ip:")
    port = input("Port:")
    username = input("Login:")
    password = input("Password:")
    ssh_login(host,username,password,port)