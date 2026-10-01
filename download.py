import ssl
import urllib.request
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')]
urllib.request.install_opener(opener)

def download_wiki_file(page_url, out_path):
    print(f"Downloading {page_url}")
    html = urllib.request.urlopen(page_url).read().decode('utf-8')
    match = re.search(r'href="(https://upload.wikimedia.org/wikipedia/commons/[^"]+)" class="internal"', html)
    if match:
        img_url = match.group(1)
        print(f"Found image: {img_url}")
        urllib.request.urlretrieve(img_url, out_path)
    else:
        print("Could not find image link on page")

download_wiki_file('https://commons.wikimedia.org/wiki/File:May_Igala_community_meeting.jpg', 'assets/real_image_2.jpg')
download_wiki_file('https://commons.wikimedia.org/wiki/File:Ateendee_at_Wiki_Indaba_2024_taking_notes.jpg', 'assets/real_image_3.jpg')

print("Done")
