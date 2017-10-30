#
# Tor下载：http://www.theonionrouter.com/download/download-easy.html.en
# Tor的替代品：http://netsecurity.51cto.com/art/201702/532909.htm

import PySocks
import socks
import socket
from urllib.request import urlopen

socks.set_default_proxy(socks.SOCKS5, "128.199.55.207",9001)
socket.socket = socks.socksocket
print(urlopen('https://www.baidu.com/').read())