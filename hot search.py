import requests
from lxml import etree
headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'Host': 'top.baidu.com',
            'Upgrade-Insecure-Requests': '1',
      }
# 获取百度热榜
bd_hot_url = 'https://top.baidu.com/board?tab=realtime'
response = requests.get(bd_hot_url,headers = headers)
html = etree.HTML(response.text)
bd_hot_block = html.xpath("//div[contains(@class,'category-wrap_iQLoo')]")
writeTXT=open(r'D:\output.txt','a')

#writeTXT.write(response.text)
for single in bd_hot_block:
    # 获取标题
    title = single.xpath('string(.//div[@class="c-single-text-ellipsis"]/text())')
    print('标题是：{}'.format(title))
    # 获取链接
    url = single.xpath('string(./a/@href)')
    print('链接是：{}'.format(url))
    # 获取热搜排名
    rank = single.xpath('string(./a/div/text())')
    print('排名是：{}'.format(rank))
    # 获取图片地址
    pic = single.xpath('string(./a/img/@src)')
    print('图片地址是：{}'.format(pic))
    # 获取热搜指数hot-index
    zhishu = single.xpath('string(.//div[contains(@class,"hot-index_1Bl1a")]/text())')
    print('热搜指数是：{}'.format(zhishu))
    # 获取简介hot-desc
    desc = single.xpath('string(.//div[contains(@class,"hot-desc")]/text())')
    print('描述是：{}'.format(desc))

    writeTXT.write('\n'+'标题是：'+title)
    writeTXT.write('\n'+'链接是：'+url)
    #writeTXT.write('\n'+'排名是：'+rank)
    #writeTXT.write('\n'+'图片地址是：'+pic)
    #writeTXT.write('\n'+'热搜指数是：'+zhishu)
    #writeTXT.write('\n'+'描述是：'+desc)




#writeTXT.write('abcdefgh')


writeTXT.close()

