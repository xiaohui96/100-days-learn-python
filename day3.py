import getpass
username = input('请输入用户名：')
password = input("请输入密码: ")
# 如果希望输入密码时终端没有回显，可以使用getpass模块的getpass函数
if username == 'admin' and password == '123456':
    print("身份验证成功")
else:
    print("身份验证失败")