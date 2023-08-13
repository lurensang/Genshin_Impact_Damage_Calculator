#-*- coding = utf-8 -*-

from bs4 import BeautifulSoup           # 网页解析，获取数据
import re                               # 正则表达式，进行文字匹配
import urllib.request, urllib.error     # 制定URL获取网页数据

find_talent_description = re.compile(r'<span class="obc-tmpl__icon-text">(.*?)</span> <!----></div></h3> <pre class="obc-tmpl__paragraph-box obc-tmpl__pre-text">')
find_rate_num = re.compile(r'(\d+\.?\d*)', re.M)

# 得到指定一个URL的网页内容
def askURL(url):
    # 获取头部信息：网页F12-Network-刷新然后停止，点击最前面的阶段，选择唯一一项，拉到最下面能看见user-agent
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}    # 用户代理 模仿浏览器头部信息向服务器发消息
    request = urllib.request.Request(url, headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:  # 检查错误
        if hasattr(e, "code"):      # has attribute 判断是否包含属性
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

# 从网页爬取角色倍率数据
def fatch_traveler_data(web_id):
    base_url = ["https://bbs.mihoyo.com/ys/obc/content/", "/detail?bbs_presentation_style=no_header"]
    url = base_url[0] + str(web_id) + base_url[1]
    
    # 爬取网页
    html = askURL(url)

    skills_tab_pos = []
    soup = BeautifulSoup(html, "html.parser")
    skill_attr_block = soup.find_all('li', class_ = "obc-tmpl__switch-item", attrs={"data-target": "skill.attr"})
    all_rates = [0]*len(skill_attr_block)

    skills_tab_pos = [0, 1, 2, 6, 7, 11, 12]
    for skill in skills_tab_pos:      # 符合要求的字符串
        item = skill_attr_block[skill]
        data = item.find_all('div', class_ = "obc-tmpl__scroll-x-wrapper")[0].div.table.tbody.find_all('tr')
        all_rates[skill] = []
        for seg in range(len(data)-1):
            all_rates[skill].append([])
            vals = data[seg].find_all('td')
            for lv in range(len(vals)-1):
                rate_temp_str = vals[lv+1].string
                rate_temp_num_str = re.findall(find_rate_num, rate_temp_str)
                if len(rate_temp_num_str) == 1:
                    rate_temp_num = float(rate_temp_num_str[0])
                else:
                    rate_temp_num = []
                    for i in rate_temp_num_str:
                        rate_temp_num.append(float(i))
                all_rates[skill][seg].append(rate_temp_num)
    while 0 in all_rates:
        all_rates.remove(0)
    return all_rates