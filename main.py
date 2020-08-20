from spider import Spider
import time
from postman import Post_man
from random import randint
'''

主函数，主要逻辑代码
'''

def main():
    spider = Spider()
    postman = Post_man()
    ids = []
    while(True):
        # 追踪数据列表
        target_data = ["梦蝶","幽篁伞","混元金斗","五火七禽扇","九龙神火罩"]
        # 交易所数据
        data = spider.get_data()
        for key in data.keys():
            if key in ids:
                break;
            if data[key] in target_data:
                message = "["+str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)+"]"+data[key]
                print(message, end="\n")
                postman.send_email(message)
                ids.append(key)
        time.sleep(randint(4, 8))

main()