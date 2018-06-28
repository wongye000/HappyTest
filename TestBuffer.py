# encoding=utf-8
import telnetlib
import time
import datetime
import re
import xlwt

def do_TestBuffer(Host, username, password, finish, commands):

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

def do_WriteResult(file_path,result):
    with open(file_path,"a") as f:
        f.write(result)

def process_data(file_path):
    #处理数据文件，获取需要的数值
    with open(file_path, "r") as f:
        data_all = f.readlines()
    data_result = [re.split(r"[\s]+", i) for i in data_all if re.search(r"buffers/cache", i)]
    bufferArray = [x[2][0:] for x in data_result]
    return bufferArray

if __name__ == '__main__':
    # 配置选项
    Host = '192.168.2.1'  # Telnet服务器IP
    username = 'root'  # 登录用户名
    password = '123456'  # 登录密码
    finish = '# '  # 命令提示符
    commands = ['free -m'] #设置命令

    #设置文件名，日期用以区分
    t = datetime.date.today()
    file_path = "c:/log/buffer%s.txt" % t

    #设置循环次数和间隔时间
    for i in range(5):
        result = do_TestBuffer(Host, username, password, finish, commands)
        do_WriteResult(file_path,result)
        time.sleep(5)
    print process_data(file_path)

