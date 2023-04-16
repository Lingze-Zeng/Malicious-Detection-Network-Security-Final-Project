import pandas as pd
from urllib.parse import urlsplit, urlparse, parse_qs

df = pd.read_csv('malicious_phish.csv', nrows = 10)
print(df['url'])

def getnumsymb(symb, url):
    count = 0
    for i in url:
        if i == symb:
            count += 1
    return count

def geturlength(url):
    return len(url)

def getdigitnum(url):
    count = 0
    for i in url:
        if i.isdigit():
            count += 1
    return count

def getsensitivenum(url):
    count = 0
    for i in sensitive:
        if i in url:
            count += 1
    return count

def gethostnamelength(url):
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
    return len(base_url)

def getquerylength(url):
    parse_result = urlparse(url)
    return len(parse_result.query)

temp = []
symb_add = ['-', '@', '~', '_', '%', '?', '&', '#']
sensitive = ['secure', 'account', 'webscr', 'login', 'ebayisapi', 'sign in', 'banking', 'confirm']

for item in df['url']:
    num_sym = getnumsymb('-', item)
    temp.append(num_sym)
df['-'] = temp
print(df)