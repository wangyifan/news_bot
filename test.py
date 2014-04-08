import urllib2, urllib
from weibo import APIClient

app_key = "123954073"
app_secret = "54a668937f1b58ebe4888697332a14fe"
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
AUTH_URL = 'https://api.weibo.com/oauth2/authorize'

def GetCode():
    client = APIClient(app_key, app_secret, redirect_uri=CALLBACK_URL)
    referer_url = client.get_authorize_url()
    print referer_url
    r = client.request_access_token(raw_input("input code:").strip())
    print r.expires_in
    client.set_access_token(r.access_token, r.expires_in)
    import ipdb;ipdb.set_trace()
    print client
GetCode()


