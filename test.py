import urllib2, urllib, cookielib
from weibo import APIClient

app_key = "123954073"
app_secret = "54a668937f1b58ebe4888697332a14fe"
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
cookie = "SINAGLOBAL=2504826777148.9917.1370037816124; _ga=GA1.2.1410165789.1374270762; SSOLoginState=1395713153; _s_tentry=login.sina.com.cn; Apache=2690913113765.4185.1395713161921; ULV=1395713161931:25:5:1:2690913113765.4185.1395713161921:1394826679691; wvr=5; UOR=,,news.cnfol.com; JSESSIONID=A146654237E29EB142C5928A64A7442A; SUS=SID-2129325272-1396982333-JA-hmg03-3ff37984372d31e6e2eb4e05846f9998; SUE=es%3Db952aa315be5b2c56e59ff2ef43e23d4%26ev%3Dv1%26es2%3D4212721c8e66755a85ba6d969150ca12%26rs0%3Dyg%252B9SmKn2I4q89%252FxUdgZryOGJAFch31QcAPQJxBReLsVzjFfFMbusEbGvhV5vrDiK4rbvj7ruP79dl7P6AG1%252FTFp3x%252FihCHxZQg1sWgNSuYnzEiHAZTZv61gbiOgaOd23Fs8g7%252B3JeHgotkQXlYhSfjFCz5XAXqvfLjpQNDN2OI%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1396982333%26et%3D1397068733%26d%3Dc909%26i%3Df4f6%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D2129325272%26name%3Dwangyifan%2540uchicago.edu%26nick%3Dwangyifan%26fmp%3D%26lcp%3D2011-05-20%252012%253A15%253A55; SUB=AVtYxjVbES%2Fxb5ABavHAqIZ5a%2FXhjmiU03CsMyec4K%2B4h9MoJ%2FVgzlhANPGkgjQcAqCvZl0O2miYkCEq0hurVOFIAuedeSDSS3c3ok7RsLuo7Cx7vCn2IFeCmv5UlOZcw2wQkTb1F7nIzsCL8HwErJc%3D; SUBP=002A2c-gVlwEm1uAWxfgXELuuu1xVxBxAArR-1k8t7QF-FxCmDSTtgOuHY-u_F%3D; ALF=1399500409"

def GetCode(client):
    auth_url = client.get_authorize_url()
    print auth_url
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'en-US,en;q=0.8,de;q=0.6,es;q=0.4,ja;q=0.2,zh-CN;q=0.2,zh-TW;q=0.2',
        'Cookie': cookie
        }
    req = urllib2.Request(auth_url)
    for key, value in headers.iteritems():
        req.add_header(key, value)
    resp = urllib2.urlopen(req)
    print resp.url
    code = resp.url[-32:]
    return code

client = APIClient(app_key, app_secret, redirect_uri=CALLBACK_URL)
auth_code = GetCode(client)
r = client.request_access_token(auth_code)
client.set_access_token(r.access_token, r.expires_in)
for status in client.statuses.friends_timeline.get()['statuses']:
    print status['text']

