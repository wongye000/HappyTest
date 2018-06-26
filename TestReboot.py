# encoding=utf-8
import telnetlib
import time

def do_reboot(Host, username, password, finish, commands):
    for i in range(10):
        # 连接Telnet服务器
        tn = telnetlib.Telnet(Host, port=9086, timeout=10)
        tn.set_debuglevel(2)

        # 输入登录用户名
        tn.read_until('Ambarella login: ')
        tn.write(username + '\n')

        # 输入登录密码
        tn.read_until('Password: ')
        tn.write(password + '\n')

        # 登录完毕后执行命令
        tn.read_until(finish)

        for command in commands:
            tn.write(command + '\n')

        time.sleep(60)

        # tn.read_until(finish)
        # tn.close()  # tn.write('exit\n')


if __name__ == '__main__':
    # 配置选项
    Host = '192.168.2.1'  # Telnet服务器IP
    username = 'root'  # 登录用户名
    password = '123456'  # 登录密码
    finish = '# '  # 命令提示符
    commands = ['shutdown -r now'] #设置命令
    do_reboot(Host, username, password, finish, commands)