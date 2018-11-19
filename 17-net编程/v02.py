'''
Client端流程
1. 建立通信的socket
2. 发送内容到指定的服务器
3. 接收服务器给定的反馈内容
'''
import socket

def clientFunc():
    # 1. 建立通信的socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 发送内容到指定的服务器
    text = "Do you hunger?"

    # 发送的数据必须是bytes格式
    data= text.encode()

    # 发送,注意对方的地址是tuple类型
    sock.sendto(data, ("127.0.0.1", 7852))

    # 3. 接收反馈
    data, addr = sock.recvfrom(200)
    data = data.decode()
    print(data)

if __name__ == "__main__":
    clientFunc()