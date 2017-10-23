
import urllib.request
import json

if __name__ == '__main__':

    url = "https://m.toutiao.com/list/?tag=__all__&ac=wap&count=20&format=json_raw&as=A195492C9A625E6&cp=59CAE255EED66E1&min_behot_time=1506420098"
    headers = []
    agent = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.211.111.36')
    content_type = ("Content-Type","application/json; charset=utf-8")
    ajaxRequest= ("X-Requested-With","XMLHttpRequest")
    refer = ("Referer","https://m.toutiao.com/")
    host = ("Host","m.toutiao.com")
    headers.append(agent)
    headers.append(content_type)
    headers.append(ajaxRequest)
    headers.append(refer)
    opener = urllib.request.build_opener()
    opener.addheaders = headers
    data = opener.open(url).read()

    myjson = json.loads(data)
    result = json.dumps(myjson, ensure_ascii=False)
    print(result)
