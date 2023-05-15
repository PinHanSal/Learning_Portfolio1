import requests, json
import prettytable
keyword = input('關鍵字:')

t=prettytable.PrettyTable(['商品名稱','價格'], encoding='utf-8')
t.align['商品名稱'] = 'l'
t.align['價格'] = 'l'
#for p in range(1, int(page)):
page = 1
while page != '0':
    r1 = requests.get('https://ecshweb.pchome.com.tw/search/v3.3/all/results',
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
            },
    params={
    'page': page,
    'q': keyword,
            })
    d = json.loads(r1.text)


    for i in range(0, len(d['prods']), 1):
        t.add_row([d['prods'][i]['name'], d['prods'][i]['price']])
    print(t)
    page_str = int(input('前往頁碼:'))
    page = page_str
    t.clear_rows()

