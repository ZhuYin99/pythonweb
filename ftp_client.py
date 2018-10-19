from socket import * 
import sys 
import time 

#基本文件操作功能
class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd 

    def do_list(self):
        self.sockfd.send(b'L') #发送请求
        #等待回复
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
            print("文件列表展示完毕\n")
        else:
            #由服务器发送失败原因
            print(data)


    def do_get(self,filename):
        self.sockfd.send(('G ' + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            fd = open(filename,'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
            print("%s 下载完毕\n"%filename)
        else:
            print(data)
    def do_set(self,filename):
        try:
            fd = open(filename,'rb')
        except:
            print('文件不存在')
            return
        filename = filename.split('/')[-1]
        self.sockfd.send(('S ' + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            while True:
                data = fd.read(1024)
                if not data:
                    time.sleep(1)
                    data = '##'
                    self.sockfd.send(data.encode())                                    
                    break
                self.sockfd.send(data)
            fd.close()
            print("文件发送完毕")
        else:
            print(data)
            return
         

    def do_quit(self):
        self.sockfd.send(b'Q')

#网络连接
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return 
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)  #文件服务器地址

    sockfd = socket()

    try:
        sockfd.connect(ADDR)
    except:
        print("连接服务器失败")
        return

    ftp = FtpClient(sockfd) #功能类对象
    while True:
        print("========== 命令选项 ===========")
        print("********** list *************")
        print("********* get file **********")
        print("********* set file **********")
        print("********** quit *************")
        print("===============================")

        cmd = input("请输入命令>>")

        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd[:3] == 'get':
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd.strip() == "quit":
            ftp.do_quit()
            sockfd.close()
            sys.exit("谢谢使用")
        elif cmd[:3] == 'set':
            filename = cmd[4:]            
            ftp.do_set(filename) 
        else:
            print("请输入正确命令!!!")
            continue

    
if __name__ == "__main__":
    main()