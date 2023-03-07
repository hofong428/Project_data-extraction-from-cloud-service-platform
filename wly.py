import execjs
import requests

headers = {
    'authority': 'api.wei-liu.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://wei-liu.com',
    'pragma': 'no-cache',
    'referer': 'https://wei-liu.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

def get_token():
    res = requests.get('https://api.wei-liu.com/api/v1/Token/code', headers=headers)
    data = res.json().get('data')
    item1 = data.get('item1')
    item2 = data.get('item2')
    return item1, item2

def login():
    i1, i2 = get_token()
    with open('wly.js', encoding='utf-8') as f:
        js_code = f.read()
    cell = execjs.compile(js_code)
    pwd = cell.call('get_psd',i1,i2,'123456789')
    print(pwd)
    data = {"username": "14568978",
            "password": pwd,
            "code": "",
            "grant_type": "password",
            "userType": 1,
            "language": "zh-CN"}
    response = requests.post('https://api.wei-liu.com/api/v1/Token', headers=headers, json=data)

    print(response.text)
    print(response)

if __name__=='__main__':
    login()

