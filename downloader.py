import requests
class Downloader():
    '''
    获取网页html并返回
    '''
    def get_html(self, cookie):
        url = "https://www.lezhuan.com/weapon/trade.php"
        headers = {
            "Host": "www.lezhuan.com",
            "Connection": "keep-alive",
            # Content-Length: 68,
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://www.lezhuan.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            # Referer: https://www.lezhuan.com/fast/insert.php?fastNO=1468717
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": cookie,
        }
        # 查看当前交易大厅的所有交易信息
        res = requests.post(url, headers=headers)
        html = res.text.encode('iso-8859-1').decode('gbk')
        return html