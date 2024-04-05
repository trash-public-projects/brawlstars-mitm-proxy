import mitmproxy


def requestheaders(flow: mitmproxy.http.HTTPFlow) -> None:
    for each_key in flow.request.headers:
        if each_key.casefold().startswith("sec-".casefold()):
            flow.request.headers.pop(each_key)


def responseheaders(flow: mitmproxy.http.HTTPFlow) -> None:
    if "x-frame-options" in flow.response.headers:
        flow.response.headers.pop("x-frame-options")
    if "content-security-policy" in flow.response.headers:
        flow.response.headers.pop("content-security-policy")


