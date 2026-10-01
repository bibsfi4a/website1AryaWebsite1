import ssl
import urllib.request
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')]
urllib.request.install_opener(opener)

page_url = 'https://commons.wikimedia.org/wiki/File:Community_meeting_(8330375152).jpg'
out_path = 'assets/real_image_4.jpg'

html = urllib.request.urlopen(page_url).read().decode('utf-8')
match = re.search(r'href="(https://upload.wikimedia.org/wikipedia/commons/[^"]+)" class="internal"', html)
if match:
    img_url = match.group(1)
    urllib.request.urlretrieve(img_url, out_path)
    print("Success")
else:
    print("Fail")
