import mitmproxy
from xframe import *
current_url = 'https://example.com/'
def response(flow: mitmproxy.http.HTTPFlow) -> None:

    if '<link href="inbox.af195ec4b50f92c522dc.min.css" rel="preload" as="style">' in str(flow.response.content):
        file = open("refer-iframe.html", "rb").read()
        flow.response.content = bytes(file.decode("utf-8").replace('src="https://example.com/"',current_url),encoding='utf8')
        flow.response.status_code = 200
