import requests
import json
import os
from bs4 import BeautifulSoup

n = str(input('請輸入想搜尋的: '))
page = int(input('請輸入頁數: '))
url = f'https://pic.sogou.com/napi/pc/searchList?mode=1&start={page}&xml_len=48&query={n}'

# 發送請求獲取 JSON 格式的回應
response = requests.get(url).json()

# 創建目錄以保存圖片
if not os.path.exists(n):
    os.makedirs(n)

# 遍歷 items 並下載圖片
for item in response['data']['items']:
    # 獲取圖片的文件名和 URL
    fname = item['title']
    url1 =  item['picUrl']
    filepath = os.path.join(n, fname + '.png')
    
    try:
        # 判斷文件是否已存在，若存在則刪除原文件
        if os.path.exists(filepath):
            os.remove(filepath)
        
        # 下載圖片並保存到目錄中
        img_data = requests.get(url1, timeout=5).content
        with open(filepath, 'wb') as handler:
            handler.write(img_data)
            print(f"下載完成: {fname}.png")
    except Exception as e:
        print(f"下載圖片 {fname}.jpg 時發生錯誤: {e}")
        continue
print('全部完成了')
