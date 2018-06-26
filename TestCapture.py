# encoding=utf-8
import telnetlib
import time
import os
import datetime

def do_TestCapture(Host, username, password, finish, commands):

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
    time.sleep(5)
    result = tn.read_very_eager()
    return(result)



if __name__ == '__main__':
    # 配置选项
    Host = '192.168.2.1'  # Telnet服务器IP
    username = 'root'  # 登录用户名
    password = '123456'  # 登录密码
    finish = '# '  # 命令提示符
    commands = ['ls /tmp/capture/ | wc -l'] #设置命令

    t = datetime.date.today()
    name_test = "c:/log/CaptureTest%s" % t
    test_dir = os.mkdir(name_test)

    #设置循环
    for i in range(1,4):
        top_read = do_TestCapture(Host, username, password, finish, commands)
        with open("%s/CaptureTest.txt" % name_test,"a") as f:
            f.write(("test%d %s: " + top_read) % (i,datetime.datetime.now()))
        time.sleep(10)