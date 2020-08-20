from downloader import Downloader
from lxml import etree
class Spider():
    '''
    解析网页，提取数据
    '''
    def parse_data(self):
        downloader = Downloader()
        html = downloader.get_html("PHPSESSID=f47jj9br11fvtld6viktf6gg24")
        html = etree.HTML(html)
        # 商品名字
        names = []
        html_data = html.xpath('//*[@class="hall_box"]//li//span[1]')
        for name in html_data:
            names.append(name.text)

        # 商品交易id
        ids = []
        html_data = html.xpath('//*[@class="hall_box"]//li//@data-single')
        for id in html_data:
            ids.append(id)
            # print(ids)

        # 将商品存到dict
        items = {}
        i = 0
        for id in ids:
            items[id] = names[i]
            i += 1

        return items