from bs4 import BeautifulSoup
import requests, prettytable


t = prettytable.PrettyTable(['地區','氣溫'], encoding = 'utf-8')
# t.align['地區'] = 'c'
# t.align['氣溫'] = 'c'

r1 = requests.get('https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html?ID=Wed%20Mar%2008%202023%2023:22:57%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)')
b1=BeautifulSoup(r1.text,'html.parser')
# 標籤:<th scope="row">地區, <span class="tem-C is-active">氣溫

for rows in b1.find_all('tr'):

    tem = rows.find_all("span")
    cit = rows.find_all('th')
    temperature = tem[0].text.strip()
    city = cit[0].text.strip()
    t.add_row([city,temperature])
    
print(t)

