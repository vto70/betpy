import urllib.request

import lxml.html
with urllib.request.urlopen("urls_btts.txt") as url:
    s = url.read()
#I'm guessing this would output the html source code?
print(s)
